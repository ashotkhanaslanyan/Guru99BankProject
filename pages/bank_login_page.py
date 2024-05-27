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

    