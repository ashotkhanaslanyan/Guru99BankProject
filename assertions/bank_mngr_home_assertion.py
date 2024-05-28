from selenium.webdriver.support import expected_conditions as EC

from data.page_data import parser
from assertions.base_assertion import BaseAssertion

class BankMngrHomeAssertion(BaseAssertion):

    def __init__(self, driver, wait, logger):
        self.bank_mngr_home_page = parser.parser("bank_mngr_home_page.yml")
        super().__init__(driver, wait, logger)

    def check_title(self):
        expected_title = self.bank_mngr_home_page["title"]
        actual_title = self.driver.title
        try:
            assert expected_title in actual_title, f"'{expected_title}' not found in page title '{actual_title}'"
            self.logger.info(f"Title check passed: '{expected_title}' is in page title.")
        except AssertionError as e:
            self.logger.error(f"Title check failed: '{expected_title}' not found in page title '{actual_title}'.")
            raise e