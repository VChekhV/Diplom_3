from random import randint
import allure
from pages.base_page import BasePage
from faker import Faker
from locators import Locators
from constants import Constants


class MainFunctionsPage(BasePage):

    @allure.step("проверка открытия и закрытия всплывающего окна")
    def is_popup_visible(self):
        popup = self.find_element_with_wait(Locators.INGREDIENT_POPUP)
        return "visible" in popup.get_attribute('visibility')

    @allure.step("переход по клику на «Конструктор»")
    def go_to_constructor_page(self):
        self.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        self.find_element_with_wait(Locators.SIGN_IN_TITLE)
        self.click_on_element(Locators.CONSTRUCTOR_BTN)
        return self.find_element_with_wait(Locators.CONSTRUCTOR_TITLE)

    @allure.step("переход по клику на «Лента заказов»")
    def go_to_orders_list_page(self):
        self.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        self.find_element_with_wait(Locators.SIGN_IN_TITLE)
        self.click_on_element(Locators.ORDERS_LIST_BTN)
        return self.find_element_with_wait(Locators.ORDER_LIST_TITLE)

    @allure.step("если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def open_ingredients_ditales(self):
        self.click_on_element(Locators.BURGER_LOCATOR)
        return self.find_element_with_wait(Locators.INGREDIENT_DETAILS_TITLE)

    @allure.step("закрытие всплывающего окна по нажатию крестика")
    def close_popup(self):
        self.find_element_with_wait(Locators.INGREDIENT_DETAILS_TITLE)
        self.click_on_element(Locators.CLOSE_ICON_BTN)

    @allure.step("добавление ингредиентов в заказ")
    def add_ingredients(self):
        self.drag_and_drop_item(Locators.SAUSE_SPICY_X_INGREDIENT, Locators.BASKET_LOCATOR)
        self.find_element_with_wait(Locators.SAUSE_SPICY_X_INGREDIENT)

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