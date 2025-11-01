Feature: Login Functionality
    As a user
    I want to be able to login to the application
    So that I can access secure areas

    Background:
        Given I am on the login page

    @smoke @login
    Scenario: Successful login with valid credentials
        When I enter username "tomsmith"
        And I enter password "SuperSecretPassword!"
        And I click the login button
        Then I should see a success message
        And I should be redirected to the secure area
        And logout button should be visible

    @regression @login
    Scenario: Login fails with invalid username
        When I enter username "invaliduser"
        And I enter password "SuperSecretPassword!"
        And I click the login button
        Then I should see an error message containing "Your username is invalid!"
        And logout button should not be visible

    @regression @login
    Scenario: Login fails with invalid password
        When I enter username "tomsmith"
        And I enter password "wrongpassword"
        And I click the login button
        Then I should see an error message containing "Your password is invalid!"
        And logout button should not be visible

    @regression @login
    Scenario: Login fails with empty credentials
        When I click the login button
        Then I should see an error message containing "Your username is invalid!"
        And logout button should not be visible

    @smoke @login
    Scenario Outline: Login with multiple invalid credentials
        When I enter username "<username>"
        And I enter password "<password>"
        And I click the login button
        Then I should see an error message containing "<error_message>"

        Examples:
            | username  | password             | error_message             |
            | wronguser | SuperSecretPassword! | Your username is invalid! |
            | tomsmith  | wrongpass            | Your password is invalid! |
            | ""        | ""                   | Your username is invalid! |