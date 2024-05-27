from selenium.webdriver.support import expected_conditions as EC

from data.page_data import parser
from assertions.base_assertion import BaseAssertion
from repository.home_page_repo import HomePageRepo

class HomeAssertion(BaseAssertion):

    def __init__(self, driver, wait, logger):
        self.home_page = parser.parser("home_page.yml")
        self.repo = HomePageRepo
        super().__init__(driver, wait, logger)

    def check_title(self):
        expected_title=self.home_page["title"]
        actual_title = self.driver.title
        try:
            assert expected_title in actual_title, f"'{expected_title}' not found in page title '{actual_title}'"
            self.logger.info(f"Title check passed: '{expected_title}' is in page title.")
        except AssertionError as e:
            self.logger.error(f"Title check failed: '{expected_title}' not found in page title '{actual_title}'.")
            raise e

    def check_blank_message(self):
        expected_message = self.home_page["empty_email_message"]
        actual_message = self.wait.until(
            EC.presence_of_element_located(self.repo.BLANK_MSG)
            ).text
        try:
            assert expected_message in actual_message, f"'{expected_message}' not found in blank email message '{actual_message}'"
            self.logger.info(f"Message check passed: '{expected_message}' found.")
        except AssertionError as e:
            self.logger.error(f"Message check failed: '{expected_message}' not found in blank email message. '{actual_message}'")
            raise e
    
    def check_invalid_email_message(self):
        expected_message = self.home_page["invalid_email_message"]
        actual_message = self.wait.until(
            EC.presence_of_element_located(self.repo.BLANK_MSG)
        ).text
        try:
            assert expected_message in actual_message, f"'{expected_message}' not found in invalid email message '{actual_message}'"
            self.logger.info(f"Message check passed: '{expected_message}' found.")
        except AssertionError as e:
            self.logger.error(f"Message check failed: '{expected_message}' not found in invalid email message. '{actual_message}'")
            raise e