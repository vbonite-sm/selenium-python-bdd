"""
Behave environment setup
Replaces pytest's conftest.py - much cleaner!
"""
import allure
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage


def before_all(context):
    """
    Runs once before all tests
    Setup global configuration here
    """
    context.config.setup_logging()


def before_scenario(context, scenario):
    """
    Runs before each scenario
    Initialize driver and page objects
    """
    # Initialize WebDriver
    context.driver = DriverFactory.get_driver()
    
    # Initialize page objects
    context.login_page = LoginPage(context.driver)
    
    # Add scenario name to Allure report
    allure.dynamic.title(scenario.name)
    allure.dynamic.description(scenario.description)


def after_scenario(context, scenario):
    """
    Runs after each scenario
    Cleanup and screenshot on failure
    """
    # Take screenshot on failure
    if scenario.status == "failed":
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name=f"failure_{scenario.name}",
            attachment_type=allure.attachment_type.PNG
        )
    
    # Quit driver
    if hasattr(context, 'driver'):
        context.driver.quit()


def after_step(context, step):
    """
    Runs after each step
    Take screenshot on step failure
    """
    if step.status == "failed":
        if hasattr(context, 'driver'):
            allure.attach(
                context.driver.get_screenshot_as_png(),
                name=f"step_failure_{step.name}",
                attachment_type=allure.attachment_type.PNG
            )


def after_all(context):
    """
    Runs once after all tests
    Final cleanup here
    """
    pass
