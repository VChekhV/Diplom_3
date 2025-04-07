from random import randint
import allure
from pages.base_page import BasePage
from faker import Faker
from locators import Locators
from constants import Constants


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
    def sign_in(self):
        self.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        self.wait_for_page(Constants.PERSONAL_ACCOUNT_URL)
        self.fill_login_form(Locators.INPUT_EMAIL, Constants.EMAIL, Locators.INPUT_PASSWORD, Constants.PASSWORD, Locators.SIGN_IN_BTN)
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

    @allure.step("получение номера заказа")
    def find_new_order_number_in_orders_list(self):
        self.click_on_element(Locators.ORDERS_LIST_BTN)
        self.find_element_with_wait(Locators.ORDER_LIST_TITLE)
        return self.get_text_from_element(Locators.ORDER_NUMBER_IN_LIST)

    @allure.step("после оформления заказа его номер появляется в разделе «В работе»")
    def find_new_order_number_in_progress(self):
        self.wait_for_element_visible(Locators.ORDER_IN_PROGRESS)
        return '#' + self.get_text_from_element(Locators.ORDER_IN_PROGRESS)