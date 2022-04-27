import inspect

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from lib.config import Config
from lib.utils import highlight_and_screenshot, info, element_info_attach, Wait
from lib import driver


def s(*args, chain=None, **kwargs):
    """
        Ленивый поисковик элементов на странице.
        Поиск осуществляется при выполнении действия (клик, ввод данных, и т.п.), получения
        свойств (видимость, размер, координаты, и т.п.), или использовании метода find(). В качестве параметров
        метод может применять:

            именованные параметры. Например, передав именованный параметр href="/app/common/Login/", мы инициируем
            поиск элемента с соответствующим параметром. Список поддерживаемых параметров: id, id_contains, xpath,
            name, tag_name, class_value, class_name, css, text, link_text_contains, attr, text_contains, value,
            type, checked, selected, href, button, а так же wait (время поиска элемента). Прочие именованные
            параметры автоматически формируют поиск аттрибута с таким названием

            аргументы типа str. В таком случае они считаются css селекторами

        С помощью этого метода можно строить цепочку поиска с последующим действием, например
        s(Be.name("email)).s(href="/app/common/Login/").s("condision").click(). В случае ненахождения какого-либо
        элемента метод возбуждает исключение классического WebDriver-а
    """
    from .element import Element

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

    wait = kwargs.pop('wait', Config.wait_timeout)
    locator = Locator((args, kwargs), "s", wait, '//*', chain=chain)
    if not chain:
        locator.add_stack_info(inspect.getframeinfo(inspect.currentframe().f_back))
    return Element(locator=locator)


def ss(*args, chain=None, **kwargs):
    """
        Аналогия метода s(), с той разницей что возвращает список элементов, а не первый найденный элемент. В случае
        ненахождения элемента возвращает пустой список.
    """
    from .elementList import ElementList

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

    wait = kwargs.pop('wait', Config.wait_timeout)

    locator = Locator((args, kwargs), 'ss', wait, '//*', chain=chain)
    if not chain:
        locator.add_stack_info(inspect.getframeinfo(inspect.currentframe().f_back))
    return ElementList(locator)


def xpath_literal(xs):
    """ Вспомогательный метод формирования xpath-а"""
    if "'" not in xs:
        return "'%s'" % xs
    if '"' not in xs:
        return '"%s"' % xs
    return "concat('%s')" % xs.replace("'", "',\"'\",'")


def _list_common_elements(list1, list2):
    """ Сравнение двух списков и формирование списка, состоящего из неповторяющихся элементов обоих списков """
    # если не пустой только один, то возвращаем второй
    if not(list1 and list2):
        return list1 or list2 or []

    common = []
    for i1 in list1:
        for i2 in list2:
            if i2.id == i1.id:
                common.append(i2)
    res = []
    for item in common:
        if item not in res:
            res.append(item)
    return res


__ARG_TO_SELECTOR__ = {
    'id':
        lambda _xpath_prefix, val: (By.ID, val),
    'id_contains':
        lambda _xpath_prefix, val: (By.XPATH, '%s[contains(@id, %s)]' % (_xpath_prefix, xpath_literal(val))),
    'xpath':
        lambda _xpath_prefix, val: (By.XPATH, val),
    'name':
        lambda _xpath_prefix, val: (By.NAME, val),
    'tag_name':
        lambda _xpath_prefix, val: (By.TAG_NAME, val),
    'class_value':
        lambda _xpath_prefix, val: (By.XPATH, '%s[@class=%s]' % (_xpath_prefix, xpath_literal(val))),
    'class_name':
        lambda _xpath_prefix, val: (By.CLASS_NAME, val),
    'css':
        lambda _xpath_prefix, val: (By.CSS_SELECTOR, val),
    'text':
        lambda _xpath_prefix, val: (By.LINK_TEXT, val),
    'partial_link_text':
        lambda _xpath_prefix, val: (By.PARTIAL_LINK_TEXT, val),
    'attr':
        lambda _xpath_prefix, val: (By.XPATH, '%s[@%s]' % (_xpath_prefix, val)),
    'xpath_text':
        lambda _xpath_prefix, val: (By.XPATH,
                                    "%s[contains(text(),%s)]" % (_xpath_prefix, xpath_literal(val))),
    'text_contains':
        lambda _xpath_prefix, val: (By.XPATH,
                                    '%s/text()[contains(.,%s)]/..' % (_xpath_prefix, xpath_literal(val))),
    'value':
        lambda _xpath_prefix, val: (By.XPATH,
                                    '%s[@value=%s]' % (_xpath_prefix, xpath_literal(val))),
    'type':
        lambda _xpath_prefix, val: (By.XPATH,
                                    '%s[@type=%s]' % (_xpath_prefix, xpath_literal(val))),
    'checked':
        lambda _xpath_prefix, val: (By.XPATH,
                                    _xpath_prefix + ('[@checked]' if val else '[not(@checked)]')),
    'selected':
        lambda _xpath_prefix, val: (By.XPATH,
                                    _xpath_prefix + ('[@selected]' if val else '[not(@selected)]')),
    'href':
        lambda _xpath_prefix, val: (By.XPATH, '%s[@href=%s]' % (_xpath_prefix, xpath_literal(val))),
    'button':
        lambda _xpath_prefix, value: (By.XPATH, "%sinput[@type='submit' or @type='button' and @value='{0}']"
                                                 "|%sbutton[text()=%s]" % (_xpath_prefix, _xpath_prefix, value)),
    # Отказались от attribute_value, сохранено как шаблон
    'attribute_value':
        lambda _xpath_prefix, val: (By.XPATH,
                                    "%s[@%s=%s]" % (_xpath_prefix, val[0], xpath_literal(val[1])))
}


def _get_selector(_xpath_prefix, locator_type, locator):
    """ Получение конечного локатора для поиска элемента """
    func = __ARG_TO_SELECTOR__.get(locator_type, None)
    if func:
        end_locator = func(_xpath_prefix, locator)
    else:
        func = __ARG_TO_SELECTOR__.get('attribute_value', None)
        end_locator = func(_xpath_prefix, (locator_type, locator))
    return end_locator


class Locator:
    """ Класс локатора """

    def __init__(self, args=None, operation_type='s', wait=None, xpath_prefix='', slice=None, chain=None):
        """
            Объект класса Locator со следующими св-ми:
                operation_type - тип операции
                locator_list - список локаторов (словари {'type': тип_локатора , 'value': значение_локатора})
                wait - ожидание элемента
                xpath_prefix - xpath-префикс
                slice - срез (для списка элементов)
        """
        self.operation_type = operation_type        # Тип операции (s, ss, ss_s, slice, slice_int, filter)
        self.locator_list = self._parse_args(args)  # Список объектов-локаторов
        self.wait = wait                            # Ожидание
        self.xpath_prefix = xpath_prefix            # xpath prefix
        self.slice = slice                          # срез
        self.chain = chain  # предыдущий локатор

        self._stack_info = None
        if self.chain:
            self._stack_info = self.chain._stack_info

        self.element_name = ""

    def add_stack_info(self, info):
        self._stack_info = info

    def __str__(self):
        file_path = self._stack_info[0]
        line_number = self._stack_info[1]
        raw_code_str = self._stack_info[3]
        return "file '%s', line number %s, '%s'" % (file_path, str(line_number), raw_code_str)

    def _set_element_name(self):

        if self._stack_info:
            raw_code_str: str = self._stack_info[3][0].strip()
            try:
                if raw_code_str[0] == "'" or raw_code_str[0] == '"':
                    self.element_name = raw_code_str.split(":")[0].strip()
                else:
                    self.element_name = raw_code_str.split("=")[0].strip()
                    if "(" in self.element_name or ")" in self.element_name:
                        self.element_name = ""
            except:
                pass
        else:
            self.element_name = ""
        return self.element_name

    def chain(self, *args, **kwargs):
        return Locator(*args, chain=self, **kwargs)

    def search(self, element_name="", reason="rf", wait=None):

        # TODO если задан элемент типа
        #  (css=".widgets-map-layers-system-name", xpath_text=map_type).s(xpath="..").s(xpath_text=map_name)
        #  (несколько поисков один от другого), до мы заскриншотим и зааттачим конечный элемент, без промежуточных
        #  поисков. Стоит ли аттачить промежуточные поиски?

        if reason == "ff" or reason == "sr":
            message = "Осуществляем поиск элемента " + element_name
        else:
            message = "Осуществляем повторный поиск элемента " + element_name
        info(message)
        if Config.detailed_steps:
            with allure.step(message):
                element_info_attach(self._stack_info)
                r = self._search(wait=wait)
                if isinstance(r, WebElement):
                    with allure.step("Элемент найден"):
                        pass
                    highlight_and_screenshot(r)
                if isinstance(r, list):
                    for i in r:
                        highlight_and_screenshot(i)
        else:
            r = self._search(wait=wait)
        info("Поиск успешно выполнен")
        return r

    def _search(self, wait=None):
        """Поиск элементов по локаторам"""

        if self.chain:
            target = self.chain._search()
        else:
            target = driver.current

        if wait:
            w = wait
        else:
            w = self.wait

        if self.operation_type == 's':
            Wait(target, w).bool(lambda dd: self._find_first(target))
            result = self._find_first(target)
        elif self.operation_type == 'ss':
            Wait(target, w).bool(lambda dd: self._find_first(target))
            result = self._find_all(target)
        elif self.operation_type == "slice" or self.operation_type == "slice int":
            result = target[self.slice]
        else:
            raise ValueError(self.operation_type)
        return result

    def _find_first(self, base):
        """ Ф-я поиска элемента по списку локаторов """
        elements = None
        for locator in self.locator_list:
            _by, _value = _get_selector(self.xpath_prefix, locator['type'], locator['value'])
            found = base.find_elements(by=_by, value=_value)

            if not found:
                base.find_element(by=_by, value=_value)

            elements = _list_common_elements(elements, found)

        return elements[0]

    def _find_all(self, base):
        """ Ф-я поиска элементов по списку локаторов """
        elements = None
        for locator in self.locator_list:
            by, value = _get_selector(self.xpath_prefix, locator['type'], locator['value'])
            found = base.find_elements(by=by, value=value)
            elements = _list_common_elements(elements, found)

        return elements

    def _parse_args(self, args):
        if not args:
            return []
        else:
            args, kwargs = args
            return [{'type': 'css', 'value': v} for v in args] + [{'type': k, 'value': v} for k, v in kwargs.items()]
