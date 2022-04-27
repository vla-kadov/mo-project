from lib import *
from allure import title, step, feature


el = {
    "Форма авторизации": s(".auth-body"),
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Основной заголовок формы авторизации": s("[data-test-id='3e9p2b']"),
    "Название портала на странице авторизации": s("[data-test-id='a9kt3r']"),
    "Дополнение к названию портала на странице авторизации": s("[data-test-id='25gqh9']"),
    "Логотип портала на странице авторизации": s(".customer-logo"),
    "Форма с текстом ошибки авторизаии": s("[data-test-id='lziqy2']"),
    "Название портала на странице загрузки портала": s("#welcome_msg"),
    "Имя пользователя на портале": s("#user_panel_fringe", wait=50),
    "Кнопка входа": s("button"),
    "Заголовок поля ввода имени пользователя": s("[for='username']"),
    "Заголовок поля ввода пароля пользователя": s("[for='password']"),
    "Кнопка входа через СУДИР": s("[href='/login/sudir/auth']")
}

variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG",
    "error_username": "username_not_existence",
    "error_password": "test_password"
}

@feature('Тестируем авторизацию в портале')
class TestAuthOnPortal(TestCase):

    @title('Проверяем title страницы не странице авторизации')
    def test_1_auth_page_title(self):
        """Проверяем title страницы на странице авторизации. Title должен быть 'Видеонаблюдение'"""
        assert_title("Видеонаблюдение")

    @title('Проверяем наличие названия и логотипа портала в форме авторизации')
    def test_2_auth_page_portal_name(self):
        with step("Проверяем наличие основного заголовка с названием портала"):
            el["Основной заголовок формы авторизации"].assert_element_existence_and_displayed()
            el["Основной заголовок формы авторизации"].assert_element_text("Городская система видеонаблюдения")
        with step("Проверяем наличие названия портала на странице авторизации"):
            el["Название портала на странице авторизации"].assert_element_existence_and_displayed()
            el["Название портала на странице авторизации"].assert_element_text("доступ через КМС")
        with step("Проверяем наличие дополнения к названию портала на странице авторизации"):
            el["Дополнение к названию портала на странице авторизации"].assert_element_existence_and_displayed()
            el["Дополнение к названию портала на странице авторизации"].assert_element_text("(внутренняя сеть Правительства Москвы)")
        with step("Проверяем наличие логотипа портала на странице авторизации"):
            el["Логотип портала на странице авторизации"].assert_element_existence_and_displayed()

    @title('Проверяем наличие и текст заголовков над полями ввода логина и пароля')
    def test_3_auth_page_input_name(self):
        with step("Проверяем наличие заголовка на полем ввода имени пользователя"):
            el["Заголовок поля ввода имени пользователя"].assert_element_existence_and_displayed()
            el["Заголовок поля ввода имени пользователя"].assert_element_text("Имя пользователя")
        with step("Проверяем наличие заголовка на полем ввода пароля пользователя"):
            el["Заголовок поля ввода пароля пользователя"].assert_element_existence_and_displayed()
            el["Заголовок поля ввода пароля пользователя"].assert_element_text("Пароль")

    @title('Проверяем подсказки в полях ввода логина и пароля')
    def test_4_auth_page_input_placeholder(self):
        el["Поле ввода пароля"].assert_element_placeholder("Введите пароль")
        el["Поле ввода логина"].assert_element_placeholder("Введите логин")

    @title('Проверяем наличие и названия кнопок входа на портал')
    def test_5_auth_page_enter_button(self):
        with step("Проверяем наличие и название кнопки входа на портал стандартным методом авторизации"):
            el["Кнопка входа"].assert_element_existence_and_displayed()
            el["Кнопка входа"].assert_element_text("Войти")
        with step("Проверяем наличие и название кнопки входа на портал с помощью метода СУДИР-авторизации"):
            el["Кнопка входа через СУДИР"].assert_element_existence_and_displayed()
            el["Кнопка входа через СУДИР"].assert_element_text("Войти через СУДИР")

    @title('Проверяем обработку ситуации некорректного вода логина и/или пароля')
    def test_6_auth_error(self):
        with step("Вводим корректный логин, но некорректный пароль для проверки корректности текста ошибки"):
            el["Поле ввода логина"].send_keys(variables["username"])
            el["Поле ввода пароля"].send_keys(variables["error_password"])
            el["Кнопка входа"].mouse_click()
            el["Форма с текстом ошибки авторизаии"].assert_element_text("Неверный логин и/или пароль. Проверьте раскладку клавиатуры, не нажата ли клавиша «Caps Lock» и попробуйте авторизоваться еще раз.")
            refresh()
        with step("Вводим некорректный логин и некорректный пароль для проверки корректности текста ошибки"):
            el["Поле ввода логина"].send_keys(variables["error_username"])
            el["Поле ввода пароля"].send_keys(variables["error_password"])
            el["Кнопка входа"].mouse_click()
            el["Форма с текстом ошибки авторизаии"].assert_element_text("Введенные логин и/или пароль не верны.")
            refresh()
        with step("Не заполняем поля ввода логина и пароля для проверки корректности текста ошибки"):
            el["Кнопка входа"].mouse_click()
            el["Форма с текстом ошибки авторизаии"].assert_element_text("Необходимо ввести значения полей")

    @title('Проверяем позитивный сценарий входа на портал (успешность авторизации)')
    def test_7_auth_success(self):
        with step("Вводим логин/пароль и нажимаем кнопку входа на портал"):
            el["Поле ввода логина"].send_keys(variables["username"])
            el["Поле ввода пароля"].send_keys(variables["password"])
            el["Кнопка входа"].click()
        with step("Проверяем наличие страницы загрузки с названием портала"):
            el["Название портала на странице загрузки портала"].assert_element_displayed()
            el["Название портала на странице загрузки портала"].assert_element_text_contains("Городская система видеонаблюдения")
            el["Название портала на странице загрузки портала"].assert_element_text_contains("доступ через КМС")
            el["Название портала на странице загрузки портала"].assert_element_text_contains("(внутренняя сеть Правительства Москвы)")
        with step("Проверяем загрузку портала и наличие имени пользователя на основной странице портала"):
            el["Имя пользователя на портале"].assert_element_existence_and_displayed()
            el["Имя пользователя на портале"].assert_element_text_contains(variables["username"])
