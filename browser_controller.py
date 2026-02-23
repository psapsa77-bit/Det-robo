"""
Controlador do Navegador usando Selenium
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os
import time


class BrowserController:
    """Classe para controlar o navegador web"""

    def __init__(self):
        self.driver = None
        self.is_running = False

    def start(self):
        """Inicia o navegador Chrome"""
        if self.is_running:
            return

        chrome_options = Options()
        # Opções para melhor compatibilidade
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--start-maximized')

        # Tenta usar o Chrome instalado no sistema com webdriver-manager
        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.is_running = True
            self.driver.get('https://www.google.com')
        except Exception as e:
            raise Exception(f"Erro ao iniciar o navegador. Certifique-se de que o Chrome está instalado: {str(e)}")

    def stop(self):
        """Fecha o navegador"""
        if self.driver:
            self.driver.quit()
            self.driver = None
            self.is_running = False

    def navigate(self, url):
        """Navega para uma URL específica"""
        if not self.is_running:
            raise Exception("Navegador não está em execução. Inicie o navegador primeiro.")

        # Adiciona https:// se não tiver protocolo
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url

        self.driver.get(url)

    def go_back(self):
        """Volta para a página anterior"""
        if not self.is_running:
            raise Exception("Navegador não está em execução.")
        self.driver.back()

    def go_forward(self):
        """Avança para a próxima página"""
        if not self.is_running:
            raise Exception("Navegador não está em execução.")
        self.driver.forward()

    def refresh(self):
        """Atualiza a página atual"""
        if not self.is_running:
            raise Exception("Navegador não está em execução.")
        self.driver.refresh()

    def take_screenshot(self):
        """Tira uma captura de tela da página atual"""
        if not self.is_running:
            raise Exception("Navegador não está em execução.")

        # Cria pasta screenshots se não existir
        os.makedirs('screenshots', exist_ok=True)

        # Gera nome do arquivo com timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'screenshots/screenshot_{timestamp}.png'

        self.driver.save_screenshot(filename)
        return filename

    def scroll(self, direction):
        """Rola a página na direção especificada"""
        if not self.is_running:
            raise Exception("Navegador não está em execução.")

        scroll_scripts = {
            'down': 'window.scrollBy(0, 500);',
            'up': 'window.scrollBy(0, -500);',
            'top': 'window.scrollTo(0, 0);',
            'bottom': 'window.scrollTo(0, document.body.scrollHeight);'
        }

        script = scroll_scripts.get(direction)
        if script:
            self.driver.execute_script(script)
        else:
            raise Exception(f"Direção de scroll inválida: {direction}")

    def get_status(self):
        """Retorna o status atual do navegador"""
        if not self.is_running or not self.driver:
            return {
                'running': False,
                'url': None,
                'title': None
            }

        try:
            return {
                'running': True,
                'url': self.driver.current_url,
                'title': self.driver.title
            }
        except:
            return {
                'running': False,
                'url': None,
                'title': None
            }

    # Métodos avançados para automação
    def wait_for_element(self, selector, by=By.CSS_SELECTOR, timeout=10):
        """Espera um elemento aparecer na página"""
        if not self.is_running:
            raise Exception("Navegador não está em execução.")

        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, selector))
            )
            return element
        except TimeoutException:
            raise Exception(f"Elemento '{selector}' não encontrado após {timeout} segundos")

    def wait_for_clickable(self, selector, by=By.CSS_SELECTOR, timeout=10):
        """Espera um elemento estar clicável"""
        if not self.is_running:
            raise Exception("Navegador não está em execução.")

        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, selector))
            )
            return element
        except TimeoutException:
            raise Exception(f"Elemento '{selector}' não está clicável após {timeout} segundos")

    def find_element(self, selector, by=By.CSS_SELECTOR):
        """Encontra um elemento na página"""
        if not self.is_running:
            raise Exception("Navegador não está em execução.")

        try:
            return self.driver.find_element(by, selector)
        except NoSuchElementException:
            raise Exception(f"Elemento '{selector}' não encontrado")

    def find_elements(self, selector, by=By.CSS_SELECTOR):
        """Encontra múltiplos elementos na página"""
        if not self.is_running:
            raise Exception("Navegador não está em execução.")

        return self.driver.find_elements(by, selector)

    def click_element(self, selector, by=By.CSS_SELECTOR, wait=True):
        """Clica em um elemento"""
        if not self.is_running:
            raise Exception("Navegador não está em execução.")

        try:
            if wait:
                element = self.wait_for_clickable(selector, by)
            else:
                element = self.find_element(selector, by)

            element.click()
            time.sleep(0.5)  # Pequena pausa após o clique
        except Exception as e:
            raise Exception(f"Erro ao clicar no elemento '{selector}': {str(e)}")

    def type_text(self, selector, text, by=By.CSS_SELECTOR, clear_first=True):
        """Digite texto em um campo"""
        if not self.is_running:
            raise Exception("Navegador não está em execução.")

        try:
            element = self.wait_for_element(selector, by)
            if clear_first:
                element.clear()
            element.send_keys(text)
            time.sleep(0.3)
        except Exception as e:
            raise Exception(f"Erro ao digitar no elemento '{selector}': {str(e)}")

    def get_text(self, selector, by=By.CSS_SELECTOR):
        """Obtém o texto de um elemento"""
        if not self.is_running:
            raise Exception("Navegador não está em execução.")

        try:
            element = self.wait_for_element(selector, by)
            return element.text
        except Exception as e:
            raise Exception(f"Erro ao obter texto do elemento '{selector}': {str(e)}")

    def element_exists(self, selector, by=By.CSS_SELECTOR):
        """Verifica se um elemento existe"""
        if not self.is_running:
            return False

        try:
            self.driver.find_element(by, selector)
            return True
        except NoSuchElementException:
            return False

    def wait_for_page_load(self, timeout=10):
        """Espera a página carregar completamente"""
        if not self.is_running:
            raise Exception("Navegador não está em execução.")

        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def execute_script(self, script):
        """Executa JavaScript na página"""
        if not self.is_running:
            raise Exception("Navegador não está em execução.")

        return self.driver.execute_script(script)

    def get_attribute(self, selector, attribute, by=By.CSS_SELECTOR):
        """Obtém um atributo de um elemento"""
        if not self.is_running:
            raise Exception("Navegador não está em execução.")

        try:
            element = self.find_element(selector, by)
            return element.get_attribute(attribute)
        except Exception as e:
            raise Exception(f"Erro ao obter atributo '{attribute}' do elemento '{selector}': {str(e)}")
