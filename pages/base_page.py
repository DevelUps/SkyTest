# DOCUMENTACION: Esta clase contiene los métodos y atributos necesarios para interactuar con la página de login
from playwright.sync_api import Page

class BasePage:# Clase base para las páginas
    def __init__(self, page: Page):# Constructor de la clase
        self.page = page# Guarda la página en un atributo

    def navigate(self, url):# Método para navegar a una URL
        #""" Navega a una URL """
        self.page.goto(url)# Navega a la URL

    def is_element_visible(self, selector, timeout=5000):# Método para verificar si un elemento es visible
        """ Verifica si un elemento está visible en la página. """
        try:# Intenta encontrar el elemento
            self.page.wait_for_selector(selector, timeout=timeout)# Espera a que el elemento sea visible
            return True # Devuelve True si el elemento es visible
        except: # Si no se encuentra el elemento
            return False # Devuelve False si el elemento no es visible
