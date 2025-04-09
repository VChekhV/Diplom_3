from locators import Locators
from pages.personal_account_page import PersonalAccountPage
from constants import Constants
import allure
class TestPersonalAccountPage:

    @allure.title("переход по клику на «Личный кабинет»,")
    def test_go_to_personal_account(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        result = personal_account_page.go_to_personal_page()
        assert driver.current_url == Constants.PERSONAL_ACCOUNT_URL
        assert result

    @allure.title("выход из аккаунта")
    def test_logout_from_personal_account(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.sign_in()
        result = personal_account_page.sign_out()
        assert driver.current_url == Constants.PERSONAL_ACCOUNT_URL
        assert result

    @allure.title("переход в раздел «История заказов»")
    def test_go_to_history_list(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        personal_account_page.wait_for_page(Constants.PERSONAL_ACCOUNT_URL)
        personal_account_page.fill_login_form(Locators.INPUT_EMAIL, Constants.EMAIL, Locators.INPUT_PASSWORD, Constants.PASSWORD, Locators.SIGN_IN_BTN)
        personal_account_page.find_element_with_wait(Locators.CONSTRUCTOR_TITLE)
        personal_account_page.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        personal_account_page.click_on_element(Locators.HISTORY_BTN)
        assert driver.current_url == Constants.ORDERS_HISTORY_URL