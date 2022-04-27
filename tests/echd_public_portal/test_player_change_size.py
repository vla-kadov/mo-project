from lib import *
from allure import title, step, feature

el = {
    "Окно плеера": s(".media-container-window",wait=30),
    "Кнопка растягивания окна плеера": s("[data-tooltip-key='hint.player.size.expand']"),
    "Кнопка возврата исходного размера плеера после растягивания": s("[data-tooltip-key='hint.player.size.restore']"),
    "Вход в полноэкранный режим плеера": s("[data-player-command='maximumSize']"),
    "Выход из полноэкранного режима плеера": s("[data-tooltip-key='hint.player.fullscreen.off']"),
    "Кнопка закрытия формы уведомления": s(".ui-close", wait=30)

}


@feature('Работа с плеером: Изменение размера плеера')
class TestPlayerChangeSize(TestCase):

    @title('Закрываем окно с уведомлением об ответственности за распространение ссылок на обмен видео')
    def test_1_close_notification_form(self):
        el["Кнопка закрытия формы уведомления"].assert_element_existence_and_displayed()
        sleep(5)
        el["Кнопка закрытия формы уведомления"].click()

    @title("Проверяем наличие окна плеера на странице")
    def test_2_player_existence(self):
        el["Окно плеера"].assert_element_existence_and_displayed()

    @title("Нажимаем кнопку разворачивания плеера по доступной области экрана (не fullscreen)")
    def test_3_expand_player_size(self):
        el["Кнопка растягивания окна плеера"].click()

    @title("Нажимаем кнопку возврата с исходный размер плеера")
    def test_4_restore_expand_player_size(self):
        el["Кнопка возврата исходного размера плеера после растягивания"].click()

    @title("Нажимаем кнопку перевода плеера в полноэкранный режим трансляции")
    def test_5_full_screen_player_size(self):
        el["Вход в полноэкранный режим плеера"].click()

    @title("Нажимаем кнопку отключения полноэкранного режима трансляции в плеере")
    def test_6_restore_full_screen_player_size(self):
        el["Выход из полноэкранного режима плеера"].click()
