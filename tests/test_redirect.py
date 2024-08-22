from pages.home_page import HomePage
from data import Data
import allure


class TestLogoRedirect:

    @allure.title('Редирект на главную страницу через логотип Самоката')
    @allure.step('Переход на домашнюю страницу при нажатии на логотип Самоката')
    def test_logo_scooter_redirect_to_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.logo_scooter_redirect_to_home_page()
        assert home_page.home_page_title_displayed()

    @allure.title('Редирект на страницу Дзена через логотип Яндекса')
    @allure.step('Переход на страницу Дзена и переключение на новую вкладку при нажатии на логотип Яндекса')
    def test_logo_yandex_redirect_to_dzen(self, driver):
        home_page = HomePage(driver)
        home_page.logo_yandex_redirect_to_dzen()
        assert home_page.get_page_title() == Data.DZEN_ID_TEXT
