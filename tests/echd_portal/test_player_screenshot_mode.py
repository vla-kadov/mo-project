from lib import *
from allure import title, step, feature

el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Кнопка открытия списка камер": s(".widgets-search-panel-header"),
    "Кнопка открытия 1 камеры в списке": ss(".camera-item")[0],
    "Окно плеера": s(".media-container-window"),
    "Иконка камеры в плеере": s("[data-player='cameraTypeIcon']"),
    "Кнопка создания скриншота": s("div[data-camera-option-command='snapshot']", wait=50),
    "Заголовок формы создания скриншота": s("[data-test-id='8wal3y']"),
    "Кнопка 'Закрыть' режим скриншотов": ss("[data-test-id='1rju'] .ui-shadow-button")[2],
    "Кнопка 'Сохранить' режим скриншотов": ss("[data-test-id='1rju'] .ui-shadow-button")[1],
    "Кнопка 'Редактировать' режим скриншотов": ss("[data-test-id='1rju'] .ui-shadow-button")[0],
    "Кнопка изменения размера формы создания скриншотов": ss("[data-test-id='azqvxj']")[0],
    "Кнопка закрытия формы со скриншотами": ss("[data-test-id='azqvxj']")[1]

}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}


@feature('Работа с плеером: Создание скриншотов в плеере')
class TestPlayerScreenshotMode(TestCase):

    @title('Авторизуемся на портале')
    def test_1_auth_success(self):
        with step("Вводим логин/пароль и нажимаем кнопку входа на портал"):
            el["Поле ввода логина"].send_keys(variables["username"])
            el["Поле ввода пароля"].send_keys(variables["password"])
            el["Кнопка входа"].click()

    @title('Нажимаем кнопку открытия списка камер и открываем первую камеру списка')
    def test_2_camera_list_open_camera(self):
        el["Кнопка открытия списка камер"].click()
        el["Кнопка открытия 1 камеры в списке"].click()
        sleep(10)

    @title("Проверяем наличие окна плеера на странице")
    def test_3_player_existence(self):
        el["Окно плеера"].assert_element_existence_and_displayed()

    @title("Нажимаем кнопку создания скриншота в плеере")
    def test_4_player_create_screenshot(self):
        el["Кнопка создания скриншота"].click()
        sleep(20)

    @title("Проверяем заголовок формы создания скриншота")
    def test_5_player_screenshot_head(self):
        el["Заголовок формы создания скриншота"].assert_element_interaction()
        el["Заголовок формы создания скриншота"].assert_element_text("Режим просмотра скриншота")

    @title("Проверяем наличие кнопки редактирования скриншота")
    def test_6_player_screenshot_assert_edit_buttom(self):
        el["Кнопка 'Редактировать' режим скриншотов"].assert_element_interaction()
        el["Кнопка 'Редактировать' режим скриншотов"].assert_element_text("Редактировать")

    @title("Проверяем наличие кнопки сохранения скриншота")
    def test_7_player_screenshot_assert_save_buttom(self):
        el["Кнопка 'Сохранить' режим скриншотов"].assert_element_interaction()
        el["Кнопка 'Сохранить' режим скриншотов"].assert_element_text("Сохранить")
        el["Кнопка 'Сохранить' режим скриншотов"].click()

    @title("Проверяем наличие кнопки закрытия формы создания скриншота")
    def test_8_player_screenshot_assert_decline_buttom(self):
        el["Кнопка 'Закрыть' режим скриншотов"].assert_element_interaction()
        el["Кнопка 'Закрыть' режим скриншотов"].assert_element_text("Закрыть")

    @title("Изменяем размер окна формы создания скриншота в плеере")
    def test_9_player_screenshot_change_form_size(self):
        el["Кнопка изменения размера формы создания скриншотов"].assert_element_interaction()
        el["Кнопка изменения размера формы создания скриншотов"].click()

    @title("Возвращаем исходный размер окна формы создания скриншота в плеере")
    def test_10_player_screenshot_change_form_size_restore(self):
        el["Кнопка изменения размера формы создания скриншотов"].assert_element_interaction()
        el["Кнопка изменения размера формы создания скриншотов"].click()

    @title("Нажимаем кнопку закрытия формы создания скриншота в плеере")
    def test_11_player_create_screenshot_close(self):
        el["Кнопка закрытия формы со скриншотами"].assert_element_interaction()
        el["Кнопка закрытия формы со скриншотами"].click()
