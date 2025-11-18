"""
Processador de Comandos em Linguagem Natural
"""
import re


class CommandProcessor:
    """Processa comandos em linguagem natural e os converte em ações"""

    def __init__(self):
        self.patterns = [
            # Navegação
            (r'(?:abr[ae]|acess[ae]|v[áa] para|navegue? para|entre no?)\s+(.+)', 'navigate'),
            (r'(?:pesquis[ae]|busqu[ae]|procur[ae])\s+(?:por\s+)?(.+)', 'search'),

            # Controle
            (r'(?:volt[ae]|voltar|p[áa]gina anterior)', 'back'),
            (r'(?:avan[çc][ae]|avan[çc]ar|pr[óo]xim[ao]|pr[óo]xima p[áa]gina)', 'forward'),
            (r'(?:atuali[zs][ae]|atuali[zs]ar|recarreg[ae]|recarregar|refresh)', 'refresh'),

            # Screenshots
            (r'(?:tir[ae]|tirar)\s+(?:um?\s+)?(?:screenshot|captura|print|foto)', 'screenshot'),
            (r'(?:screenshot|captura|print|foto)', 'screenshot'),

            # Browser control
            (r'(?:inici[ae]|iniciar|abr[ae]|abrir)\s+(?:o\s+)?(?:navegador|browser)', 'start'),
            (r'(?:fech[ae]|fechar|par[ae]|parar)\s+(?:o\s+)?(?:navegador|browser)', 'stop'),

            # Scroll
            (r'(?:rol[ae]|rolar|descer)\s+(?:para\s+)?(?:baixo|down)', 'scroll_down'),
            (r'(?:rol[ae]|rolar|subir)\s+(?:para\s+)?(?:cima|up)', 'scroll_up'),
            (r'(?:v[áa]\s+para|ir para)\s+(?:o\s+)?(?:topo|in[íi]cio)', 'scroll_top'),
            (r'(?:v[áa]\s+para|ir para)\s+(?:o\s+)?(?:fim|final|fundo)', 'scroll_bottom'),

            # Clique
            (r'(?:cliqu[ae]|clicar)\s+(?:em|no?)\s+(.+)', 'click'),

            # Preencher formulário
            (r'(?:escrev[ae]|escrever|digit[ae]|digitar|preench[ae]|preencher)\s+["\'](.+?)["\']', 'type'),

            # Informação
            (r'(?:qual|me mostre|mostre|exib[ae]|exibir)\s+(?:o\s+)?(?:t[íi]tulo|url|endere[çc]o)', 'info'),
        ]

    def process(self, command):
        """
        Processa um comando em linguagem natural
        Retorna: (action, parameter, suggestion)
        """
        command = command.lower().strip()

        if not command:
            return None, None, "Por favor, digite um comando"

        # Tenta encontrar um padrão correspondente
        for pattern, action in self.patterns:
            match = re.search(pattern, command, re.IGNORECASE)
            if match:
                # Se tem grupo de captura, pega o parâmetro
                param = match.group(1).strip() if match.groups() else None
                return action, param, None

        # Se não encontrou padrão, tenta detectar se parece com URL
        if self._looks_like_url(command):
            return 'navigate', command, None

        # Se não reconheceu, retorna sugestão
        suggestion = self._suggest_command(command)
        return None, None, suggestion

    def _looks_like_url(self, text):
        """Verifica se o texto parece uma URL"""
        url_indicators = ['.com', '.br', '.org', '.net', 'www.', 'http://', 'https://']
        return any(indicator in text.lower() for indicator in url_indicators)

    def _suggest_command(self, command):
        """Sugere comandos baseado na entrada"""
        suggestions = {
            'google': 'Talvez você quis dizer: "abra google.com" ou "pesquise google"?',
            'youtube': 'Talvez você quis dizer: "abra youtube.com"?',
            'pesqui': 'Use: "pesquise por [termo]" ou "busque [termo]"',
            'abr': 'Use: "abra [site]" ou "acesse [url]"',
            'naveg': 'Use: "navegue para [url]"',
        }

        for key, suggestion in suggestions.items():
            if key in command:
                return suggestion

        return (
            "Não entendi o comando. Experimente:\n"
            "• 'abra google.com'\n"
            "• 'pesquise por python'\n"
            "• 'volte' ou 'avance'\n"
            "• 'tire um screenshot'\n"
            "• 'atualize a página'"
        )

    def get_search_url(self, query):
        """Gera URL de busca no Google"""
        import urllib.parse
        encoded_query = urllib.parse.quote(query)
        return f"https://www.google.com/search?q={encoded_query}"

    def get_action_description(self, action, param):
        """Retorna descrição amigável da ação"""
        descriptions = {
            'navigate': f"Navegando para: {param}",
            'search': f"Pesquisando no Google: {param}",
            'back': "Voltando para página anterior",
            'forward': "Avançando para próxima página",
            'refresh': "Atualizando página",
            'screenshot': "Tirando screenshot",
            'start': "Iniciando navegador",
            'stop': "Fechando navegador",
            'scroll_down': "Rolando para baixo",
            'scroll_up': "Rolando para cima",
            'scroll_top': "Indo para o topo da página",
            'scroll_bottom': "Indo para o final da página",
            'info': "Obtendo informações da página",
        }
        return descriptions.get(action, f"Executando: {action}")
