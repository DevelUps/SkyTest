import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def login_page(page: Page):
    """ Devuelve una instancia de LoginPage usando el fixture `page` de Playwright """
    from pages.login_page import LoginPage
    return LoginPage(page)
