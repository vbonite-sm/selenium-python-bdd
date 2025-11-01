"""
Base Page Object - Parent class for all page objects
Contains common methods used across all pages
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import Config
import allure
import os
from datetime import datetime


class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
    
    @allure.step("Navigate to URL: {url}")
    def navigate_to(self, url):
        """Navigate to a specific URL"""
        self.driver.get(url)
    
    @allure.step("Get current page title")
    def get_title(self):
        """Returns the current page title"""
        return self.driver.title
    
    @allure.step("Get current URL")
    def get_current_url(self):
        """Returns current URL"""
        return self.driver.current_url
    
    @allure.step("Wait for element to be visible: {locator}")
    def wait_for_element_visible(self, locator, timeout=None):
        """
        Wait for element to be visible
        
        Args:
            locator (tuple): Locator tuple (By.ID, "value")
            timeout (int): Custom timeout
        
        Returns:
            WebElement: The visible element
        """
        if timeout:
            wait = WebDriverWait(self.driver, timeout)
        else:
            wait = self.wait
        
        try:
            element = wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="element_not_visible",
                attachment_type=allure.attachment_type.PNG
            )
            raise TimeoutException(f"Element {locator} not visible after {timeout or Config.EXPLICIT_WAIT} seconds")
    
    @allure.step("Wait for element to be clickable: {locator}")
    def wait_for_element_clickable(self, locator, timeout=None):
        """Wait for element to be clickable"""
        if timeout:
            wait = WebDriverWait(self.driver, timeout)
        else:
            wait = self.wait
        
        try:
            element = wait.until(EC.element_to_be_clickable(locator))
            return element
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="element_not_clickable",
                attachment_type=allure.attachment_type.PNG
            )
            raise TimeoutException(f"Element {locator} not clickable")
    
    @allure.step("Click element: {locator}")
    def click(self, locator):
        """Click on an element"""
        element = self.wait_for_element_clickable(locator)
        element.click()
    
    @allure.step("Enter text '{text}' into element: {locator}")
    def send_keys(self, locator, text):
        """Send keys to an element"""
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Get text from element: {locator}")
    def get_text(self, locator):
        """Get text from an element"""
        element = self.wait_for_element_visible(locator)
        return element.text
    
    @allure.step("Check if element is displayed: {locator}")
    def is_element_displayed(self, locator):
        """Check if element is displayed"""
        try:
            element = self.wait_for_element_visible(locator, timeout=5)
            return element.is_displayed()
        except:
            return False
    
    @allure.step("Take screenshot: {name}")
    def take_screenshot(self, name="screenshot"):
        """Take screenshot and attach to allure report"""
        if Config.SCREENSHOT_ON_FAILURE:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{name}_{timestamp}.png"
            screenshot_path = os.path.join(Config.SCREENSHOT_PATH, screenshot_name)
            
            # Create directory if it doesn't exist
            os.makedirs(Config.SCREENSHOT_PATH, exist_ok=True)
            
            # Save screenshot
            self.driver.save_screenshot(screenshot_path)
            
            # Attach to allure
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=screenshot_name,
                attachment_type=allure.attachment_type.PNG
            )
            
            return screenshot_path