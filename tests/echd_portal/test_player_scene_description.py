from lib import *
from allure import title, step, feature

el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Кнопка открытия списка камер": s(".widgets-search-panel-header"),
    "Кнопка открытия 1 камеры в списке": ss(".camera-item")[0],
    "Окно плеера": s(".media-container-window",wait=30),
    "Иконка камеры в плеере": s("[data-player='cameraTypeIcon']"),
    "Форма с описанием сцены обзора": s(".copy-to-clipboard"),
    "Кнопка закрытия описания сцены обзора": s(".copy-to-clipboard .ui-window-close"),
    "Кнопка отмены открытия описания сцены обзора": s("[data-action='close-window']"),
    "Кнопка копирования описания сцены обзора": s(".copy-to-clipboard-button")

}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}


@feature('Работа с плеером: Сцена обзора камеры')
class TestPlayerSceneDescription(TestCase):

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

    @title("Нажимаем на иконку камеры для отображения описания сцены обзора камеры")
    def test_4_scene_description_icon_existence(self):
        with step("Нажимаем на иконку камеры для отображения описания сцены обзора камеры"):
            el["Иконка камеры в плеере"].click()

    @title("Проверяем заголовок формы описания сцены обзора камеры")
    def test_5_scene_description_header_text(self):
        header = el["Форма с описанием сцены обзора"].s(".ui-window-header[data-drag-handle='true'] div")
        header.assert_element_text("Выбранная камера")

    @title("Проверяем наличие описания сцены обзора в форме")
    def test_6_scene_description_body_text(self):
        header = el["Форма с описанием сцены обзора"].ss(".copy-to-clipboard .ui-window-content div")[1]
        header.assert_element_text_contains("PVN")

    @title("Проверяем наличие описания сцены обзора в форме")
    def test_7_scene_description_copy_text(self):
        header = el["Форма с описанием сцены обзора"].s(".ui-window-content small")
        header.assert_element_text_contains("Для копирования текста в буфер обмена нажмите кнопку")

    @title("Проверяем текст кнопки отмены открытия формы")
    def test_8_scene_description_decline_button(self):
        el["Кнопка отмены открытия описания сцены обзора"].assert_element_text("Отмена")

    @title("Проверяем текст кнопки подтверждения копирования текста в буфер обмена")
    def test_9_scene_description_confirm_button(self):
        el["Кнопка копирования описания сцены обзора"].assert_element_text("ОК")

    @title("Закрываем форму с описанием сцены обзора камеры")
    def test_10_scene_description_close_button(self):
        el["Кнопка закрытия описания сцены обзора"].click()
