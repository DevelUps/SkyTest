import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api():
    """ Configura la base URL para las pruebas de API """
    return APIClient("https://reqres.in/api")  # 🔥 Puedes cambiar esta API de prueba por la real

def test_get_users(api):
    """ Prueba GET: Obtener lista de usuarios """
    response = api.get("/users?page=2")
    assert response.status_code == 200
    assert "data" in response.json()
    assert len(response.json()["data"]) > 0

def test_create_user(api):
    """ Prueba POST: Crear un usuario """
    payload = {"name": "John Doe", "job": "Tester"}
    response = api.post("/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["job"] == "Tester"

def test_update_user(api):
    """ Prueba PUT: Actualizar usuario """
    payload = {"name": "Jane Doe", "job": "QA Lead"}
    response = api.put("/users/2", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"

def test_delete_user(api):
    """ Prueba DELETE: Eliminar usuario """
    response = api.delete("/users/2")
    assert response.status_code == 204  # 🔥 DELETE no devuelve contenido
