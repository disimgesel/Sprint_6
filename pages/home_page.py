from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class HomePage(BasePage):

    @allure.step('Возвращение текста элемента вопроса')
    def questions_about_important(self, locator_button, locator_text):
        self.wait_and_find_element(locator_button)
        element = self.driver.find_element(*locator_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)
        self.wait_element(locator_text)
        return self.driver.find_element(*locator_text).text

    @allure.step('Клик на кнопку "Заказать"')
    def click_button_order_in_body(self, locator):
        self.wait_element_in_body(locator)
        button = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step('Ожидание элемента вопроса')
    def wait_element_in_body(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    @allure.step('Отображение заголовка на домашней странице')
    def home_page_title_displayed(self, locator):
        return self.check_element_is_displaying(locator)
