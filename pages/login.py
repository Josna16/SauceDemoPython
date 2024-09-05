from pages.base import Base
from selenium.webdriver.common.by import By


class Login(Base):
    login_logo = (By.CLASS_NAME, "login_logo")
    username_editfield = (By.ID, "user-name")
    password_editfield = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.XPATH, "//*[contains(text(), 'Epic sadface')]")
    error_text = "Sorry, this user has been banned."

    def __init__(self, driver):
        super().__init__(driver)

    def login_page_loaded(self):
        return self.driver.find_element(*self.login_logo).is_displayed()

    def enter_username(self, username):
        self.driver.find_element(*self.username_editfield).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_editfield).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def error_message_displayed(self):
        return self.driver.find_element(*self.error_message).is_displayed()

    def verify_error_message(self):
        text = self.driver.find_element(*self.error_message).text
        print(text)
        if text.find(self.error_text) !=-1:
            return True
        else:
            return False

