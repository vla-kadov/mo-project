# Включает в себя тесты из файлов loaderAndMap.json и supportAndInformation.json
from lib import *
import allure
from allure import title, step


el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Кнопка открытия формы раскладок": s("[data-tooltip-key='hint.presets.open'] .title"),
    "Кнопка открытия списка типов раскладок": s("[data-tooltip-key='hint.simple.presets.toggle.config.selection']"),
    "Выбор раскладки типа 1 на 2": s("[data-tooltip-text='Открыть раскладку 1 на 2']"),
    "Выбор раскладки типа 2 на 2": s("[data-tooltip-text='Открыть раскладку 2 на 2']"),
    "Выбор раскладки типа 3 на 4": s("[data-tooltip-text='Открыть раскладку 3 на 4']"),
    "Выбор раскладки типа 5 + 1": s("[data-tooltip-text='Открыть раскладку на 5 + 1 камеру']"),
    "Выбор раскладки типа 7 + 1": s("[data-tooltip-text='Открыть раскладку на 7 + 1 камеру']"),
    "Выбор раскладки типа 10 + 1": s("[data-tooltip-text='Открыть раскладку на 10 + 1 камеру']"),
    "Выбор раскладки типа 1 на 1": s("[data-tooltip-text='Открыть раскладку 1 на 1']"),
    "Кнопки выбора камер в раскладке": ss(".no-camera")
}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}


@allure.feature('Функционал работы с раскладками: Смена типов раскладок')
class TestLayoutTypes(TestCase):

    @title('Авторизуемся на портале')
    def test_1_auth_success(self):
        with step("Вводим логин/пароль и нажимаем кнопку входа на портал"):
            el["Поле ввода логина"].send_keys(variables["username"])
            el["Поле ввода пароля"].send_keys(variables["password"])
            el["Кнопка входа"].click()

    @title('Проверяем текст и наличие кнопки открытия формы раскладок')
    def test_2_assert_layout_button(self):
        el["Кнопка открытия формы раскладок"].assert_element_existence_and_displayed()
        el["Кнопка открытия формы раскладок"].assert_element_text_contains("Раскладки")

    @title('Нажимаем кнопку открытия формы работы с раскладками')
    def test_3_click_layout_button(self):
        el["Кнопка открытия формы раскладок"].click()

    @title('Проверяем включение раскладки типа 1 на 1')
    def test_4_assert_layout_1_1_type(self):
        with step("Нажимаем кнопку выбора типа раскладки"):
            el["Кнопка открытия списка типов раскладок"].click()
        with step("Проверяем наличие хинта-подсказки типа раскадки 1 на 1"):
            el["Выбор раскладки типа 1 на 1"].assert_hint_text("Открыть раскладку 1 на 1")
        with step("Выбираем тип раскадки 1 на 1"):
            el["Выбор раскладки типа 1 на 1"].click()
        with step("Проверяем, что больше 1 камеры в раскладке указать нельзя - типа выбран корректно"):
            el["Кнопки выбора камер в раскладке"][0].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][0].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][1].assert_element_not_existence()

    @title('Проверяем включение раскладки типа 1 на 2')
    def test_5_assert_layout_1_2_type(self):
        with step("Нажимаем кнопку выбора типа раскладки"):
            el["Кнопка открытия списка типов раскладок"].click()
        with step("Проверяем наличие хинта-подсказки типа раскадки 1 на 2"):
            el["Выбор раскладки типа 1 на 2"].assert_hint_text("Открыть раскладку 1 на 2")
        with step("Выбираем тип раскадки 1 на 2"):
            el["Выбор раскладки типа 1 на 2"].click()
        with step("Проверяем, что больше 2 камер в раскладке указать нельзя - типа выбран корректно"):
            el["Кнопки выбора камер в раскладке"][0].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][0].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][1].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][1].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][2].assert_element_not_existence()

    @title('Проверяем включение раскладки типа 2 на 2')
    def test_6_assert_layout_2_2_type(self):
        with step("Нажимаем кнопку выбора типа раскладки"):
            el["Кнопка открытия списка типов раскладок"].click()
        with step("Проверяем наличие хинта-подсказки типа раскадки 2 на 2"):
            el["Выбор раскладки типа 2 на 2"].assert_hint_text("Открыть раскладку 2 на 2")
        with step("Выбираем тип раскадки 2 на 2"):
            el["Выбор раскладки типа 2 на 2"].click()
        with step("Проверяем, что больше 4 камер в раскладке указать нельзя - типа выбран корректно"):
            el["Кнопки выбора камер в раскладке"][0].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][0].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][1].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][1].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][2].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][2].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][3].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][3].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][4].assert_element_not_existence()

    @title('Проверяем включение раскладки типа 3 на 4')
    def test_7_assert_layout_3_4_type(self):
        with step("Нажимаем кнопку выбора типа раскладки"):
            el["Кнопка открытия списка типов раскладок"].click()
        with step("Проверяем наличие хинта-подсказки типа раскадки 3 на 4"):
            el["Выбор раскладки типа 3 на 4"].assert_hint_text("Открыть раскладку 3 на 4")
        with step("Выбираем тип раскадки 3 на 4"):
            el["Выбор раскладки типа 3 на 4"].click()
        with step("Проверяем, что больше 12 камер в раскладке указать нельзя - типа выбран корректно"):
            el["Кнопки выбора камер в раскладке"][0].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][0].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][1].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][1].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][2].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][2].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][3].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][3].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][4].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][4].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][5].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][5].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][6].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][6].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][7].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][7].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][8].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][8].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][9].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][9].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][10].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][10].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][11].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][11].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][12].assert_element_not_existence()

    @title('Проверяем включение раскладки типа 5 + 1')
    def test_8_assert_layout_5_1_type(self):
        with step("Нажимаем кнопку выбора типа раскладки"):
            el["Кнопка открытия списка типов раскладок"].click()
        with step("Проверяем наличие хинта-подсказки типа раскадки 5 + 1"):
            el["Выбор раскладки типа 5 + 1"].assert_hint_text("Открыть раскладку на 5 + 1 камеру")
        with step("Выбираем тип раскадки 5 + 1"):
            el["Выбор раскладки типа 5 + 1"].click()
        with step("Проверяем, что больше 6 камеры в раскладке указать нельзя - типа выбран корректно"):
            el["Кнопки выбора камер в раскладке"][0].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][0].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][1].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][1].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][2].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][2].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][3].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][3].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][4].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][4].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][5].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][5].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][6].assert_element_not_existence()

    @title('Проверяем включение раскладки типа 7 + 1')
    def test_9_assert_layout_7_1_type(self):
        with step("Нажимаем кнопку выбора типа раскладки"):
            el["Кнопка открытия списка типов раскладок"].click()
        with step("Проверяем наличие хинта-подсказки типа раскадки 7 + 1"):
            el["Выбор раскладки типа 7 + 1"].assert_hint_text("Открыть раскладку на 7 + 1 камеру")
        with step("Выбираем тип раскадки 7 + 1"):
            el["Выбор раскладки типа 7 + 1"].click()
        with step("Проверяем, что больше 8 камеры в раскладке указать нельзя - типа выбран корректно"):
            el["Кнопки выбора камер в раскладке"][0].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][0].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][1].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][1].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][2].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][2].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][3].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][3].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][4].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][4].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][5].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][5].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][6].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][6].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][7].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][7].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][8].assert_element_not_existence()

    @title('Проверяем включение раскладки типа 10 + 1')
    def test_10_assert_layout_10_1_type(self):
        with step("Нажимаем кнопку выбора типа раскладки"):
            el["Кнопка открытия списка типов раскладок"].click()
        with step("Проверяем наличие хинта-подсказки типа раскадки 10 + 1"):
            el["Выбор раскладки типа 10 + 1"].assert_hint_text("Открыть раскладку на 10 + 1 камеру")
        with step("Выбираем тип раскадки 10 + 1"):
            el["Выбор раскладки типа 10 + 1"].click()
        with step("Проверяем, что больше 11 камеры в раскладке указать нельзя - типа выбран корректно"):
            el["Кнопки выбора камер в раскладке"][0].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][0].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][1].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][1].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][2].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][2].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][3].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][3].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][4].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][4].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][5].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][5].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][6].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][6].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][7].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][7].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][8].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][8].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][9].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][9].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][10].assert_element_existence_and_displayed()
            el["Кнопки выбора камер в раскладке"][10].assert_element_text("Камера не выбрана")
            el["Кнопки выбора камер в раскладке"][11].assert_element_not_existence()
