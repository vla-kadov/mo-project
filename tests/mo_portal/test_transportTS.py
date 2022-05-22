from lib import *

button_spravochniki = s(xpath = '//a[@href = "#"][contains(text(), "Справочники")]')
button_transport = s(xpath ='//a[@href = "/system/transport/list"][contains(text(), "Транспортные средства")]')
button_create = s(xpath = '//a[@href = "/system/transport/create"]')
field_extId = s(xpath = '//input[@id="extId"]')
field_ip = s(xpath = '//input[@id="ip"]')
field_bnso = s(xpath = '//input[@id="bnso"]')
field_gosNomer = s(xpath = '//input[@id="registrationNumber"]')
select_transportType = s(xpath = '//select[@id="transportType"]//option[@value="BUS"]')
button_create_box = s (xpath = '//input[@id = "create"]')

variables = {
    "extId": "9215032",
    "ip": "10.186.254.199",
    "bnso": "18030999999",
    "gosNomer": "н756750auto"
    }

class TestEx(TestCase):
    def test_1(self):
        button_spravochniki.click()
        button_transport.click()
        button_create.click()
        field_extId.send_keys(variables["extId"])
        field_ip.send_keys(variables["ip"])
        field_bnso.send_keys(variables["bnso"])
        field_gosNomer.send_keys(variables["gosNomer"])
        select_transportType.click()
        button_create_box.click()