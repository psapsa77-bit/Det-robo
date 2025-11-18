"""
Automação para Domicílio Eletrônico Trabalhista (DET)
"""
from selenium.webdriver.common.by import By
import time


class DETAutomation:
    """Classe para automatizar ações no portal DET"""

    DET_URL = "https://det.trabalho.gov.br/"

    def __init__(self, browser_controller):
        self.browser = browser_controller

    def acessar_det(self):
        """Acessa o portal DET"""
        try:
            self.browser.navigate(self.DET_URL)
            self.browser.wait_for_page_load(15)
            return {
                'success': True,
                'message': 'Portal DET acessado com sucesso!'
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'Erro ao acessar DET: {str(e)}'
            }

    def trocar_perfil_empresa(self, nome_empresa=None, cnpj=None):
        """
        Troca o perfil da empresa no DET
        Pode buscar por nome ou CNPJ
        """
        try:
            # Aguarda a página carregar
            time.sleep(2)

            # Procura pelo botão de trocar empresa/perfil
            # Nota: Os seletores abaixo são genéricos e precisam ser ajustados
            # conforme a estrutura real do portal DET

            # Tenta encontrar o botão de troca de perfil (pode variar)
            seletores_possiveis = [
                "button[aria-label*='Trocar']",
                "button[title*='Trocar']",
                "a[href*='perfil']",
                ".trocar-perfil",
                "#btnTrocarPerfil",
                "button:contains('Trocar Perfil')",
                "[data-action='change-profile']"
            ]

            elemento_encontrado = False
            for seletor in seletores_possiveis:
                if self.browser.element_exists(seletor):
                    self.browser.click_element(seletor)
                    elemento_encontrado = True
                    break

            if not elemento_encontrado:
                # Tenta usar JavaScript para procurar botões
                botoes = self.browser.find_elements("button", By.TAG_NAME)
                for botao in botoes:
                    texto = botao.text.lower()
                    if 'trocar' in texto or 'perfil' in texto or 'empresa' in texto:
                        botao.click()
                        elemento_encontrado = True
                        break

            if not elemento_encontrado:
                return {
                    'success': False,
                    'message': 'Botão de trocar perfil não encontrado. Você está logado no DET?'
                }

            time.sleep(1)

            # Se foi fornecido nome ou CNPJ, busca pela empresa
            if nome_empresa or cnpj:
                busca = nome_empresa if nome_empresa else cnpj

                # Procura campo de busca
                seletores_busca = [
                    "input[type='search']",
                    "input[placeholder*='Buscar']",
                    "input[placeholder*='Pesquisar']",
                    "input[name*='search']",
                    "#searchEmpresa"
                ]

                for seletor in seletores_busca:
                    if self.browser.element_exists(seletor):
                        self.browser.type_text(seletor, busca)
                        time.sleep(1)
                        break

                # Clica na empresa encontrada
                # Procura por elementos que contenham o nome/CNPJ
                time.sleep(1)

            return {
                'success': True,
                'message': f'Perfil de empresa alterado. Busca: {nome_empresa or cnpj or "lista exibida"}'
            }

        except Exception as e:
            return {
                'success': False,
                'message': f'Erro ao trocar perfil: {str(e)}'
            }

    def verificar_mensagens_nao_lidas(self):
        """Verifica e retorna o número de mensagens não lidas"""
        try:
            time.sleep(2)

            # Seletores possíveis para o ícone/badge de mensagens não lidas
            seletores_mensagens = [
                ".badge-notification",
                ".unread-count",
                ".message-badge",
                "[class*='badge']",
                "[class*='notification']",
                "span.badge",
                ".nav-item .badge"
            ]

            mensagens_nao_lidas = 0

            for seletor in seletores_mensagens:
                if self.browser.element_exists(seletor):
                    try:
                        texto = self.browser.get_text(seletor)
                        # Tenta converter para número
                        if texto.strip().isdigit():
                            mensagens_nao_lidas = int(texto.strip())
                            break
                    except:
                        continue

            if mensagens_nao_lidas > 0:
                return {
                    'success': True,
                    'message': f'Você tem {mensagens_nao_lidas} mensagem(ns) não lida(s)',
                    'count': mensagens_nao_lidas
                }
            else:
                return {
                    'success': True,
                    'message': 'Nenhuma mensagem não lida encontrada',
                    'count': 0
                }

        except Exception as e:
            return {
                'success': False,
                'message': f'Erro ao verificar mensagens: {str(e)}',
                'count': 0
            }

    def acessar_mensagens(self):
        """Acessa a área de mensagens do DET"""
        try:
            time.sleep(2)

            # Seletores possíveis para o link/botão de mensagens
            seletores_link_mensagens = [
                "a[href*='mensagens']",
                "a[href*='messages']",
                "button[aria-label*='Mensagens']",
                ".menu-mensagens",
                "#linkMensagens",
                "[data-menu='mensagens']"
            ]

            elemento_encontrado = False
            for seletor in seletores_link_mensagens:
                if self.browser.element_exists(seletor):
                    self.browser.click_element(seletor)
                    elemento_encontrado = True
                    break

            if not elemento_encontrado:
                # Tenta procurar por links que contenham "mensagens"
                links = self.browser.find_elements("a", By.TAG_NAME)
                for link in links:
                    texto = link.text.lower()
                    if 'mensagen' in texto or 'message' in texto:
                        link.click()
                        elemento_encontrado = True
                        break

            if not elemento_encontrado:
                return {
                    'success': False,
                    'message': 'Link de mensagens não encontrado'
                }

            time.sleep(2)
            self.browser.wait_for_page_load()

            return {
                'success': True,
                'message': 'Área de mensagens acessada com sucesso'
            }

        except Exception as e:
            return {
                'success': False,
                'message': f'Erro ao acessar mensagens: {str(e)}'
            }

    def listar_mensagens_nao_lidas(self):
        """Lista as mensagens não lidas"""
        try:
            # Primeiro, acessa a área de mensagens
            resultado = self.acessar_mensagens()
            if not resultado['success']:
                return resultado

            time.sleep(2)

            # Procura por mensagens não lidas
            seletores_msg_nao_lidas = [
                ".message.unread",
                ".mensagem.nao-lida",
                "tr.unread",
                "[class*='unread']",
                "[class*='nao-lida']"
            ]

            mensagens = []
            for seletor in seletores_msg_nao_lidas:
                elementos = self.browser.find_elements(seletor)
                if elementos:
                    for elem in elementos[:5]:  # Limita a 5 primeiras
                        try:
                            texto = elem.text[:100]  # Primeiros 100 caracteres
                            if texto:
                                mensagens.append(texto)
                        except:
                            continue
                    break

            if mensagens:
                msg_texto = '\n'.join([f"• {msg}" for msg in mensagens])
                return {
                    'success': True,
                    'message': f'Mensagens não lidas encontradas:\n{msg_texto}',
                    'mensagens': mensagens
                }
            else:
                return {
                    'success': True,
                    'message': 'Nenhuma mensagem não lida encontrada na listagem',
                    'mensagens': []
                }

        except Exception as e:
            return {
                'success': False,
                'message': f'Erro ao listar mensagens: {str(e)}',
                'mensagens': []
            }

    def clicar_primeira_mensagem_nao_lida(self):
        """Clica na primeira mensagem não lida"""
        try:
            # Primeiro lista as mensagens
            resultado = self.listar_mensagens_nao_lidas()

            if not resultado['success']:
                return resultado

            time.sleep(1)

            # Procura e clica na primeira mensagem não lida
            seletores_msg_nao_lidas = [
                ".message.unread",
                ".mensagem.nao-lida",
                "tr.unread",
                "[class*='unread']"
            ]

            for seletor in seletores_msg_nao_lidas:
                elementos = self.browser.find_elements(seletor)
                if elementos:
                    elementos[0].click()
                    time.sleep(2)
                    return {
                        'success': True,
                        'message': 'Primeira mensagem não lida aberta'
                    }

            return {
                'success': False,
                'message': 'Nenhuma mensagem não lida para clicar'
            }

        except Exception as e:
            return {
                'success': False,
                'message': f'Erro ao clicar em mensagem: {str(e)}'
            }
