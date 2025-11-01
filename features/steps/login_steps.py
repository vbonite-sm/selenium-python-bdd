"""
Step definitions for login feature
Behave syntax - much simpler than pytest-bdd!
"""
from behave import given, when, then
import allure


@given('I am on the login page')
def open_login_page(context):
    """Open the login page"""
    with allure.step("Given I am on the login page"):
        context.login_page.open()


@when('I enter username "{username}"')
def enter_username(context, username):
    """Enter username"""
    with allure.step(f'When I enter username "{username}"'):
        context.login_page.enter_username(username)


@when('I enter password "{password}"')
def enter_password(context, password):
    """Enter password"""
    masked_password = "*" * len(password)
    with allure.step(f'When I enter password "{masked_password}"'):
        context.login_page.enter_password(password)


@when('I click the login button')
def click_login_button(context):
    """Click login button"""
    with allure.step("When I click the login button"):
        context.login_page.click_login_button()


@then('I should see a success message')
def verify_success_message(context):
    """Verify success message is displayed"""
    with allure.step("Then I should see a success message"):
        flash_message = context.login_page.get_flash_message()
        assert "You logged into a secure area!" in flash_message, \
            f"Expected success message, but got: {flash_message}"


@then('I should be redirected to the secure area')
def verify_secure_area(context):
    """Verify user is on secure area"""
    with allure.step("Then I should be redirected to the secure area"):
        current_url = context.login_page.get_current_url()
        assert "/secure" in current_url, \
            f"Expected to be on /secure page, but current URL is: {current_url}"


@then('logout button should be visible')
def verify_logout_button_visible(context):
    """Verify logout button is visible"""
    with allure.step("Then logout button should be visible"):
        assert context.login_page.is_logout_button_displayed(), \
            "Logout button should be visible after successful login"


@then('logout button should not be visible')
def verify_logout_button_not_visible(context):
    """Verify logout button is not visible"""
    with allure.step("Then logout button should not be visible"):
        assert not context.login_page.is_logout_button_displayed(), \
            "Logout button should not be visible after failed login"


@then('I should see an error message containing "{error_text}"')
def verify_error_message(context, error_text):
    """Verify error message contains expected text"""
    with allure.step(f'Then I should see an error message containing "{error_text}"'):
        flash_message = context.login_page.get_flash_message()
        assert error_text in flash_message, \
            f"Expected error message to contain '{error_text}', but got: {flash_message}"
