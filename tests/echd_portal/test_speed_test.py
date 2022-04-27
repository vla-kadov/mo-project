# Включает в себя тесты из файлов loaderAndMap.json и supportAndInformation.json
from lib import *
import allure
from allure import title, step


el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Кнопка запуска теста скорости": s("[data-test-name='BUTTON_SPEED_TEST']"),
    "Заголовок формы теста скорости": s("[data-test-id='xjdr1i']"),
    "Кнопка отмены открытия формы теста скорости": s("[data-test-id='p5nkvl']"),
    "Информаиционная панель формы измерения теста скорости": s("[data-test-id='5wn5o1']"),
    "Кнопка запуска/остановки процесса измерения скорости": s("[data-test-id='d0so32'] [data-test-id='19kwuz']"),
    "Текст с рекомендациями по количеству камер для просмотра": ss("[data-test-id='5wn5o1'] [data-test-id='o1t8o1']")[1]
}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}


body = s(tag_name="body")


@allure.feature('Проверка функционала измерения скорости соединения пользовательского АРМ')
class TestSpeedTest(TestCase):

    @title('Авторизуемся на портале')
    def test_1_auth_success(self):
        with step("Вводим логин/пароль и нажимаем кнопку входа на портал"):
            el["Поле ввода логина"].send_keys(variables["username"])
            el["Поле ввода пароля"].send_keys(variables["password"])
            el["Кнопка входа"].click()

    @title('Проверяем наличие хинта-подсказки у кнопки открытия формы измерения теста скорости')
    def test_2_check_speed_test_button_hint(self):
        el["Кнопка запуска теста скорости"].assert_element_existence_and_displayed()
        el["Кнопка запуска теста скорости"].assert_hint_text("Тест скорости")

    @title('Нажимаем кнопку открытия формы измерения теста скорости')
    def test_3_check_speed_test_button(self):
        el["Кнопка запуска теста скорости"].click()

    @title('Проверяем наличие и текст заголовка формы измерения теста скорости')
    def test_4_check_speed_test_head(self):
        el["Заголовок формы теста скорости"].assert_element_existence_and_displayed()
        el["Заголовок формы теста скорости"].assert_element_text("Тест скорости")

    @title('Проверяем наличие текста с подсказкой о способе запуска процесса измерения скорости')
    def test_5_check_speed_test_text(self):
        el["Информаиционная панель формы измерения теста скорости"].assert_element_text('Для измерения скорости нажмите кнопку "Начать".')

    @title('Проверяем название и нажимаем кнопку запуска процесса измерения скорости')
    def test_6_check_speed_test_start_button(self):
        el["Кнопка запуска/остановки процесса измерения скорости"].assert_element_text("Начать")
        el["Кнопка запуска/остановки процесса измерения скорости"].click()

    @title('Проверяем наличие текста-подсказки о запущенном процессе измерения теста скорости')
    def test_7_check_speed_test_running_text(self):
        el["Информаиционная панель формы измерения теста скорости"].assert_element_text("Идёт измерение скорости. Пожалуйста, подождите...")

    @title('Проверяем текст кнопки прерывания процесса измерения теста скорости')
    def test_8_check_speed_test_cancel_button(self):
        el["Кнопка запуска/остановки процесса измерения скорости"].assert_element_text("Остановить")

    @title('Проверяем наличие текста с рекомендуемым для одновременного просмотра количеством камер')
    def test_9_check_speed_test_result_text(self):
        el["Текст с рекомендациями по количеству камер для просмотра"].assert_element_text_contains("Рекомендуется открывать")

    @title('Нажимаем кнопку закрытия формы измерения теста скорости и проверяем успешность закрытия')
    def test_10_check_speed_test_result_text(self):
        el["Кнопка отмены открытия формы теста скорости"].click()
        sleep(1)
        el["Кнопка отмены открытия формы теста скорости"].assert_element_not_existence()
