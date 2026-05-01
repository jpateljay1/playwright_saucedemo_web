# Playwright Saucedemo Web Automation

A Python Playwright automation framework built with Pytest and the Page Object Model (POM) for testing the Saucedemo login page.

## Features
- Page Object Model design pattern
- Custom UI Element verifications with soft-assertion logging patterns
- `pytest-html` for beautiful HTML reports
- Built-in logging configured in `pytest.ini`

## How to run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install Playwright browsers:
   ```bash
   python3 -m playwright install chromium
   ```
3. Run the tests:
   ```bash
   python3 -m pytest
   ```
