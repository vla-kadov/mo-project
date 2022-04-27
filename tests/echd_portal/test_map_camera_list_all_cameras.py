# Включает в себя тесты из файлов loaderAndMap.json и supportAndInformation.json
from lib import *
import allure
from allure import title, step


el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Кнопка открытия списка камер": s(".widgets-search-panel-header"),
    "Кнопка 'камеры' формы работы со списками камер и адресов": ss(".widgets-search-panel-mode-group-name")[0],
    "Кнопка активного режима работы со списками камер": s(".widgets-search-panel-active"),
    "Поле ввода имени камеры для поиска": s(".video-analytics-search-panel_search-text-input"),
    "Сброс результатов поиска и ввода текста": s(".video-analytics-search-panel_search-text-input-clear"),
    "Подпись к количеству результатов": s(".widgets-search-panel-results-title"),
    "Количество результатов": s(".widgets-search-panel-results-count"),
    "Название чек-бокса 'с учётом фильтра'": s("[data-bind='text: messages.useFilter']"),
    "Чек-бокс 'с учётом фильтра'": ss(".widgets-search-panel-options .ui-checkbox-control")[0],
    "Скроллбар списка камер": s(".visible .cctv-list-container .iScrollLoneScrollbar .iScrollIndicator"),
    "Иконка камеры в списке камер": ss(".widgets-search-panel .camera-icon")[0],
    "Адресс камеры в списке камер": ss(".cctv-list-item .camera-item .camera-description")[0],
    "Тип камеры в списке камер": ss(".camera-type")[0],
    "Имя камеры в списке камер": ss(".camera-name")[0],
    "Иконка-признак контрактной камер в списке камер": ss(".contact-camera-icon")[0],
    "Кнопка отображения камеры на карте из списка камер": ss(".center-at-camera")[0],
    "Кнопка добавления камеры в избранное из списка камер": ss(".camera-not-favorite")[0],
    "Кнопка добавления камеры в маршрут из списка камер": ss(".camera-not-in-route")[0]

}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}


@allure.feature('Панель со списком камер: Общим список камер')
class TestMapCameraListAllCameras(TestCase):

    @title('Авторизуемся на портале')
    def test_1_auth_success(self):
        with step("Вводим логин/пароль и нажимаем кнопку входа на портал"):
            el["Поле ввода логина"].send_keys(variables["username"])
            el["Поле ввода пароля"].send_keys(variables["password"])
            el["Кнопка входа"].click()

    @title('Нажимаем кнопку открытия списка камер')
    def test_2_camera_list_open(self):
        el["Кнопка открытия списка камер"].click()

    @title('Проверяем название кнопки переключения режима на работу со списками камер')
    def test_3_camera_list_all_mode_name(self):
        el["Кнопка 'камеры' формы работы со списками камер и адресов"].assert_element_text("камеры")

    @title('Проверяем, что по умолчанию выбран режим отображения всех камер')
    def test_4_camera_list_default_type(self):
        el["Кнопка активного режима работы со списками камер"].assert_element_text("все")

    @title('Проверка наличия поля ввода и текста подсказки поля ввода имени камеры для поиска')
    def test_5_camera_list_all_name_search_input(self):
        el["Поле ввода имени камеры для поиска"].assert_element_placeholder("Поиск..")

    @title('Проверка наличия кнопки сброса ввода и результатов поиска по имени камеры в списке')
    def test_6_camera_list_all_name_search_input_clear(self):
        el["Сброс результатов поиска и ввода текста"].assert_element_interaction()

    @title('Проверяем наличие текста с информацией о количестве камер в списке')
    def test_7_camera_list_all_search_input_results_count(self):
        el["Подпись к количеству результатов"].assert_element_text("Результатов:")
        el["Количество результатов"].assert_element_existence_and_displayed()

    @title("Проверяем наличие чекбокс 'с учётом фильтра' и предустановленное состояние чекбокса")
    def test_8_camera_list_all_include_filter_check(self):
        with step('Проверяем наличие чекбокса "С учётом фильтра" и то, что он активирован по умолчанию'):
            el["Чек-бокс 'с учётом фильтра'"].assert_element_have_class("ui-checked")
        with step('Деактивируем чекбокс "С учётом фильтра" и проверяем факт деактивации'):
            el["Чек-бокс 'с учётом фильтра'"].click()
            el["Чек-бокс 'с учётом фильтра'"].assert_element_not_have_class("ui-checked")
        with step('Проверяем наличие названия чек-бокса'):
            el["Название чек-бокса 'с учётом фильтра'"].assert_element_text("С учетом фильтра")
        with step("Активируем чек-бокс 'С учётом фильтра'"):
            el["Чек-бокс 'с учётом фильтра'"].click()
            el["Чек-бокс 'с учётом фильтра'"].assert_element_have_class("ui-checked")

    @title('Проверяем наличие полосы прокрутки в списке камер')
    def test_9_camera_list_all_scrollbar(self):
        el["Скроллбар списка камер"].assert_element_existence_and_displayed()

    @title("Проверяем наличие информации о камерах в списке")
    def test_10_camera_list_all_camera_information(self):
        with step('Проверяем наличие иконки камеры в списке камер'):
            el["Иконка камеры в списке камер"].assert_element_existence_and_displayed()
        with step('Проверяем наличие названия типа камеры в списке камер'):
            el["Тип камеры в списке камер"].assert_element_existence_and_displayed()
        with step('Проверяем наличие имени камеры в списке камер'):
            el["Имя камеры в списке камер"].assert_element_existence_and_displayed()
        with step('Проверяем наличие адреса установки камеры в списке камер'):
            el["Адресс камеры в списке камер"].assert_element_existence_and_displayed()
        with step('Проверяем наличие иконки-признака контрактной камеры в списке камер'):
            el["Иконка-признак контрактной камер в списке камер"].assert_element_existence_and_displayed()

    @title("Проверяем наличие кнопки отображения камеры на карте")
    def test_11_camera_list_all_show_on_map(self):
        el["Кнопка отображения камеры на карте из списка камер"].assert_element_interaction()

    @title("Проверяем наличие кнопки добавления камеры в маршрут")
    def test_12_camera_list_all_add_to_route(self):
        el["Кнопка добавления камеры в маршрут из списка камер"].assert_element_interaction()

    @title("Проверяем наличие кнопки добавления камеры в список избранных камер")
    def test_13_camera_list_all_add_to_favorite(self):
        el["Кнопка добавления камеры в избранное из списка камер"].assert_element_interaction()

    @title("Вводим имя камеры в поле ввода и проверяем результаты поиска")
    def test_14_camera_list_all_search_camera_result(self):
        with step("Вводим в поле ввода название камеры"):
            el["Поле ввода имени камеры для поиска"].send_keys("DVN_UVAO_2_8600_1")
            sleep(10)
        with step("Проверяем изменение количества камер в списке"):
            el["Подпись к количеству результатов"].assert_element_text("Результатов:")
            el["Количество результатов"].assert_element_text("1")
        with step('Проверяем наличие иконки камеры в списке камер'):
            el["Иконка камеры в списке камер"].assert_element_existence_and_displayed()
        with step('Проверяем наличие названия типа камеры в списке камер'):
            el["Тип камеры в списке камер"].assert_element_text("Дворы (упр.)*")
        with step('Проверяем наличие имени камеры в списке камер'):
            el["Имя камеры в списке камер"].assert_element_text_contains("DVN_UVAO_2_8600_1")
        with step('Проверяем наличие адреса установки камеры в списке камер'):
            el["Адресс камеры в списке камер"].assert_element_text("ЮВАО Братиславская улица, дом 8")
        with step('Проверяем наличие иконки-признака контрактной камеры в списке камер'):
            el["Иконка-признак контрактной камер в списке камер"].assert_element_existence_and_displayed()
        with step("Проверяем наличие кнопки отображения камеры на карте"):
            el["Кнопка отображения камеры на карте из списка камер"].assert_element_interaction()
        with step("Проверяем наличие кнопки добавления камеры в маршрут"):
            el["Кнопка добавления камеры в маршрут из списка камер"].assert_element_interaction()
        with step("Проверяем наличие кнопки добавления камеры в список избранных камер"):
            el["Кнопка добавления камеры в избранное из списка камер"].assert_element_interaction()
        with step("Нажимаем кнопку сброса результатов поиска"):
            el["Сброс результатов поиска и ввода текста"].click()
            sleep(10)
        with step("Проверяем факт сброса результатов поиска"):
            el["Адресс камеры в списке камер"].assert_element_text_not_equal("ЮВАО Братиславская улица, дом 8")
