import requests
def test_open_google(browser): # Aqui se inyecta el fixture
    page = browser.new_page() # Aqui se crea una nueva pagina
    page.goto("https://opensource-demo.orangehrmlive.com/web/index:.php/auth/login")  # Aqui se navega a la pagina
    assert "OrangeHRM" in page.title() # Aqui se valida que el titulo contenga la palabra Google
    page.close() # Aqui se cierra la pagina
  
def test_api_status():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200