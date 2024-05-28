from pages.base_page import BasePage
from data.url_parser import urls

class BankMngrHomePage(BasePage):

    def __init__(self, driver):
        self.url = urls()["BankMngrHomePage"]
        super().__init__(driver)

    def go_to_bank_mngr_home_page(self):
        self.go_to_page(self.url)