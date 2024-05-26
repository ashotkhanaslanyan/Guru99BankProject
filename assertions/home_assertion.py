from selenium.webdriver.support import expected_conditions as EC
from assertions.base_assertion import BaseAssertion
from repository.home_page_repo import HomePageRepo

class HomeAssertion(BaseAssertion):

    def __init__(self, driver, wait):
        self.repo = HomePageRepo
        super().__init__(driver, wait)

    def check_title(self, title):
        assert title in self.driver.title, f"'{title}' not found in page title '{self.driver.title}'"

    def check_blank_message(self, message):
        assert message in self.wait.until(
            EC.presence_of_element_located(self.repo.BLANK_MSG)
            ).text, "The message was not correct" 