from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from data import Data
from data import Urls
import allure




class TestLogoRedirect:

    @allure.title('Редирект на главную страницу через логотип Самоката')
    @allure.step('Переход на домашнюю страницу при нажатии на логотип Самоката')
    def test_logo_scooter_redirect_to_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.open_page(Urls.HOME_PAGE)
        home_page.click_cookie_accept(HomePageLocators.BUTTON_ACCEPT_COOKIE)
        home_page.click_on_element(HomePageLocators.BUTTON_ORDER_TOP)
        home_page.wait_element(HomePageLocators.LOGO_SCOOTER)
        home_page.click_on_element(HomePageLocators.LOGO_SCOOTER)
        home_page.wait_element(HomePageLocators.HOME_TITLE)
        assert home_page.home_page_title_displayed(HomePageLocators.HOME_TITLE)

    @allure.title('Редирект на страницу Дзена через логотип Яндекса')
    @allure.step('Переход на страницу Дзена и переключение на новую вкладку при нажатии на логотип Яндекса')
    def test_logo_yandex_redirect_to_dzen(self, driver):
        home_page = HomePage(driver)
        home_page.open_page(Urls.HOME_PAGE)
        home_page.click_cookie_accept(HomePageLocators.BUTTON_ACCEPT_COOKIE)
        home_page.click_on_element(HomePageLocators.LOGO_YANDEX)
        home_page.switch_to_next_tab()
        assert home_page.get_page_title(HomePageLocators.DZEN_ID) == Data.DZEN_ID_TEXT