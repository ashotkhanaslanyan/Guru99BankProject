from data.page_data import parser
from pages.base_page import BasePage
from repository.home_page_repo import HomePageRepo

from data.url_parser import urls

class HomePage(BasePage):

    def __init__(self, driver):
        self.url = urls()['HomePage']
        self.home_page = parser.parser("home_page.yml")
        self.repo = HomePageRepo
        super().__init__(driver)

    def go_to_home_page(self):
        self.go_to_page(self.url)

    def submit_empty_email(self):
        self.driver.find_element(*self.repo.EMAIL_INPUT).clear()
        self.driver.find_element(*self.repo.SUBMIT_BTN).click()

    def enter_invalid_email(self):
        self.driver.find_element(*self.repo.EMAIL_INPUT).clear()
        self.driver.find_element(*self.repo.EMAIL_INPUT).send_keys(self.home_page["invalid_email_example"])

