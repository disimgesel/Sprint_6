from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Страница "Для кого самокат"
    TITLE_ORDER_TEXT = [By.XPATH, ".//div[text() = 'Для кого самокат']"]
    FIELD_NAME_INPUT = [By.XPATH, ".//input[@placeholder = '* Имя']"]
    FIELD_SURNAME_INPUT = [By.XPATH, '//input[@placeholder="* Фамилия"]']
    FIELD_DELIVERY_ADDRESS_INPUT = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']
    FIELD_METRO = [By.XPATH, '//input[@class="select-search__input"]']
    METRO_STATIONS_SELECT = [By.XPATH, '//div[@class="select-search__select"]']
    SELECT_STATION = [By.XPATH, '//button[@value="4"]']
    TELEPHONE_NUMBER = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']
    BUTTON_NEXT = [By.XPATH, '//button[text()="Далее"]']
    BUTTON_ACCEPT_COOKIE = [By.XPATH, '//button[@id="rcc-confirm-button"]']

    # Страница  "Про аренду"
    TITLE_RENT_INFO_PAGE = [By.XPATH, '//div[contains(text(),"Про аренду")]']
    FIELD_DELIVERY_DATE = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']
    FIELD_CALENDAR = [By.XPATH, '//div[@class="react-datepicker-popper"]']
    FIELD_CALENDAR_DAY = [By.XPATH, '//div[contains(@class, "react-datepicker__day react-datepicker__day--031")]']
    RENTAL_PERIOD_FIELD = [By.XPATH, '//div[text()="* Срок аренды"]']
    RENTAL_DURETION = [By.XPATH, '//div[contains(text(),"сутки")]']
    SCOOTER_COLOUR_SELECT = [By.XPATH, '//input[@id="black"]']
    FIELD_COMMENT = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']
    CREATE_ORDER_BUTTON = [By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]']
    BUTTON_CONFIRM = [By.XPATH, '//button[contains(text(),"Да")]']
    CHECK_STATUS_ORDER = [By.XPATH, '//button[contains(text(),"Посмотреть статус")]']
