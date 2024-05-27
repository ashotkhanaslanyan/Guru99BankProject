from pages.base_page import BasePage
from repository.bank_login_page_repo import BankLoginPageRepo

from data.url_parser import urls

class BankLoginPage(BasePage):

    def __init__(self, driver):
        self.url = urls()["BankLoginPage"]
        self.repo = BankLoginPageRepo
        super().__init__(driver)

    def go_to_bank_login_page(self):
        self.go_to_page(self.url)

    def login_with_empty_credentials(self):
        self.driver.find_element(*self.repo.UNAME_INPUT).clear()
        self.driver.find_element(*self.repo.PWORD_INPUT).clear()
        self.driver.find_element(*self.repo.LOGIN_BTN).click()

    def trigger_empty_uname_message(self):
        self.driver.find_element(*self.repo.UNAME_INPUT).clear()
        self.driver.find_element(*self.repo.UNAME_INPUT).click()
        self.driver.find_element(*self.repo.PWORD_INPUT).click()
    
    def trigger_empty_pword_message(self):
        self.driver.find_element(*self.repo.PWORD_INPUT).clear()
        self.driver.find_element(*self.repo.PWORD_INPUT).click()
        self.driver.find_element(*self.repo.UNAME_INPUT).click()