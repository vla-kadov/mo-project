from lib import *
from allure import title, step, feature

el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Кнопка открытия списка камер": s(".widgets-search-panel-header"),
    "Кнопка открытия 1 камеры в списке": ss(".camera-item")[0],
    "Окно плеера": s(".media-container-window", wait=30),
    "Выйти из режима архива": s(".container [data-tooltip-key='hint.player.turn.archive.off'] div"),
    "Включение паузы в лайв режиме": s(".container [data-tooltip-key='hint.player.pause'] div"),
    "Выключение паузы в лайв режиме": s(".container [data-tooltip-key='hint.player.resume'] div")
}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}


@feature('Работа с плеером: Постановка лайв трансляции на паузу')
class TestPlayerLiveModePause(TestCase):

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
        sleep(10)

    @title("Проверяем наличие окна плеера на странице")
    def test_3_player_existence(self):
        el["Окно плеера"].assert_element_interaction()

    @title("Включаем режим паузы в режиме лайв трансляции")
    def test_4_player_live_mode_pause_on(self):
        el["Включение паузы в лайв режиме"].assert_element_interaction()
        el["Включение паузы в лайв режиме"].click()

    @title("Выключаем режим паузы в режиме лайв трансляции")
    def test_5_player_live_mode_pause_off(self):
        el["Выключение паузы в лайв режиме"].assert_element_interaction()
        el["Выключение паузы в лайв режиме"].click()
