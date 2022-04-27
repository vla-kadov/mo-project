from lib import *
from allure import title, step, feature

el = {
    "Окно плеера": s(".media-container-window",wait=30),
    "Выйти из режима архива": s(".container [data-tooltip-key='hint.player.turn.archive.off'] div"),
    "Включение паузы в лайв режиме": s(".container [data-tooltip-key='hint.player.pause'] div"),
    "Выключение паузы в лайв режиме": s(".container [data-tooltip-key='hint.player.resume'] div"),
    "Кнопка закрытия формы уведомления": s(".ui-close", wait=30)
}


@feature('Работа с плеером: Постановка лайв трансляции на паузу')
class TestPlayerLiveModePause(TestCase):

    @title('Закрываем окно с уведомлением об ответственности за распространение ссылок на обмен видео')
    def test_1_close_notification_form(self):
        el["Кнопка закрытия формы уведомления"].assert_element_existence_and_displayed()
        sleep(5)
        el["Кнопка закрытия формы уведомления"].click()

    @title("Проверяем наличие окна плеера на странице")
    def test_2_player_existence(self):
        el["Окно плеера"].assert_element_existence_and_displayed()

    @title("Переводим плеер в режим live трансляции")
    def test_3_player_live_mode_on(self):
        el["Выйти из режима архива"].assert_element_existence_and_displayed()
        el["Выйти из режима архива"].click()

    @title("Включаем режим паузы в режиме лайв трансляции")
    def test_4_player_live_mode_pause_on(self):
        el["Включение паузы в лайв режиме"].assert_element_existence_and_displayed()
        el["Включение паузы в лайв режиме"].click()

    @title("Выключаем режим паузы в режиме лайв трансляции")
    def test_5_player_live_mode_pause_off(self):
        el["Выключение паузы в лайв режиме"].assert_element_existence_and_displayed()
        el["Выключение паузы в лайв режиме"].click()