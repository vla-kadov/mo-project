# Включает в себя тесты из файлов loaderAndMap.json и supportAndInformation.json
from lib import *
import allure
from allure import title, step


el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Кнопка открытия формы раскладок": s("[data-tooltip-key='hint.presets.open'] .title"),
    "Заголовок форма раскладок": s("[data-bind='visible: options.showTitleOnTop'] [data-bind='html: options.titleText']"),
    "Кнопка выхода из портала": s(".presets-user-exit[data-bind='text: options.userExit, click: exit']")
}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}


@allure.feature('Функционал работы с раскладками: Выход пользователя из портала через форму раскладок')
class TestLayoutLogout(TestCase):

    @title('Авторизуемся на портале')
    def test_1_auth_success(self):
        with step("Вводим логин/пароль и нажимаем кнопку входа на портал"):
            el["Поле ввода логина"].send_keys(variables["username"])
            el["Поле ввода пароля"].send_keys(variables["password"])
            el["Кнопка входа"].click()

    @title('Нажимаем кнопку открытия формы раскладок и проверяем факт открытия')
    def test_2_assert_layout_open(self):
        with step("Нажимаем кнопку открытия формы работы с раскладками"):
            el["Кнопка открытия формы раскладок"].click()
        with step("Проверяем факт успешного открытия формы"):
            el["Заголовок форма раскладок"].assert_element_existence_and_displayed()
            el["Заголовок форма раскладок"].assert_element_text("Раскладки")

    @title('Проверяем текст и наличие кнопки выхода пользователя из портала через форму раскладок')
    def test_3_asert_layout_logout_button(self):
        el["Кнопка выхода из портала"].assert_element_existence_and_displayed()
        el["Кнопка выхода из портала"].assert_element_text("Выйти")

    @title('Нажимаем кнопку выхода пользователя из портала и проверяем факт успешного выхода')
    def test_4_asert_layout_logout(self):
        with step("Нажимаем кнопку выхода пользователя из портала через форму работы с раскладками"):
            el["Кнопка выхода из портала"].click()
        with step("Проверяем наличие страницы авторизации после нажатии кнопки выхода"):
            el["Поле ввода пароля"].assert_element_existence_and_displayed()
