from lib import *
import allure
from allure import title, step


el = {
    "Текст загрузки портала": s(id="info_msg"),
    "Название портала": s(id="welcome_msg", wait=30),
    "Иконка камеры на странице загрузки портала": s(id="loading_cam"),
    "Полоса состояния загрузки портала": s(id="indicator_wrap"),
    "Карта": s(css="#map", wait=30)
}


@allure.feature('Элементы страницы загрузки портала')
class TestLoadingPage(TestCase):

    @title('Проверяем наличие названия портала на странице загрузки портала')
    def test_1_check_portal_name_load_page(self):
        with step("Проверяем что на странице загрузки есть название портала"):
            el["Название портала"].assert_element_displayed()
            el["Название портала"].assert_element_text_contains("Городская система видеонаблюдения")

    @title('Проверяем загрузку карты на портале')
    def test_2_check_map_loading(self):
        with step("Проверяем что загрузилась карта"):
            el["Карта"].assert_element_displayed()
