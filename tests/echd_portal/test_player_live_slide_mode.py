from lib import *
from allure import title, step, feature

el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Кнопка открытия списка камер": s(".widgets-search-panel-header"),
    "Кнопка открытия 1 камеры в списке": ss(".camera-item")[0],
    "Окно плеера": s(".media-container-window", wait=30),
    "Перезагрузить видеопоток": s(".container [data-tooltip-key='hint.player.camera.reconnect'] div", wait=10),
    "Режим просмотра кадрами": s(".container [data-tooltip-key='hint.player.camera.slide.mode'] div", wait=10),
    "Загрузить текущий кадр в покадровом режиме просмотра": s(".container [data-tooltip-key='hint.player.camera.slide.next'] div", wait=10),
    "Вернуться в стандартный режим просмотра": s(".container [data-tooltip-key='hint.player.camera.play.video'] div", wait=10),
    "Выйти из режима архива": s(".container [data-tooltip-key='hint.player.turn.archive.off'] div"),
    "Включить автообновления кадров": s(".container [data-tooltip-key='hint.player.slide.show.start'] div"),
    "Выключить автообновления кадров": s(".container [data-tooltip-key='hint.player.slide.show.stop'] div")
}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}


@feature('Работа с плеером: Покадровый просмотр видео в режиме лайв трансляции')
class TestPlayerLiveSlideMode(TestCase):

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

    @title("Нажимаем кнопку включения просмотра видео в покадровом режиме в live видео")
    def test_4_player_slide_mod_on(self):
        el["Режим просмотра кадрами"].assert_element_existence_and_displayed()
        el["Режим просмотра кадрами"].click()

    @title("Нажимаем кнопку получения нового кадра в режиме покадрового просмотра live видео")
    def test_5_player_slide_mod_new_slide(self):
        sleep(5)
        el["Загрузить текущий кадр в покадровом режиме просмотра"].assert_element_existence_and_displayed()
        el["Загрузить текущий кадр в покадровом режиме просмотра"].click()

    @title("Включаем режим автообновления кадров режиме покадрового просмотра live видео")
    def test_6_player_slide_mod_auto_play_on(self):
        el["Включить автообновления кадров"].assert_element_existence_and_displayed()
        el["Включить автообновления кадров"].click()

    @title("Отключаем режим автообновления кадров режиме покадрового просмотра live видео")
    def test_7_player_slide_mod_auto_play_off(self):
        el["Выключить автообновления кадров"].assert_element_existence_and_displayed()
        el["Выключить автообновления кадров"].click()

    @title("Нажимаем кнопку выхода из режимма покадрового просмотра видео")
    def test_8_player_slide_mod_off(self):
        el["Вернуться в стандартный режим просмотра"].click()

    @title("Нажимаем кнопку перезагрузки видеопотока")
    def test_9_player_refresh_video(self):
        el["Перезагрузить видеопоток"].click()
