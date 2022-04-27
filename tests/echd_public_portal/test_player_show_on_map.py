from lib import *
from allure import title, step, feature

el = {
    "Окно плеера": s(".media-container-window",wait=30),
    "Опции плеера": s("[data-tooltip-key='js.camera.player.options.bar']"),
    "Показать на карте": s("[data-command='showOnMap'] .ui-option-text"),
    "Список элементов меню": s("[data-player-container='optionsMenu'] .ui-options-menu"),
    "Кнопка закрытия формы уведомления": s(".ui-close", wait=30)
}


@feature('Работа с плеером: Отображение камеры на карте через меню опций плеера')
class TestPlayerShowOnMap(TestCase):

    @title('Закрываем окно с уведомлением об ответственности за распространение ссылок на обмен видео')
    def test_1_close_notification_form(self):
        el["Кнопка закрытия формы уведомления"].assert_element_existence_and_displayed()
        sleep(5)
        el["Кнопка закрытия формы уведомления"].click()

    @title("Проверяем наличие окна плеера на странице")
    def test_2_player_existence(self):
        el["Окно плеера"].assert_element_existence_and_displayed()

    @title("Нажимаем кнопку опций плеера для отображения списка опций")
    def test_3_player_options_on(self):
        el["Опции плеера"].assert_element_existence_and_displayed()
        el["Опции плеера"].click()

    @title("Проверяем текст и нажимаем кнопку отображения камеры на карте из меню опций плеера")
    def test_4_player_options_show_on_map(self):
        el["Показать на карте"].assert_element_existence_and_displayed()
        el["Показать на карте"].assert_element_text("Показать на карте")
        el["Показать на карте"].click()
