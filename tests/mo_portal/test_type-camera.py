#from lib.finder import s
#from unittest import TestCase

from lib import *

button_creat = s(xpath = '//a[@class="create"]')

class TestEx(TestCase):
    def test_1(self):
        button_creat.click()