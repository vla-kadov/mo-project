# Включает в себя тесты из файла mapTypes.json
from lib import *
from allure import title, step, feature


@title('Находим чекбокс включения/выключения опции Яндекс Карт')
def checkbox_map_option(option_name):
    _checkbox_map_option = s(xpath_text=option_name).s_parent().s_parent().s(".ui-checkbox-icon").set_element_name(option_name)
    return _checkbox_map_option


el = {
    "Кнопка закрытия плеера": s("[data-player-command='close']", wait=20),
    "Текущий тип карты": s(".widgets-map-layers-header .ui-widget-title-content"),
    "Кнопка открытия форма выбора карты": s("div.widgets-map-layers-header.widget-toggle.ui-widget-title"),
    "Форма выбора карты": s("[data-widget-name='MapLayersPanel']"),
    "Чекбокс пробки": checkbox_map_option("Пробки"),
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Чекбокс дорожные события": checkbox_map_option("Дорожные события")
}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}

@feature("Работа с панелью выбора картографии")
class TestMapTypes(TestCase):

    @title('Авторизуемся на портале')
    def test_1_auth_success(self):
        with step("Вводим логин/пароль и нажимаем кнопку входа на портал"):
            el["Поле ввода логина"].send_keys(variables["username"])
            el["Поле ввода пароля"].send_keys(variables["password"])
            el["Кнопка входа"].click()

    @title("Проверяем название кнопки выбора картографии (дефолтная картография). Кнопка должна называться (Яндекс: Схема)")
    def test_2_camera_close(self):
        el["Текущий тип карты"].assert_element_interaction()
        el["Текущий тип карты"].assert_element_text("Яндекс: Схема")

    @title("Нажимаем кнопку открытия формы выбора типа картографии")
    def test_3_click_map_change_button_open(self):
        """Нажимаем кнопку открытия формы выбора типа картографии"""
        el["Кнопка открытия форма выбора карты"].click()
        el["Форма выбора карты"].assert_element_displayed()

    @title('Выбираем тип карты ЕГИП: Карта, и проверяем успешность выбора по заголовку формы выбора')
    def test_4_select_egip_map(self):
        """Выбираем тип карты ЕГИП Карта, и проверяем выбор по заголовку  формы выбора"""
        map_type=el["Форма выбора карты"].ss(".widgets-map-layers-system")[0].s(".widgets-map-layers-system-layers").ss(".widgets-map-layers-layer")[0]
        map_type.click()
        map_type.assert_element_interaction()
        map_type.assert_element_text("Карта")

    @title('Выбираем тип карты ЕГИП: Спутник, и проверяем успешность выбора по заголовку формы выбора')
    def test_5_select_egip_sputnik(self):
        """Выбираем тип карты ЕГИП Спутник, и проверяем выбор по заголовку  формы выбора"""
        map_type=el["Форма выбора карты"].ss(".widgets-map-layers-system")[0].s(".widgets-map-layers-system-layers").ss(".widgets-map-layers-layer")[1]
        map_type.click()
        map_type.assert_element_interaction()
        map_type.assert_element_text("Спутник")

    @title('Выбираем тип карты ЕГИП: Гибрид, и проверяем успешность выбора по заголовку формы выбора')
    def test_6_select_egip_hybrid(self):
        """Выбираем тип карты ЕГИП Схемы, и проверяем выбор по заголовку  формы выбора"""
        map_type=el["Форма выбора карты"].ss(".widgets-map-layers-system")[0].s(".widgets-map-layers-system-layers").ss(".widgets-map-layers-layer")[2]
        map_type.click()
        map_type.assert_element_interaction()
        map_type.assert_element_text("Гибрид")

    @title('Выбираем тип карты Яндекс: Схемы, и проверяем успешность выбора по заголовку формы выбора')
    def test_7_select_yandex_scheme(self):
        """Выбираем тип карты Яндекс Схема, и проверяем выбор по заголовку  формы выбора"""
        map_type=el["Форма выбора карты"].ss(".widgets-map-layers-system")[1].s(".widgets-map-layers-system-layers").ss(".widgets-map-layers-layer")[0]
        map_type.click()
        map_type.assert_element_interaction()
        map_type.assert_element_text("Схема")

    @title("Проверяем наличие чекбосов опций и подписей к ним")
    def test_8_assert_checkbox(self):
        """ Проверяем что есть чекбоксы Пробки и Дорожные работы и их названия """
        with step("Проверяем наличие чекбокса 'Пробки' и подписи к нему"):
            el["Чекбокс пробки"].assert_element_existence()
            el["Чекбокс пробки"].s_parent().s("[data-bind='text: mapToggle.name']").assert_element_text("Пробки")
        with step("Проверяем наличие чекбокса 'Дорожные события' и подписи к нему"):
            el["Чекбокс дорожные события"].assert_element_existence()
            el["Чекбокс дорожные события"].s_parent().s("[data-bind='text: mapToggle.name']").assert_element_text("Дорожные события")

    @title("Выбираем опцию 'Пробки'")
    def test_9_check_map_option_traffic_jam(self):
        """ Выбираем чекбокс Пробки, проверяем что он выбрался, а чекбокс Дорожные события - нет """
        with step('Находим чекбокс "Пробки" и кликаем по нему'):
            el["Чекбокс пробки"].click()
        with step('Проверяем что чекбокс "Пробки" чекнут'):
            el["Чекбокс пробки"].s_parent().assert_element_have_class("ui-checked")
        with step('Проверяем что чекбокс "Дорожные события" не чекнут'):
            el["Чекбокс дорожные события"].assert_element_not_have_class("ui-checked")

    @title("Снимаем опцию 'Пробки'")
    def test_10_uncheck_map_option_traffic_jam(self):
        """ Отжимаем чекбокс Пробки, проверяем что и он, и Дорожные события - не выбраны """
        with step('Находим чекбокс "Пробки" и кликаем по нему'):
            el["Чекбокс пробки"].click()
        with step('Проверяем что чекбокс "Пробки" не чекнут'):
            el["Чекбокс пробки"].s_parent().assert_element_not_have_class("ui-checked")
        with step('Проверяем что чекбокс "Дорожные события" не чекнут'):
            el["Чекбокс дорожные события"].s_parent().assert_element_not_have_class("ui-checked")

    @title("Выбираем опцию 'Дорожные события'")
    def test_11_check_map_option_road_events(self):
        """ Выбираем чекбокс Дорожные события, проверяем что и он, и Дорожные события - выбрались """
        with step('Находим чекбокс "Дорожные события" и кликаем по нему'):
            el["Чекбокс дорожные события"].click()
        with step('Проверяем что чекбокс "Пробки" чекнут'):
            el["Чекбокс пробки"].s_parent().assert_element_have_class("ui-checked")
        with step('Проверяем что чекбокс "Дорожные события" не чекнут'):
            el["Чекбокс дорожные события"].s_parent().assert_element_have_class("ui-checked")

    @title("Снимаем опцию 'Пробки' при выбранных 'Дорожные события'")
    def test_12_uncheck_map_option_traffic_jam_with_check_road_events(self):
        """ Снимаем опцию 'Пробки' при выбранных 'Дорожные события'. Должны сняться оба чекбокса """
        with step('Находим чекбокс "Дорожные события" и кликаем по нему'):
            el["Чекбокс пробки"].click()
        with step('Проверяем что чекбокс "Пробки" не чекнут'):
            el["Чекбокс пробки"].s_parent().assert_element_not_have_class("ui-checked")
        with step('Проверяем что чекбокс "Дорожные события" не чекнут'):
            el["Чекбокс дорожные события"].s_parent().assert_element_not_have_class("ui-checked")

    @title("Выбираем чекбокс 'Дорожные события' и затем отжимаем его")
    def test_13_check_and_uncheck_option_road_events(self):
        """ Выбираем чекбокс 'Дорожные события' и затем отжимаем его. Проверяем что чекбокс 'Пробки' остался выбранным """
        with step('Находим чекбокс "Дорожные события" и два раза кликаем по нему'):
            el["Чекбокс дорожные события"].click()
            el["Чекбокс дорожные события"].click()
        with step('Проверяем что чекбокс "Пробки" чекнут'):
            el["Чекбокс пробки"].s_parent().assert_element_have_class("ui-checked")
        with step('Проверяем что чекбокс "Дорожные события" не чекнут'):
            el["Чекбокс дорожные события"].s_parent().assert_element_not_have_class("ui-checked")
