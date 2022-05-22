from lib import *

button_reestr_camera = s(xpath = '//a[@class="dropdown-toggle" and contains(text(), "Реестр камер")]/span')
button_camera = s(xpath ='//a[@href="/system/camera/list"]')
button_create = s(xpath = '//a[@href = "/system/camera/create"]')
field_IDBK = s(xpath = '//input[@id = "numericExtId"]')
field_vsmKey = s(xpath = '//input[@id = "vsmKey"]')
field_name = s(xpath = '//input[@id = "name"]')
field_description = s(xpath = '//textarea[@id = "description"]')
field_cameraUrl = s(xpath = '//input[@id = "cameraUrl"]')
field_additionalUrl = s(xpath = '//input[@id = "additionalUrl"]')
field_cameraVideoUsername = s(xpath = '//input[@id = "cameraVideoUsername"]')
field_cameraVideoPassword = s(xpath = '//input[@id = "cameraVideoPassword"]')
field_archiveDepth = s(xpath = '//input[@id = "archiveDepth"]')
field_shortName = s(xpath = '//input[@id = "shortName"]')
field_address = s(xpath = '//input[@id = "address"]')
field_lat = s(xpath = '//input[@id = "lat"]')
field_lng = s(xpath = '//input[@id = "lng"]')
field_ip = s(xpath = '//input[@id = "ip"]')
button_district = s(xpath = '//select[@id = "district.id"]//option[@value="131"]')
button_apiTypeHide = s(xpath = '//select[@id = "apiTypeHide"]//option[@value="NETRIS"]')
button_cameraType = s(xpath = '//select[@id = "cameraType.id"]//option[@value="7753"]')
button_serverId = s(xpath = '//select[@id = "serverId"]//option[@value="eeb5293c-f47e-4622-beb3-234d8d7176f5"]')
button_checkbox_cameraGroup = s(xpath = '//input[@value = "13919"]')
button_create_enter = s(xpath='//input[@class = "btn btn-default btn-success"]')

variables = {
    "IDBK": "9215032",
    "vsmKey": "9215032_1",
    "name": "autotest",
    "description": "autotest",
    "cameraUrl": "rtsp://10.31.128.49:2033/rtsp___82.138.10.141_555_ch01.264_dev_0/live",
    "additionalUrl": "rtsp://10.31.128.49:2033/rtsp___82.138.10.141_555_ch01.264_dev_0",
    "cameraVideoUsername": "autotest",
    "cameraVideoPassword": "autotest",
    "archiveDepth": "10",
    "shortName": "autotest",
    "lat": "37",
    "lng": "55",
    "address": "autotest",
    "ip": "10.31.128.254"
    }
class TestEx(TestCase):
    def test_1(self):
        button_reestr_camera.click()
        button_camera.click()
        button_create.click()
        field_IDBK.send_keys(variables["IDBK"])
        field_vsmKey.send_keys(variables["vsmKey"])
        field_name.send_keys(variables["name"])
        field_cameraUrl.send_keys(variables["cameraUrl"])
        #field_additionalUrl.send_keys(variables["additionalUrl"])
        field_cameraVideoUsername.send_keys(variables["cameraVideoUsername"])
        field_cameraVideoPassword.send_keys(variables["cameraVideoPassword"])
        field_archiveDepth.send_keys(variables["archiveDepth"])
        field_shortName.send_keys(variables["shortName"])
        field_address.send_keys(variables["address"])
        field_lat.send_keys(variables["lat"])
        field_lng.send_keys(variables["lng"])
        field_ip.send_keys(variables["ip"])
        button_district.click()
        button_apiTypeHide.click()
        button_cameraType.click()
        button_serverId.click()
        button_checkbox_cameraGroup.click()
        button_create_enter.click()
        sleep(5)
