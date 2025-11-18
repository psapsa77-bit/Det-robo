"""
Controlador do Navegador usando Selenium
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os


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

        # Tenta usar o Chrome instalado no sistema
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
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
