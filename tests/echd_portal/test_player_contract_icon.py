from lib import *
from allure import title, step, feature

el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Кнопка открытия списка камер": s(".widgets-search-panel-header"),
    "Кнопка открытия 1 камеры в списке": ss(".camera-item")[0],
    "Окно плеера": s(".media-container-window",wait=30),
    "Признак контрактной камеры": s(".right-header-container .contact-camera-icon"),
    "Свернуть плеер в миниатюру": s("[data-tooltip-key='hint.player.minimize']")
}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}

@feature('Работа с плеером: Признак контрактной камеры')
class TestPlayerContractIcon(TestCase):

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

    @title("Проверяем наличие иконки-признака контрактной камеры")
    def test_4_contract_icon_existence(self):
        el["Признак контрактной камеры"].assert_element_existence_and_displayed()

    @title("Проверяем наличие иконки-признака контрактной камеры в режиме миниатюры")
    def test_5_contract_icon_existence_miniature(self):
        with step("Переводим плеер в режим миниатюры для проверки наличия иконки контрактной камеры в данном режиме"):
            el["Свернуть плеер в миниатюру"].mouse_click()
            sleep(10)
        with step("Проверяем наличие иконки-признака контрактной камеры в режиме миниатюры"):
            el["Признак контрактной камеры"].mouse_move_to_element()
            el["Признак контрактной камеры"].assert_element_existence_and_displayed()
