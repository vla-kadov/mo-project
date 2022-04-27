# -*- coding: utf-8 -*-
# Набор воспомогательных функций и классов, вынесенных в отдельный модуль
import allure
from allure_commons.types import AttachmentType
import time
import logging

from selenium.webdriver.support.wait import WebDriverWait

from lib.config import Config


# Создаем логер для дальнейшего логирования всех действий в текстовый лог
logging.basicConfig(format='[%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    handlers=[logging.FileHandler("work_log.log", 'w', 'utf-8'), logging.StreamHandler()])


def info(message):
    """ Запись в лог информации со статусом INFO """
    logging.info(message)


@allure.step('{attach_info}')
def attach_info(attach_info='', **kwargs):
    pass


def wait_interaction(ob, wait=Config.wait_timeout):
    """ Ожидание интерактивности элемента """
    r = Wait(ob, wait).bool(lambda dd: dd._element.is_enabled() and dd._element.is_displayed())
    if Config.detailed_steps:
        m = "" if r else " не"
        with allure.step("Элемент %s%s доступен для взаимодействия" % (ob.element_name, m)):
            info("Элемент %s доступен для взаимодействия" % ob.element_name)


def highlight_and_screenshot(element):
    """ Подсветка, скриншотирование, и аттач элемента в allure """
    # TODO найти более "элегантный" способ выделения элемента, который не двигает верстку

    driver = element._parent
    driver.execute_script('arguments[0].scrollIntoView();', element)

    def apply_style(s):

        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)

    original_style = element.get_attribute('style')
    apply_style("border: 2px solid red;")
    # Вариант когда вместо рамки - синий бэкграунд
    # apply_style("background-color: #0000ff; opacity: 0.9")

    allure.attach(driver.get_screenshot_as_png(), name="element screenshot", attachment_type=AttachmentType.PNG)
    #time.sleep(0.1)
    apply_style(original_style)
    outer_html = element.get_attribute('outerHTML')
    tag_html = outer_html[:outer_html.find('>') + 1]
    allure.attach(tag_html, name="tag HTML", attachment_type=AttachmentType.TEXT)
    # allure.attach(outer_html, name="outerHTML", attachment_type=AttachmentType.HTML)


def element_info_attach(element_stack_info):
    _file_path = element_stack_info[0]
    _line_number = element_stack_info[1]
    _raw_str = element_stack_info[3][0].lstrip()

    # TODO два варианта аттача информации об элементе в репорт, выбрать по вкусу (через attach_info или allure.attach)
    # attach_info("Element info", element_location=_file_path + ": " + str(_line_number), raw_str=_raw_str)
    allure.attach(_file_path + ": " + str(_line_number) + "\n\n" + _raw_str, name="Element info", attachment_type=AttachmentType.TEXT)


class Wait(WebDriverWait):
    """ Класс-наследник классического WebDriverWait-а """
    def __init__(self, driver, timeout=Config.wait_timeout, poll_frequency=Config.pool_frequency):
        super().__init__(driver,  timeout, poll_frequency)

    def bool(self, method):
        """ Данный метод в случае провала проверки не роняет исключение, а просто возвращает False """
        if self._timeout != 0:
            try:
                self.until(method)
                return True
            except:
                return False
