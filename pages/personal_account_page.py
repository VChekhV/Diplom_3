import allure
from pages.base_page import BasePage
from locators import Locators
from constants import Constants


class PersonalAccountPage(BasePage):

    @allure.step("переход по клику на «Личный кабинет»")
    def go_to_personal_page(self):
        self.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        self.wait_for_page(Constants.PERSONAL_ACCOUNT_URL)
        return self.find_element_with_wait(Locators.SIGN_IN_TITLE)

    @allure.step("авторизация пользователя")
    def sign_in(self):
        self.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        self.wait_for_page(Constants.PERSONAL_ACCOUNT_URL)
        self.fill_login_form(Locators.INPUT_EMAIL, Constants.EMAIL, Locators.INPUT_PASSWORD, Constants.PASSWORD, Locators.SIGN_IN_BTN)
        self.find_element_with_wait(Locators.CONSTRUCTOR_TITLE)


    @allure.step("выход из аккаунта")
    def sign_out(self):
        self.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        self.click_on_element(Locators.SIGN_OUT_BTN)
        return self.find_element_with_wait(Locators.SIGN_IN_TITLE)