import argparse
import configparser
import sys


parser = argparse.ArgumentParser()
parser.add_argument('--browser', help='Браузер для запуска тестов', default='chrome')
parser.add_argument('--use_grid', help='Использовать удаленный сервер', default=False)
parser.add_argument('--grid_hub_host', help='Адрес удаленного сервера', default='http://docker-host.netris.ru:4444/wd/hub')
parser.add_argument('--webdriver_platform', help='Платформа, используемая для запуска тестов', default='Windows')
parser.add_argument('--use_proxy', help='Использовать прокси для логирования har', default=False)
if sys.platform == "win32":
    p = ".\\browsermob-proxy\\bin\\browsermob-proxy.bat"
else:
    p = ".\\browsermob-proxy\\bin\\browsermob-proxy"
parser.add_argument('--browsermob_proxy_path', help='Путь до прокси', default=p)
parser.add_argument('--detailed_steps', help='Добавлять в репорт информацию обо всех действиях', default=False)
parser.add_argument('--attach_html', help='Добавлять в allure репорт html страницу после каждого действия', default=False)
parser.add_argument('--portal_address', '-a', help='Example: https://echd.mos.ru', default="")


args = parser.parse_args()


ini_config = configparser.ConfigParser()


# в ini попадают аргументы из коммандной строки или дефолтовые
ini_config.add_section("Settings")
ini_config.set("Settings", "browser", args.browser)
ini_config.set("Settings", "use_grid", str(args.use_grid))
ini_config.set("Settings", "grid_hub_host", args.grid_hub_host)
ini_config.set("Settings", "webdriver_platform", args.webdriver_platform)
ini_config.set("Settings", "use_proxy", str(args.use_proxy))
ini_config.set("Settings", "browsermob_proxy_path", args.browsermob_proxy_path)
ini_config.set("Settings", "detailed_steps", str(args.detailed_steps))
ini_config.set("Settings", "attach_html", str(args.attach_html))
ini_config.set("Settings", "portal_address", args.portal_address)

with open("config.ini", "w") as config_file:
    ini_config.write(config_file)
