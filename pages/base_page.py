from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с ожиданием')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Открытие страницы')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Клик на кнопку разрешения использования cookies')
    def click_cookie_accept(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).click()

    @allure.step('Ожидание прогрузки элемента и скролл до него')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    @allure.step('Ввод занчения в поле')
    def input_in_field(self, locator, meaning):
        element = self.wait_and_find_element(locator)
        element.send_keys(meaning)

    @allure.step('Проверка прогрузки элемента')
    def check_element_is_displaying(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Получение текста элемента')
    def get_text_from_element(self, locator):  # Получили текст элемента
        element = self.wait_and_find_element(locator)
        return element.text

    @allure.step('Переключение на другую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получение заголовка страницы')
    def get_page_title(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return self.driver.title
