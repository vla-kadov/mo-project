import configparser
import json
import os
# TODO не удалять импорт, нужен для работы кода в eval() (см. метод setup)
import inspect

from browsermobproxy import Server
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
import requests

from lib.config import Config
from lib.driver import Driver, replace_current_driver
from lib.utils import attach_info


def br(_proxy=None):
    """ Ф-я которая возвращает оригинальный selenium-объект исходя из имени, адреса удаленного подключения, и факта
        использования прокси-сервера """

    # TODO возможно будет правиться для работы с Selenoid-ом
    # TODO работа с прокси настроена только для Chrome через chrome_options, добавить на другие браузеры
    # TODO научить работать прокси на удаленных машинах

    firefoxProfile = webdriver.FirefoxProfile()
    firefoxProfile.set_preference("plugin.state.flash", 2)
    firefoxProfile.set_preference("browser.helperApps.neverAsk.saveToDisk", 'image/jpeg')

    prefs = {
        "profile.default_content_setting_values.plugins": 1,
             "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
             "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1
             }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", prefs)
    if _proxy:
        chrome_options.add_argument("--proxy-server={0}".format(_proxy))
        chrome_options.add_argument('ignore-certificate-errors')
    driver = None
    if Config.use_grid:
        driver = webdriver.Remote(
            command_executor=Config.grid_hub_host,
            desired_capabilities=dict(browserName=Config.browser, platform=Config.webdriver_platform)
        )
    else:
        if Config.browser == "firefox":
            driver = webdriver.Firefox(firefoxProfile, executable_path=Config.firefox_webdriver_path)
        if Config.browser == "chrome":
            driver = webdriver.Chrome(executable_path=Config.chrome_webdriver_path, chrome_options=chrome_options)
        if Config.browser == "edge":
            driver = webdriver.Edge(executable_path=Config.edge_webdriver_path)
    if Config.browser != "safari":
        driver.set_window_position(0, 0)
    driver.maximize_window()

    return driver


class IniConfigParse:

    """ Класс для чтения ini-конфига. Важно - конфиг должен лежать в корне проекта (создается в configuration.py) """

    def __init__(self):

        self.ini_config = configparser.ConfigParser()
        self.ini_config.read('config.ini')

        self.use_grid = True if self.get_setting('use_grid') == 'True' else False
        self.use_proxy = True if self.get_setting('use_proxy') == 'True' else False
        self.detailed_steps = True if self.get_setting('detailed_steps') == 'True' else False
        self.attach_html = True if self.get_setting('attach_html') == 'True' else False

        self.browser = self.get_setting('browser')
        self.grid_hub_host = self.get_setting('grid_hub_host')
        self.webdriver_platform = self.get_setting('webdriver_platform')
        self.browsermob_proxy_path = self.get_setting('browsermob_proxy_path')

        self.portal_address = self.get_setting('portal_address')

    def get_setting(self, setting_name):
        return self.ini_config.get("Settings", setting_name)

    def _get_dict(self):
        dictionary = {}
        for section in self.ini_config.sections():
            dictionary[section] = {}
            for option in self.ini_config.options(section):
                dictionary[section][option] = self.ini_config.get(section, option)
        return dictionary


class TestCase:
    """
        Базовый класс для написания тестов. Содержит методы setup, teardown, setup_class, teardown_class, которые
        работают с параметрами и автоматичепски подготавливают все для работы тестов
    """

    work_driver: Driver = None
    proxy = None
    server = None

    def setup_class(self):

        # Создаем объект ридера конфига
        ini = IniConfigParse()

        # Получаем словарь со всеми параметрами конфига и аттачим в репорт
        d = ini._get_dict()['Settings']
        attach_info('config.ini', **d)

        # Получаем параметры из config.ini и записываем их в Config
        Config.portal_address = ini.portal_address
        Config.browser = ini.browser
        Config.use_proxy = ini.use_proxy
        Config.browsermob_proxy_path = ini.browsermob_proxy_path
        Config.use_grid = ini.use_grid
        Config.grid_hub_host = ini.grid_hub_host
        Config.webdriver_platform = ini.webdriver_platform
        Config.detailed_steps = ini.detailed_steps
        Config.attach_html = ini.attach_html

        # Если используем прокси - запускаем сервер проки
        if Config.use_proxy:
            self.server = Server(Config.browsermob_proxy_path)
            self.server.start()
            self.proxy = self.server.create_proxy(params={'trustAllServers':'true'})

        # Получаем объект оригинального selenium исходя из параметров
        if Config.use_proxy:
            b = br(_proxy=self.proxy.proxy)
        else:
            b = br()

        # Заворачиваем оригиналный вебдрайвер в глобальную обертку
        self.work_driver = replace_current_driver(b)

        # Получаем название и версию браузера
        browser_version = self.work_driver.browser_version
        browser_name = self.work_driver.browser_name

        # Получаем версию тестируемого портала
        url_split=str(Config.portal_address).split("/")
        url_version="%s//%s/assets/metadata.json" % (url_split[0], url_split[2])
        try:
            version = requests.get(url_version)
            portal_hash = version.json()['hash']
            portal_version = version.json()['version']
        except:
            portal_hash = "UNKNOWN"
            portal_version = "UNKNOWN"

        # Аттачим в репорт ОС, браузер и версию
        attach_info("ОС, браузер, версия браузера, версия портала, hash коммита", OS=Config.webdriver_platform, browser_name=browser_name, browser_version=browser_version, portal_version=portal_version, portal_hash=portal_hash)
        # with allure.step("ОС, браузер, версия"):
        #     allure.attach("ОС " + Config.webdriver_platform + "\nБраузер " + browser_name + "\nВерсия " + browser_version, name="parameters", attachment_type=AttachmentType.TEXT)

        # Аттачим в репорт capabilities, просто чтобы было
        with allure.step("Capabilities"):
            allure.attach(json.dumps(self.work_driver.capabilities), name="capabilities.json", attachment_type=AttachmentType.JSON)

        # Если был задан параметр portal_address, осуществляем переход по заданной ссылке
        if Config.portal_address != '':
            self.work_driver.get(Config.portal_address)

        # Создаем файл categories.json в который набор категорий тестов
        with open("./allure-results/categories.json", "w") as f:
            f.write('[{"name":"Ignored tests","matchedStatuses":["skipped"]},{"name":"Infrastructure problems",'
                    '"matchedStatuses":["broken","failed"],"messageRegex":".*bye-bye.*"},{"name":"Outdated tests",'
                    '"matchedStatuses":["broken"],"traceRegex":".*FileNotFoundException.*"},{"name":"Product '
                    'defects","matchedStatuses":["failed"]},{"name":"Test defects","matchedStatuses":["broken"]},'
                    '{"name":"Test passed","matchedStatuses":["passed"]}]')

        # Создаем файл environment.properties в который записываем ОС, браузер и версию
        with open("./allure-results/environment.properties", "w") as f:
            f.write("OS=%s\n" % Config.webdriver_platform)
            f.write("Browser=%s\n" % browser_name)
            f.write("Browser_version=%s\n" % browser_version)
            f.write("Portal_hash=%s\n" % portal_hash)
            f.write("Portal_version=%s" % portal_version)

    def teardown_class(self):

        # По окончанию всех тестов закрываем браузер и разрываем сессию
        self.work_driver.close()
        self.work_driver.quit()

        # Если использовали прокси - останавливаем сервер прокси
        if Config.use_proxy:
            self.server.stop()

    def setup(self):
        """ Перед началом теста аттачим исходный код теста и запускаем запись нового HAR-файла """

        # костыль для аттача в аллюр непосредтсвенно сырого кода теста. Завернул в исключение на всякий случай.
        if Config.detailed_steps:
            try:
                test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
                code_line = "inspect.getsourcelines(self.%s)" % test_name
                code_file = "inspect.getsourcefile(self.%s)" % test_name
                c = eval(code_line)
                fname = eval(code_file)
                r = "File " + fname + "; line " + str(c[1]) + "\n\n##############################\n\n"
                for i in c[0]:
                    r = r + i
                r = r + "\n##############################"
                allure.attach(r, name="Test source", attachment_type=AttachmentType.TEXT)
            except:
                pass

        # TODO https://stackoverflow.com/questions/50550496/browsermob-proxy-python-how-to-get-response-body
        # TODO с опциями har раздувается до мегабайтов
        # TODO self.proxy.new_har("myhar",options={'captureHeaders': True,'captureContent':True})
        # Если используем прокси, то перед каждым тестом начинаем новую запись har-файла
        if Config.use_proxy:
            self.proxy.new_har("myhar")

    def teardown(self) -> None:
        """ По окончанию теста аттачим к репорту скриншот и HTML-код страницы + HAR если включено """
        if Config.detailed_steps:
            allure.attach(self.work_driver.original_webdriver.get_screenshot_as_png(), name='Screenshot after test', attachment_type=AttachmentType.PNG)

        if Config.attach_html:
            allure.attach(self.work_driver.original_webdriver.page_source, name='Page source after test', attachment_type=AttachmentType.HTML)

        if Config.use_proxy:
            # TODO в HAR складываются лишние запросы типа статики, yandex-а, и т.п. Добавить фильтрацию? Можно ли
            #  сделать настройку правил фильтрации через параметры или конфиги?
            with open('myhar.har', 'w') as har_file:
                json.dump(self.proxy.har, har_file)
            allure.attach.file("myhar.har", name='HAR after test', attachment_type=AttachmentType.JSON)
            os.remove('myhar.har')
