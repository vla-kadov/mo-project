from lib import *
from allure import title, step, feature


el = {
    "Кнопка закрытия плеера": s("[data-player-command='close']", wait=40),
    "Окно плеера": s(".media-container-window", wait=40),
    "Кнопка 'Авторизоваться'": s(".user-link"),
    "Форма авторизации": s(".auth-body"),
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button")
}


@feature('Тестируем авторизацию в портале')
class TestAuthOnPortal(TestCase):

    @title('Проверяем наличие кнопки для авторизации')
    def test_1_close_player(self):
        """Проверяем наличие кнопки для авторизации"""
        el["Кнопка закрытия плеера"].click()
        el["Окно плеера"].assert_element_not_existence()
        el["Кнопка 'Авторизоваться'"].assert_element_text("Авторизоваться")

    @title('Проверяем наличие формы авторизации')
    def test_2_open_auth_page(self):
        """Нажимаем на кнопку 'Авторизоваться, проверяем что перешли на страницу авторизации'"""
        el["Кнопка 'Авторизоваться'"].click()
        el["Форма авторизации"].assert_element_existence()
        assert_title("Видеонаблюдение")

    @title('Авторизация на основной портал')
    def test_3_auth(self):
        el["Поле ввода логина"].send_keys("netris_preprod")
        el["Поле ввода пароля"].send_keys("Nxy2MhG")
        el["Кнопка входа"].click()

    @title('Проверяем, что после авторизации открылся плеер')
    def test_4_assert_player_existence(self):
        el["Окно плеера"].assert_element_existence_and_displayed()
