from locators import Locators
from pages.change_password_page import ChangePasswordPage
from constants import Constants
import allure


class TestChangePasswordPage:

    @allure.title("переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_change_password_page(self, driver):
        change_password_page = ChangePasswordPage(driver)
        change_password_page.go_to_password_change_page()
        result = change_password_page.find_element_with_wait(Locators.CHANGE_PASSWORD_TITLE)
        assert result

    @allure.title("ввод почты и клик по кнопке «Восстановить»")
    def test_input_imail_on_change_password_page(self, driver):
        change_password_page = ChangePasswordPage(driver)
        change_password_page.go_to_password_change_page()
        change_password_page.find_element_with_wait(Locators.CHANGE_PASSWORD_TITLE)
        change_password_page.fill_email_form()
        result = change_password_page.find_element_with_wait(Locators.SAVE_NEW_PASSWORD_BTN)
        assert result

    @allure.title("клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_show_password(self, driver):
        change_password_page = ChangePasswordPage(driver)
        change_password_page.go_to_password_change_page()
        change_password_page.find_element_with_wait(Locators.CHANGE_PASSWORD_TITLE)
        change_password_page.fill_email_form()
        change_password_page.find_element_with_wait(Locators.SAVE_NEW_PASSWORD_BTN)
        assert change_password_page.is_password_invisible()
        change_password_page.fill_password_form()
        change_password_page.show_password()
        assert change_password_page.is_password_visible()