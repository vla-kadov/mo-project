# Включает в себя тесты из файлов loaderAndMap.json и supportAndInformation.json
from lib import *
import allure
from allure import title, step


el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Кнопка открытия списка камер": s(".widgets-search-panel-header"),
    "Кнопка активации списка избранных камер": ss(".widgets-search-panel-mode")[2],
    "Поле ввода имени камеры для поиска": s(".video-analytics-search-panel_search-text-input"),
    "Сброс результатов поиска и ввода текста": s(".video-analytics-search-panel_search-text-input-clear"),
    "Подпись к количеству результатов": s(".widgets-search-panel-results-title"),
    "Количество результатов": s(".widgets-search-panel-results-count"),
    "Название чек-бокса 'с учётом фильтра'": s("[data-bind='text: messages.useFilter']"),
    "Чек-бокс 'с учётом фильтра'": ss(".widgets-search-panel-options .ui-checkbox-control")[0],
    "Название чек-бокса 'Показать на карте только избранные'": s("[data-bind='text: specificOptionMessage']"),
    "Чек-бокс 'Показать на карте только избранные'": ss(".widgets-search-panel-options .ui-checkbox-control")[2],
    "Иконка камеры в списке камер": ss(".widgets-search-panel .camera-icon")[0],
    "Адрес камеры в списке камер": ss(".cctv-list-item .camera-item .camera-description")[0],
    "Тип камеры в списке камер": ss(".camera-type")[0],
    "Имя камеры в списке камер": ss(".camera-name")[0],
    "Иконка-признак контрактной камер в списке камер": ss(".contact-camera-icon")[0],
    "Кнопка отображения камеры на карте из списка камер": ss(".center-at-camera")[0],
    "Кнопка добавления камеры в избранное из списка камер": ss(".camera-not-favorite")[0],
    "Кнопка удаления камеры в избранное из списка камер": ss(".camera-is-favorite")[0],
    "Кнопка добавления камеры в маршрут из списка камер": ss(".camera-not-in-route")[0],
    "Кнопка закрытия плеера": s("[data-player-command='close']"),
    "Кнопка очистки списка избранных камер": s(".widgets-search-panel-results-clear"),
    "Текст формы подтверждения очистки списка избранных камер": s(".confirm-window .ui-window-content"),
    "Кнопка отмены очистки списка избранных камер": s("[data-key='js.button.cancel']"),
    "Кнопка подтверждения очистки списка избранных камер": s("[data-key='js.button.ok']")

}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}


@allure.feature('Панель со списком камер: избранные камеры')
class TestMapCameraListFavouriteCameras(TestCase):

    @title('Авторизуемся на портале')
    def test_1_auth_success(self):
        with step("Вводим логин/пароль и нажимаем кнопку входа на портал"):
            el["Поле ввода логина"].send_keys(variables["username"])
            el["Поле ввода пароля"].send_keys(variables["password"])
            el["Кнопка входа"].click()

    @title('Нажимаем кнопку открытия списка камер')
    def test_2_camera_list_open(self):
        el["Кнопка открытия списка камер"].click()

    @title("Добавляем первую камеру в списке в список избранных камер")
    def test_3_camera_list_open_first_camera(self):
        el["Кнопка добавления камеры в избранное из списка камер"].click()

    @title("Выполняем поиск нужной нам камеры в списке для её открытия и закрытия")
    def test_4_camera_list_open_test_camera(self):
        with step("Вводим в поле ввода название камеры"):
            el["Поле ввода имени камеры для поиска"].send_keys("DVN_UVAO_2_8600_1")
            sleep(10)
        with step("Добавляем нужную нам камеру в список избранных камер"):
            el["Кнопка добавления камеры в избранное из списка камер"].click()
        with step("Нажимаем кнопку сброса результатов поиска"):
            el["Сброс результатов поиска и ввода текста"].click()
            sleep(1)

    @title("Выполняем переход в список избранных камер")
    def test_5_camera_list_open_last_list(self):
        el["Кнопка активации списка избранных камер"].assert_element_text("избранные")
        el["Кнопка активации списка избранных камер"].click()

    @title('Проверка наличия поля ввода и текста подсказки поля ввода имени камеры для поиска в списке избранных камер')
    def test_6_camera_list_favourite_name_search_input(self):
        el["Поле ввода имени камеры для поиска"].assert_element_placeholder("Поиск..")

    @title('Проверка наличия кнопки сброса ввода и результатов поиска по имени камеры в списке избранных камер')
    def test_7_camera_list_favourite_name_search_input_clear(self):
        el["Сброс результатов поиска и ввода текста"].assert_element_interaction()

    @title('Проверяем наличие текста и корректности подсчета количества камер в списке избранных камер')
    def test_8_camera_list_favourite_search_input_results_count(self):
        el["Подпись к количеству результатов"].assert_element_text("Результатов:")
        el["Количество результатов"].assert_element_existence_and_displayed()

    @title("Проверяем наличие чекбокс 'с учётом фильтра' и предустановленное состояние чекбокса в списке избранных камер")
    def test_9_camera_list_favourite_include_filter_check(self):
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

    @title("Проверяем наличие чекбокс 'Показать на карте только избранные' и предустановленное состояние чекбокса в списке избранных камер")
    def test_10_camera_list_favourite_only_favourite_cams_filter_check(self):
        with step('Проверяем наличие чекбокса "Показать на карте только избранные" и то, что он деактивирован по умолчанию'):
            el["Чек-бокс 'Показать на карте только избранные'"].assert_element_not_have_class("ui-checked")
        with step('Активируем чекбокс "Показать на карте только избранные" и проверяем факт активации'):
            el["Чек-бокс 'Показать на карте только избранные'"].click()
            el["Чек-бокс 'Показать на карте только избранные'"].assert_element_have_class("ui-checked")
        with step('Проверяем наличие названия чек-бокса'):
            el["Название чек-бокса 'Показать на карте только избранные'"].assert_element_text("Показать на карте только избранные")
        with step("Деактивируем чек-бокс 'Показать на карте только избранные'"):
            el["Чек-бокс 'Показать на карте только избранные'"].click()
            el["Чек-бокс 'Показать на карте только избранные'"].assert_element_not_have_class("ui-checked")

    @title("Удаляем из списка избранных камер первую камер с помощью нажатия на соответствующую кнопку")
    def test_11_camera_list_favourite_first_camera_remove_from_list(self):
        with step("Проверяем количество камер в списке избранных камер"):
            el["Количество результатов"].assert_element_text("2")
        with step("Нажимаем кнопку удаления камеры из списка избранных"):
            el["Кнопка удаления камеры в избранное из списка камер"].click()
            sleep(2)
        with step("Проверяем количество камер в списке избранных камер после удаления"):
            el["Количество результатов"].assert_element_text("1")

    @title("Проверяем функционал поиска в списке избранных камер")
    def test_12_camera_list_favourite_search_mode(self):
        with step("Вводим в поле ввода название камеры"):
            el["Поле ввода имени камеры для поиска"].send_keys("DVN_UVAO_2_8600_1")
            sleep(2)
        with step("Проверяем изменение количества камер в списке"):
            el["Подпись к количеству результатов"].assert_element_text("Результатов:")
            el["Количество результатов"].assert_element_text("1")
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
            el["Адрес камеры в списке камер"].assert_element_text("ЮВАО Братиславская улица, дом 8")
        with step('Проверяем наличие иконки-признака контрактной камеры в списке камер'):
            el["Иконка-признак контрактной камер в списке камер"].assert_element_existence_and_displayed()
        with step("Проверяем наличие кнопки отображения камеры на карте"):
            el["Кнопка отображения камеры на карте из списка камер"].assert_element_interaction()
        with step("Проверяем наличие кнопки добавления камеры в маршрут"):
            el["Кнопка добавления камеры в маршрут из списка камер"].assert_element_interaction()
        with step("Проверяем наличие кнопки добавления камеры в список избранных камер"):
            el["Кнопка удаления камеры в избранное из списка камер"].assert_element_interaction()

    @title("Проверяем функционал очистки списка избранных камер")
    def test_13_camera_list_favourite_clear_all_cameras_list(self):
        with step("Проверяем наличие и текст кнопки очистки списка избранных камер"):
            el["Кнопка очистки списка избранных камер"].assert_element_text("Очистить все")
        with step("Нажимаем кнопку очистки списка избранных камер"):
            el["Кнопка очистки списка избранных камер"].click()
        with step("Проверяем наличие предупреждения об очистки списка камер и кнопки отмены или подтверждения"):
            el["Текст формы подтверждения очистки списка избранных камер"].assert_element_text("Вы действительно хотите удалить выбранные камеры из списка избранных?")
            el["Кнопка отмены очистки списка избранных камер"].assert_element_text("Отмена")
            el["Кнопка подтверждения очистки списка избранных камер"].assert_element_text("ОК")
            el["Кнопка подтверждения очистки списка избранных камер"].click()
            el["Сброс результатов поиска и ввода текста"].click()
            sleep(2)
        with step("Проверяем факт очистки списка избранных камер"):
            el["Количество результатов"].assert_element_text("0")