from pages.base_page import BasePage
from utils.config import BASE_URL

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "input[name='username']"
        self.password_input = "input[name='password']"
        self.login_button = "button[type='submit']"
        self.dashboard_header = "h6"

    def navigate(self):
        self.page.goto(BASE_URL)  # Ahora usa la URL desde config.py

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def is_logged_in(self):
        return self.is_element_visible(self.dashboard_header)

