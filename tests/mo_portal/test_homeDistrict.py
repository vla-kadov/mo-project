from lib import *

button_spravochniki = s(xpath = '//a[@href = "#"][contains(text(), "Справочники")]')
button_homeDistrict = s(xpath ='//ul[@class="dropdown-menu"]//a[@href = "/system/homeDistrict/list"]')
button_create = s(xpath = '//a[@href = "/system/homeDistrict/create"]')
field_homeDistrict= s(xpath = '//input[@id = "name"]')
button_create_box = s (xpath = '//input[@id = "create"]')

variables = {
    "name": "autotest"
    }

class TestEx(TestCase):
    def test_1(self):
        button_spravochniki.click()
        button_homeDistrict.click()
        button_create.click()
        field_homeDistrict.send_keys(variables["name"])
        button_create_box.click()