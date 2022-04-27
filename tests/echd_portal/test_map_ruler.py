# Включает в себя тесты из файлов loaderAndMap.json и supportAndInformation.json
from lib import *
import allure
from allure import title, step


el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Линейка": s("[data-test-id='u22uhi'] [data-test-id='19kwuz']")
}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}


@allure.feature('Проверка функционала работы с линейкой на карте')
class TestMapRuler(TestCase):

    @title('Авторизуемся на портале')
    def test_1_auth_success(self):
        with step("Вводим логин/пароль и нажимаем кнопку входа на портал"):
            el["Поле ввода логина"].send_keys(variables["username"])
            el["Поле ввода пароля"].send_keys(variables["password"])
            el["Кнопка входа"].click()

    @title("Проверяем наличие и текст кнопки включения функционала линейки на карте")
    def test_2_map_ruler_button(self):
        el["Линейка"].assert_element_existence_and_displayed()
        el["Линейка"].assert_hint_text("Измерить расстояние")

    @title("Проверяем работу функционала линейки")
    def test_3_map_ruler_on_off(self):
        with step("Включаем функционал использования линейки"):
            el["Линейка"].mouse_click()
        with step("Выключаем функционал использования линейки"):
            el["Линейка"].mouse_click()
