from selenium.webdriver.common.by import By


class BasePageLocators:

    BUTTON_ORDER_HEADER = [By.XPATH, ".//button[text() = 'Заказать' and @class = 'Button_Button__ra12g']"]
    DZEN_ID = (By.XPATH, '//title[contains(text(), "Дзен")]')
    BUTTON_ACCEPT_COOKIE = [By.XPATH, '//button[@id="rcc-confirm-button"]']
