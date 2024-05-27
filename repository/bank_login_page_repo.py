from selenium.webdriver.common.by import By

class BankLoginPageRepo:
    UNAME_INPUT = (By.XPATH, ".//input[@type='text' and @name='uid']")
    PWORD_INPUT = (By.XPATH, ".//input[@type='password' and @name='password']")
    LOGIN_BTN = (By.XPATH, ".//input[@type='submit' and @name='btnLogin]")
    RESET_BTN = (By.XPATH, ".//input[@type='reset' and @name='btnReset]")