from pages.home_page import HomePage
from pages.base_page import BasePage
from data import Data
from pages.order_page import OrderPage
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from data import Urls
import allure
import pytest
from faker import Faker

faker = Faker('ru_RU')


class TestOrder:

    @allure.title('Проверка позитивного сценария точки входа в оформление заказа самоката')
    @allure.description('Проверяю только точку входа в оформление заказа через кнопку "Заказать" в шапке страницы')
    def test_open_order_form_header(self, driver):
        order = HomePage(driver)
        order.open_page(Urls.HOME_PAGE)
        order_in_header = BasePage(driver)
        order_in_header.wait_element(BasePageLocators.BUTTON_ORDER_HEADER)
        order_in_header.click_on_element(BasePageLocators.BUTTON_ORDER_HEADER)
        order_in_header.wait_element(OrderPageLocators.TITLE_ORDER_TEXT)
        order_page = OrderPage(driver)
        title_text = order_page.get_text_from_element(OrderPageLocators.TITLE_ORDER_TEXT)
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
        order.click_cookie_accept(OrderPageLocators.BUTTON_ACCEPT_COOKIE)
        order.click_on_top_order_button()
        order.input_customer_information(name, surname, address, phone)
        order.wait_element(OrderPageLocators.BUTTON_NEXT)
        order.click_on_next_button()
        order.select_rent_info(comment)
        assert order.check_status_button_is_displayed()
