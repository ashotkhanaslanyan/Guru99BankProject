class BaseAssertion:

    def __init__(self, driver, wait, logger):
        self.driver = driver
        self.wait = wait
        self.logger = logger

    def check_title(self):
        return self.driver.title