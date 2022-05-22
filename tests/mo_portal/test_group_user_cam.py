from lib import *

button_reestr_camera = s(xpath = '//a[@class="dropdown-toggle" and contains(text(), "Реестр камер")]/span')
button_camera = s(xpath ='//ul[@class="dropdown-menu"]//a[@href="/system/cameraGroup/list"][1]')
button_create = s(xpath = '//a[@href = "/system/cameraGroup/create"]')
field_nameGroup= s(xpath = '//input[@id = "name"]')
field_description = s(xpath = '//input[@id = "description"]')
box_Groupmobile_camera = s (xpath = '//input[@id = "mobileGroup"]')
box_GroupTS_camera = s (xpath = '//input[@id = "transportGroup"]')
button_create_box = s (xpath = '//input[@id = "create"]')

variables = {
    "name": "autotest",
    "description": "autotest"
}

class TestEx(TestCase):
    def test_1(self):
        button_reestr_camera.click()
        button_camera.click()
        button_create.click()
        sleep(5)
        field_nameGroup.send_keys(variables["name"])
        field_description.send_keys(variables["description"])
        box_Groupmobile_camera.click()
        box_GroupTS_camera.click()
        button_create_box.click()