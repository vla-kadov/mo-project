# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver

from .element import Element
from .all_methods import *


# Глобальная переменная в которой хранится объект Driver. За счет глобальности с объектом можно работать из любого файла
# библиотеки, и реализовать "неявное" использование
global current


def replace_current_driver(selenium_driver: WebDriver):
    """Заменяет текущий глобальный драйвер на указанный"""
    global current
    current = Driver(selenium_driver)
    return current


class Driver:
    """
        Класс представляет собой расширение класса WebDriver из оригинального selenium-а. Основная архитектурная идея
        номер один -  оригинальный объекто ведбрайвера записываем в self.driver, и при написании своих методов вызываем
        оригинальные методы как self.driver.<некий оригинальный метод>. Основная архитектурная идея номер два - выносим
        все методы в отделбные ф-ии, например w_get(self.driver), в который передаем оригинальный объект, и уже внутри
        функции реализуем логику (с проверками, репортингом, и т.п.
    """

    def __init__(self, selenium_driver: WebDriver):
        self.driver: WebDriver = selenium_driver

    def __getattr__(self, item):
        return getattr(self.driver, item)

    @property
    def original_webdriver(self) -> WebDriver:
        """ Метод возвращает объект оригинального WebDriver-а """
        return self.driver

    @property
    def browser_name(self):
        """ Имя браузера """
        return str(self.driver.capabilities["browserName"])

    @property
    def browser_version(self):
        """ Версия браузера """
        return str(self.driver.capabilities['browserVersion'])

    @property
    def platform(self):
        """ Рабочая ОС """
        return str(self.driver.capabilities['platformName'])

    @property
    def capabilities(self) -> dict:
        return self.driver.capabilities

    def page_load_time(self) -> float:
        """ Возвращает время загрузки страницы """
        time_load_end = self.driver.execute_script("return window.performance.timing.loadEventEnd;")
        time_navigation_start = self.driver.execute_script("return window.performance.timing.navigationStart;")
        return float((time_load_end - time_navigation_start) / 1000)

    ####################################################################################################################

    def get(self, url: str):
        """ Переход по указанной ссылке """
        w_get(self.driver, url)
        return self

    @property
    def url(self) -> str:
        """ Возвращает текущий url страницы """
        current_url: str = w_url(self.driver)
        return current_url

    @property
    def title(self) -> str:
        """ Возвращает текущий заголовок страницы """
        current_title: str = w_title(self.driver)
        return current_title

    def execute_script(self, script, *args):
        """ Выполняет на странице произвольный js-скрипт """
        return self.driver.execute_script(script, *args)

    def sleep(self, s=1):
        """ Пауза выполнения """
        w_sleep(s)
        return self

    def close(self):
        self.driver.close()
        return self

    def quit(self):
        try:
            self.driver.quit()
        except:
            pass
        return self

    def stop_client(self):
        self.driver.stop_client()
        return self

    def back(self):
        """ Шаг назад в истории браузера """
        w_back(self)
        return self

    def forward(self):
        """ Шаг врепед в истории браузера """
        w_forward(self)
        return self

    def refresh(self):
        """ Обновить страницу """
        w_refresh(self)
        return self

    def delete_all_cookies(self):
        """ Удалить все куки """
        w_delete_all_cookies(self)
        return self

    def get_screenshot_as_png(self):
        """ Сделать скриншот текущей страницы """
        screen = w_get_screenshot_as_png(self)
        return screen

    def get_screenshot_as_file(self, filename) -> bool:
        b: bool = w_get_screenshot_as_file(self, filename)
        return b

    def save_screenshot(self, filename) -> bool:
        return self.get_screenshot_as_file(filename)

    @property
    def get_page_size(self):
        """ Определяет размер всей старницы, включая той части что скрыта скролом """
        height = """var scrollHeight = Math.max(
              document.body.scrollHeight, document.documentElement.scrollHeight,
              document.body.offsetHeight, document.documentElement.offsetHeight,
              document.body.clientHeight, document.documentElement.clientHeight
            );
            return scrollHeight; """
        width = """var scrollWidth = Math.max(
              document.body.scrollWidth, document.documentElement.scrollWidth,
              document.body.offsetWidth, document.documentElement.offsetWidth,
              document.body.clientWidth, document.documentElement.clientWidth
            );
            return scrollWidth; """
        w = self.driver.execute_script(height)
        h = self.driver.execute_script(width)
        return [int(h), int(w)]

    @property
    def get_work_size(self):
        """ Определяет размер рабочей области браузера """
        w = self.driver.execute_script("return document.body.clientWidth")
        h = self.driver.execute_script("return window.innerHeight")
        return [int(h), int(w)]

    @property
    def get_window_size(self):
        """ Определяет размер окна браузера (рабочая область + поля + панель меню) """
        rz = self.driver.get_window_size()
        w = rz["width"]  # Ширина
        h = rz["height"]  # Высота
        return [int(w), int(h)]
