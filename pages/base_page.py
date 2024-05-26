from selenium.webdriver.support.ui import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete")