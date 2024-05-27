from selenium.webdriver.common.by import By

class HomePageRepo:
    EMAIL_INPUT = (By.XPATH, ".//input[@type='text' and @name='emailid']")
    SUBMIT_BTN = (By.XPATH, ".//input[@type='submit' and @name='btnLogin']")
    ACCESS_HEADER = (By.XPATH, ".//tbody//td/h2")
    BLANK_MSG = (By.ID, "message9")
    UNAME = (By.XPATH, ".//tbody//td[text()='User ID :']/following-sibling::td")
    PWORD = (By.XPATH, ".//tbody//td[text()='Password :']/following-sibling::td")