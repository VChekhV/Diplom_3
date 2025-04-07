from random import randint
import allure
from pages.base_page import BasePage
from faker import Faker
from locators import Locators
from constants import Constants


class ChangePasswordPage(BasePage):

    @allure.step("заполнение поля для email")
    def fill_email_form(self):
        self.set_text_to_element(Locators.INPUT_EMAIL, Constants.EMAIL)
        self.click_on_element(Locators.CHANGE_PASSWORD_BTN)

    @allure.step("заполнение поля для пароля")
    def fill_password_form(self):
        self.set_text_to_element(Locators.NEW_PASSWORD_INPUT, Constants.PASSWORD)

    @allure.step("пароль виден")
    def is_password_visible(self):
        password_label = self.find_element_with_wait(Locators.NEW_PASSWORD_INPUT)
        return "text" in password_label.get_attribute('type')

    @allure.step("пароль не виден")
    def is_password_invisible(self):
        password_label = self.find_element_with_wait(Locators.NEW_PASSWORD_INPUT)
        return "password" in password_label.get_attribute('type')

    @allure.step("переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def go_to_password_change_page(self):
        self.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        self.wait_for_page(Constants.PERSONAL_ACCOUNT_URL)
        self.click_on_element(Locators.CHANGE_PASSWORD_LINK)
        self.wait_for_page(Constants.CHANGE_PASSWORD_URL)

    @allure.step("клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def show_password(self):
        self.click_on_element(Locators.SHOW_PASSWORD_BTN)