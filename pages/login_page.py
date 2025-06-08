import allure
from pages.base_page import BasePage
from urls import Urls
from locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.login_page_url
        self.locators = LoginPageLocators()

    @allure.step("Клик по кнопке 'Восстановить пароль'")
    def click_on_forgot_password(self):
        wait = WebDriverWait(self.driver, 10)
        self.click_on_element(self.locators.FORGOT_PASSWORD_BUTTON)

    @allure.step("Проверка видимости кнопки входа")
    def is_login_button_visible(self):
        return self.is_element_visible(self.locators.SUBMIT_BUTTON_LOGIN_TO_ACCOUNT)