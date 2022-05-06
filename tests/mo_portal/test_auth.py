#from lib.finder import s
#from unittest import TestCase

from lib import *
#from allure import title, step, feature

#edit_search = s(xpath='//*[@id="text"]')
#button_search = s(xpath='/html/body/table/tbody/tr[2]/td/form/div[2]/button')
#logo_main = s(xpath='/html/body/header/div/div/div[2]/a')

login_form = s(xpath = '//input[@id = "username"]')
password_form = s(xpath = '//input[@id = "password"]')
#zagolovokOsn = s(xpath = '//div[@data-test-id = "3e9p2b"]')
#dopPortal_name = s(xpath = '//div[@data-test-id = "n2hhpw"]')
logo_portal = s(xpath = '//div[@class = "customer-logo"]')
#url_text_portal = s(xpath = '//a[text() ="br.support@mosreg.ru"]')
button_enter = s(xpath = '//button[@data-test-id = "19kwuz"]')
button_control_panel = s(xpath = '//span[@class = "user-link"][contains(text(), "Панель управления")]')
button_reestr_camera = s(xpath = '//li[@class = "dropdown"]/li[@class = "dropdown open"][1]')
button_camera_type = s(xpath = '//a[@href="/system/cameraType"]')
#username_pole = s(xpath = '//label[@data-test-id="17kdzo"] [1]')
#password_pole = s(xpath = '//label[@data-test-id="17kdzo"] [2]')

variables = {
    "username": "admin",
    "password": "kvartalnov",
    #"error_username": "username_not_existence",
    #"error_password": "test_password"
}

class TestEx(TestCase):
    def test_1(self):
        #edit_search.send_keys("Vova")
        login_form.send_keys(variables["username"])
        password_form.send_keys(variables["password"])
        button_enter.click()
        logo_portal.assert_element_existence_and_displayed()
        sleep(5)
        button_control_panel.click()
        button_reestr_camera.click()
        button_camera_type.click()