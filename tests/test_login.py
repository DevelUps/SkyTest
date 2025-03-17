from pages.login_page import LoginPage
from utils.config import DEFAULT_USERNAME, DEFAULT_PASSWORD

def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(DEFAULT_USERNAME, DEFAULT_PASSWORD)

    assert login_page. is_logged_in() == True
