class BaseAssertion:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def check_title(self):
        return self.driver.title