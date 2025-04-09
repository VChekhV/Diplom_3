from locators import Locators
from pages.main_functions_page import MainFunctionsPage
import allure

class TestMainFunctionsPage:

    @allure.title("переход по клику на «Конструктор»")
    def test_go_to_constructor_section(self, driver):
        main_functions_page = MainFunctionsPage(driver)
        result = main_functions_page.go_to_constructor_page()
        assert result

    @allure.title("переход по клику на «Лента заказов»")
    def test_go_to_order_list_section(self, driver):
        main_functions_page = MainFunctionsPage(driver)
        result = main_functions_page.go_to_orders_list_page()
        assert result

    @allure.title("если кликнуть на ингредиент, появится всплывающее окно с деталям")
    def test_poppup_with_ingredients_details(self, driver):
        main_functions_page = MainFunctionsPage(driver)
        result = main_functions_page.open_ingredients_ditales()
        assert result

    @allure.title("всплывающее окно закрывается кликом по крестику")
    def test_popup_close(self, driver):
        main_functions_page = MainFunctionsPage(driver)
        popup = main_functions_page.open_ingredients_ditales()
        assert popup.is_displayed()
        main_functions_page.close_popup()
        popup = main_functions_page.wait_for_element_invisible(Locators.INGREDIENT_POPUP)
        assert not popup.is_displayed()

    @allure.title("при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_counter(self, driver):
        main_functions_page = MainFunctionsPage(driver)
        main_functions_page.add_ingredients()
        counter = main_functions_page.get_text_from_element(Locators.SAUSE_SPICY_X_INGREDIENT_COUNTER)
        assert counter == "1"

    @allure.title("залогиненный пользователь может оформить заказ")
    def test_make_order_authorised_user(self, driver):
        main_functions_page = MainFunctionsPage(driver)
        main_functions_page.sign_in()
        main_functions_page.make_new_order()
        result = main_functions_page.find_element_with_wait(Locators.ORDER_SUBTITLE)
        assert result