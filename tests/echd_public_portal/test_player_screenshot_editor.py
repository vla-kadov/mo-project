from lib import *
from allure import title, step, feature

el = {
    "Окно плеера": s(".media-container-window"),
    "Иконка камеры в плеере": s("[data-player='cameraTypeIcon']"),
    "Кнопка создания скриншота": s("div[data-camera-option-command='snapshot']", wait=50),
    "Заголовок формы создания скриншота": s("[data-test-id='8wal3y']"),
    "Кнопка 'Редактировать' режим скриншотов": ss("[data-test-id='1rju'] .ui-shadow-button")[0],
    "Кнопка изменения размера формы создания скриншотов": ss("[data-test-id='azqvxj']")[0],
    "Кнопка закрытия формы со скриншотами": ss("[data-test-id='azqvxj']")[1],
    "Кнопка 'Сохранить' редактора скриншотов": ss("[data-test-id='1rju'] .ui-shadow-button"),
    "Инструмент выбора цвета": s("[data-test-id='1rju'] [type='color']"),
    "Рисование": ss("[data-test-id='1rju'] #surface1")[0],
    "Рисование квадрата": ss("[data-test-id='1rju'] #surface1")[1],
    "Рисование круга": ss("[data-test-id='1rju'] #surface1")[2],
    "Рисование отрезков": ss("[data-test-id='1rju'] #surface1")[3],
    "Рисование стрелки": ss("[data-test-id='1rju'] #surface1")[4],
    "Добавление текста": ss("[data-test-id='1rju'] #surface1")[5],
    "Выбор толщины линии": ss("[data-test-id='1rju'] #surface1")[6],
    "Выбор размера шрифта": ss("[data-test-id='1rju'] #surface1")[7],
    "Отменить действие": ss("[data-test-id='1rju'] #surface1")[8],
    "Повторить действие": ss("[data-test-id='1rju'] #surface1")[9],
    "16 размер шрифта": ss("[data-test-id='1jdd6']")[0],
    "24 размер шрифта": ss("[data-test-id='1jdd6']")[1],
    "36 размер шрифта": ss("[data-test-id='1jdd6']")[2],
    "48 размер шрифта": ss("[data-test-id='1jdd6']")[3],
    "Текст подтверждения закрытия редактора": s(".confirm-window .ui-window-content"),
    "Кнопка подтверждения закрытия редактора": s("[data-key='js.button.ok']"),
    "Кнопка отмены закрытия редактора": s("[data-key='js.button.cancel']"),
    "Кнопка восстановления в редакторе": s(id="snapshot.button.restore"),
    "Область для рисования на скриншоте": s("[data-test-id='3mo93x'] canvas"),
    "Кнопка закрытия формы уведомления": s(".ui-close", wait=50)

}


@feature('Работа с плеером: Редактор скриншотов в плеере')
class TestPlayerScreenshotEditor(TestCase):

    @title('Закрываем окно с уведомлением об ответственности за распространение ссылок на обмен видео')
    def test_1_close_notification_form(self):
        el["Кнопка закрытия формы уведомления"].assert_element_existence_and_displayed()
        sleep(5)
        el["Кнопка закрытия формы уведомления"].click()

    @title("Проверяем наличие окна плеера на странице")
    def test_2_player_existence(self):
        el["Окно плеера"].assert_element_existence_and_displayed()

    @title("Нажимаем кнопку создания скриншота в плеере")
    def test_3_player_create_screenshot(self):
        sleep(20)
        el["Кнопка создания скриншота"].click()

    @title("Переходим в режим редактирования скриншота")
    def test_4_player_screenshot_assert_edit_button(self):
        el["Кнопка 'Редактировать' режим скриншотов"].assert_element_text("Редактировать")
        el["Кнопка 'Редактировать' режим скриншотов"].click()

    @title("Проверяем заголовок формы редактирования скриншота")
    def test_5_player_screenshot_edit__head(self):
        el["Заголовок формы создания скриншота"].assert_element_interaction()
        el["Заголовок формы создания скриншота"].assert_element_text("Режим редактирования скриншота")

    @title("Изменяем размер окна формы создания скриншота в плеере")
    def test_6_player_screenshot_edit_change_form_size(self):
        el["Кнопка изменения размера формы создания скриншотов"].assert_element_interaction()
        el["Кнопка изменения размера формы создания скриншотов"].click()

    @title("Возвращаем исходный размер окна формы создания скриншота в плеере")
    def test_7_player_screenshot_edit_change_form_size_restore(self):
        el["Кнопка изменения размера формы создания скриншотов"].assert_element_interaction()
        el["Кнопка изменения размера формы создания скриншотов"].click()

    @title("Проверяем наличие инструмента редактирования скриншота: Выбор цвета")
    def test_8_player_screenshot_edit_color_change(self):
        el["Инструмент выбора цвета"].assert_element_interaction()

    @title("Проверяем наличие инструмента редактирования скриншота: Повторить действие")
    def test_9_player_screenshot_edit_redo(self):
        el["Повторить действие"].assert_element_interaction()

    @title("Проверяем наличие инструмента редактирования скриншота: Отменить действие")
    def test_10_player_screenshot_edit_undo(self):
        el["Отменить действие"].assert_element_interaction()

    @title("Проверяем наличие и работоспособность инструмента редактирования скриншота: Выбор размера шрифта")
    def test_11_player_screenshot_edit_font_size(self):
        with step("Проверяем наличие и раскрываем выпадающий список для выбора размера шрифта"):
            el["Выбор размера шрифта"].assert_element_interaction()
            el["Выбор размера шрифта"].mouse_click()
        with step("Проверяем наличие текста с описанием размера шрифта и выбираем 16 шрифт"):
            el["16 размер шрифта"].assert_element_text("16")
            el["16 размер шрифта"].click()
        with step("Проверяем наличие текста с описанием размера шрифта и выбираем 24 шрифт"):
            el["24 размер шрифта"].assert_element_text("24")
            el["24 размер шрифта"].click()
        with step("Проверяем наличие текста с описанием размера шрифта и выбираем 36 шрифт"):
            el["36 размер шрифта"].assert_element_text("36")
            el["36 размер шрифта"].click()
        with step("Проверяем наличие текста с описанием размера шрифта и выбираем 48 шрифт"):
            el["48 размер шрифта"].assert_element_text("48")
            el["48 размер шрифта"].click()

    @title("Проверяем наличие инструмента редактирования скриншота: Выбор толщины линии")
    def test_12_player_screenshot_edit_line_size(self):
        el["Выбор толщины линии"].assert_element_interaction()

    @title("Проверяем наличие инструмента редактирования скриншота: Добавление текста")
    def test_13_player_screenshot_edit_text_add(self):
        el["Добавление текста"].assert_element_interaction()

    @title("Проверяем наличие инструмента редактирования скриншота: Рисование стрелки")
    def test_14_player_screenshot_edit_arrow_add(self):
        el["Рисование стрелки"].assert_element_interaction()

    @title("Проверяем наличие инструмента редактирования скриншота: Рисование отрезков")
    def test_15_player_screenshot_edit_line_add(self):
        el["Рисование отрезков"].assert_element_interaction()

    @title("Проверяем наличие инструмента редактирования скриншота: Рисование круга")
    def test_16_player_screenshot_edit_circle_add(self):
        el["Рисование круга"].assert_element_interaction()

    @title("Проверяем наличие инструмента редактирования скриншота: Рисование квадрата")
    def test_17_player_screenshot_edit_square_add(self):
        el["Рисование квадрата"].assert_element_interaction()

    @title("Проверяем наличие инструмента редактирования скриншота: Рисование")
    def test_18_player_screenshot_edit_marker_add(self):
        el["Рисование"].assert_element_interaction()

    @title("Проверяем логику отображения кнопки 'Восстановить' внося изменения в скриншот")
    def test_19_player_screenshot_edit_check_restore_button(self):
        with step("Проверяем отсутствие кнопки 'Восстановить до внесения изменений"):
            el["Кнопка восстановления в редакторе"].assert_element_not_existence()
        with step("Рисуем на скриншоте инструментом для рисования для проверки появления кнопки восстановления"):
            el["Область для рисования на скриншоте"].click()
        with step("Проверяем наличие кнопки 'Восстановить' после внесения изменений в скриншот"):
            el["Кнопка восстановления в редакторе"].assert_element_existence_and_displayed()
            el["Кнопка восстановления в редакторе"].assert_element_text("Восстановить")
        with step("Нажимаем на кнопку 'Восстановить' и проверяем, что после нажатия кнопка исчезла"):
            el["Кнопка восстановления в редакторе"].click()
            el["Кнопка восстановления в редакторе"].assert_element_not_existence()

    @title("Нажимаем кнопку закрытия формы создания скриншота в плеере и проверяем наличие подтверждения о выходе из редактора")
    def test_20_player_screenshot_edit_form_close(self):
        with step("Нажимаем кнопку закрытия формы редактирования скриншота"):
            el["Кнопка закрытия формы со скриншотами"].click()
        with step("Проверяем наличие текста-предупреждения о закрытии редактора скриншота"):
            el["Текст подтверждения закрытия редактора"].assert_element_text("Вы уверены, что хотите закрыть редактор?")
        with step("Проверяем наличие кнопки и название кнопки отмены закрытия редактора"):
            el["Кнопка отмены закрытия редактора"].assert_element_interaction()
            el["Кнопка отмены закрытия редактора"].assert_element_text_contains("Отмена")
        with step("Проверяем название кнопки подтверждения закрытия редактора и нажимаем на неё"):
            el["Кнопка подтверждения закрытия редактора"].assert_element_text("ОК")
            el["Кнопка подтверждения закрытия редактора"].click()
        with step("Проверяем отсутствие на странице формы редакторирования скриншота"):
            el["Заголовок формы создания скриншота"].assert_element_not_existence()
