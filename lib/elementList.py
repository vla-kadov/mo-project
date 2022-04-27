# -*- coding: utf-8 -*-
from lib.element import Element
from lib.finder import Locator


class ElementList(list):
    """
    Список элементов.
    По факту совесем даже не список, больше обертка над локатором.
    На каждое действие перезапрашивает элементы.
    """
    # TODO после поиска возвращается обычный список, можно ли возвращать ElementList

    def __init__(self, locator=None):
        super().__init__()
        self.locator = locator

    def __bool__(self):
        return len(self) > 0

    def __len__(self):
        return len(self.locator.search())

    def __getitem__(self, item):
        if isinstance(item, slice):
            locator = Locator(operation_type='slice', slice=item, chain=self.locator)
            return ElementList(locator)
        else:
            locator = Locator(operation_type='slice int', slice=item, chain=self.locator)
            return Element(locator)

    def __iter__(self):
        for el in self.locator.search():
            yield Element(None, element=el)

    def find(self):
        """ реализовать поиск всех элементов """
        return [Element(locator=self.locator, element=i) for i in self.locator.search()]

    def _find(self):
        """ реализовать поиск всех элементов """
        return [Element(locator=self.locator, element=i) for i in self.locator._search()]

    # TODO реализовать find_more_that_zero (поиск всех элементов, и чтобы был хотя бы один)
    # TODO реализовать поиск с учетом количества (поиск всех элементов и проверка что их количество равно заданному)
