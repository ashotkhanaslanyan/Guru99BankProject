from pages.base_page import BasePage
from repository.home_page_repo import HomePageRepo

from data.url_parser import urls

class HomePage(BasePage):

    def __init__(self, driver):
        self.url = urls()['HomePage']
        self.repo = HomePageRepo
        super().__init__(driver)

    def go_to_home_page(self):
        self.go_to_page(self.url)

    def submit_empty_email(self):
        self.driver.find_element(*self.repo.EMAIL_INPUT).clear()
        self.driver.find_element(*self.repo.SUBMIT_BTN).click()