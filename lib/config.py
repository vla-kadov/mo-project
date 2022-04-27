# -*- coding: utf-8 -*-


class Config:

    # Параметр: использовать ли удаленное подключение
    use_grid = False

    # Параметр: использовать ли прокси для логирования запросов
    use_proxy = False

    # Параметр: путь до каталога со скриптами запуска прокси
    browsermob_proxy_path = ''

    # Параметр: использовать ли подробное логирование и репортинг всех действий
    detailed_steps = False

    # Параметр: браузер, используемый для запуска тестов
    browser = 'chrome'

    # Параметр: адрес удаленного grid-хоста
    grid_hub_host = ''

    # Параметр: платформа запуска тестов
    webdriver_platform = 'Windows'

    # Параметр: время ожидания по умолчанию
    wait_timeout = 120

    # Параметр: частота попыток при ожидании
    pool_frequency = 0.1

    # Параметр: путь до драйвера chrome
    chrome_webdriver_path = 'C:/chromedriver/chromedriver.exe'

    # Параметр: путь до драйвера firefox
    firefox_webdriver_path = ''

    # Параметр: путь до драйвера edge
    edge_webdriver_path = ''

    # Параметр: базовый url
    portal_address = ''

    # Параметр: Прикадывать HTML страницу действия к отчёту allure
    attach_html = False
