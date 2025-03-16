import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    """ Agrega la opción --browser en pytest """
    parser.addoption("--browser", action="store", default="chromium", help="Selecciona el navegador: chromium, firefox o webkit")

@pytest.fixture(scope="session")
def browser_type(pytestconfig):
    """ Configura el navegador basado en la opción pasada en pytest """
    browser_name = pytestconfig.getoption("browser")
    
    with sync_playwright() as p:
        if browser_name == "firefox":
            browser = p.firefox.launch(headless=True)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=True)
        else:
            browser = p.chromium.launch(headless=True)
        
        yield browser
        browser.close()
