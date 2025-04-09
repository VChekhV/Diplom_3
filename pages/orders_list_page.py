from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.base_page import BasePage
from locators import Locators


class OrdersListPage(BasePage):
    @allure.step("переход по клику на «Лента заказов»")
    def open_orders_list(self):
        self.click_on_element(Locators.ORDERS_LIST_BTN)
        self.find_element_with_wait(Locators.ORDER_LIST_TITLE)

    @allure.step("если кликнуть на заказ, откроется всплывающее окно с деталями")
    def open_order_popup(self):
        self.click_on_element(Locators.ORDER)
        return self.wait_for_element_visible(Locators.ORDERS_POPUP)

    @allure.step("авторизация пользователя")
    def sign_in(self, email, password, personal_account_url):
        self.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        self.wait_for_page(personal_account_url)
        self.fill_login_form(
            Locators.INPUT_EMAIL, email,
            Locators.INPUT_PASSWORD, password,
            Locators.SIGN_IN_BTN
        )
        self.find_element_with_wait(Locators.CONSTRUCTOR_TITLE)

    @allure.step("создание нового заказа")
    def make_new_order(self):
        self.drag_and_drop_item(Locators.BUN, Locators.BASKET_LOCATOR)
        self.drag_and_drop_item(Locators.SAUSE_SPICY_X_INGREDIENT, Locators.BASKET_LOCATOR)
        self.click_on_element(Locators.MAKE_ORDER_BTN)
        self.find_element_with_wait(Locators.ORDER_SUBTITLE)
        self.wait_for_element_invisible(Locators.LOADER, 10)

    @allure.step("получение номера заказа")
    def get_new_order_number(self):
        return '#0' + self.get_text_from_element(Locators.ORDER_NUMBER)

    @allure.step("получение номера заказа из списка")
    def find_new_order_number_in_orders_list(self):
        self.click_on_element(Locators.ORDERS_LIST_BTN)
        self.find_element_with_wait(Locators.ORDER_LIST_TITLE)
        latest_order = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.LATEST_ORDER_NUMBER))
        # Возвращаем номер без дополнительного '#' (только цифры)
        return latest_order.text.lstrip('#')

    @allure.step("получение номера заказа в разделе 'В работе'")
    def find_new_order_number_in_progress(self):
        # Ждем, пока номер заказа появится в разделе "В работе"
        order_in_progress = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER_IN_PROGRESS))
        return '#' + order_in_progress.text