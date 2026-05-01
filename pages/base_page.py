# Import the Page type from Playwright to enable type checking and
# auto-completion
from playwright.sync_api import Page


# A base class containing common methods and properties shared across multiple
# page objects
class BasePage:
    # The __init__ method is a constructor that is called when an object of
    # this class is created
    def __init__(self, page: Page):
        # We store the Playwright page object as a class property so that
        # other methods can use it
        self.page = page

    # This function is a common wrapper to navigate to any given URL
    def navigate(self, url: str):
        # This calls Playwright's built-in goto() method to actually load the
        # web page
        self.page.goto(url)
