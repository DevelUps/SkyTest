from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def is_element_visible(self, selector, timeout=5000):
        """ Verifica si un elemento está visible en la página. """
        try:
            self.page.wait_for_selector(selector, timeout=timeout)
            return True
        except:
            return False
