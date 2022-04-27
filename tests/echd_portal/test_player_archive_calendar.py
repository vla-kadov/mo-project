from lib import *
from allure import title, step, feature
import datetime

el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Кнопка открытия списка камер": s(".widgets-search-panel-header"),
    "Кнопка открытия 1 камеры в списке": ss(".camera-item")[0],
    "Кнопка перехода в режим архива": s("[data-camera-option-command='videoArchive'][data-camera-option-argument='on']"),
    "Окно плеера": s(".media-container-window",wait=30),
    "Кнопка открытия календаря позиционирования": s(".camera-archive-controls [data-command='stream-seeker'] div"),
    "Заголовок формы календаря позиционирования": ss(".netris-datetimepicker-title")[1],
    "Элемент календаря 'Календарь'": ss(".netris-datetimepicker-calendar-tab")[1],
    "Элемент календаря 'Дата'": ss(".netris-datetimepicker-date-tab")[1],
    "Элемент календаря 'Время'": ss(".netris-datetimepicker-time-tab")[1],
    "Кнопка закрытия календаря": ss(".netris-datetimepicker-button-cancel")[1],
    "Кнопка перехода на выбранное время в календаре": ss(".netris-datetimepicker-button-apply")[1],
    "Кнопка отмены открытия формы календаря": ss(".netris-datetimepicker-popup-close")[1],
    "Поле ввода даты и времени для позиционирования": ss("input.netris-datetimepicker-range-tab-datetime")[2],
    "Полоса позиционирования по архиву": s(".ui-stream-slider-position")
}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}

@feature('Работа с плеером: Работа с календарём и позиционирования по архиву')
class TestPlayerArchiveCalendar(TestCase):

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

    @title('Нажимаем кнопку перехода в режим архивной трансляции')
    def test_3_open_camera_archive(self):
        el["Кнопка перехода в режим архива"].click()
        sleep(10)

    @title("Проверяем наличие окна плеера на странице")
    def test_4_player_existence(self):
        el["Окно плеера"].assert_element_existence_and_displayed()

    @title("Проверяем наличие полосы позиционирования по архиву")
    def test_5_player_archive_timeline_existence(self):
        el["Полоса позиционирования по архиву"].assert_element_existence_and_displayed()

    @title("Нажимаем кнопку открытия календаря для позиционирования по архиву")
    def test_6_player_archive_calendar_open(self):
        el["Кнопка открытия календаря позиционирования"].click()

    @title("Проверяем наличие заголовка с текстом в форме работы с календарём")
    def test_7_player_archive_calendar_assert_head(self):
        el["Заголовок формы календаря позиционирования"].assert_element_text_contains("Выберите дату и время")

    @title("Проверяем наличие кнопки отмены открытия календаря")
    def test_8_player_archive_calendar_decline_button(self):
        el["Кнопка отмены открытия формы календаря"].assert_element_existence_and_displayed()

    @title("Проверяем наличие и доступность кнопок смены детальности выбора нужной даты и времени")
    def test_9_player_archive_calendar_detailed_time_type_change(self):
        with step("Проверем возможность указать дату на календаре для позиционирования (Раздел 'Календарь')"):
            el["Элемент календаря 'Календарь'"].assert_element_text_contains("Календарь")
            el["Элемент календаря 'Календарь'"].click()
        with step("Проверем возможность указать дату без календаря для позиционирования (Раздел 'Дата')"):
            el["Элемент календаря 'Дата'"].assert_element_text_contains("Дата")
            el["Элемент календаря 'Дата'"].click()
        with step("Проверем возможность указать время для позиционирования (Раздел 'Время')"):
            el["Элемент календаря 'Время'"].assert_element_text_contains("Время")
            el["Элемент календаря 'Время'"].click()

    @title("Проверяем наличие кнопки закрытия клендаря")
    def test_10_player_archive_calendar_close_button(self):
        el["Кнопка закрытия календаря"].assert_element_existence_and_displayed()

    @title("Проверяем наличие поля ввода даты и времени для позиционирования и вводим нужную дату")
    def test_11_player_archive_calendar_input_form(self):
        with step("Очищаем поле ввода даты и времени"):
            el["Поле ввода даты и времени для позиционирования"].assert_element_existence_and_displayed()

    @title("Проверем наличие кнопки и выполняем позиционирование на указанное время")
    def test_12_player_archive_calendar_change_position(self):
        el["Кнопка перехода на выбранное время в календаре"].assert_element_text_contains("Перейти")
        el["Кнопка перехода на выбранное время в календаре"].click()
