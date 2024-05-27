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
        
    def check_empty_cred_login_alert(self):
        expected_alert_message = self.bank_login_page["alert_message"]
        actual_alert_message = self.wait.until(
            EC.alert_is_present()).text
        try:
            assert expected_alert_message in actual_alert_message, f"'{expected_alert_message}' not found in the alert message '{actual_alert_message}'"
            self.logger.info(f"Alert check passed: '{expected_alert_message}' is in page title.")
        except AssertionError as e:
            self.logger.error(f"Alert check failed: '{expected_alert_message}' not found in alert message '{actual_alert_message}'.")
            raise e
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()

    def check_empty_uname_field_message(self):
        expected_message = self.bank_login_page["empty_uname_message"]
        actual_message = self.wait.until(
            EC.presence_of_element_located(self.repo.UNAME_MSG)
            ).text
        try:
            assert expected_message in actual_message, f"'{expected_message}' not found in blank username message '{actual_message}'"
            self.logger.info(f"Message check passed: '{expected_message}' found.")
        except AssertionError as e:
            self.logger.error(f"Message check failed: '{expected_message}' not found in blank username message '{actual_message}'.")
            raise e

    def check_empty_pword_field_message(self):
        expected_message = self.bank_login_page["empty_pword_message"]
        actual_message = self.wait.until(
            EC.presence_of_element_located(self.repo.PWORD_MSG)
            ).text
        try:
            assert expected_message in actual_message, f"'{expected_message}' not found in blank password message '{actual_message}'"
            self.logger.info(f"Message check passed: '{expected_message}' found.")
        except AssertionError as e:
            self.logger.error(f"Message check failed: '{expected_message}' not found in blank password message '{actual_message}'.")
            raise e