from lib import *
from allure import title, step, feature

el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Кнопка открытия списка камер": s(".widgets-search-panel-header"),
    "Кнопка открытия 1 камеры в списке": ss(".camera-item")[0],
    "Окно плеера": s(".media-container-window",wait=30),
    "Опции плеера": s("[data-tooltip-key='js.camera.player.options.bar']"),
    "Показать на карте": s("[data-command='showOnMap'] .ui-option-text"),
    "Список элементов меню": s("[data-player-container='optionsMenu'] .ui-options-menu")
}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}


@feature('Работа с плеером: Отображение камеры на карте через меню опций плеера')
class TestPlayerShowOnMap(TestCase):

    @title('Авторизуемся на портале')
    def test_1_auth_success(self):
        with step("Вводим логин/пароль и нажимаем кнопку входа на портал"):
            el["Поле ввода логина"].send_keys(variables["username"])
            el["Поле ввода пароля"].send_keys(variables["password"])
            el["Кнопка входа"].click()

    @title('Нажимаем кнопку открытия списка камер и открываем первую камеру списка')
    def test_2_camera_list_open_camera(self):
        el["Кнопка открытия списка камер"].click()
        el["Кнопка открытия 1 камеры в списке"].click()

    @title("Проверяем наличие окна плеера на странице")
    def test_3_player_existence(self):
        el["Окно плеера"].assert_element_existence_and_displayed()

    @title("Нажимаем кнопку опций плеера для отображения списка опций")
    def test_4_player_options_on(self):
        el["Опции плеера"].assert_element_existence_and_displayed()
        el["Опции плеера"].click()

    @title("Проверяем текст и нажимаем кнопку отображения камеры на карте из меню опций плеера")
    def test_5_player_options_show_on_map(self):
        el["Показать на карте"].assert_element_existence_and_displayed()
        el["Показать на карте"].assert_element_text("Показать на карте")
        el["Показать на карте"].click()
