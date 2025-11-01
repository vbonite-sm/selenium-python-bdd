"""
Driver Factory for browser initialization
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config.config import Config
import allure


class DriverFactory:
    """Factory class to create browser instances"""
    
    @staticmethod
    @allure.step("Initialize {browser_name} browser")
    def get_driver(browser_name=None):
        """
        Returns a WebDriver instance based on browser name
        
        Args:
            browser_name (str): Name of browser (chrome, firefox)
        
        Returns:
            WebDriver: Browser driver instance
        """
        if browser_name is None:
            browser_name = Config.BROWSER
        
        browser_name = browser_name.lower()
        
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            if Config.HEADLESS:
                options.add_argument("--headless")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-extensions")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )
            
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            if Config.HEADLESS:
                options.add_argument("--headless")
            
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )
        else:
            raise ValueError(f"Browser '{browser_name}' is not supported")
        
        # Set timeouts
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        
        return driver