# coding=utf-8
import pytest
from tests.base_test import BaseTest
from pages.home_page import HomePage
from assertions.home_assertion import HomeAssertion

class TestEmail(BaseTest):

    @pytest.fixture
    def load_page(self):
        self.page = HomePage(self.driver)
        self.assertion = HomeAssertion(self.driver, self.wait)
        self.page.go_to_home_page()

    def test_home_page_title(self, load_page):
        self.assertion.check_title("Guru99 Bank Home Page")

    def test_empty_email_submission(self, load_page):
        self.page.submit_empty_email()
        self.assertion.check_blank_message("Email ID must not be blank")