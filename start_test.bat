cls
rmdir /Q /S allure-results
del /Q work_log.log

python configuration.py --use_proxy False --detailed_steps True --portal_address https://ya.ru
pytest --alluredir ./allure-results tests\mo_portal\test_auth.py -v -s

allure serve allure-results
