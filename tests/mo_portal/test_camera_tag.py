from lib import *

button_reestr_camera = s(xpath = '//a[@class="dropdown-toggle" and contains(text(), "Реестр камер")]/span')
button_cameraTag = s(xpath ='//a[@href = "/system/tag"]')
button_create = s(xpath = '//a[@href = "/system/tag/create"]')
field_label = s(xpath = '//input[@id = "name"]')
box_availability_portal = s(xpath = '//input[@id = "visible"]')
field_position = s(xpath = '//input[@id = "position"]')
variables = {
    "name": "autotest",
    "position": "autotest"
}
class TestEx(TestCase):
    def test_1(self):
        button_reestr_camera.click()
        button_cameraTag.click()
        button_create.click()
        field_label.send_keys(variables["name"])
        box_availability_portal.click()
        field_position.send_keys(variables["position"])
