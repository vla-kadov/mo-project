from lib import *
button_spravochniki_camera = s(xpath = '//a[@href = "#"][contains(text(), "Справочники")]')
button_user = s(xpath = '//a[@href = "/system/user/search"]')
button_create = s(xpath = '//a[@href = "/system/user/create"]')
field_firstName = s(xpath = '//input[@id = "firstName"]')
field_lastName = s(xpath = '//input[@id = "lastName"]')
field_middleName = s(xpath = '//input[@id = "middleName"]')
field_phone = s(xpath = '//input[@id = "phone"]')
field_email = s(xpath = '//input[@id = "email"]')
field_username = s(xpath = '//input[@id = "username"]')
field_password = s(xpath = '//input[@id = "password"]')
field_type = s(xpath = '//input[@id = "type"]')
field_organization = s(xpath = '//input[@id = "organization"]')
field_organizationArea = s(xpath = '//input[@id = "organizationArea"]')
field_organizationUnit = s(xpath = '//input[@id = "organizationUnit"]')
field_position = s(xpath = '//input[@id = "position"]')
button_homeDistrict = s(xpath = '//select[@id = "homeDistrict"]//option[@value ="8"]')
button_priority = s(xpath = '//select[@id = "priority"]//option[@value ="0"]')
field_comment = s(xpath = '//input[@id = "comment"]')
button_checkbox_role = s(xpath = '//input[@id = "ROLE_ADMIN"]')
button_create_enter = s(xpath = '//button[@class = "btn btn-success pull-right"]')

variables = {
    "firstName": "autotest",
    "lastName": "autotest",
    "middleName": "autotest",
    "phone": "+1234567",
    "email": "autotest@auto.ru",
    "username": "autotest",
    "password": "autotest",
    "type": "autotest",
    "organization": "autotest",
    "organizationArea": "autotest",
    "organizationUnit": "autotest",
    "position": "autotest",
    "comment": "autotest",
    "ROLE_ADMIN": "autotest"
}
class TestEx(TestCase):
    def test_1(self):
        button_spravochniki_camera.click()
        button_user.click()
        button_create.click()
        field_firstName.send_keys(variables["firstName"])
        field_lastName.send_keys(variables["lastName"])
        field_middleName.send_keys(variables["middleName"])
        field_phone.send_keys(variables["phone"])
        field_email.send_keys(variables["email"])
        field_username.send_keys(variables["username"])
        field_password.send_keys(variables["password"])
        field_type.send_keys(variables["type"])
        field_organization.send_keys(variables["organization"])
        field_organizationUnit.send_keys(variables["organizationUnit"])
        field_organizationArea.send_keys(variables["organizationArea"])
        field_position.send_keys(variables["position"])
        field_comment.send_keys(variables["comment"])
        button_homeDistrict.click()
        button_priority.click()
        button_checkbox_role.click()
        button_create_enter.click()
        sleep(3)