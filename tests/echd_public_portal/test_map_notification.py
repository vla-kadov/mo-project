from lib import *
from allure import title, step, feature


el = {
    "Карта": s("#main[style='opacity: 1;']", wait=50),
    "Форма с уведомлением": s(".notification-message"),
    "Кнопка закрытия формы уведомления": s(".ui-close")
}


@feature('Уведомление об ответственности за распространение видео с ресурса "Обмен видео"')
class TestMapNotification(TestCase):

    @title('Проверяем загрузку карты на портале')
    def test_1_check_map_loading(self):
        """Проверяем наличие лоадера на стартовой странице портала"""
        with step("Проверяем что загрузилась карта"):
            el["Карта"].assert_element_displayed()

    @title('Находим форму с уведомлением')
    def test_2_assert_notification_form(self):
            el["Форма с уведомлением"].assert_element_existence_and_displayed()

    @title('Проверяем текст заголовка формы с уведомлением')
    def test_3_assert_notification_form_head(self):
        header=el["Форма с уведомлением"].s(xpath_text="Уважаемый пользователь!")
        header.assert_element_text("Уважаемый пользователь!")

    @title('Проверяем текст тела формы с уведомлением')
    def test_4_assert_notification_form_body(self):
        body=el["Форма с уведомлением"].s(css="[data-bind='html: message'] [style='text-align: justify']")
        body.assert_element_text_contains("Вы получили доступ к информации, хранящейся в государственной информационной системе «Единый центр хранения и обработки данных» (ЕЦХД). В данной системе обрабатывается информация ограниченного доступа, поступающая с камер городской системы видеонаблюдения.")

    @title('Закрываем формы с уведомлением')
    def test_5_close_notification_form(self):
        el["Кнопка закрытия формы уведомления"].click()
