#from lib.finder import s
#from unittest import TestCase

from lib import *
button_reestr_camera = s(xpath = '//a[@class="dropdown-toggle" and contains(text(), "Реестр камер")]/span')
button_type_camera = s(xpath ='//a[@href="/system/cameraType"]')
button_create = s(xpath = '//a[@class="create"]/..')
field_name = s(xpath = '//input[@id = "name"]')
field_color = s(xpath = '//input[@id = "color"]')
field_description = s(xpath = '//input[@id = "description"]')
field_visible = s(xpath = '//input[@id = "visible"]')
button_create_enter = s(xpath = '//input[@class="save"]')
variables = {
    "name": "autotest",
    "color": "000000",
    "description": "autotest"
}
class TestEx(TestCase):
    def test_1(self):
        sleep(3)
        button_reestr_camera.click()
        button_type_camera.click()
        button_create.click()
        field_name.send_keys(variables["name"])
        field_color.send_keys(variables["color"])
        field_description.send_keys(variables["description"])
        field_visible.click()
        button_create_enter.click()
        sleep(3)