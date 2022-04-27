# Базовый модуль с набором функций
import allure

from lib import driver as current_work_driver
from lib.driver import Driver
from lib.utils import info
from lib.config import Config
from unittest import TestCase


assert_object = TestCase()


def get(url) -> Driver:
    return current_work_driver.current.get(url)


def refresh() -> Driver:
    return current_work_driver.current.refresh()


def back() -> Driver:
    return current_work_driver.current.back()


def forward() -> Driver:
    return current_work_driver.current.forward()


def title() -> str:
    return current_work_driver.current.title


def url() -> str:
    return current_work_driver.current.url


def close_and_quit():
    current_work_driver.current.close()
    current_work_driver.current.quit()


def sleep(s):
    current_work_driver.current.sleep(s)


def driver() -> Driver:
    return current_work_driver.current


########################################################################################################################


def assert_title(ttl: str):
    info("Проверяем что заголовок страницы равен '%s'" % ttl)
    if Config.detailed_steps:
        with allure.step("Проверяем что заголовок страницы равен '%s'" % ttl):
            assert_object.assertEqual(title(), ttl)
            with allure.step("Проверка пройдена успешно"):
                pass
    else:
        assert_object.assertEqual(title(), ttl)
    info("Проверка пройдена успешно")


def assert_url(_url: str):
    info("Проверяем что URL страницы равен '%s'" % _url)
    if Config.detailed_steps:
        with allure.step("Проверяем что URL страницы равен '%s'" % _url):
            assert_object.assertEqual(url(), _url)
            with allure.step("Проверка пройдена успешно"):
                pass
    else:
        assert_object.assertEqual(title(), _url)
    info("Проверка пройдена успешно")
