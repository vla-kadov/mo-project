# Включает в себя тесты из файлов loaderAndMap.json и supportAndInformation.json
from lib import *
import allure
from allure import title, step


el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Кнопка открытия списка камер": s(".widgets-search-panel-header"),
    "Кнопка включения режима поиска по адресам": ss("[data-bind='text: modeGroup.name']")[1],
    "Активная система поиска по адресам": s(".widgets-search-panel-mode.widgets-search-panel-active"),
    "Система поиска по адресам ЕГИП": ss(".widgets-search-panel-mode")[0],
    "Система поиска по адресам Яндекс": ss(".widgets-search-panel-mode")[1],
    "Поле ввода адреса для поиска": s(".video-analytics-search-panel_search-text-input"),
    "Сброс результатов поиска и ввода текста": s(".video-analytics-search-panel_search-text-input-clear"),
    "Подпись к количеству результатов": s(".widgets-search-panel-results-title"),
    "Количество результатов": s(".widgets-search-panel-results-count"),
    "Запуска процеса поиска по адресам": s(".ui-button-inline"),
    "Информация об адресе в результатах поиска": s(".camera-information"),
    "Показать результат на карте": s(".center-at-camera"),
    "Отображение иконки-результата поиска на карте": s(".map-route-handler-show"),
    "Показать ближайшие камеры по результату поиска": s(".nearest-cameras"),
    "Заголовок формы с ближайшими камерами по результату поиска": s("div.map-cameras-client-cluster-popup-title"),
    "Кнопка закрытия формы с ближайшими камерами по результату поиска": s(".map-hint .ui-close"),
    "Список результатов поиска соседних камер": ss(".map-cameras-popup-list .camera-name")[0],
    "Отсутствие результатов поиска соседних камер": ss(".map-cameras-client-cluster-popup div")[2]

}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}


@allure.feature('Панель со списком камер: поиск по адресам')
class TestMapCameraListAddressSearch(TestCase):

    @title('Авторизуемся на портале')
    def test_1_auth_success(self):
        with step("Вводим логин/пароль и нажимаем кнопку входа на портал"):
            el["Поле ввода логина"].send_keys(variables["username"])
            el["Поле ввода пароля"].send_keys(variables["password"])
            el["Кнопка входа"].click()

    @title('Нажимаем кнопку открытия списка камер')
    def test_2_camera_list_open(self):
        el["Кнопка открытия списка камер"].click()

    @title('Проверяем название и нажимаем кнопку открытия режима поиска камер по адресам')
    def test_3_camera_list_open_address_search(self):
        el["Кнопка включения режима поиска по адресам"].assert_element_text("адреса")
        el["Кнопка включения режима поиска по адресам"].click()

    @title('Проверяем выбранную по умолчанию систему поиска по адресам (Яндекс)')
    def test_4_camera_list_address_search_default_system(self):
        el["Активная система поиска по адресам"].assert_element_text("Яндекс")

    @title('Проверяем наличие второй системы поиска по адресам (ЕГИП)')
    def test_5_camera_list_address_search_EGIP_system(self):
        el["Система поиска по адресам ЕГИП"].assert_element_text("ЕГИП")

    @title('Проверяем наличие поля ввода адреса для поиска и подсказку в поле ввода')
    def test_6_camera_list_address_search_input_address(self):
        el["Поле ввода адреса для поиска"].assert_element_existence_and_displayed()
        el["Поле ввода адреса для поиска"].assert_element_placeholder("Поиск..")

    @title('Проверяем наличие кнопки сброса результатов поиска и введённого текста')
    def test_7_camera_list_address_search_input_address_clear(self):
        el["Сброс результатов поиска и ввода текста"].assert_element_interaction()

    @title('Проверяем наличие текста с информацией о количестве результатов поиска')
    def test_8_camera_list_address_search_input_address_results_count(self):
        el["Подпись к количеству результатов"].assert_element_text("Результатов:")
        el["Количество результатов"].assert_element_text("0")

    @title('Переключаемся на систему поиска по адресам ЕГИП и проверяем корректность работы поиска')
    def test_9_camera_list_address_search_EGIP_system_test(self):
        with step("Активируем систему поиска по адресам ЕГИП"):
            el["Система поиска по адресам ЕГИП"].click()
        with step("Вводим адрес в поле ввода для выполнения поиска"):
            el["Поле ввода адреса для поиска"].send_keys("Братиславская")
        with step("Провеляем текст кнопки запуска процеса поиска и запускаем поиск"):
            el["Запуска процеса поиска по адресам"].assert_element_text("Искать")
            el["Запуска процеса поиска по адресам"].click()
        with step("Проверяем наличие результатов поиска"):
            el["Информация об адресе в результатах поиска"].assert_element_text_contains("Братиславская")
        with step("Проверяем текст и нажимаем кнопку отображения результата на карте"):
            el["Показать результат на карте"].assert_element_existence_and_displayed()
            el["Показать результат на карте"].click()
            el["Отображение иконки-результата поиска на карте"].assert_element_existence_and_displayed()
        with step("Проверяем функционал отображения списка соседних камер по результату поиска"):
            el["Показать ближайшие камеры по результату поиска"].click()
            sleep(2)
            el["Заголовок формы с ближайшими камерами по результату поиска"].assert_element_text_contains("Соседние камеры")
            el["Кнопка закрытия формы с ближайшими камерами по результату поиска"].assert_element_interaction()
            el["Отсутствие результатов поиска соседних камер"].assert_element_text_not_equal("Соседние камеры отсутствуют")
            el["Список результатов поиска соседних камер"].assert_element_interaction()

    @title('Сбрасываем предыдущие результаты поиска')
    def test_10_camera_list_address_search_clear_result(self):
        el["Сброс результатов поиска и ввода текста"].click()

    @title('Переключаемся на систему поиска по адресам Яндекс и проверяем корректность работы поиска')
    def test_11_camera_list_address_search_yandex_system_test(self):
        with step("Активируем систему поиска по адресам Яндекс"):
            el["Система поиска по адресам Яндекс"].click()
        with step("Вводим адрес в поле ввода для выполнения поиска"):
            el["Поле ввода адреса для поиска"].send_keys("Братиславская")
        with step("Провеляем текст кнопки запуска процеса поиска и запускаем поиск"):
            el["Запуска процеса поиска по адресам"].assert_element_text("Искать")
            el["Запуска процеса поиска по адресам"].click()
        with step("Проверяем наличие результатов поиска"):
            el["Информация об адресе в результатах поиска"].assert_element_text_contains("Братиславская")
        with step("Проверяем текст и нажимаем кнопку отображения результата на карте"):
            el["Показать результат на карте"].assert_element_existence_and_displayed()
            el["Показать результат на карте"].click()
            el["Отображение иконки-результата поиска на карте"].assert_element_existence_and_displayed()
        with step("Проверяем функционал отображения списка соседних камер по результату поиска"):
            el["Показать ближайшие камеры по результату поиска"].click()
            sleep(2)
            el["Заголовок формы с ближайшими камерами по результату поиска"].assert_element_text_contains("Соседние камеры")
            el["Кнопка закрытия формы с ближайшими камерами по результату поиска"].assert_element_interaction()
            el["Отсутствие результатов поиска соседних камер"].assert_element_text_not_equal("Соседние камеры отсутствуют")
            el["Список результатов поиска соседних камер"].assert_element_interaction()
