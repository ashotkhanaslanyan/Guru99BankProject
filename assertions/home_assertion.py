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
        title=self.home_page["title"]
        actual_title = self.driver.title
        try:
            assert title in actual_title, f"'{title}' not found in page title '{actual_title}'"
            self.logger.info(f"Title check passed: '{title}' is in page title.")
        except AssertionError as e:
            self.logger.error(f"Title check failed: '{title}' not found in page title '{actual_title}'.")
            raise e

    def check_blank_message(self):
        message = self.home_page["email_message"]
        actual_message = self.wait.until(
            EC.presence_of_element_located(self.repo.BLANK_MSG)
            ).text
        try:
            assert message in actual_message, f"'{message}' not found in email message '{actual_message}'"
            self.logger.info(f"Message check passed: '{message}' found.")
        except AssertionError as e:
            self.logger.error(f"Message check failed: '{message}' not found in email message. '{actual_message}'")
            raise e 