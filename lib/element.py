from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import selenium.common.exceptions

from lib.finder import s, ss, Locator
from lib.all_methods import *
from lib import driver


class Element:
    """Ленивая обертка для selenium'ного элемента"""

    def __init__(self, locator: Locator = None, element: WebElement = None):
        """
            Можно инициализировать либо локатором, либо уже найденым элементом оригинального selenium-а.
            В первом случае элемент можно будет "обновлять" по локатору, во втором - элемент фиксированный.
        """
        if not (locator or element):
            raise ValueError()

        self.locator: Locator = locator  # Список локаторов/фильтров/срезов для поиска элемента
        self._element: WebElement = element  # Элемент классического WebElement-а, если есть и/или найден
        self._id = None

        self.element_name = ""
        self._set_element_name()

    def set_element_name(self, element_name):
        """ Метод для явного задания имени элемента вручную """
        self.element_name = '"' + element_name + '"'
        return self

    def _set_element_name(self):
        if self.locator:
            self.element_name = self.locator._set_element_name()

    def __eq__(self, element):
        """ Сравнение двух элементов """
        element.find()
        return hasattr(element, '_id') and self._id == element._id

    def __ne__(self, element):
        return not self.__eq__(element)

    def __bool__(self):
        """ Метод bool для проверки, найден ли элемент """
        try:
            self.find()
            return True
        except:
            return False

    def __str__(self):
        return self.element_name

    def _scroll_to_visible(self):
        """ Скрол страницы до видимости элемента """
        self._element._parent.execute_script('arguments[0].scrollIntoView();', self._element)

    # property #########################################################################################################

    @property
    def id(self):
        """ Возвращает id элемента """
        return self._id

    @property
    def original_webelement(self):
        """ Врзвращает объект классического WebElenemt-а """
        self.find()
        return self._element

    @property
    def text(self) -> str:
        """ Возвращает текст элемена """
        return w_element_text(self)

    @property
    def placeholder(self) -> str:
        """ Возвращает текст элемена """
        return w_element_placeholder(self)

    @property
    def tag_name(self) -> str:
        """ Возвращает имя тега элемента """
        self.find()
        return str(self._element.tag_name)

    @property
    def inner_html(self) -> str:
        """ Возвращает htmt-код который находится ВНУТРИ элемента """
        self.find()
        return str(self._element.get_attribute('innerHTML'))

    @property
    def outer_html(self) -> str:
        """ Возвращает htmt-код который находится ВНУТРИ элемента """
        return str(self._element.get_attribute('outerHTML'))

    @property
    def tag_html(self):
        """ Возвращает html-код верхнего тега найденного элемента (содержащий искомый локатор) """
        self.find()
        return str(self.outer_html[:self.outer_html.find('>') + 1])

    @property
    def size(self):
        """ Возвращает список - размер элемента """
        val = self._element.size
        return [val['width'], val['height']]

    @property
    def width(self):
        val = self._element.size
        return val['width']

    @property
    def height(self):
        val = self._element.size
        return val['height']

    @property
    def location(self):
        """ Возвращает список с координатами элемента """
        return [self._element.location['x'], self._element.location['y']]

    @property
    def x(self) -> int:
        """ х-коорината элемента """
        return int(self._element.location['x'])

    @property
    def y(self) -> int:
        """ у-координата элемента """
        return int(self._element.location['y'])

    # Поиск элемента ###################################################################################################

    def find(self, wait=Config.wait_timeout):
        """
            Поиск элемента. Выделяется несколько вариантов
            1. Если у объекта нет оригинального веб-элемента ("if not self._element") - осуществляем поиск "с нуля"
            2. Если элемент находился в рамках одной сессии (запуск браузера), а потом повторно пытается использоваться
                в другой сессии (например перезапускали браузер,
                см. проверку self._element._parent.session_id != driver.current.driver.session_id), то осуществляем
                повторный поиск элемента
            3. Если элемент находился ранее, а потом произошло изменение страницы, то элемент считается неактуальным и
                неприкрепленным к странице. В этом случае опять же осуществляется повторный поиск
            4. В остальных случаях пользуемся ранее найденным элементом без перепоиска
        """

        # Вариант 1
        try:
            if not self._element:
                # Ищем элемент впервые
                self._element: WebElement = self.locator.search(element_name=self.element_name, reason="ff", wait=wait)
                self._id = self._element._id
            else:
                # Вариант 2
                if self._element._parent.session_id != driver.current.driver.session_id:
                    # Обновился браузер/сессия
                    self._element: WebElement = self.locator.search(element_name=self.element_name, reason="sr", wait=wait)
                    self._id = self._element._id
                else:
                    # Вариант 3
                    el = None
                    try:
                        self._element.is_enabled()
                        el = self._element
                    except:
                        pass
                    if not el:
                        self._element: WebElement = self.locator.search(element_name=self.element_name, reason="rf",
                                                                        wait=wait)
                        self._id = self._element._id
        except selenium.common.exceptions.StaleElementReferenceException:
            time.sleep(10)
            self._element: WebElement = self.locator.search(element_name=self.element_name, reason="ff", wait=wait)
            self._id = self._element._id
        except:
            pass
        return self

    def _find(self, wait=None):
        """ Метод аналогичен методу find, но он не оставляет "следов" в репорте и логах (используется внутри движка в
            некоторых местах дабы не перегружать отчеты избыточной повторной информацией) """
        if not self._element:
            self._element: WebElement = self.locator._search(wait=wait)
            self._id = self._element._id
        else:
            if self._element._parent.session_id != driver.current.driver.session_id:
                self._element: WebElement = self.locator._search(wait=wait)
                self._id = self._element._id
            else:
                el = None
                try:
                    self._element.is_enabled()
                    el = self._element
                except:
                    pass
                if not el:
                    self._element: WebElement = self.locator._search(wait=wait)
                    self._id = self._element._id
        return self

    def is_find(self, wait=None) -> bool:
        """ Возвращает True если элемент найден, и False - если нет """
        try:
            self.find(wait=wait)
            return True
        except:
            return False

    def _is_find(self, wait=None) -> bool:
        """ Тот же is_find но без логирования """
        try:
            self._find(wait=wait)
            return True
        except:
            return False

    def s(self, *args, **kwargs):

        # Не несущий никакой функциональности код, но благодаря нему PyCharm добавляет автокомплит типов локатора
        kwargs.get('id')
        kwargs.get('css')
        kwargs.get('xpath')
        kwargs.get('class_name')
        kwargs.get('text')
        kwargs.get('xpath_text')
        kwargs.get('value')
        kwargs.get('type')
        kwargs.get('name')
        kwargs.get('tag_name')
        kwargs.get('wait')

        return s(*args, chain=self.locator, **kwargs)

    def ss(self, *args, **kwargs):

        # Не несущий никакой функциональности код, но благодаря нему PyCharm добавляет автокомплит типов локатора
        kwargs.get('id')
        kwargs.get('css')
        kwargs.get('xpath')
        kwargs.get('class_name')
        kwargs.get('text')
        kwargs.get('xpath_text')
        kwargs.get('value')
        kwargs.get('type')
        kwargs.get('name')
        kwargs.get('tag_name')
        kwargs.get('wait')

        return ss(*args, chain=self.locator, **kwargs)

    def s_parent(self):
        return s(xpath="..", chain=self.locator)

    # Методы элемента ##################################################################################################

    def sleep(self, time_to_sleep=1):
        """ Пауза выполнения """
        w_sleep(time_to_sleep)
        return self

    def click(self):
        """ Клик по элементу """
        self.find()
        w_element_click(self)
        return self

    def send_keys(self, value):
        """ Ввод значения с клавиатуры """
        self.find()
        w_element_send_keys(self, value)
        return self

    def send_hot_keys(self, value):
        """ Ввод значения с клавиатуры """
        self.find()
        w_element_send_hot_keys(self, value)
        return self

    def press_enter(self):
        """ Нажатие клавиши ENTER на выбранном элементе """
        self.find()
        self.send_keys(Keys.ENTER)
        return self

    def press_escape(self):
        """ Нажатие клавиши ESCAPE на выбранном элементе """
        self.find()
        self.send_keys(Keys.ESCAPE)
        return self

    def clear(self):
        """ Очистка выбранного элемента (например поля ввода от ранее введенных данных) """
        self.find()
        w_element_clear(self)
        return self

    def get_value(self) -> str:
        """ Возвращает значение атрибута value """
        self.find()
        return str(self._element.get_attribute('value'))

    def get_css(self, value):
        """ Возвращает значение выбранного css-свойства объекта """
        self.find()
        return str(self._element.value_of_css_property(str(value)))

    def get_attribute(self, attribute_name):
        """ Возвращаем заданный атрибут """
        self.find()
        return w_element_get_attribute(self, attribute_name)

    def assert_hint_text(self, attribute_name):
        """ Возвращаем заданный атрибут """
        self.find()
        return w_element_get_hint(self, attribute_name)
    # Методы основанные на ActionChains ################################################################################

    def mouse_click(self):
        """ Клик мышью по элементу """
        self.find()
        w_element_mouse_click(self)
        return self

    def mouse_move_to_element(self):
        """ Перевод курсора мыши на элемент """
        self.find()
        w_mouse_move_to_element(self)
        return self

    # TODO добавить другие методы из ActionChains. Часть методов перенести в driver
    # click_and_hold
    # context_click
    # double_click
    # drag_and_drop
    # key_down, key_up
    # И другие методы при необходимости

    def attach_allure_screenshot(self):
        """ Делаем скриншот элемента и аттачим в allure """
        self.find()
        w_element_attach_allure_screenshot(self)

    # is_ - булевы проверки свойств элемента ###########################################################################

    def is_displayed(self) -> bool:
        """ Виден ли элемент на дисплее """
        self.find()
        v = w_element_is_displayed(self)
        return v

    def is_enabled(self) -> bool:
        """ Доступен ли элемент для взаимодействия """
        self.find()
        v = w_element_is_enabled(self)
        return v

    def is_selected(self) -> bool:
        """ Выбран ли элемент """
        self.find()
        v = w_element_is_selected(self)
        return v

    def is_check(self) -> bool:
        """ Чекнут ли элемент """
        self.find()
        v = bool(self._element.get_attribute('checked'))
        return v

    def is_text(self, txt) -> bool:
        self.find()
        v = txt == self.text
        return v

    def is_partial_text(self, txt) -> bool:
        """ Содержит ли элемент текст """
        self.find()
        v = txt in self.text
        return v

    def is_css_property(self, prop) -> bool:
        """ Имеет ли элемент указанное css-войство """
        self.find()
        v = bool(self.get_css(prop) == "")
        return v

    # Ассерты ##########################################################################################################

    def assert_element_existence(self):
        """ Проверяем что элемент существует на странице """
        w_assert_element_existence(self)
        return self

    def assert_element_existence_and_displayed(self):
        """ Проверяем что элемент существует на странице и видим """
        w_assert_element_existence(self)
        self.find(wait=Config.wait_timeout)
        w_assert_element_displayed(self)
        return self

    def assert_element_not_existence(self, wait=1):
        """ Проверяем что элемент не существует на странице """
        w_assert_element_not_existence(self, wait=wait)
        return self

    def assert_element_not_displayed(self):
        """ Проверяем что элемент не виден на странице """
        self.find()
        w_assert_element_not_displayed(self)
        return self

    def assert_element_text(self, text: str):
        """ Проверяем что текст элемента равен заданному """
        self.find()
        w_assert_element_text_equal(self, element_name=self.element_name, assertion_text=text)
        return self

    def assert_element_placeholder(self, text: str):
        """ Проверяем что подсказка поля ввода текста элемента равен заданному """
        self.find()
        w_assert_element_placeholder_text_equal(self, element_name=self.element_name, assertion_text=text)
        return self

    def assert_element_text_contains(self, text: str):
        """ Проверяем что текст элемента содержит заданную строку """
        self.find()
        w_assert_element_text_contains(self, text)
        return self

    def assert_element_text_not_equal(self, text: str):
        """ Проверяем что текст элемента не равен заданному """
        self.find()
        w_assert_element_text_not_equal(self, text)
        return self

    def assert_element_not_text(self):
        """ Проверяем что элемент не содержит текста """
        self.find()
        w_assert_element_not_text(self)
        return self

    def assert_element_enabled(self):
        """ Проверяем что элемент доступен для взаимодействия """
        self.find()
        w_assert_element_enabled(self)
        return self

    def assert_element_not_enabled(self):
        """ Проверяем что элемент не доступен для взаимодействия """
        self.find()
        w_assert_element_not_enabled(self)
        return self

    def assert_element_displayed(self):
        """ Проверяем что элемент отображается на экране """
        self.find()
        w_assert_element_displayed(self)
        return self

    def assert_element_interaction(self):
        """ Проверяем что элемент доступен для взаимодействия """
        self.assert_element_existence_and_displayed()
        self.assert_element_enabled()
        return self

    def assert_element_have_class(self, class_name):
        """ Проверяем что элемент содержит в себе указанный класс """
        self.find()
        w_assert_element_have_class(self, class_name)
        return self

    def assert_element_not_have_class(self, class_name):
        """ Проверяем что элемент не содержит в себе указанный класс """
        self.find()
        w_assert_element_not_have_class(self, class_name)
        return self

    def assert_element_have_attribute(self, attribute):
        """ Проверяем что элемент содержит в себе указанный атрибут """
        self.find()
        w_assert_element_have_attribute(self, attribute)
        return self

    def assert_element_not_have_attribute(self, attribute):
        """ Проверяем что элемент содержит в себе указанный атрибут """
        self.find()
        w_assert_element_not_have_attribute(self, attribute)
        return self

    # TODO подумать о добавлении простейших проверок верстки
    #  местопожение в рамках интервала
    #  местоположение относительно страницы
    #  местоположение относительно других элементов
