# coding=utf-8
import pytest
from tests.base_test import BaseTest
from pages.home_page import HomePage
from assertions.home_assertion import HomeAssertion

class TestEmail(BaseTest):

    @pytest.fixture
    def load_page(self):
        self.page = HomePage(self.driver, self.wait)
        self.assertion = HomeAssertion(self.driver, self.wait)
        self.page.go_to_home_page()

    def test_title(self, load_page):
        self.assertion.check_title("Guru99 Bank Home Page")