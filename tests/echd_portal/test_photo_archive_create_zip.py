# Включает в себя тесты из файлов loaderAndMap.json и supportAndInformation.json
from lib import *
import allure
from allure import title, step


el = {
    "Поле ввода логина": s(id="username"),
    "Поле ввода пароля": s(id="password"),
    "Кнопка входа": s("button"),
    "Открыть форму работы с заданиями по скриншотам": s("#photo_archive"),
    "Кнопка выделения видимых скриншотов": s(".ui-button .ui-checkbox-control"),
    "Кнопка запуска процесса создания архива скриншотов": s(".photo-archive-controls-download"),
    "Уведомление о запуске процесса создания архива скриншотов": s(".notification-message-rows"),
    "Текст уведомления о завершении создании архива скриншотов": s(".visible .ui-window-container .ui-window-content"),
    "Кнопка закрытия формы с уведомлением о завршении создания архива скриншотов": s(".visible .ui-window-close"),
    "Кнопка подтверждения скачивания архива скриншотов": s("[download='photo-archive.zip']"),
    "Первый скриншот в списке": ss("img.photo-archive-shadow")[0]

}
variables = {
    "username": "netris_preprod",
    "password": "Nxy2MhG"
}


body = s(tag_name="body")


@allure.feature('Проверка функционала фотоархива: Выгрузка ZIP архива снимков')
class TestPhotoArchiveCreateZip(TestCase):

    @title('Авторизуемся на портале')
    def test_1_auth_success(self):
        with step("Вводим логин/пароль и нажимаем кнопку входа на портал"):
            el["Поле ввода логина"].send_keys(variables["username"])
            el["Поле ввода пароля"].send_keys(variables["password"])
            el["Кнопка входа"].click()

    @title('Открываем панель для работы с функционалом снятия скриншотов по расписанию')
    def test_2_open_photo_archive_panel(self):
        el["Открыть форму работы с заданиями по скриншотам"].click()

    @title('Проверяем отсутствие кнопки создания архива скриншотов до выбора камер в составе архива')
    def test_3_photo_archive_check_not_visible_zip_create_button(self):
        el["Кнопка запуска процесса создания архива скриншотов"].assert_element_not_existence()

    @title('Проверяем стандартное состояние чек-бокса выделения видимых камер для добавления их в задание на создание архива скриншотов')
    def test_4_photo_archive_panel_checkbox_default(self):
        el["Первый скриншот в списке"].assert_element_interaction()
        el["Кнопка выделения видимых скриншотов"].assert_element_not_have_class("ui-checked")

    @title('Выделяем всем видимые камеры для дальнейшего запуска процесса создания архива скриншотов')
    def test_5_photo_archive_panel_add_visible_cameras(self):
        with step("Нажимаем кноку выделения видимых камер"):
            el["Кнопка выделения видимых скриншотов"].click()
        with step("Проверяем факт выделения видимых камер"):
            el["Кнопка выделения видимых скриншотов"].assert_element_have_class("ui-checked")

    @title('Проверяем появление кнопки создания архива скриншотов после выделения камер')
    def test_6_photo_archive_check_visible_zip_create_button(self):
        el["Кнопка запуска процесса создания архива скриншотов"].assert_element_interaction()

    @title('Нажимаем кнопку сохранения архива с выбранными снимками')
    def test_7_photo_archive_run_zip_create(self):
        el["Кнопка запуска процесса создания архива скриншотов"].click()

    @title('Проверяем наличие всплывающего сообщение о запуске процесса создания архива со снимками')
    def test_8_photo_archive_notify_about_zip_task_runned(self):
        el["Уведомление о запуске процесса создания архива скриншотов"].assert_element_text("Началось создание архива снимков. Вы получите уведомление после завершения операции.")

    @title('Проверяем форму уведомления о завершении процесса создания архива со снимками')
    def test_9_photo_archive_information_about_zip_task_finish(self):
        with step("Проверяем текст уведомления о завершении процесса выгрузки архива со снимками"):
            el["Текст уведомления о завершении создании архива скриншотов"].assert_element_text("Создание архива снимков завершено.")
        with step("Проверяем наличие кнопки закрытия формы с уведомлением о завершении процесса выгрузки архива со снимками"):
            el["Кнопка закрытия формы с уведомлением о завршении создания архива скриншотов"].assert_element_interaction()
        with step("Проверяем доступность и название кнопки сохранения архива скриншотов"):
            el["Кнопка подтверждения скачивания архива скриншотов"].assert_element_text("Сохранить")
            el["Кнопка подтверждения скачивания архива скриншотов"].assert_element_interaction()
        with step("Закрываем форму с уведомлением о завершении процесса создания скриншота"):
            el["Кнопка закрытия формы с уведомлением о завршении создания архива скриншотов"].click()
            el["Текст уведомления о завершении создании архива скриншотов"].assert_element_not_existence()
