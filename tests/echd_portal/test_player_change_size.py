from lib import *
from allure import title, step, feature

el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Кнопка открытия списка камер": s(".widgets-search-panel-header"),
    "Кнопка открытия 1 камеры в списке": ss(".camera-item")[0],
    "Окно плеера": s(".media-container-window", wait=30),
    "Кнопка растягивания окна плеера": s("[data-tooltip-key='hint.player.size.expand']"),
    "Кнопка возврата исходного размера плеера после растягивания": s("[data-tooltip-key='hint.player.size.restore']"),
    "Вход в полноэкранный режим плеера": s("[data-player-command='maximumSize']"),
    "Выход из полноэкранного режима плеера": s("[data-tooltip-key='hint.player.fullscreen.off']")

}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}

@feature('Работа с плеером: Изменение размера плеера')
class TestPlayerChangeSize(TestCase):

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
        el["Окно плеера"].assert_element_existence_and_displayed()

    @title("Нажимаем кнопку разворачивания плеера по доступной области экрана (не fullscreen)")
    def test_4_expand_player_size(self):
        el["Кнопка растягивания окна плеера"].click()

    @title("Нажимаем кнопку возврата с исходный размер плеера")
    def test_5_restore_expand_player_size(self):
        el["Кнопка возврата исходного размера плеера после растягивания"].click()

    @title("Нажимаем кнопку перевода плеера в полноэкранный режим трансляции")
    def test_6_full_screen_player_size(self):
        el["Вход в полноэкранный режим плеера"].click()

    @title("Нажимаем кнопку отключения полноэкранного режима трансляции в плеере")
    def test_7_restore_full_screen_player_size(self):
        el["Выход из полноэкранного режима плеера"].click()
