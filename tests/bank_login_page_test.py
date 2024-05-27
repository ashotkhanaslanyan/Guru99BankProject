import pytest
from tests.base_test import BaseTest
from pages.bank_login_page import BankLoginPage
from assertions.bank_login_assertions import BankLoginAssertion

class TestBankLoginPage(BaseTest):

    @pytest.fixture
    def load_page(self):
        self.page = BankLoginPage(self.driver)
        self.assertion = BankLoginAssertion(self.driver, self.wait, self.logger)
        self.page.go_to_bank_login_page()

    def test_bank_login_page_title(self, load_page):
        self.assertion.check_title()

    def test_bank_login_with_empty_credentials(self, load_page):
        self.page.login_with_empty_credentials()
        self.assertion.check_empty_cred_login_alert()