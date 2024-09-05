from selenium import webdriver
from pages.login import Login
from pages.main_page import MainPage
from data.data import Data
import pytest


class Test:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.login_page = Login(self.driver)
        self.main_page = MainPage(self.driver)
        self.login_page.go_to_url(Data.URL)
        self.driver.maximize_window()

    def test_successful_login(self, setup):
        assert self.login_page.login_page_loaded() == True
        self.login_page.enter_username(Data.STANDARD_USER)
        self.login_page.enter_password(Data.PASSWORD)
        self.login_page.click_login()
        assert self.main_page.demo_main_page_loaded() == True

    def test_failed_login(self, setup):
        assert self.login_page.login_page_loaded() == True
        self.login_page.enter_username(Data.LOCKOUT_USER)
        self.login_page.enter_password(Data.PASSWORD)
        self.login_page.click_login()
        assert self.login_page.error_message_displayed() == True
        assert self.login_page.verify_error_message() == True

    def test_extract_data(self, setup):
        assert self.login_page.login_page_loaded() == True
        self.login_page.enter_username(Data.STANDARD_USER)
        self.login_page.enter_password(Data.PASSWORD)
        self.login_page.click_login()
        self.main_page.save_item_names_in_file()
        self.main_page.logout()
        self.login_page.login_page_loaded()

    def teardown(self):
        self.driver.quit()
