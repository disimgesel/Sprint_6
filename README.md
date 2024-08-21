# qa_python_6
Проект содержит UI тесты для web-сервиса "Яндекс.Самокат", URL = https://stellarburgers.nomoreparties.site/
В директории tests находятся файлы с тестами:
    - test_home_page:
        - def test_questions_about_important (Проверка отображения текста овета на вопрос)
    - test_order_page:
        - def test_open_order_form_header (Проверка позитивного сценария точки входа в оформление заказа самоката)
        - def test_order_page (Проверка позитивного сценария оформления заказа самоката)
    - test_redirect:
        - def test_logo_scooter_redirect_to_home_page (Редирект на главную страницу через логотип Самоката)
        - def test_logo_yandex_redirect_to_dzen (Редирект на страницу Дзена через логотип Яндекса)
В проекте содержится отчет Allure (http://192.168.50.69:63059/index.html Сформированный отчет в моей локальной сети)
