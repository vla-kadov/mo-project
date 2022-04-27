# TODO текущие проблемы
# TODO 3. Параметры - через ini-конфиг, не доразобрался с pytest conftest
# TODO 4. har-файлы содержат не всю инфу, поразбираться
# TODO 5. Изучить вопрос параллелизации тестов с учетом конфига и прокси


import allure
from lib.test_case import TestCase
from lib.finder import s

element = {
    "Информационное сообщение": s(css='#info_msg'),
    "Карта": s(id='map', wait=10),
    "Кнопка закрытия окна камеры": s(css='div.media-container-window .ui-glossy-button.close'),
    "Форма поддержки": s(css='#support_button_fringe > div'),
    "Сообщение технической поддержки": s(css='div.ui-window-content > div > p'),
    "Номер технической поддержки": s(css='div.tel'),
    "Кнопка закрытия формы поддержки": s(css="div.support-window .ui-window-close"),
    "Текст кнопки поддержки": s(css="#support_button_fringe > div"),
    "Кнопка информации о портале": s(css="#logo")
}


@allure.feature('Обращения по работе портала и информационные панели')
class TestSupportAndInformation(TestCase):

    @allure.title('Проверяем наличие лоадера на портале')
    def test_01_check_portal_loading(self):
        element["Информационное сообщение"].assert_element_existence()

    @allure.title('Проверяем загрузку карты на портале')
    def test_02_check_map_loading(self):
        element["Карта"].assert_element_existence()

    @allure.title('Нажимаем на кнопку закрытия плеера')
    def test_03_click_camera_close_button(self):
        element["Кнопка закрытия окна камеры"].click()

    @allure.title('Нажимаем на кнопку открытия формы поддержки')
    def test_4_click_support_button(self):
        element["Форма поддержки"].click()

    @allure.title('Проверяем наличие текста обращения в СТП. Должен присутствовать текст (Обратиться в службу технической поддержки можно по телефону:)')
    def test_5_assert_support_text(self):
        element["Сообщение технической поддержки"].assert_element_text('Обратиться в службу технической поддержки можно по телефону:')

    @allure.title("Проверяем наличие номера телефона СТП. Должен присутствовать номер телефона ('8 (495) 587-00-02')")
    def test_6_assert_support_phone_number_text(self):
        element["Номер технической поддержки"].assert_element_text("8 (495) 587-00-02")

    @allure.title('Нажимаем на кнопку закрытия формы поддержки')
    def test_7_click_support_button_close(self):
        s(css="div.support-window .ui-window-close").click()

    @allure.title('Проверяем название кнопки поддержки. Название кнопки должно быть (Сообщить о проблеме)')
    def test_8_assert_support_button_text(self):
        element["Текст кнопки поддержки"].assert_element_text("Сообщить о проблеме")

    @allure.title('Нажимаем на кнопку открытия информации о портале')
    def test_9_click_info_logo_panel(self):
        element["Кнопка информации о портале"].click()

    @allure.title('Нажимаем на кнопку закрытия информации о портале')
    def test_10_click_info_logo_close_panel(self):
        element["Кнопка информации о портале"].click()
