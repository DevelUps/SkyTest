import requests

class APIClient:
    """ Cliente API para manejar requests en las pruebas """

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint, params=None, headers=None):
        """ Realiza una solicitud GET """
        response = self.session.get(f"{self.base_url}{endpoint}", params=params, headers=headers)
        return response

    def post(self, endpoint, data=None, json=None, headers=None):
        """ Realiza una solicitud POST """
        response = self.session.post(f"{self.base_url}{endpoint}", data=data, json=json, headers=headers)
        return response

    def put(self, endpoint, data=None, json=None, headers=None):
        """ Realiza una solicitud PUT """
        response = self.session.put(f"{self.base_url}{endpoint}", data=data, json=json, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        """ Realiza una solicitud DELETE """
        response = self.session.delete(f"{self.base_url}{endpoint}", headers=headers)
        return response
