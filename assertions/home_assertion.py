from selenium.webdriver.support import expected_conditions as EC
from data.page_data import parser
from assertions.base_assertion import BaseAssertion
from repository.home_page_repo import HomePageRepo

class HomeAssertion(BaseAssertion):

    def __init__(self, driver, wait):
        self.home_page = parser.parser("home_page.yml")
        self.repo = HomePageRepo
        super().__init__(driver, wait)

    def check_title(self):
        title=self.home_page["title"]
        assert title in self.driver.title, f"'{title}' not found in page title '{self.driver.title}'"

    def check_blank_message(self):
        message = self.home_page["email_message"]
        assert message in self.wait.until(
            EC.presence_of_element_located(self.repo.BLANK_MSG)
            ).text, f"'{message}' not found in email message" 