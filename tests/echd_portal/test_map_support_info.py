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


@allure.feature('Форма обращений: Основная форма со способами связи')
class TestSupportInfo(TestCase):

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

    @allure.title('Проверяем наличие текста с указанием способов связи со службой эксплуатации')
    def test_3_assert_support_feedback_type(self):
        with step("Проверяем наличие текста с подсказкой о возможности отправить обращение через заявку на портале"):
            el["Сообщение технической поддержки"][0].assert_element_existence_and_displayed()
            el["Сообщение технической поддержки"][0].assert_element_text(
                'Для обращения в службу технической поддержки выберите тему обращения и введите описание проблемы в форме: Обращение')
        with step("Проверяем наличие текста с подсказкой о возможности связаться по электронной почте"):
            el["Сообщение технической поддержки"][1].assert_element_existence_and_displayed()
            el["Сообщение технической поддержки"][1].assert_element_text('Также обратиться в службу технической поддержки можно по электронной почте support.echd@mos.ru или по телефону:')
        with step("Проверяем наличие номера телефона службы эксплуатации"):
            el["Номер технической поддержки"].assert_element_existence_and_displayed()
            el["Номер технической поддержки"].assert_element_text("8 (495) 587-00-02")

    @allure.title('Нажимаем на кнопку закрытия формы поддержки')
    def test_4_click_support_button_close(self):
        el["Кнопка закрытия формы поддержки"].assert_element_existence_and_displayed()
        el["Кнопка закрытия формы поддержки"].click()
