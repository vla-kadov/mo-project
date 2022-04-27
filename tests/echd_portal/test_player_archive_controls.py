from lib import *
from allure import title, step, feature

el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Кнопка открытия списка камер": s(".widgets-search-panel-header"),
    "Кнопка открытия 1 камеры в списке": ss(".camera-item")[0],
    "Кнопка перехода в режим архива": s("[data-camera-option-command='videoArchive'][data-camera-option-argument='on']"),
    "Окно плеера": s(".media-container-window",wait=30),
    "Ускоренное воспроизведение назад": s("[data-command='rewind-play'] div"),
    "Текущая скорость воспроизведение назад": s("[data-command='rewind-play'] span"),
    "1 минута назад": s("[data-command='previous-part']"),
    "10 секунд назад": s("[data-command='previous-step']"),
    "Пауза": s("[data-command='pause'] div"),
    "Воспроизведение": s("[data-command='normal-play']"),
    "Кадр вперёд": s("[data-command='next-step']"),
    "1 минута вперёд": s("[data-command='next-part']"),
    "Ускоренное воспроизведение вперёд": s("[data-command='forward-play'] div"),
    "Текущая скорость воспроизведение вперёд": s("[data-command='forward-play'] span"),
    "Кнопка закрытия формы уведомления": s(".ui-close", wait=30)
}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}

@feature('Работа с плеером: Кнопки управления архивной трансляцией (скорость, постановка на паузу и т.д.')
class TestPlayerArchiveControls(TestCase):

    @title('Авторизуемся на портале')
    def test_1_auth_success(self):
        with step("Вводим логин/пароль и нажимаем кнопку входа на портал"):
            el["Поле ввода логина"].assert_element_displayed()
            el["Поле ввода логина"].send_keys(variables["username"])
            el["Поле ввода пароля"].send_keys(variables["password"])
            el["Кнопка входа"].click()

    @title('Нажимаем кнопку открытия списка камер и открываем первую камеру списка')
    def test_2_camera_list_open_camera(self):
        el["Кнопка открытия списка камер"].assert_element_displayed()
        el["Кнопка открытия списка камер"].click()
        el["Кнопка открытия 1 камеры в списке"].click()
        sleep(10)

    @title('Нажимаем кнопку перехода в режим архивной трансляции')
    def test_3_open_camera_archive(self):
        el["Кнопка перехода в режим архива"].click()
        sleep(10)

    @title("Проверяем наличие окна плеера на странице")
    def test_4_player_existence(self):
        el["Окно плеера"].assert_element_displayed()

    @title("Проверяем работу с кнопкой ускоренного воспроизведения вперёд (меняем скорости и проверяем факт их смены")
    def test_5_player_archive_controls_forward_play(self):
        with step("Нажимаем кнопку ускоренного воспроизведения вперёд для включения 2 скорости"):
            el["Ускоренное воспроизведение вперёд"].assert_element_displayed()
            el["Ускоренное воспроизведение вперёд"].click()
            el["Текущая скорость воспроизведение вперёд"].assert_element_text("2x")
        with step("Нажимаем кнопку ускоренного воспроизведения вперёд для включения 4 скорости"):
            el["Ускоренное воспроизведение вперёд"].click()
            el["Текущая скорость воспроизведение вперёд"].assert_element_text("4x")
        with step("Нажимаем кнопку ускоренного воспроизведения вперёд для включения 6 скорости"):
            el["Ускоренное воспроизведение вперёд"].click()
            el["Текущая скорость воспроизведение вперёд"].assert_element_text("6x")
        with step("Нажимаем кнопку ускоренного воспроизведения вперёд для включения 8 скорости"):
            el["Ускоренное воспроизведение вперёд"].click()
            el["Текущая скорость воспроизведение вперёд"].assert_element_text("8x")
        with step("Нажимаем кнопку ускоренного воспроизведения вперёд для включения 16 скорости"):
            el["Ускоренное воспроизведение вперёд"].click()
            el["Текущая скорость воспроизведение вперёд"].assert_element_text("16x")
        with step("Нажимаем кнопку ускоренного воспроизведения вперёд для включения 32 скорости"):
            el["Ускоренное воспроизведение вперёд"].click()
            el["Текущая скорость воспроизведение вперёд"].assert_element_text("32x")
        with step("Немного проигрываем архив вперёд перед выполнением следующих тестов"):
            sleep(10)

    @title("Проверяем хинт-подсказку к кнопке позиционирования на 1 минуту вперёд")
    def test_6_player_archive_controls_next_part_hint(self):
        el["1 минута вперёд"].assert_hint_text("1 минута вперёд")

    @title("Нажимаем кнопку позиционирования на 1 минуту вперёд")
    def test_7_player_archive_controls_next_part(self):
        el["1 минута вперёд"].click()

    @title("Проверяем хинт-подсказку к кнопке позиционирования на 1 секунду вперёд")
    def test_8_player_archive_controls_next_step_hint(self):
        el["Кадр вперёд"].assert_hint_text("1 секунда вперёд")

    @title("Нажимаем кнопку позиционирования на 1 секунду вперёд")
    def test_9_player_archive_controls_next_step(self):
        el["Кадр вперёд"].click()

    @title("Проверяем кнопку постановки видео на паузу и снятия с паузы")
    def test_10_player_archive_controls_pause_play(self):
        with step("Снимаем воспроизведение с паузы"):
            el["Воспроизведение"].assert_element_displayed()
            el["Воспроизведение"].click()
            sleep(2)
        with step("Ставим воспроизведение не паузу"):
            el["Пауза"].assert_element_displayed()
            el["Пауза"].click()

    @title("Проверяем хинт-подсказку к кнопке позиционирования на 10 секунд назад")
    def test_11_player_archive_controls_previous_step_hint(self):
        el["10 секунд назад"].assert_element_displayed()
        el["10 секунд назад"].assert_hint_text("10 секунд назад")

    @title("Нажимаем кнопку позиционирования на 10 секунд назад")
    def test_12_player_archive_controls_previous_step(self):
        el["10 секунд назад"].assert_element_displayed()
        el["10 секунд назад"].click()

    @title("Проверяем хинт-подсказку позиционирования на 1 минуту назад")
    def test_13_player_archive_controls_previous_part_hint(self):
        el["1 минута назад"].assert_hint_text("1 минута назад")

    @title("Нажимаем кнопку позиционирования на 1 минуту назад")
    def test_14_player_archive_controls_previous_part(self):
        el["1 минута назад"].click()

    @title("Проверяем работу кнопки ускоренного воспроизведения назад. Меняем скорости и проверяем факт их смены")
    def test_15_player_archive_controls_rewind_play(self):
        with step("Нажимаем кнопку ускоренного воспроизведения назад для включения 2 скорости"):
            el["Ускоренное воспроизведение назад"].click()
            el["Текущая скорость воспроизведение назад"].assert_element_text("2x")
        with step("Нажимаем кнопку ускоренного воспроизведения назад для включения 4 скорости"):
            el["Ускоренное воспроизведение назад"].click()
            el["Текущая скорость воспроизведение назад"].assert_element_text("4x")
        with step("Нажимаем кнопку ускоренного воспроизведения назад для включения 6 скорости"):
            el["Ускоренное воспроизведение назад"].click()
            el["Текущая скорость воспроизведение назад"].assert_element_text("6x")
        with step("Нажимаем кнопку ускоренного воспроизведения назад для включения 8 скорости"):
            el["Ускоренное воспроизведение назад"].click()
            el["Текущая скорость воспроизведение назад"].assert_element_text("8x")
        with step("Нажимаем кнопку ускоренного воспроизведения назад для включения 16 скорости"):
            el["Ускоренное воспроизведение назад"].click()
            el["Текущая скорость воспроизведение назад"].assert_element_text("16x")
        with step("Нажимаем кнопку ускоренного воспроизведения назад для включения 32 скорости"):
            el["Ускоренное воспроизведение назад"].click()
            el["Текущая скорость воспроизведение назад"].assert_element_text("32x")
