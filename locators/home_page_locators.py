from selenium.webdriver.common.by import By


class HomePageLocators:

    QUESTION_PRICE_BUTTON = [By.XPATH, ".//div[@id='accordion__heading-0']"]
    QUESTION_PRICE_TEXT = [By.XPATH, ".//p[text() = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.']"]
    SEVERAL_SCOOTERS_BUTTON = [By.XPATH, ".//div[@id='accordion__heading-1']"]
    SEVERAL_SCOOTERS_TEXT = [By.XPATH, ".//p[text() = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']"]
    COST_CALCULATION_BUTTON = [By.XPATH, ".//div[@id='accordion__heading-2']"]
    COST_CALCULATION_TEXT = [By.XPATH, ".//p[text() = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']"]
    SCOOTER_TODAY_BUTTON = [By.XPATH, ".//div[@id='accordion__heading-3']"]
    SCOOTER_TODAY_TEXT = [By.XPATH, ".//p[text() = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.']"]
    EXTEND_ORDER_BUTTON = [By.XPATH, ".//div[@id='accordion__heading-4']"]
    EXTEND_ORDER_TEXT = [By.XPATH, ".//p[text() = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']"]
    DELIVER_CHARGING_BUTTON = [By.XPATH, ".//div[@id='accordion__heading-5']"]
    DELIVER_CHARGING_TEXT = [By.XPATH, ".//p[text() = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']"]
    CANCEL_ORDER_BUTTON = [By.XPATH, ".//div[@id='accordion__heading-6']"]
    CANCEL_ORDER_TEXT = [By.XPATH, ".//p[text() = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']"]
    LIVE_OUTSIDE_MKD_BUTTON = [By.XPATH, ".//div[@id='accordion__heading-7']"]
    LIVE_OUTSIDE_MKD_TEXT = [By.XPATH, ".//p[text() = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']"]
    BUTTON_ORDER_BODY = [By.XPATH, ".//button[text() = 'Заказать' and @class = 'Button_Button__ra12g Button_Middle__1CSJM']"]
    BUTTON_ACCEPT_COOKIE = [By.XPATH, '//button[@id="rcc-confirm-button"]']
    BUTTON_ORDER_TOP = (By.XPATH, '//div[contains(@class, "Header_Nav")]')
    LOGO_SCOOTER = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')
    HOME_TITLE = (By.XPATH, '//div[contains(@class, "Home_Header__")]')
    LOGO_YANDEX = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')
    DZEN_ID = (By.XPATH, '//title[contains(text(), "Дзен")]')
