import pytest

@pytest.fixture(scope="session")
def browser_context(browser):
    """ Devuelve un contexto del navegador usando el fixture integrado de Playwright """
    context = browser.new_context()
    yield context
    context.close()

