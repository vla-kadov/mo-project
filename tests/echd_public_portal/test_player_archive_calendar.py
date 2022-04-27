from lib import *
from allure import title, step, feature
import datetime

el = {
    "Окно плеера": s(".media-container-window",wait=30),
    "Кнопка открытия календаря позиционирования": s(".camera-archive-controls [data-command='stream-seeker'] div"),
    "Заголовок формы календаря позиционирования": s(".netris-datetimepicker-title"),
    "Элемент календаря 'Календарь'": s(".netris-datetimepicker-calendar-tab"),
    "Элемент календаря 'Дата'": s(".netris-datetimepicker-date-tab"),
    "Элемент календаря 'Время'": s(".netris-datetimepicker-time-tab"),
    "Кнопка закрытия календаря": s(".netris-datetimepicker-button-cancel"),
    "Кнопка перехода на выбранное время в календаре": s(".netris-datetimepicker-button-apply"),
    "Кнопка отмены открытия формы календаря": s(".netris-datetimepicker-popup-close"),
    "Поле ввода даты и времени для позиционирования": s("input.netris-datetimepicker-range-tab-datetime"),
    "Полоса позиционирования по архиву": s(".ui-stream-slider-position"),
    "Кнопка закрытия формы уведомления": s(".ui-close", wait=30)
}


@feature('Работа с плеером: Работа с календарём и позиционирования по архиву')
class TestPlayerArchiveCalendar(TestCase):

    @title('Закрываем окно с уведомлением об ответственности за распространение ссылок на обмен видео')
    def test_1_close_notification_form(self):
        el["Кнопка закрытия формы уведомления"].assert_element_existence_and_displayed()
        sleep(20)
        el["Кнопка закрытия формы уведомления"].click()

    @title("Проверяем наличие окна плеера на странице")
    def test_2_player_existence(self):
        el["Окно плеера"].assert_element_existence_and_displayed()

    @title("Проверяем наличие полосы позиционирования по архиву")
    def test_3_player_archive_timeline_existence(self):
        sleep(30)
        el["Полоса позиционирования по архиву"].assert_element_existence_and_displayed()

    @title("Нажимаем кнопку открытия календаря для позиционирования по архиву")
    def test_4_player_archive_calendar_open(self):
        el["Кнопка открытия календаря позиционирования"].click()

    @title("Проверяем наличие заголовка с текстом в форме работы с календарём")
    def test_5_player_archive_calendar_assert_head(self):
        el["Заголовок формы календаря позиционирования"].assert_element_text_contains("Выберите дату и время")

    @title("Проверяем наличие кнопки отмены открытия календаря")
    def test_6_player_archive_calendar_decline_button(self):
        el["Кнопка отмены открытия формы календаря"].assert_element_existence_and_displayed()

    @title("Проверяем наличие и доступность кнопок смены детальности выбора нужной даты и времени")
    def test_7_player_archive_calendar_detailed_time_type_change(self):
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
    def test_8_player_archive_calendar_close_button(self):
        el["Кнопка закрытия календаря"].assert_element_existence_and_displayed()

    @title("Проверяем наличие поля ввода даты и времени для позиционирования и вводим нужную дату")
    def test_9_player_archive_calendar_input_form(self):
        with step("Очищаем поле ввода даты и времени"):
            el["Поле ввода даты и времени для позиционирования"].assert_element_existence_and_displayed()

    @title("Проверем наличие кнопки и выполняем позиционирование на указанное время")
    def test_10_player_archive_calendar_change_position(self):
        el["Кнопка перехода на выбранное время в календаре"].assert_element_text_contains("Перейти")
        el["Кнопка перехода на выбранное время в календаре"].click()
