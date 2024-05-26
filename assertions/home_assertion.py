from selenium.webdriver.support import expected_conditions as EC
from assertions.base_assertion import BaseAssertion

class HomeAssertion(BaseAssertion):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def check_title(self, title):
        self.wait.until(EC.title_contains(title))