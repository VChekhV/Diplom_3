# test_orders_list_page.py
from locators import Locators
from pages.orders_list_page import OrdersListPage
import allure
from constants import Constants


class TestOrdersListPage:
    @allure.title("если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_orders_list_poppup_with_ingredients_details(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.open_orders_list()
        popup = orders_list_page.open_order_popup()
        assert popup.is_displayed()

    @allure.title("заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_users_orders_displayed(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.sign_in(
            Constants.EMAIL,
            Constants.PASSWORD,
            Constants.PERSONAL_ACCOUNT_URL
        )
        orders_list_page.make_new_order()
        user_order_number = orders_list_page.get_new_order_number()  # Формат: "#0210478"
        orders_list_page.click_on_element(Locators.CLOSE_ICON_BTN)
        order_number = orders_list_page.find_new_order_number_in_orders_list()  # Формат: "0210478"

        # Сравниваем, убрав '#' из user_order_number
        assert user_order_number.lstrip('#') == order_number

    @allure.title("при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_count_of_all_orders(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.open_orders_list()
        before_order = int(orders_list_page.get_text_from_element(Locators.ALL_ORDERS))
        orders_list_page.sign_in(
            Constants.EMAIL,
            Constants.PASSWORD,
            Constants.PERSONAL_ACCOUNT_URL
        )
        orders_list_page.make_new_order()
        orders_list_page.click_on_element(Locators.CLOSE_ICON_BTN)
        orders_list_page.open_orders_list()
        after_order = int(orders_list_page.get_text_from_element(Locators.ALL_ORDERS))
        assert before_order < after_order

    @allure.title("при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_count_of_today_orders(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.open_orders_list()
        before_order = int(orders_list_page.get_text_from_element(Locators.TODAY_ORDERS))
        orders_list_page.sign_in(
            Constants.EMAIL,
            Constants.PASSWORD,
            Constants.PERSONAL_ACCOUNT_URL
        )
        orders_list_page.make_new_order()
        orders_list_page.click_on_element(Locators.CLOSE_ICON_BTN)
        orders_list_page.open_orders_list()
        after_order = int(orders_list_page.get_text_from_element(Locators.TODAY_ORDERS))
        assert before_order < after_order

    @allure.title("после оформления заказа его номер появляется в разделе В работе")
    def test_order_in_progress(self, driver):
        orders_list_page = OrdersListPage(driver)
        orders_list_page.sign_in(
            Constants.EMAIL,
            Constants.PASSWORD,
            Constants.PERSONAL_ACCOUNT_URL
        )
        orders_list_page.make_new_order()
        user_order_number = orders_list_page.get_new_order_number()
        orders_list_page.click_on_element(Locators.CLOSE_ICON_BTN)
        orders_list_page.open_orders_list()
        # Ждем, пока номер заказа появится в разделе "В работе"
        order_number = orders_list_page.find_new_order_number_in_progress()
        assert user_order_number == order_number