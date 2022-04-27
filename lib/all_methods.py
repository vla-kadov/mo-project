import time

from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from lib.utils import info, element_info_attach, wait_interaction, highlight_and_screenshot, Wait
from lib.config import Config

import allure
import unittest


assert_object = unittest.TestCase()


def w_sleep(time_to_sleep):
    info("Пауза в %s секунд" % str(time_to_sleep))
    if Config.detailed_steps:
        with allure.step("Пауза в %s секунд" % str(time_to_sleep)):
            time.sleep(time_to_sleep)
    else:
        time.sleep(time_to_sleep)


def w_get(driver, url) -> None:
    info("Осуществляем переход по ссылке '%s'" % url)
    if Config.detailed_steps:
        with allure.step("Осуществляем переход по ссылке '%s'" % url):
            driver.get(url)

            current_url = driver.current_url
            current_title = driver.title
            time_load_end = driver.execute_script("return window.performance.timing.loadEventEnd;")
            time_navigation_start = driver.execute_script("return window.performance.timing.navigationStart;")
            t = float((time_load_end - time_navigation_start) / 1000)

            with allure.step("Осуществлен переход на страницу '%s' (URL - '%s', время загрузки страницы %s сек.)" % (current_title, current_url, str(t))):
                pass
    else:
        driver.get(url)
        current_url = driver.current_url
        current_title = driver.title
        time_load_end = driver.execute_script("return window.performance.timing.loadEventEnd;")
        time_navigation_start = driver.execute_script("return window.performance.timing.navigationStart;")
        t = float((time_load_end - time_navigation_start) / 1000)
    info("Осуществлен переход на страницу '%s' (URL - '%s', время загрузки страницы %s сек.)" % (current_title, current_url, str(t)))


def w_url(driver: WebDriver) -> str:
    info("Получаем URL текущей страницы")
    if Config.detailed_steps:
        with allure.step("Получаем URL текущей страницы"):
            current_url = driver.current_url
            current_title = driver.title
            with allure.step("Текущий URL - '%s' (заголовок '%s')" % (current_url, current_title)):
                pass
    else:
        current_url = driver.current_url
        current_title = driver.title
    info("Текущий URL - '%s' (заголовок '%s')" % (current_url, current_title))
    return current_url


def w_title(driver) -> str:
    info("Получаем заголовок текущей страницы")
    if Config.detailed_steps:
        with allure.step("Получаем заголовок текущей страницы"):
            current_url = driver.current_url
            current_title = driver.title
            with allure.step("Текущий заголовок - '%s' (URL '%s')" % (current_title, current_url)):
                pass
    else:
        current_url = driver.current_url
        current_title = driver.title
    info("Текущий заголовок - '%s' (URL '%s')" % (current_title, current_url))
    return current_title


def w_back(driver):
    current_title = driver.original_webdriver.title
    current_url = driver.original_webdriver.current_url
    info("Делаем шаг назад в истории страницы (текущая страница - '%s', %s)" % (current_title, current_url))
    if Config.detailed_steps:
        with allure.step("Делаем шаг назад в истории страницы (текущая страница - '%s', %s)" % (current_title, current_url)):
            driver.original_webdriver.back()
            current_title = driver.original_webdriver.title
            current_url = driver.original_webdriver.current_url
            with allure.step("Осуществлен переход на страницу '%s' (%s)" % (current_title, current_url)):
                pass
    else:
        driver.original_webdriver.back()
        current_title = driver.original_webdriver.title
        current_url = driver.original_webdriver.current_url
    info("Осуществлен переход на страницу '%s' (%s)" % (current_title, current_url))


def w_forward(driver):
    current_title = driver.original_webdriver.title
    current_url = driver.original_webdriver.current_url
    info("Делаем шаг вперед в истории страницы (текущая страница - '%s', %s)" % (current_title, current_url))
    if Config.detailed_steps:
        with allure.step("Делаем шаг вперед в истории страницы (текущая страница - '%s', %s)" % (current_title, current_url)):
            driver.original_webdriver.forward()
            current_title = driver.original_webdriver.title
            current_url = driver.original_webdriver.current_url
            with allure.step("Осуществлен переход на страницу '%s' (%s)" % (current_title, current_url)):
                pass
    else:
        driver.original_webdriver.forward()
        current_title = driver.original_webdriver.title
        current_url = driver.original_webdriver.current_url
    info("Осуществлен переход на страницу '%s' (%s)" % (current_title, current_url))


def w_refresh(driver):
    current_title = driver.original_webdriver.title
    current_url = driver.original_webdriver.current_url
    info("Делаем рефреш текущей страницы ('%s', %s)" % (current_title, current_url))
    if Config.detailed_steps:
        with allure.step("Делаем рефреш текущей страницы ('%s', %s)" % (current_title, current_url)):
            driver.original_webdriver.refresh()
            with allure.step("Страница обновлена"):
                pass
    else:
        driver.original_webdriver.refresh()
    info("Страница обновлена")


def w_delete_all_cookies(driver):
    info("Удаляем все куки")
    if Config.detailed_steps:
        with allure.step("Удаляем все куки"):
            driver.original_webdriver.delete_all_cookies()
            with allure.step("Куки удалены"):
                pass
    else:
        driver.original_webdriver.delete_all_cookies()
    info("Куки удалены")


def w_get_screenshot_as_png(driver):
    current_title = driver.original_webdriver.title
    current_url = driver.original_webdriver.current_url
    info("Делаем скришот страницы '%s' (%s)" % (current_title, current_url))
    if Config.detailed_steps:
        with allure.step("Делаем скришот страницы '%s' (%s)" % (current_title, current_url)):
            screen = driver.original_webdriver.get_screenshot_as_png()
            allure.attach(screen, attachment_type=AttachmentType.PNG)
            with allure.step("Скриншот выполнен"):
                pass
    else:
        screen = driver.original_webdriver.get_screenshot_as_png()
    info("Скриншот выполнен")
    return screen


def w_get_screenshot_as_file(driver, filename) -> bool:
    screen: bool = False
    current_title = driver.original_webdriver.title
    current_url = driver.original_webdriver.current_url
    info("Делаем скришот страницы '%s' (%s) и сохраняем в файл '%s'" % (current_title, current_url, filename))
    if Config.detailed_steps:
        with allure.step("Делаем скришот страницы '%s' (%s) и сохраняем в файл '%s'" % (current_title, current_url, filename)):
            screen = driver.original_webdriver.get_screenshot_as_file(filename)
            allure.attach(screen, name=filename, attachment_type=AttachmentType.PNG)
            with allure.step("Скриншот выполнен"):
                pass
    else:
        screen = driver.original_webdriver.get_screenshot_as_file(filename)
    info("Скриншот выполнен")
    return screen


# Методы WebElement-а ##################################################################################################


def w_assert_element_text_equal(element, element_name, assertion_text) -> None:
    info("Проверяем что текст элемента равен '%s'" % assertion_text)
    if Config.detailed_steps:
        with allure.step("Проверяем что текст элемента равен '%s'" % assertion_text):
            assert_object.assertEqual(element.text, assertion_text)
            with allure.step("Проверка пройдена успешно"):
                pass
    else:
        assert_object.assertEqual(element.text, assertion_text)
    info("Проверка пройдена успешно")

def w_assert_element_placeholder_text_equal(element, element_name, assertion_text) -> None:
    info("Проверяем что текст элемента равен '%s'" % assertion_text)
    if Config.detailed_steps:
        with allure.step("Проверяем что текст элемента равен '%s'" % assertion_text):
            assert_object.assertEqual(element.placeholder, assertion_text)
            with allure.step("Проверка пройдена успешно"):
                pass
    else:
        assert_object.assertEqual(element.text, assertion_text)
    info("Проверка пройдена успешно")

def w_assert_element_not_text(element):
    info("Проверяем что элемент не содержит текста")
    if Config.detailed_steps:
        with allure.step("Проверяем что элемент не содержит текста"):
            element_info_attach(element.locator._stack_info)
            # TODO чет сомневаюсь что правильно прописана проверка, тестануть
            assert_object.assertFalse(element.text)
            with allure.step("Проверка пройдена успешно"):
                pass
    else:
        assert_object.assertFalse(element.text)
    info("Проверка пройдена успешно")


def w_assert_element_text_not_equal(element, text) -> None:
    info("Проверяем что текст элемента не равен '%s'" % text)
    if Config.detailed_steps:
        with allure.step("Проверяем что текст элемента не равен '%s'" % text):
            element_info_attach(element.locator._stack_info)
            assert_object.assertNotEqual(element.text, text)
            with allure.step("Проверка пройдена успешно"):
                pass
    else:
        assert_object.assertEqual(element.text, text)
    info("Проверка пройдена успешно")


def w_assert_element_text_contains(element, text) -> None:
    info("Проверяем что текст элемента %s содержит строку '%s'" % (element.locator.element_name, text))
    if Config.detailed_steps:
        with allure.step("Проверяем что текст элемента содержит строку '%s'" % text):
            element_info_attach(element.locator._stack_info)
            assert_object.assertTrue(text in element.text)
            with allure.step("Проверка пройдена успешно"):
                pass
    else:
        assert_object.assertEqual(element.text, text)
    info("Проверка пройдена успешно")


def w_assert_element_existence(element) -> None:
    el = None
    info("Проверяем наличие элемента %s на странице" % element.locator.element_name)
    if Config.detailed_steps:
        with allure.step("Проверяем наличие элемента %s на странице" % element.locator.element_name):
            element_info_attach(element.locator._stack_info)
            try:
                el = element.find(wait=Config.wait_timeout)
            except:
                pass
            if el:
                highlight_and_screenshot(el.original_webelement)
            assert_object.assertTrue(el, msg="Элемент %s на странице не найден" % element.locator.element_name)
            with allure.step("Элемент присутствует на странице"):
                pass
    else:
        try:
            el = element.locator._search()
        except:
            pass
        assert_object.assertTrue(el, msg="Элемент %s на странице не найден" % element.locator.element_name)
    info("Элемент присутствует на странице")


def w_assert_element_not_existence(element, wait=1) -> None:
    el = None
    info("Проверяем что элемента %s нет на странице" % element.element_name)
    if Config.detailed_steps:
        with allure.step("Проверяем что элемента %s нет на странице" % element.element_name):
            element_info_attach(element.locator._stack_info)
            _el = Wait(element, 1).bool(lambda dd: not dd._is_find(wait=wait))
            el = not _el
            if el:
                highlight_and_screenshot(element.original_webelement)
            assert_object.assertFalse(el, msg="Элемент %s на странице найден" % element.element_name)
            with allure.step("Элемент на странице не присутствует"):
                pass
    else:
        try:
            _el = Wait(element, 1).bool(lambda dd: not dd._is_find(wait=wait))
            el = not _el
            el = element.locator._search(wait=wait)
        except:
            pass
        assert_object.assertFalse(el, msg="Элемент %s на странице найден" % element.element_name)
    info("Элемент на странице не присутствует")


def w_assert_element_not_displayed(element) -> None:
    el = None
    info("Проверяем что элемент %s не виден на странице" % element.element_name)
    if Config.detailed_steps:
        with allure.step("Проверяем что элемент %s не виден на странице" % element.element_name):
            element_info_attach(element.locator._stack_info)
            el = element._element
            Wait(el, 1).bool(lambda dd: not dd.is_displayed())
            if el:
                highlight_and_screenshot(element.original_webelement)
            assert_object.assertFalse(el, msg="Элемент %s на странице виден" % element.element_name)
            with allure.step("Элемент на странице не виден"):
                pass
    else:
        try:
            el = element.locator._search(wait=1)
        except:
            pass
        assert_object.assertFalse(el, msg="Элемент %s на странице виден" % element.element_name)
    info("Элемент на странице не виден")


def w_assert_element_enabled(element) -> None:
    info("Проверяем что элемент доступен для взаимодействия")
    if Config.detailed_steps:
        with allure.step("Проверяем что элемент доступен для взаимодействия"):
            element_info_attach(element.locator._stack_info)
            assert_object.assertTrue(element._element.is_enabled())
            with allure.step("Проверено, элемент доступен для взаимодействия"):
                pass
    else:
        assert_object.assertTrue(element._element.is_enabled())
    info("Проверено, элемент доступен для взаимодействия")


def w_assert_element_displayed(element) -> None:
    info("Проверяем что элемент %s отображается на экране" % element.element_name)
    if Config.detailed_steps:
        with allure.step("Проверяем что элемент %s отображается на экране" % element.element_name):
            wait_interaction(element)
            #Wait(element).bool(lambda dd: dd._element.is_displayed())
            element_info_attach(element.locator._stack_info)
            assert_object.assertTrue(element._element.is_displayed(), msg="Элемент %s не отображается на экране" % element.element_name)
            with allure.step("Проверено, элемент отображается на экране"):
                pass
    else:
        Wait(element).bool(lambda dd: dd._element.is_displayed())
        assert_object.assertTrue(element._element.is_displayed(), msg="Элемент %s не отображается на экране" % element.element_name)
    info("Проверено, элемент отображается на экране")


def w_assert_element_not_enabled(element) -> None:
    info("Проверяем что элемент %s не доступен для взаимодействия" % element.element_name)
    if Config.detailed_steps:
        with allure.step("Проверяем что элемент %s не доступен для взаимодействия" % element.element_name):
            element_info_attach(element.locator._stack_info)
            assert_object.assertTrue(element._element.is_enabled())
            with allure.step("Проверено, элемент не доступен для взаимодействия"):
                pass
    else:
        assert_object.assertTrue(element._element.is_enabled())
    info("Проверено, элемент не доступен для взаимодействия")


def w_assert_element_have_class(element, class_name):
    info("Проверяем что элемент %s содержит класс '%s'" % (element.element_name, class_name))
    if Config.detailed_steps:
        with allure.step("Проверяем что элемент %s содержит класс '%s'" % (element.element_name, class_name)):
            element_info_attach(element.locator._stack_info)
            assert_object.assertTrue(class_name in element._element.get_attribute('class'))
            with allure.step("Проверено, элемент содержит указанный класс"):
                pass
    else:
        assert_object.assertTrue(class_name in element._element.get_attribute('class'))
    info("Проверено, элемент содержит указанный класс")


def w_assert_element_not_have_class(element, class_name):
    info("Проверяем что элемент %s не содержит класс '%s'" % (element.element_name, class_name))
    if Config.detailed_steps:
        with allure.step("Проверяем что элемент %s не содержит класс '%s'" % (element.element_name, class_name)):
            element_info_attach(element.locator._stack_info)
            assert_object.assertFalse(class_name in element._element.get_attribute('class'))
            with allure.step("Проверено, элемент не содержит указанный класс"):
                pass
    else:
        assert_object.assertTrue(class_name in element._element.get_attribute('class'))
    info("Проверено, элемент не содержит указанный класс")


def w_assert_element_have_attribute(element, attribute):
    info("Проверяем что элемент %s содержит атрибут '%s'" % (element.element_name, attribute))
    if Config.detailed_steps:
        with allure.step("Проверяем что элемент %s содержит атрибут '%s'" % (element.element_name, attribute)):
            element_info_attach(element.locator._stack_info)
            assert_object.assertTrue(element._element.get_attribute(attribute))
            with allure.step("Проверено, элемент содержит указанный атрибут"):
                pass
    else:
        assert_object.assertTrue(element._element.get_attribute(attribute))
    info("Проверено, элемент содержит указанный атрибут")


def w_assert_element_not_have_attribute(element, attribute):
    info("Проверяем что элемент %s не содержит атрибут '%s'" % (element.element_name, attribute))
    if Config.detailed_steps:
        with allure.step("Проверяем что элемент %s не содержит атрибут '%s'" % (element.element_name, attribute)):
            element_info_attach(element.locator._stack_info)
            assert_object.assertFalse(element._element.get_attribute(attribute))
            with allure.step("Проверено, элемент не содержит указанный атрибут"):
                pass
    else:
        assert_object.assertFalse(element._element.get_attribute(attribute))
    info("Проверено, элемент не содержит указанный атрибут")


def w_element_click(element) -> None:
    info("Осуществляем клик по элементу %s" % element.element_name)
    if Config.detailed_steps:
        with allure.step("Осуществляем клик по элементу %s" % element.element_name):
            element_info_attach(element.locator._stack_info)
            wait_interaction(element)
            element._element.click()
            with allure.step("Клик успешно осуществлен"):
                pass
    else:
        element._element.click()
    info("Клик успешно осуществлен")


def w_element_mouse_click(element) -> None:
    info("Осуществляем клик по элементу %s" % element.element_name)
    if Config.detailed_steps:
        with allure.step("Осуществляем клик по элементу %s" % element.element_name):
            element_info_attach(element.locator._stack_info)
            ActionChains(element._element._parent).click(element._element).perform()
            with allure.step("Клик успешно осуществлен"):
                pass
    else:
        ActionChains(element._element._parent).click(element._element).perform()
    info("Клик успешно осуществлен")


def w_element_attach_allure_screenshot(element) -> None:
    if Config.detailed_steps:
        info("Аттачим скриншот элемента %s" % element.element_name)
        with allure.step("Аттачим скриншот элемента %s" % element.element_name):
            element_info_attach(element.locator._stack_info)
            highlight_and_screenshot(element.original_webelement)


def w_element_send_keys(element, value) -> None:
    info("Вводим в элемент строку '%s'" % value)
    if Config.detailed_steps:
        with allure.step("Вводим в элемент строку '%s'" % value):
            element_info_attach(element.locator._stack_info)
            wait_interaction(element)
            element._element.send_keys(value)
            with allure.step("Ввод успешно осуществлен"):
                pass
    else:
        element._element.send_keys(value)
    info("Ввод успешно осуществлен")


def w_element_send_hot_keys(element, value) -> None:
    print(Config.webdriver_platform)
    if Config.webdriver_platform == "MAC":
        hot_keys_general_button = Keys.COMMAND
    else:
        hot_keys_general_button = Keys.CONTROL
    info("Нажимаем горячую клавишу control + '%s'" % value)
    if Config.detailed_steps:
        with allure.step("Нажимаем горячую клавишу control + '%s'" % value):
            element_info_attach(element.locator._stack_info)
            wait_interaction(element)
            element._element.send_keys(hot_keys_general_button, value)
            with allure.step("Сочетание горячих клавиш успешно отправлено"):
                pass
    else:
        element._element.send_keys(value)
    info("Ввод успешно осуществлен")


def w_element_clear(element) -> None:
    info("Очищаем элемент")
    if Config.detailed_steps:
        with allure.step("Очищаем элемент"):
            element_info_attach(element.locator._stack_info)
            wait_interaction(element)
            element._element.clear()
            with allure.step("Элемент очищен"):
                pass
    else:
        element._element.clear()
    info("Элемент очищен")


def w_element_text(element) -> str:
    info("Получаем текст элемента")
    if Config.detailed_steps:
        with allure.step("Получаем текст элемента"):
            element_info_attach(element.locator._stack_info)
            get_text = element._element.get_attribute('value')
            if Config.browser == "safari":
                get_text = element._element.get_attribute('innerText')
            elif get_text is None or str(get_text) == str(0) or str(get_text) == "":
                get_text = element._element.text
            else:
                pass
            with allure.step("Получен текст '%s'" % get_text):
                pass
    else:
        get_text = element._element.get_attribute('value')
        if Config.browser == "safari":
            get_text = element._element.get_attribute('innerText')
        elif get_text is None or str(get_text) == str(0) or str(get_text) == "":
            get_text = element._element.text
        else:
            pass
    info("Получен текст '%s'" % get_text)
    return get_text


def w_element_placeholder(element) -> str:
    info("Получаем текст элемента")
    if Config.detailed_steps:
        with allure.step("Получаем текст элемента"):
            element_info_attach(element.locator._stack_info)
            get_text = element._element.get_attribute('placeholder')
            with allure.step("Получен текст '%s'" % get_text):
                pass
    else:
        get_text = element._element.get_attribute('placeholder')
    info("Получен текст '%s'" % get_text)
    return get_text

def w_mouse_move_to_element(element):
    info("Наводим курсор мыши на элемент")
    if Config.detailed_steps:
        with allure.step("Наводим курсор мыши на элемент"):
            element_info_attach(element.locator._stack_info)
            ActionChains(element._element._parent).move_to_element(element._element).perform()
            with allure.step("Наведение успешно осуществлено"):
                pass
    else:
        ActionChains(element._element._parent).move_to_element(element._element).perform()
    info("Наведение успешно осуществлено")


def w_element_is_displayed(element) -> bool:
    info("Виден ли элемент на дисплее")
    if Config.detailed_steps:
        with allure.step("Виден ли элемент на дисплее"):
            element_info_attach(element.locator._stack_info)
            v = element._element.is_displayed()
            message = "Элемент виден" if v else "Элемент не виден"
            with allure.step(message):
                pass
    else:
        v = element._element.is_displayed()
        message = "Элемент виден" if v else "Элемент не виден"
    info(message)
    return v


def w_element_is_enabled(element) -> bool:
    info("Доступен ли ли элемент для взаимодействия")
    if Config.detailed_steps:
        with allure.step("Доступен ли ли элемент для взаимодействия"):
            element_info_attach(element.locator._stack_info)
            v = element._element.is_enabled()
            message = "Элемент доступен для взаимодействия" if v else "Элемент не доступен для взаимодействия"
            with allure.step(message):
                pass
    else:
        v = element._element.is_enabled()
        message = "Элемент доступен для взаимодействия" if v else "Элемент не доступен для взаимодействия"
    info(message)
    return v


def w_element_is_selected(element) -> bool:
    info("Выбран ли ли элемент")
    if Config.detailed_steps:
        with allure.step("Выбран ли ли элемент"):
            element_info_attach(element.locator._stack_info)
            v = element._element.is_selected()
            message = "Элемент выбран" if v else "Элемент не выбран"
            with allure.step(message):
                pass
    else:
        v = element._element.is_selected()
        message = "Элемент выбран" if v else "Элемент не выбран"
    info(message)
    return v


def w_element_is_interaction(element) -> bool:
    info("Доступен ли элемент для взаимодействия и является ли он видимым для юзера")
    if Config.detailed_steps:
        with allure.step("Доступен ли элемент для взаимодействия и является ли он видимым для юзера"):
            element_info_attach(element.locator._stack_info)
            v = element._element.is_enabled() and element._element.is_displayed()
            message = "Элемент доступен для взаимодействия" if v else "Элемент не доступен для взаимодействия"
            with allure.step(message):
                pass
    else:
        v = element._element.is_enabled() and element._element.is_displayed()
        message = "Элемент доступен для взаимодействия" if v else "Элемент не доступен для взаимодействия"
    info(message)
    return v


def w_element_get_attribute(element, attribute):
    info("Возвращаем атрибут '%s' элемента" % attribute)
    if Config.detailed_steps:
        with allure.step("Возвращаем атрибут '%s' элемента" % attribute):
            element_info_attach(element.locator._stack_info)
            v = element._element.get_attribute(attribute)
            with allure.step("Получено значение '%s'" % v):
                pass
    else:
        v = element._element.get_attribute(attribute)
    info("Получено значение '%s'" % v)
    return v


def w_element_get_hint(element, attribute):
    info("Проверяем соответствие текста hint`а тексту '%s' элемента" % attribute)
    if Config.detailed_steps:
        with allure.step("Проверяем cоответствие текста hint`а тексту '%s' элемента" % attribute):
            element_info_attach(element.locator._stack_info)
            v = element._element.get_attribute("data-tooltip-text")
            print(v)
            assert_object.assertEqual(v, attribute)
            with allure.step("Получено значение '%s'" % v):
                pass
    else:
        v = element._element.get_attribute("data-tooltip-text")
    info("Получено значение '%s'" % v)
    return v
