from data import Data
from pages.order_page import OrderPage
from data import Urls
import allure
import pytest
from faker import Faker
faker = Faker('ru_RU')


class TestOrder:

    @allure.title('Проверка позитивного сценария точки входа в оформление заказа самоката')
    @allure.description('Проверяю только точку входа в оформление заказа через кнопку "Заказать" в шапке страницы')
    def test_open_order_form_header(self, driver):
        order = OrderPage(driver)
        order.open_page(Urls.HOME_PAGE)
        order.click_cookie_accept()
        title_text = order.open_order_form_header()
        assert title_text == Data.EXPECTED_TITLE_TEXT

    @allure.title('Проверка позитивного сценария оформления заказа самоката')
    @allure.description('Сквозная проверка процесса оформления заказа с использованием двух наборов данных и точкой входа кнопки "Заказать в теле страницы".')
    @pytest.mark.parametrize("name, surname, address, phone, comment", [
        (faker.first_name(), faker.last_name(), faker.street_name(), faker.numerify('8831#########'), faker.ascii_free_email()),
        (faker.first_name(), faker.last_name(), faker.street_name(), faker.numerify('8831#########'), faker.ascii_free_email())
    ])
    def test_order_page(self, driver, name, surname, address, phone, comment):
        order = OrderPage(driver)
        order.open_page(Urls.HOME_PAGE)
        order.click_cookie_accept()
        order.click_on_top_order_button()
        order.input_customer_information(name, surname, address, phone)
        order.wait_element_button_next()
        order.click_on_next_button()
        order.select_rent_info(comment)
        assert order.check_status_button_is_displayed()
