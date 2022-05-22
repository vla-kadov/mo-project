#from lib.finder import s
#from unittest import TestCase

from lib import *
button_spravochniki_camera = s(xpath = '//a[@class="dropdown-toggle" and contains(text(), "Реестр камер")]/span')
button_district = s(xpath = '//a[@href="/system/district/index"] [1]')
button_create = s(xpath = '//a[@class="create"]/..')
field_name = s(xpath = '//input[@id = "name"]')
field_color = s(xpath = '//input[@id = "color"]')
field_description = s(xpath = '//input[@id = "description"]')
button_create_enter = s(xpath = '//input[@class="save"]')
variables = {
    "name": "autotest",
    "color": "#fc6566",
    "description": "autotest"
}
class TestEx(TestCase):
    def test_1(self):
        sleep(3)
        button_spravochniki_camera.click()
        sleep(2)
        button_district.click()
        sleep(2)
        button_create.click()
        field_name.send_keys(variables["name"])
        field_color.send_keys(variables["color"])
        field_description.send_keys(variables["description"])
        button_create_enter.click()
        sleep(3)