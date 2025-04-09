from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Перейти по URL: {url}")
    def go_to_url(self, url):
        return self.driver.get(url)

    @allure.step("Переключиться на окно #{window_number}")
    def switch_to(self, window_number, current_url, time=5):
        self.driver.switch_to.window(self.driver.window_handles[window_number])
        WebDriverWait(self.driver, time).until(EC.url_changes(current_url))

    @allure.step("Ожидание загрузки страницы: {url}")
    def wait_for_page(self, url, time=5):
        WebDriverWait(self.driver, time).until(lambda driver: driver.current_url == url)

    @allure.step("Поиск элемента с ожиданием: {locator}")
    def find_element_with_wait(self, locator, time=5):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Поиск элементов с ожиданием: {locator}")
    def find_elements_with_wait(self, locator, time=5):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Клик по элементу: {locator}")
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step("Получить текст из элемента: {locator}")
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step("Ввести текст '{text}' в элемент: {locator}")
    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step("Прокрутить страницу вниз")
    def scroll_page_to_the_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Перетащить элемент {item_to_drag_locator} на {drop_target_locator}")
    def drag_and_drop_item(self, item_to_drag_locator, drop_target_locator):
        item_to_drag = self.driver.find_element(*item_to_drag_locator)
        drop_target = self.driver.find_element(*drop_target_locator)
        action = ActionChains(self.driver)
        action.drag_and_drop(item_to_drag, drop_target).perform()

    @allure.step("Ожидание исчезновения элемента: {locator}")
    def wait_for_element_invisible(self, locator, time=5):
        WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Ожидание появления элемента: {locator}")
    def wait_for_element_visible(self, locator, time=5):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Заполнение формы логина")
    def fill_login_form(self, locator_email, email, locator_password, password, btn_locator):
        with allure.step(f"Ввести email: {email}"):
            self.set_text_to_element(locator_email, email)
        with allure.step(f"Ввести пароль: {'*' * len(password)}"):
            self.set_text_to_element(locator_password, password)
        with allure.step("Кликнуть по кнопке входа"):
            self.click_on_element(btn_locator)