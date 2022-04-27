# Включает в себя тесты из файлов loaderAndMap.json и supportAndInformation.json
from lib import *
import allure
from allure import title, step


el = {
    "Кнопка закрытия плеера": s("[data-player-command='close']", wait=20),
    "Форма поддержки": s("[data-widget-name='SupportButton']", wait=30),
    "Сообщение технической поддержки": s(css='div.ui-window-content > div > p'),
    "Номер технической поддержки": s(css='div.tel'),
    "Кнопка закрытия формы поддержки": s(css="div.support-window .ui-window-close")
}

body = s(tag_name="body")


@allure.feature('Форма с информацией о поддержке ресурса')
class TestSupportInfo(TestCase):

    @title('Нажимаем кнопку закрытия плеера')
    def test_1_click_camera_close_button(self):
        """Закрываем плеер для проверки формы обращения в поддержку"""
        with step("Нажимаем на кнопку закрытия плеера"):
            el["Кнопка закрытия плеера"].click()

    @allure.title('Проверяем текст и Нажимаем на кнопку открытия формы поддержки')
    def test_2_assert_support_button(self):
        with step("Проверяем название кнопки открытия формы поддержки"):
            el["Форма поддержки"].assert_element_text_contains("Сообщить о проблеме")
        with step("Нажимаем кнопку открытия формы поддержки"):
            el["Форма поддержки"].assert_element_interaction()
            el["Форма поддержки"].click()

    @allure.title('Проверяем наличие текста обращения в СТП. Должен присутствовать текст (Обратиться в службу технической поддержки можно по телефону:)')
    def test_3_assert_support_text(self):
        el["Сообщение технической поддержки"].assert_element_existence_and_displayed()
        el["Сообщение технической поддержки"].assert_element_text(
            'Обратиться в службу технической поддержки можно по телефону:')

    @allure.title("Проверяем наличие номера телефона СТП. Должен присутствовать номер телефона ('8 (495) 587-00-02')")
    def test_4_assert_support_phone_number_text(self):
        el["Номер технической поддержки"].assert_element_existence_and_displayed()
        el["Номер технической поддержки"].assert_element_text("8 (495) 587-00-02")

    @allure.title('Нажимаем на кнопку закрытия формы поддержки')
    def test_5_click_support_button_close(self):
        el["Кнопка закрытия формы поддержки"].assert_element_existence_and_displayed()
        el["Кнопка закрытия формы поддержки"].click()
