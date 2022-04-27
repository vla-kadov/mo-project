from lib import *
from allure import title, step, feature

el = {
    "Окно плеера": s(".media-container-window",wait=30),
    "Признак контрактной камеры": s(".contact-camera-icon"),
    "Свернуть плеер в миниатюру": s("[data-tooltip-key='hint.player.minimize']"),
    "Кнопка закрытия формы уведомления": s(".ui-close", wait=30)
}


@feature('Работа с плеером: Признак контрактной камеры')
class TestPlayerContractIcon(TestCase):

    @title('Закрываем окно с уведомлением об ответственности за распространение ссылок на обмен видео')
    def test_1_close_notification_form(self):
        el["Кнопка закрытия формы уведомления"].assert_element_existence_and_displayed()
        sleep(5)
        el["Кнопка закрытия формы уведомления"].click()

    @title("Проверяем наличие окна плеера на странице")
    def test_2_player_existence(self):
        el["Окно плеера"].assert_element_existence_and_displayed()

    @title("Проверяем наличие иконки-признака контрактной камеры")
    def test_3_contract_icon_existence(self):
        el["Признак контрактной камеры"].assert_element_existence_and_displayed()

    @title("Проверяем наличие иконки-признака контрактной камеры в режиме миниатюры")
    def test_4_contract_icon_existence_miniature(self):
        with step("Переводим плеер в режим миниатюры для проверки наличия иконки контрактной камеры в данном режиме"):
            el["Свернуть плеер в миниатюру"].mouse_click()
            sleep(10)
        with step("Проверяем наличие иконки-признака контрактной камеры в режиме миниатюры"):
            el["Признак контрактной камеры"].mouse_move_to_element()
            el["Признак контрактной камеры"].assert_element_existence_and_displayed()
