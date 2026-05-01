# Import Playwright's Page object for type hinting
from playwright.sync_api import Page
# Import the LoginPage object we created to interact with the login page
from pages.login_page import LoginPage
import logging

# Set up a logger for this file
logger = logging.getLogger(__name__)


# Test case 1: Verify a user can log in with valid credentials
# Playwright's pytest plugin automatically provides the 'page' fixture
def test_valid_login(page: Page):
    logger.info("Starting test: test_valid_login")
    # Create an instance of our LoginPage, passing the current browser page
    login_page = LoginPage(page)

    # Step 1: Navigate to the application url
    login_page.navigate_to_login()

    # Step 2: Perform a login with valid standard user credentials
    login_page.login("standard_user", "secret_sauce")

    # Step 3: Verify successful login by checking if the URL changed
    # The 'assert' keyword fails the test if the condition is False
    logger.info(f"Verifying URL is inventory.html. Current: {page.url}")
    assert page.url == "https://www.saucedemo.com/inventory.html"
    logger.info("test_valid_login passed successfully.")


# Test case 2: Verify an error is shown when a locked out user tries to log in
def test_invalid_login(page: Page):
    logger.info("Starting test: test_invalid_login")
    # Create an instance of our LoginPage
    login_page = LoginPage(page)

    # Step 1: Navigate to the application url
    login_page.navigate_to_login()

    # Step 2: Perform a login using the locked out user's credentials
    login_page.login("locked_out_user", "secret_sauce")

    # Step 3: Fetch the error message text displayed on the screen
    error_msg = login_page.get_error_message()

    # Step 4: Verify that the correct error message text is included
    logger.info("Verifying expected error message is present.")
    assert "Sorry, this user has been locked out." in error_msg
    logger.info("test_invalid_login passed successfully.")


# Test case 3: Verify all expected UI elements are displayed on the landing page
def test_landing_page_ui_elements(page: Page):
    logger.info("Starting test: test_landing_page_ui_elements")
    # Create an instance of our LoginPage
    login_page = LoginPage(page)

    # Step 1: Navigate to the application url
    login_page.navigate_to_login()

    # Step 2: Verify all landing page UI elements are visible
    login_page.verify_landing_page_ui()
    logger.info("test_landing_page_ui_elements passed successfully.")
