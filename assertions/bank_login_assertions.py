from selenium.webdriver.support import expected_conditions as EC

from data.page_data import parser
from assertions.base_assertion import BaseAssertion
from repository.bank_login_page_repo import BankLoginPageRepo

class BankLoginAssertion(BaseAssertion):

    def __init__(self, driver, wait, logger):
        self.bank_login_page = parser.parser("bank_login_page.yml")
        self.repo = BankLoginPageRepo
        super().__init__(driver, wait, logger)

    def check_title(self):
        expected_title = self.bank_login_page["title"]
        actual_title = self.driver.title
        try:
            assert expected_title in actual_title, f"'{expected_title}' not found in the page title '{actual_title}'"
            self.logger.info(f"Title check passed: '{expected_title}' is in page title.")
        except AssertionError as e:
            self.logger.error(f"Title check failed: '{expected_title}' not found in page title '{actual_title}'.")
            raise e