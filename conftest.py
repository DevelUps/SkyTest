import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(params=["chromium", "firefox", "webkit"])
def browser_type(request):
    return request.param

@pytest.fixture
def browser(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch()
        yield browser
        browser.close()
