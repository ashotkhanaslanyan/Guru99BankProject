import pytest
from tests.base_test import BaseTest
from pages.bank_login_page import BankLoginPage
from assertions.bank_login_assertion import BankLoginAssertion
from assertions.bank_mngr_home_assertion import BankMngrHomeAssertion

class TestBankLoginPage(BaseTest):

    @pytest.fixture
    def load_page(self):
        self.page = BankLoginPage(self.driver)
        self.assertion = BankLoginAssertion(self.driver, self.wait, self.logger)
        self.bank_mngr_home_assertion = BankMngrHomeAssertion(self.driver, self.wait, self.logger)
        self.page.go_to_bank_login_page()

    def test_bank_login_page_title(self, load_page):
        self.assertion.check_title()

    def test_bank_login_with_empty_credentials(self, load_page):
        self.page.login_with_empty_credentials()
        self.assertion.check_invalid_cred_login_alert()

    def test_bank_login_empty_credential_messages(self, load_page):
        self.page.trigger_empty_uname_message()
        self.assertion.check_empty_uname_field_message()
        self.page.trigger_empty_pword_message()
        self.assertion.check_empty_pword_field_message()

    def test_bank_login_with_invalid_credentials(self, load_page):
        self.page.login_with_invalid_credentials()
        self.assertion.check_invalid_cred_login_alert()

    def test_bank_login_reset_credentials(self, load_page):
        self.page.reset_login_credentials()
        self.assertion.check_uname_field_empty()
        self.assertion.check_pword_field_empty()

    @pytest.mark.needs_credentials
    def test_valid_credentials_login(self, load_page):
        self.page.login_with_valid_credentials()
        self.bank_mngr_home_assertion.check_title()