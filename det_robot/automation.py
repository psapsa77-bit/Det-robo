"""
Módulo de Automação Core do DET Robot
"""
import time
import logging
from typing import Optional, Dict, List, Any
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from det_robot.config import DETConfig


class DETAutomation:
    """
    Classe principal para automação do portal DET

    Responsável por:
    - Gerenciar sessão do navegador
    - Acessar portal DET
    - Trocar perfis de empresas
    - Navegar por mensagens
    - Extrair dados estruturados
    """

    def __init__(self, config: Optional[DETConfig] = None):
        """
        Inicializa automação DET

        Args:
            config: Configurações customizadas (opcional)
        """
        self.config = config or DETConfig()
        self.driver: Optional[webdriver.Chrome] = None
        self.is_running = False
        self.current_profile: Optional[Dict[str, str]] = None

        # Setup logging
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(
            level=self.config.LOG_LEVEL,
            format=self.config.LOG_FORMAT,
            handlers=[
                logging.FileHandler(self.config.LOGS_DIR / f'det_robot_{datetime.now().strftime("%Y%m%d")}.log'),
                logging.StreamHandler()
            ]
        )

        self.logger.info(f"DET Automation inicializado - v{self.config.__version__ if hasattr(self.config, '__version__') else '1.0.0'}")

    def start_browser(self) -> Dict[str, Any]:
        """
        Inicia navegador Chrome com configurações otimizadas

        Returns:
            Dict com status da operação
        """
        if self.is_running:
            return {'success': True, 'message': 'Navegador já está em execução'}

        try:
            self.logger.info("Iniciando navegador Chrome...")

            chrome_options = Options()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument(f'--window-size={self.config.WINDOW_SIZE[0]},{self.config.WINDOW_SIZE[1]}')
            chrome_options.add_argument('--start-maximized')
            chrome_options.add_argument('--disable-blink-features=AutomationControlled')
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)

            if self.config.HEADLESS:
                chrome_options.add_argument('--headless')

            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.set_page_load_timeout(self.config.PAGE_LOAD_TIMEOUT)
            self.is_running = True

            self.logger.info("Navegador iniciado com sucesso")
            return {
                'success': True,
                'message': 'Navegador iniciado com sucesso',
                'headless': self.config.HEADLESS
            }

        except Exception as e:
            self.logger.error(f"Erro ao iniciar navegador: {str(e)}")
            return {
                'success': False,
                'message': f'Erro ao iniciar navegador: {str(e)}'
            }

    def stop_browser(self) -> Dict[str, Any]:
        """
        Fecha navegador e limpa recursos

        Returns:
            Dict com status da operação
        """
        if self.driver:
            try:
                self.logger.info("Fechando navegador...")
                self.driver.quit()
                self.driver = None
                self.is_running = False
                self.current_profile = None

                self.logger.info("Navegador fechado com sucesso")
                return {'success': True, 'message': 'Navegador fechado com sucesso'}
            except Exception as e:
                self.logger.error(f"Erro ao fechar navegador: {str(e)}")
                return {'success': False, 'message': f'Erro ao fechar navegador: {str(e)}'}

        return {'success': True, 'message': 'Navegador já estava fechado'}

    def access_det(self) -> Dict[str, Any]:
        """
        Acessa portal DET

        Returns:
            Dict com status da operação
        """
        if not self.is_running:
            return {'success': False, 'message': 'Navegador não está em execução'}

        try:
            self.logger.info(f"Acessando portal DET: {self.config.DET_URL}")
            self.driver.get(self.config.DET_URL)

            # Aguarda carregamento da página
            WebDriverWait(self.driver, self.config.PAGE_LOAD_TIMEOUT).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )

            time.sleep(2)  # Aguarda carregamento completo

            self.logger.info("Portal DET acessado com sucesso")
            return {
                'success': True,
                'message': 'Portal DET acessado com sucesso',
                'url': self.driver.current_url,
                'title': self.driver.title
            }

        except Exception as e:
            self.logger.error(f"Erro ao acessar DET: {str(e)}")
            return {'success': False, 'message': f'Erro ao acessar DET: {str(e)}'}

    def wait_for_element(self, selector: str, by: By = By.CSS_SELECTOR, timeout: Optional[int] = None):
        """
        Aguarda elemento aparecer na página

        Args:
            selector: Seletor do elemento
            by: Tipo de seletor (padrão: CSS_SELECTOR)
            timeout: Timeout customizado (opcional)

        Returns:
            WebElement encontrado
        """
        timeout = timeout or self.config.ELEMENT_WAIT_TIMEOUT
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, selector))
        )

    def take_screenshot(self, name: Optional[str] = None) -> Dict[str, Any]:
        """
        Captura screenshot da página atual

        Args:
            name: Nome customizado do arquivo (opcional)

        Returns:
            Dict com status e caminho do arquivo
        """
        if not self.is_running:
            return {'success': False, 'message': 'Navegador não está em execução'}

        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = name or f'screenshot_{timestamp}.png'
            filepath = self.config.SCREENSHOTS_DIR / filename

            self.driver.save_screenshot(str(filepath))

            self.logger.info(f"Screenshot salvo: {filepath}")
            return {
                'success': True,
                'message': f'Screenshot salvo: {filename}',
                'filepath': str(filepath)
            }

        except Exception as e:
            self.logger.error(f"Erro ao tirar screenshot: {str(e)}")
            return {'success': False, 'message': f'Erro ao tirar screenshot: {str(e)}'}

    def get_status(self) -> Dict[str, Any]:
        """
        Retorna status atual do sistema

        Returns:
            Dict com informações de status
        """
        if not self.is_running or not self.driver:
            return {
                'running': False,
                'url': None,
                'title': None,
                'profile': None
            }

        try:
            return {
                'running': True,
                'url': self.driver.current_url,
                'title': self.driver.title,
                'profile': self.current_profile
            }
        except:
            return {
                'running': False,
                'url': None,
                'title': None,
                'profile': None
            }

    def switch_profile(self, company_name: Optional[str] = None, cnpj: Optional[str] = None) -> Dict[str, Any]:
        """
        Troca perfil/empresa no DET

        Args:
            company_name: Nome da empresa (opcional)
            cnpj: CNPJ da empresa (opcional)

        Returns:
            Dict com status da operação
        """
        if not self.is_running:
            return {'success': False, 'message': 'Navegador não está em execução'}

        try:
            self.logger.info(f"Trocando perfil: {company_name or cnpj or 'abrindo seletor'}")
            time.sleep(2)

            # Seletores possíveis para botão de trocar perfil
            selectors = [
                "button[aria-label*='Trocar']",
                "button[title*='Trocar']",
                "a[href*='perfil']",
                ".trocar-perfil",
                "#btnTrocarPerfil",
                "[data-action='change-profile']"
            ]

            found = False
            for selector in selectors:
                try:
                    element = self.driver.find_element(By.CSS_SELECTOR, selector)
                    element.click()
                    found = True
                    break
                except NoSuchElementException:
                    continue

            if not found:
                # Tenta buscar por texto nos botões
                buttons = self.driver.find_elements(By.TAG_NAME, "button")
                for button in buttons:
                    if any(word in button.text.lower() for word in ['trocar', 'perfil', 'empresa']):
                        button.click()
                        found = True
                        break

            if not found:
                return {'success': False, 'message': 'Botão de trocar perfil não encontrado'}

            time.sleep(1)

            # Se fornecido nome ou CNPJ, busca pela empresa
            if company_name or cnpj:
                search_term = company_name if company_name else cnpj

                search_selectors = [
                    "input[type='search']",
                    "input[placeholder*='Buscar']",
                    "input[placeholder*='Pesquisar']",
                    "input[name*='search']",
                    "#searchEmpresa"
                ]

                for selector in search_selectors:
                    try:
                        search_input = self.driver.find_element(By.CSS_SELECTOR, selector)
                        search_input.clear()
                        search_input.send_keys(search_term)
                        time.sleep(1)
                        break
                    except NoSuchElementException:
                        continue

                self.current_profile = {'name': company_name, 'cnpj': cnpj}

            return {
                'success': True,
                'message': f'Perfil alterado: {company_name or cnpj or "seletor aberto"}'
            }

        except Exception as e:
            self.logger.error(f"Erro ao trocar perfil: {str(e)}")
            return {'success': False, 'message': f'Erro ao trocar perfil: {str(e)}'}

    def access_messages(self) -> Dict[str, Any]:
        """
        Acessa área de mensagens do DET

        Returns:
            Dict com status da operação
        """
        if not self.is_running:
            return {'success': False, 'message': 'Navegador não está em execução'}

        try:
            self.logger.info("Acessando área de mensagens...")
            time.sleep(2)

            # Seletores para link de mensagens
            selectors = [
                "a[href*='mensagens']",
                "a[href*='messages']",
                "button[aria-label*='Mensagens']",
                ".menu-mensagens",
                "#linkMensagens",
                "[data-menu='mensagens']"
            ]

            found = False
            for selector in selectors:
                try:
                    element = self.driver.find_element(By.CSS_SELECTOR, selector)
                    element.click()
                    found = True
                    break
                except NoSuchElementException:
                    continue

            if not found:
                # Busca por links com texto "mensagens"
                links = self.driver.find_elements(By.TAG_NAME, "a")
                for link in links:
                    if 'mensagen' in link.text.lower() or 'message' in link.text.lower():
                        link.click()
                        found = True
                        break

            if not found:
                return {'success': False, 'message': 'Link de mensagens não encontrado'}

            time.sleep(2)
            WebDriverWait(self.driver, self.config.PAGE_LOAD_TIMEOUT).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )

            self.logger.info("Área de mensagens acessada")
            return {'success': True, 'message': 'Área de mensagens acessada com sucesso'}

        except Exception as e:
            self.logger.error(f"Erro ao acessar mensagens: {str(e)}")
            return {'success': False, 'message': f'Erro ao acessar mensagens: {str(e)}'}

    def click_first_unread_message(self) -> Dict[str, Any]:
        """
        Clica na primeira mensagem não lida

        Returns:
            Dict com status da operação
        """
        if not self.is_running:
            return {'success': False, 'message': 'Navegador não está em execução'}

        try:
            self.logger.info("Clicando na primeira mensagem não lida...")

            # Primeiro acessa mensagens
            result = self.access_messages()
            if not result['success']:
                return result

            time.sleep(1)

            # Seletores para mensagens não lidas
            selectors = [
                ".message.unread",
                ".mensagem.nao-lida",
                "tr.unread",
                "[class*='unread']",
                "[class*='nao-lida']"
            ]

            for selector in selectors:
                try:
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    if elements:
                        elements[0].click()
                        time.sleep(2)
                        self.logger.info("Primeira mensagem não lida aberta")
                        return {'success': True, 'message': 'Primeira mensagem não lida aberta'}
                except:
                    continue

            return {'success': False, 'message': 'Nenhuma mensagem não lida encontrada'}

        except Exception as e:
            self.logger.error(f"Erro ao clicar em mensagem: {str(e)}")
            return {'success': False, 'message': f'Erro ao clicar em mensagem: {str(e)}'}

    def __enter__(self):
        """Context manager entry"""
        self.start_browser()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.stop_browser()
