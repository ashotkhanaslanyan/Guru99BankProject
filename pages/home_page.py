from pages.base_page import BasePage
from repository.home_page_repo import HomePageRepo

from data.url_parser import urls

class HomePage(BasePage):

    def __init__(self, driver, wait):
        self.url = urls()['HomePage']
        self.repo = HomePageRepo
        super().__init__(driver, wait)

    def go_to_home_page(self):
        self.go_to_page(self.url)