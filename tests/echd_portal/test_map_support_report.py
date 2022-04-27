# Включает в себя тесты из файлов loaderAndMap.json и supportAndInformation.json
from lib import *
import allure
from allure import title, step


el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Форма поддержки": s("[data-widget-name='SupportButton']", wait=30),
    "Сообщение технической поддержки": ss(css='div.ui-window-content > div > p'),
    "Номер технической поддержки": s(css='div.tel'),
    "Форма заявки по работе портала": s("[href='#helpdesk/open']"),
    "Заголовок формы заявки по работе портала": s(".ui-window-header .ui-window-header"),
    "Кнопка закрытия формы заявки по работе портала": s(".helpdesk .ui-window-close"),
    "Заголовок над выпадающем списке категорий обращения": s("[for='ticketType']"),
    "Категория обращения": s("[name='ticketType'] option[value='60']"),
    "Заголовок над выпадающем списке подкатегорий обращения": s("[for='ticketSubType']"),
    "Подкатегория обращения": s("[name='ticketSubType']"),
    "Заголовок над полем ввода текста обращения": s("[for='message']"),
    "Поле ввода текста обращения": s("[name='message']"),
    "Чек-бокс для включения функционала отправки результата обращения на почту": s("[for='subscribe']"),
    "Заголовок над полем ввода почты для обратной связи": s("[for='email']"),
    "Поле ввода почты для обратной связи": s("input[name='email']"),
    "Кнопка подтверждения отправки обращения": s("[data-tooltip-key='js.button.send']"),
    "Кнопка отмены отправки обращения": s("[data-button='1']"),
    "Кнопка закрытия формы поддержки": s(css="div.support-window .ui-window-close")
}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}


@allure.feature('Форма обращений: Форма отправки обращения с портала')
class TestSupportReport(TestCase):

    @title('Авторизуемся на портале')
    def test_1_auth_success(self):
        with step("Вводим логин/пароль и нажимаем кнопку входа на портал"):
            el["Поле ввода логина"].send_keys(variables["username"])
            el["Поле ввода пароля"].send_keys(variables["password"])
            el["Кнопка входа"].click()

    @allure.title('Проверяем текст и Нажимаем на кнопку открытия формы поддержки')
    def test_2_assert_support_button(self):
        with step("Проверяем название кнопки открытия формы поддержки"):
            el["Форма поддержки"].assert_element_interaction()
            el["Форма поддержки"].assert_element_text_contains("Оставить обращение")
        with step("Нажимаем кнопку открытия формы поддержки"):
            el["Форма поддержки"].click()

    @allure.title('Нажимаем кнопку открытия формы для отправки заявки')
    def test_3_test_support_report_form_open(self):
        el["Форма заявки по работе портала"].click()

    @allure.title("Проверяем наличие заголовка формы для отправки заявки")
    def test_4_test_support_report_form_header(self):
        el["Заголовок формы заявки по работе портала"].assert_element_interaction()
        el["Заголовок формы заявки по работе портала"].assert_element_text("Оставить обращение в службу\nтехнической поддержки")

    @allure.title("Проверяем наличие кнопки закрытия формы для отправки заявки")
    def test_5_test_support_report_form_close_button_existence(self):
        el["Кнопка закрытия формы заявки по работе портала"].assert_element_interaction()

    @allure.title("Проверяем наличие подписи над выпадающим списком и списка выбора категории обращения")
    def test_6_test_support_report_form_category(self):
        el["Заголовок над выпадающем списке категорий обращения"].assert_element_text("Категория обращения:")
        el["Категория обращения"].assert_element_interaction()

    @allure.title("Проверяем наличие подписи над выпадающим списком и списка выбора подкатегории обращения")
    def test_7_test_support_report_form_subcategory(self):
        el["Заголовок над выпадающем списке подкатегорий обращения"].assert_element_text("Подкатегория обращения:")
        el["Подкатегория обращения"].assert_element_interaction()

    @allure.title("Проверяем наличие подписи над полем ввода и поле ввода текста обращения")
    def test_8_test_support_report_form_report_text(self):
        el["Заголовок над полем ввода текста обращения"].assert_element_text("Содержание обращения:")
        el["Поле ввода текста обращения"].send_keys("Тестовое обращение")

    @allure.title("Проверяем наличие чек-бокса с текстом для включения функции обратной связи на email")
    def test_9_test_support_report_form_feedback_button_text(self):
        el["Чек-бокс для включения функционала отправки результата обращения на почту"].assert_element_text("уведомить о выполнении по e-mail")

    @allure.title("Активируем чек-бокс для включения функции обратной связи на email")
    def test_10_test_support_report_form_feedback_button_activate(self):
        el["Чек-бокс для включения функционала отправки результата обращения на почту"].click()

    @allure.title("Проверяем наличие подписи над полем ввода и поле ввода почты для обратной связи")
    def test_11_test_support_report_form_feedback_form(self):
        el["Заголовок над полем ввода почты для обратной связи"].assert_element_text("Адрес электронной почты для уведомления")
        el["Поле ввода почты для обратной связи"].send_keys("test@test.ru")

    @allure.title("Проверяем наличие и текст кнопки подтверждения отправки обращения по работе портала")
    def test_12_test_support_report_form_submit_send_button_text(self):
        el["Кнопка подтверждения отправки обращения"].assert_element_text("Отправить")

    @allure.title("Проверяем наличие и текст кнопки отмены отправки обращения по работе портала")
    def test_13_test_support_report_form_decline_button_text(self):
        el["Кнопка отмены отправки обращения"].assert_element_text("Отмена")

    @allure.title("Нажимаем кнопку отмены отправки обращения по работе портала")
    def test_14_test_support_report_form_decline_button_click(self):
        el["Кнопка отмены отправки обращения"].click()

    @allure.title('Нажимаем на кнопку закрытия формы поддержки')
    def test_15_click_support_button_close(self):
        el["Кнопка закрытия формы поддержки"].assert_element_existence_and_displayed()
        el["Кнопка закрытия формы поддержки"].click()
