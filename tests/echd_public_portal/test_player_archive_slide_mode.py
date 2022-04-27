from lib import *
from allure import title, step, feature

el = {
    "Окно плеера": s(".media-container-window",wait=30),
    "Перезагрузить видеопоток": s(".container [data-tooltip-key='hint.player.camera.reconnect'] div", wait=10),
    "Режим просмотра кадрами": s(".container [data-tooltip-key='hint.player.camera.slide.mode'] div", wait=10),
    "Загрузить текущий кадр в покадровом режиме просмотра": s(".container [data-tooltip-key='hint.player.camera.slide.next'] div", wait=10),
    "Вернуться в стандартный режим просмотра": s(".container [data-tooltip-key='hint.player.camera.play.video'] div", wait=10),
    "Кнопка 1 минуту вперёд": s("[data-tooltip-key='hint.archive.next_part_text']", wait=10),
    "Кнопка 1 секунда вперёд": s("[data-tooltip-key='hint.archive.next_step']", wait=10),
    "Кнопка 1 минуту назад": s("[data-tooltip-key='hint.archive.previous_part_text']", wait=10),
    "Кнопка 1 секунда назад": s("[data-tooltip-key='hint.archive.previous_step']", wait=10),

    "Кнопка закрытия формы уведомления": s(".ui-close", wait=30)
}


@feature('Работа с плеером: Покадровый просмотр видео в режиме архива')
class TestPlayerArchiveSlideMode(TestCase):

    @title('Закрываем окно с уведомлением об ответственности за распространение ссылок на обмен видео')
    def test_1_close_notification_form(self):
        el["Кнопка закрытия формы уведомления"].assert_element_existence_and_displayed()
        sleep(5)
        el["Кнопка закрытия формы уведомления"].click()

    @title("Проверяем наличие окна плеера на странице")
    def test_2_player_existence(self):
        el["Окно плеера"].assert_element_interaction()

    @title("Нажимаем кнопку включения просмотра видео в покадровом режиме")
    def test_3_player_slide_mod_on(self):
        el["Режим просмотра кадрами"].assert_element_interaction()
        el["Режим просмотра кадрами"].click()

    @title("Нажимаем кнопку получения нового кадра в режиме покадрового просмотра видео")
    def test_4_player_slide_mod_new_slide(self):
        el["Загрузить текущий кадр в покадровом режиме просмотра"].assert_element_interaction()
        sleep(1)
        el["Загрузить текущий кадр в покадровом режиме просмотра"].click()

    @title("Проверяем хинт-подсказку к кнопке позиционирования '1 минуту  вперёд '")
    def test_5_player_slide_mod_next_part_hint(self):
        el["Кнопка 1 минуту вперёд"].assert_element_existence_and_displayed()
        sleep(1)
        el["Кнопка 1 минуту вперёд"].assert_hint_text("1 минуту  вперед ")

    @title("Нажимаем кнопку позиционирования '1 минуту  вперёд '")
    def test_6_player_slide_mod_next_part(self):
        el["Кнопка 1 минуту вперёд"].click()

    @title("Проверяем хинт-подсказку к кнопке позиционирования '1 секунда вперед '")
    def test_7_player_slide_mod_next_step_hint(self):
        el["Кнопка 1 секунда вперёд"].assert_element_existence_and_displayed()
        sleep(1)
        el["Кнопка 1 секунда вперёд"].assert_hint_text("1 секунда вперед ")

    @title("Нажимаем кнопку позиционирования '1 секунда вперед '")
    def test_8_player_slide_mod_next_step(self):
        el["Кнопка 1 секунда вперёд"].click()

    @title("Проверяем хинт-подсказку к кнопке позиционирования '1 секунда назад '")
    def test_9_player_slide_mod_previous_step_hint(self):
        el["Кнопка 1 секунда назад"].assert_element_existence_and_displayed()
        sleep(1)
        el["Кнопка 1 секунда назад"].assert_hint_text("1 секунда назад ")

    @title("Нажимаем кнопку позиционирования '1 секунда назад '")
    def test_10_player_slide_mod_previous_step(self):
        el["Кнопка 1 секунда назад"].click()

    @title("Проверяем хинт-подсказку к кнопке позиционирования '1 минуту  назад '")
    def test_11_player_slide_mod_previous_part_hint(self):
        el["Кнопка 1 минуту назад"].assert_element_existence_and_displayed()
        el["Кнопка 1 минуту назад"].assert_hint_text("1 минуту  назад ")

    @title("Нажимаем кнопку позиционирования '1 минуту  назад '")
    def test_12_player_slide_mod_previous_part(self):
        el["Кнопка 1 минуту назад"].click()

    @title("Нажимаем кнопку выхода из режимма покадрового просмотра видео")
    def test_13_player_slide_mod_off(self):
        el["Вернуться в стандартный режим просмотра"].click()

    @title("Нажимаем кнопку перезагрузки видеопотока")
    def test_14_player_refresh_video(self):
        el["Перезагрузить видеопоток"].click()
