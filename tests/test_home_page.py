from pages.home_page import HomePage
from locators.home_page_locators import HomePageLocators
from data import QuestionsText
from data import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure


class TestQuestion:

    @allure.title('Проверка отображения текста овета на вопрос')
    @allure.description('Проверка отображения текстов оветов на 8 вопросов')
    @pytest.mark.parametrize(
    'locator_button,locator_ansver, expected_result',
    [
        [HomePageLocators.QUESTION_PRICE_BUTTON, HomePageLocators.QUESTION_PRICE_TEXT, QuestionsText.TEXT_QUESTION_PRICE],
        [HomePageLocators.SEVERAL_SCOOTERS_BUTTON, HomePageLocators.SEVERAL_SCOOTERS_TEXT, QuestionsText.TEXT_SEVERAL_SCOOTERS],
        [HomePageLocators.COST_CALCULATION_BUTTON, HomePageLocators.COST_CALCULATION_TEXT, QuestionsText.TEXT_COST_CALCULATION],
        [HomePageLocators.SCOOTER_TODAY_BUTTON, HomePageLocators.SCOOTER_TODAY_TEXT, QuestionsText.TEXT_SCOOTER_TODAY],
        [HomePageLocators.EXTEND_ORDER_BUTTON, HomePageLocators.EXTEND_ORDER_TEXT, QuestionsText.TEXT_EXTEND_ORDER],
        [HomePageLocators.DELIVER_CHARGING_BUTTON, HomePageLocators.DELIVER_CHARGING_TEXT, QuestionsText.TEXT_DELIVER_CHARGING],
        [HomePageLocators.CANCEL_ORDER_BUTTON, HomePageLocators.CANCEL_ORDER_TEXT, QuestionsText.TEXT_CANCEL_ORDER],
        [HomePageLocators.LIVE_OUTSIDE_MKD_BUTTON, HomePageLocators.LIVE_OUTSIDE_MKD_TEXT, QuestionsText.TEXT_LIVE_OUTSIDE_MKD]
    ])
    def test_questions_about_important(self, driver, locator_button, locator_ansver, expected_result):
        question = HomePage(driver)
        question.open_page(Urls.HOME_PAGE)
        question.click_cookie_accept(HomePageLocators.BUTTON_ACCEPT_COOKIE)
        ansver = question.questions_about_important(locator_button, locator_ansver)
        assert ansver == expected_result
