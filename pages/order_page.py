from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage(BasePage):

    @allure.step('Клик на кнопку "Заказать" в теле страницы')
    def click_on_top_order_button(self):
        self.click_on_element(HomePageLocators.BUTTON_ORDER_BODY)

    @allure.step('Заполнение страницы "Для кого самокат".')
    def input_customer_information(self, name, surname, address, phone):
        self.wait_element(OrderPageLocators.FIELD_NAME_INPUT)
        self.input_in_field(OrderPageLocators.FIELD_NAME_INPUT, name)
        self.wait_element(OrderPageLocators.FIELD_SURNAME_INPUT)
        self.input_in_field(OrderPageLocators.FIELD_SURNAME_INPUT, surname)
        self.wait_element(OrderPageLocators.FIELD_DELIVERY_ADDRESS_INPUT)
        self.input_in_field(OrderPageLocators.FIELD_DELIVERY_ADDRESS_INPUT, address)
        self.wait_element(OrderPageLocators.FIELD_METRO)
        self.click_on_element(OrderPageLocators.FIELD_METRO)
        self.wait_element(OrderPageLocators.METRO_STATIONS_SELECT)
        self.click_on_element(OrderPageLocators.SELECT_STATION)
        self.wait_element(OrderPageLocators.TELEPHONE_NUMBER)
        self.input_in_field(OrderPageLocators.TELEPHONE_NUMBER, phone)

    @allure.step('Клик на кнопку "Далее".')
    def click_on_next_button(self):
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполняем страницу "Про аренду"')
    def select_rent_info(self, comment):
        self.wait_element(OrderPageLocators.FIELD_DELIVERY_DATE)
        self.click_on_element(OrderPageLocators.FIELD_DELIVERY_DATE)
        self.wait_element(OrderPageLocators.FIELD_CALENDAR)
        self.click_on_element(OrderPageLocators.FIELD_CALENDAR_DAY)
        self.wait_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.wait_element(OrderPageLocators.RENTAL_DURETION)
        self.click_on_element(OrderPageLocators.RENTAL_DURETION)
        self.click_on_element(OrderPageLocators.SCOOTER_COLOUR_SELECT)
        self.wait_element(OrderPageLocators.FIELD_COMMENT)
        self.input_in_field(OrderPageLocators.FIELD_COMMENT, comment)
        self.click_on_element(OrderPageLocators.CREATE_ORDER_BUTTON)
        self.wait_element(OrderPageLocators.BUTTON_CONFIRM)
        self.click_on_element(OrderPageLocators.BUTTON_CONFIRM)

    @allure.step('Проверка отображения кнопки "Посмотреть статус"')
    def check_status_button_is_displayed(self):
        return self.check_element_is_displaying(OrderPageLocators.CHECK_STATUS_ORDER)
