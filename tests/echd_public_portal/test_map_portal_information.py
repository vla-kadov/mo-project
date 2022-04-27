# Включает в себя тесты из файлов loaderAndMap.json и supportAndInformation.json
from lib import *
import allure
from allure import title, step


el = {
    "Кнопка закрытия плеера": s("[data-player-command='close']", wait=30),
    "Кнопка информации о портале": s(css="#logo"),
    "Текст формы обучения": s(".widgets-information-panel-text span"),
    "Ссылка на adobe reader": s("[href='http://get.adobe.com/reader/']"),
    "Ссылка на руководство пользователя": s("[href='https://echd.mos.ru/files/echd_user2019_v.2.pdf']")
}

body = s(tag_name="body")


@allure.feature('Работа с формой информации о портале')
class TestMapPortalInformation(TestCase):

    @title('Проверяем закрытие плеера')
    def test_1_click_camera_close_button(self):
        """Проверяем закрытие плеера"""

        with step("Нажимаем на кнопку закрытия плеера"):
            el["Кнопка закрытия плеера"].click()

    @allure.title('Нажимаем на кнопку открытия информации о портале')
    def test_2_click_info_logo_panel(self):
        el["Кнопка информации о портале"].click()

    @allure.title('Проверяем наличие текста с подсказкой о необходимости установить adobe reader и ссылку на него')
    def test_3_assert_adobe_reader_information(self):
        with step("Проверяем наличие текста с подсказкой о необходимости установить adobe reader"):
            el["Текст формы обучения"].assert_element_text_contains("Для просмотра обучающих материалов потребуется программа просмотра PDF файлов")
        with step("Проверяем наличие ссылки на скачивание adobe reader"):
            el["Ссылка на adobe reader"].assert_element_existence_and_displayed()

    @allure.title('Проверяем название и наличие ссылки на руководство пользователя')
    def test_4_assert_portal_instruction(self):
        with step("Проверяем название кнопки для скачивания руководства пользователя портала"):
            el["Ссылка на руководство пользователя"].assert_element_text("Руководство пользователя")
        with step("Проверяем наличие ссылки на скачивание руководства пользователя"):
            el["Ссылка на руководство пользователя"].assert_element_existence_and_displayed()

    @allure.title('Нажимаем на кнопку закрытия информации о портале')
    def test_5_click_info_logo_close_panel(self):
        el["Кнопка информации о портале"].click()
