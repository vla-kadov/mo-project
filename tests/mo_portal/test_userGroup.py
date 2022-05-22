from lib import *

button_spravochniki = s(xpath = '//a[@href = "#"][contains(text(), "Справочники")]')
button_userGroup = s(xpath ='//a[@href = "/system/userGroup/search"]')
button_create = s(xpath = '//a[@href = "/system/userGroup/create"]')
field_nameGroup= s(xpath = '//input[@id = "name"]')
field_description = s(xpath = '//textarea[@id = "description"]')
button_create_box = s (xpath = '//input[@class = "save"]')

variables = {
    "name": "autotest",
    "description": "autotest"
}

class TestEx(TestCase):
    def test_1(self):
        button_spravochniki.click()
        sleep(1)
        button_userGroup.click()
        button_create.click()
        sleep(5)
        field_nameGroup.send_keys(variables["name"])
        field_description.send_keys(variables["description"])
        button_create_box.click()