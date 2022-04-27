from lib import *
from allure import title, step, feature

el = {
    "Окно плеера": s(".media-container-window",wait=30),
    "Иконка камеры": s(".camera-marker"),
    "Кнопка закрытия окна камеры": s(css='div.media-container-window .ui-glossy-button.close'),
    "Кнопка закрытия формы уведомления": s(".ui-close", wait=30)
}


@feature('Работа с плеером: Закрытие и открытие с карты')
class TestPlayerCloseReopen(TestCase):

    @title('Закрываем окно с уведомлением об ответственности за распространение ссылок на обмен видео')
    def test_1_close_notification_form(self):
        el["Кнопка закрытия формы уведомления"].assert_element_existence_and_displayed()
        sleep(5)
        el["Кнопка закрытия формы уведомления"].click()

    @title("Проверяем наличие окна плеера на странице")
    def test_2_player_existence(self):
        el["Окно плеера"].assert_element_existence_and_displayed()

    @title("Нажимаем кнопку закрытия плеера")
    def test_3_close_player(self):
        el["Кнопка закрытия окна камеры"].click()

    @title("Нажимаем на иконку камеры на карте для открытия плеера")
    def test_4_open_player(self):
        el["Иконка камеры"].click()
