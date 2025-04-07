from selenium.webdriver.common.by import By

class Locators:
    PERSONAL_ACCOUNT_BTN = (By.XPATH, '//a[@href="/account"]')  # Кнопка "Личный кабинет"
    SIGN_UP_LINK = (By.XPATH, '//a[@href="/register"]')  # Ссылка на регистрацию
    INPUT_NAME = (By.XPATH, '//label[contains(text(),"Имя")]/following-sibling::input[@name="name"]')  # Поле ввода имени
    INPUT_EMAIL = (By.XPATH, '//label[contains(text(),"Email")]/following-sibling::input[@name="name"]')  # Поле ввода почты
    INPUT_PASSWORD = (By.XPATH, '//label[contains(text(),"Пароль")]/following-sibling::input[@name="Пароль"]')  # Поле ввода пароля
    SIGN_UP_BTN = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # Кнопка "Зарегистрироваться"
    SIGN_IN_BTN = (By.XPATH, '//button[text()="Войти"]')  # Кнопка "Войти"
    SIGN_TO_ACCOUNT_BTN = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # Кнопка "Войти в аккаунт"
    SIGN_IN_TITLE = (By.XPATH, '//h2[text()="Вход"]')  # Заголовок "Вход"
    ERROR_WRONG_PASSWORD = (By.XPATH, '//p[text()="Некорректный пароль"]')  # Ошибка "Некорректный пароль"
    CONSTRUCTOR_TITLE = (By.XPATH, '//h1[text()="Соберите бургер"]')  # Заголовок "Соберите бургер"
    SIGN_IN_LINK = (By.XPATH, '//a[@href="/login"]')  # Ссылка на вход
    CONSTRUCTOR_BTN = (By.XPATH, '//a[@href="/"]')  # Кнопка перехода на страницу конструктора
    ORDERS_LIST_BTN = (By.XPATH, '//a[@href="/feed"]')  # Кнопка перехода на страницу заказов
    LOGO_BTN = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')  # Кнопка перехода на главную страницу
    PROFILE_LINK = (By.XPATH, '//a[@href="/account/profile"]')  # Ссылка на личный кабинет
    SIGN_OUT_BTN = (By.XPATH, '//button[text()="Выход"]')   # Кнопка "Выход"
    SAUCE_LINK = (By.XPATH, '//span[text()="Соусы"]')   # Ссылка "Соусы"
    FILLINGS_LINK = (By.XPATH, '//span[text()="Начинки"]')   # Ссылка "Начинки"
    BUNS_LINK = (By.XPATH, '//span[text()="Булки"]')   # Ссылка "Булки"
    CURRENT_MENU_LINK = (By.CLASS_NAME, 'tab_tab_type_current__2BEPc')  # Выбранный раздел меню
    HISTORY_BTN = (By.XPATH, '//a[text()="История заказов"]')   # Кнопка "История заказов"
    CHANGE_PASSWORD_LINK = (By.XPATH, '//a[@href="/forgot-password"]')  # Ссылка на восстановление пароля
    CHANGE_PASSWORD_TITLE = (By.XPATH, '//h2[text()="Восстановление пароля"]')  # Заголовок "Восстановление пароля"
    CHANGE_PASSWORD_BTN = (By.XPATH, '//button[text()="Восстановить"]')   # Кнопка "Восстановить"
    SAVE_NEW_PASSWORD_BTN = (By.XPATH, '//button[text()="Сохранить"]')   # Кнопка "Сохранить"
    NEW_PASSWORD_INPUT= (By.XPATH, '//input[@name="Введите новый пароль"]') # Поле ввода нового пароля
    SHOW_PASSWORD_BTN = (By.XPATH, '//div[@class="input__icon input__icon-action"]') # Кнопка отображения
    BURGER_LOCATOR = (By.XPATH, '//p[contains(text(),"Флюоресцентная булка")]')
    INGREDIENT_DETAILS_TITLE = (By.XPATH, '//h2[text()="Детали ингредиента"]') # Заголовок у popup
    INGREDIENT_POPUP = (By.XPATH, '//section[contains(@class,"Modal_modal")]')
    ORDER = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem__2x95r")]')
    ORDERS_POPUP = (By.XPATH, '//section[contains(@class,"Modal_modal_opened")]')
    CLOSE_ICON_BTN = (By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]') # Иконка крестик на popup
    SAUSE_SPICY_X_INGREDIENT_COUNTER = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']//div[contains(@class, 'counter_counter__ZNLkj')]") # Счетчик у соуса
    SAUSE_SPICY_X_INGREDIENT = (By.XPATH, '//p[contains(text(), "Соус Spicy-X")]')
    BASKET_LOCATOR = (By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]') # Поле корзины
    MAKE_ORDER_BTN = (By.XPATH, '//button[text()="Оформить заказ"]')   # Кнопка "Оформить заказ"
    ORDER_SUBTITLE = (By.XPATH, '//p[text()="идентификатор заказа"]') # Подзаголовок на popup
    ORDER_LIST_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')
    BUN = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    ORDER_NUMBER_IN_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]//p[contains(@class, 'text_type_digits-default')]")
    ALL_ORDERS = (By.XPATH, "//div[contains(@class,'undefined')]//p[contains(@class, 'text_type_digits-large')]")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li[contains(@class,'text_type_digits')]")
    LOADER = (By.XPATH, "//img[contains(@class, 'Modal_modal__loading')]")