from lib import *

button_spravochniki = s(xpath = '//a[@href = "#"][contains(text(), "Справочники")]')
button_serverAxxon = s(xpath ='//a[@href="/system/axxon/list"][contains(text(), "Сервера Axxon")]')
button_create = s(xpath = '//a[@href = "/system/axxon/create"]')
field_extId = s(xpath = '//input[@id="extId"]')
field_name = s(xpath = '//input[@id="title"]')
field_host = s(xpath = '//input[@id="hostname"]')
field_port = s(xpath = '//input[@id="port"]')
field_username = s(xpath = '//input[@id="username"]')
field_password = s(xpath = '//input[@id="password"]')
button_create_box = s (xpath = '//input[@id = "create"]')

variables = {
    "extId": "SDC-BR-2022",
    "title": "transport_axxon_autotest",
    "hostname": "10.31.135.311",
    "port": "80",
    "username": "root",
    "password": "root"
    }

class TestEx(TestCase):
    def test_1(self):
        button_spravochniki.click()
        button_serverAxxon.click()
        button_create.click()
        field_extId.send_keys(variables["extId"])
        field_name.send_keys(variables["title"])
        field_host.send_keys(variables["hostname"])
        field_port.send_keys(variables["port"])
        field_username.send_keys(variables["username"])
        field_password.send_keys(variables["password"])
        button_create_box.click()