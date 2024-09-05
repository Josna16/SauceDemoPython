from pages.base import Base
from selenium.webdriver.common.by import By


class MainPage(Base):
    app_logo = (By.CLASS_NAME, "app_logo")
    item_name = (By.XPATH, "//div[@class='inventory_item_name ']")
    hamburger_menu = (By.ID, "react-burger-menu-btn")
    logout_button = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        super().__init__(driver)

    def demo_main_page_loaded(self):
        return self.driver.find_element(*self.app_logo).is_displayed()

    def logout(self):
        self.driver.find_element(*self.hamburger_menu).click()
        self.driver.find_element(*self.logout_button).click()

    def save_item_names_in_file(self):
        names = self.driver.find_elements(*self.item_name)
        with open("extracted_data.txt", "w") as file:
            for name in names:
                file.write(name.text)
