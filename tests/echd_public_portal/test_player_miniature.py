from lib import *
from allure import title, step, feature

el = {
    "Окно плеера": s(".media-container-window",wait=30),
    "Признак контрактной камеры": s(".contact-camera-icon"),
    "Свернуть плеер в миниатюру": s("[data-tooltip-key='hint.player.minimize']"),
    "Увеличить миниатюру": s("[data-tooltip-key='hint.player.size.change']"),
    "Уменьшить миниатюру": s("[data-player-argument='false'][data-tooltip-key='hint.player.size.change']"),
    "Вывести плеер из режима миниатюр": s("[data-tooltip-key='hint.player.restore']"),
    "Перезагрузить видеопоток": s(".matrix-controls [data-player-command='reloadVideo'][data-tooltip-key='hint.player.camera.reconnect']"),
    "Режим просмотра кадрами": s("[data-tooltip-key='hint.player.camera.slide.mode']"),
    "Загрузить текущий кадр в покадровом режиме просмотра": s("[data-tooltip-key='hint.player.camera.slide.next']"),
    "Вернуться в стандартный режим просмотра": s("[data-tooltip-key='hint.player.camera.play.video']"),
    "Кнопка закрытия формы уведомления": s(".ui-close", wait=30)

}


@feature('Работа с плеером: Режим миниатюр')
class TestPlayerMiniature(TestCase):

    @title('Закрываем окно с уведомлением об ответственности за распространение ссылок на обмен видео')
    def test_1_close_notification_form(self):
        el["Кнопка закрытия формы уведомления"].assert_element_existence_and_displayed()
        sleep(5)
        el["Кнопка закрытия формы уведомления"].click()

    @title("Проверяем наличие окна плеера на странице")
    def test_2_player_existence(self):
        el["Окно плеера"].assert_element_existence_and_displayed()

    @title("Нажимаем кнопку перевода плеера в режим миниатюр")
    def test_3_miniature_mode(self):
        el["Свернуть плеер в миниатюру"].click()

    @title("Нажимаем кнопку увеличения размера миниатюры")
    def test_4_miniature_max_size(self):
        el["Увеличить миниатюру"].mouse_move_to_element()
        el["Увеличить миниатюру"].mouse_click()

    @title("Нажимаем кнопку возврата размера миниатюры в исходный режим")
    def test_5_miniature_restore_size(self):
        el["Уменьшить миниатюру"].mouse_click()
        sleep(10)

    @title("Проверяем наличие иконки-признака контрактной камеры в режиме миниатюры")
    def test_6_miniature_contract_icon(self):
        el["Признак контрактной камеры"].mouse_move_to_element()
        el["Признак контрактной камеры"].assert_element_existence_and_displayed()

    @title("Нажимаем кнопку включения просмотра видео в покадровом режиме")
    def test_7_miniature_slide_mod_on(self):
        el["Режим просмотра кадрами"].mouse_move_to_element()
        el["Режим просмотра кадрами"].click()

    @title("Нажимаем кнопку получения нового кадра в режиме покадрового просмотра видео")
    def test_8_miniature_slide_mod_new_slide(self):
        sleep(5)
        el["Загрузить текущий кадр в покадровом режиме просмотра"].mouse_move_to_element()
        el["Загрузить текущий кадр в покадровом режиме просмотра"].click()

    @title("Нажимаем кнопку выхода из режимма покадрового просмотра видео")
    def test_9_miniature_slide_mod_off(self):
        el["Вернуться в стандартный режим просмотра"].mouse_move_to_element()
        el["Вернуться в стандартный режим просмотра"].click()

    @title("Нажимаем кнопку перезагрузки видеопотока")
    def test_10_miniature_refresh_video(self):
        el["Перезагрузить видеопоток"].mouse_move_to_element()
        el["Перезагрузить видеопоток"].click()

    @title("Нажимаем кнопку вывода плеера из режима миниатюр")
    def test_11_miniature_mode_exit(self):
        el["Вывести плеер из режима миниатюр"].mouse_move_to_element()
        el["Вывести плеер из режима миниатюр"].mouse_click()
