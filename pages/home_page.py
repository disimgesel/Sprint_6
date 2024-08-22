from pages.base_page import BasePage
import allure
from locators.home_page_locators import HomePageLocators
from data import Urls


class HomePage(BasePage):

    @allure.step('Возвращение текста элемента вопроса')
    def questions_about_important(self, locator_button, locator_text):
        self.click_on_element_js(locator_button)
        self.wait_element(locator_text)
        return self.get_text_from_element(locator_text)

    @allure.step('Отображение заголовка на домашней странице')
    def home_page_title_displayed(self):
        return self.check_element_is_displaying(HomePageLocators.HOME_TITLE)

    @allure.step('Редирект на домашнюю страницу')
    def logo_scooter_redirect_to_home_page(self):
        self.open_page(Urls.HOME_PAGE)
        self.click_cookie_accept()
        self.click_on_element(HomePageLocators.BUTTON_ORDER_TOP)
        self.wait_element(HomePageLocators.LOGO_SCOOTER)
        self.click_on_element(HomePageLocators.LOGO_SCOOTER)
        self.wait_element(HomePageLocators.HOME_TITLE)

    @allure.step('Редирект на дзен')
    def logo_yandex_redirect_to_dzen(self):
        self.open_page(Urls.HOME_PAGE)
        self.click_cookie_accept()
        self.click_on_element(HomePageLocators.LOGO_YANDEX)
        self.switch_to_next_tab()
