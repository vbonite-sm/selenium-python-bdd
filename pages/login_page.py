"""
Login Page Object
Page URL: https://the-internet.herokuapp.com/login
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    """Page Object for Login page"""
    
    # URL
    PAGE_URL = "/login"
    
    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
    PAGE_HEADER = (By.TAG_NAME, "h2")
    
    @allure.step("Open login page")
    def open(self):
        """Navigate to login page"""
        from config.config import Config
        self.navigate_to(Config.BASE_URL + self.PAGE_URL)
    
    @allure.step("Enter username: {username}")
    def enter_username(self, username):
        """Enter username in the username field"""
        self.send_keys(self.USERNAME_INPUT, username)
    
    @allure.step("Enter password: ********")
    def enter_password(self, password):
        """Enter password in the password field"""
        self.send_keys(self.PASSWORD_INPUT, password)
    
    @allure.step("Click login button")
    def click_login_button(self):
        """Click the login button"""
        self.click(self.LOGIN_BUTTON)
    
    @allure.step("Login with credentials - Username: {username}")
    def login(self, username, password):
        """
        Complete login flow
        
        Args:
            username (str): Username
            password (str): Password
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    @allure.step("Get flash message")
    def get_flash_message(self):
        """Get the flash message text"""
        return self.get_text(self.FLASH_MESSAGE)
    
    @allure.step("Check if logout button is displayed")
    def is_logout_button_displayed(self):
        """Check if logout button is visible (indicates successful login)"""
        return self.is_element_displayed(self.LOGOUT_BUTTON)
    
    @allure.step("Get page header text")
    def get_page_header(self):
        """Get the page header text"""
        return self.get_text(self.PAGE_HEADER)
    
    @allure.step("Check if login was successful")
    def is_login_successful(self):
        """Verify login success by checking logout button and flash message"""
        return (self.is_logout_button_displayed() and 
                "You logged into a secure area!" in self.get_flash_message())