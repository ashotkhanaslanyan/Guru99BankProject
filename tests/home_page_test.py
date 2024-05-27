# coding=utf-8
import pytest
from tests.base_test import BaseTest
from pages.home_page import HomePage
from assertions.home_assertion import HomeAssertion

class TestHomePage(BaseTest):

    @pytest.fixture
    def load_page(self):
        self.page = HomePage(self.driver)
        self.assertion = HomeAssertion(self.driver, self.wait, self.logger)
        self.page.go_to_home_page()

    def test_home_page_title(self, load_page):
        self.assertion.check_title()

    def test_empty_email_submission(self, load_page):
        self.page.submit_empty_email()
        self.assertion.check_blank_message()

    def test_invalid_email_field(self, load_page):
        self.page.enter_invalid_email()
        self.assertion.check_invalid_email_message()

    def test_valid_email_submission(self, load_page):
        self.page.submit_valid_email()
        self.assertion.check_access_details_header()