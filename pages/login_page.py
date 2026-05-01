# Import the Page type and expect from Playwright
from playwright.sync_api import Page, expect
# Import our BasePage class so we can inherit its common methods
from pages.base_page import BasePage
import logging

# Set up a logger for this file
logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    # Constructor method for the LoginPage, passing in the Playwright Page instance
    def __init__(self, page: Page):
        # Call the constructor of the parent class (BasePage) to set self.page
        super().__init__(page)

        # Locators: These properties store the instructions for how to find
        # elements on the page. We use data-test attributes here because they
        # are very stable and don't change often.
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")
        
        # Additional Landing Page UI Locators
        self.login_logo = page.locator(".login_logo1")
        self.login_credentials_hint = page.locator("#login_credentials1")
        self.login_password_hint = page.locator(".login_password")

    # Function dedicated to navigating specifically to the saucedemo login page
    def navigate_to_login(self):
        logger.info("Navigating to Saucedemo login page.")
        # Calls the navigate method inherited from BasePage
        self.navigate("https://www.saucedemo.com/")

    # Function to type a given username into the username input field
    def enter_username(self, username: str):
        logger.info(f"Entering username: '{username}'")
        # The fill() method clears any existing text and types the new value
        self.username_input.fill(username)

    # Function to type a given password into the password input field
    def enter_password(self, password: str):
        logger.info("Entering password.")
        self.password_input.fill(password)

    # Function to click the login button
    def click_login(self):
        logger.info("Clicking the login button.")
        # click() simulates a real mouse click on the element
        self.login_button.click()

    # A high-level helper function that combines the steps to perform a full login
    def login(self, username, password):
        logger.info(f"Attempting login with username: {username}")
        # Step 1: Enter the username
        self.enter_username(username)
        # Step 2: Enter the password
        self.enter_password(password)
        # Step 3: Click the login button to submit
        self.click_login()

    # Function to retrieve the text from the error message element
    def get_error_message(self):
        logger.info("Retrieving the login error message text.")
        # text_content() extracts the visible text inside the locator
        error_text = self.error_message.text_content()
        logger.info(f"Found error message: '{error_text}'")
        return error_text

    # Function to verify that all key UI elements are displayed on the landing
    # page
    def verify_landing_page_ui(self):
        logger.info("Verifying all landing page UI elements are visible.")
        errors = []

        # Wait for the page structure to load by waiting for a reliable element
        self.username_input.wait_for(state="visible", timeout=5000)

        # Using if/else with is_visible() allows us to print custom messages
        # Checking Login Logo
        if self.login_logo.is_visible():
            logger.info("SUCCESS: Login Logo is visible on the page.")
        else:
            logger.error("FAILURE: Login Logo is MISSING!")
            errors.append("Login Logo")

        # Checking Username Input
        if self.username_input.is_visible():
            logger.info("SUCCESS: Username Input is visible on the page.")
        else:
            logger.error("FAILURE: Username Input is MISSING!")
            errors.append("Username Input")

        # Checking Password Input
        if self.password_input.is_visible():
            logger.info("SUCCESS: Password Input is visible on the page.")
        else:
            logger.error("FAILURE: Password Input is MISSING!")
            errors.append("Password Input")

        # Checking Login Button
        if self.login_button.is_visible():
            logger.info("SUCCESS: Login Button is visible on the page.")
        else:
            logger.error("FAILURE: Login Button is MISSING!")
            errors.append("Login Button")

        # Checking Login Credentials Hint
        if self.login_credentials_hint.is_visible():
            logger.info("SUCCESS: Login Credentials Hint is visible on the page.")
        else:
            logger.error("FAILURE: Login Credentials Hint is MISSING!")
            errors.append("Login Credentials Hint")

        # Checking Login Password Hint
        if self.login_password_hint.is_visible():
            logger.info("SUCCESS: Login Password Hint is visible on the page.")
        else:
            logger.error("FAILURE: Login Password Hint is MISSING!")
            errors.append("Login Password Hint")

        if errors:
            # If any errors were caught, we raise them all together at the end
            error_message = "UI Verification failed! The following elements were missing:\n- " + "\n- ".join(errors)
            raise AssertionError(error_message)

        logger.info("All landing page UI elements verified successfully!")
