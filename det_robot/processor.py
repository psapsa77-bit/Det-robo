"""
Módulo de Processamento Automatizado de CNPJs
Processa múltiplos CNPJs e coleta mensagens não lidas
"""
import logging
import time
from typing import List, Dict, Any, Optional
from datetime import datetime
from pathlib import Path

from det_robot.config import DETConfig
from det_robot.automation import DETAutomation
from det_robot.extractor import DETExtractor
from det_robot.reporter import DETReporter


class CNPJProcessor:
    """
    Processador automatizado de CNPJs

    Funcionalidades:
    - Lê lista de CNPJs de arquivo
    - Processa cada CNPJ automaticamente
    - Coleta mensagens não lidas
    - Gera relatório consolidado
    """

    def __init__(self, config: Optional[DETConfig] = None):
        """
        Inicializa processador

        Args:
            config: Configurações customizadas (opcional)
        """
        self.config = config or DETConfig()
        self.automation = None
        self.extractor = None
        self.reporter = None
        self.logger = logging.getLogger(__name__)

        # Arquivo de CNPJs
        self.cnpj_file = Path("cnpjs.txt")

        # Resultados do processamento
        self.results = []
        self.stats = {
            'total_cnpjs': 0,
            'processados': 0,
            'com_mensagens': 0,
            'total_mensagens': 0,
            'erros': 0,
            'tempo_inicio': None,
            'tempo_fim': None
        }

    def load_cnpjs(self, filepath: Optional[Path] = None) -> List[str]:
        """
        Carrega lista de CNPJs do arquivo

        Args:
            filepath: Caminho do arquivo (padrão: cnpjs.txt)

        Returns:
            Lista de CNPJs formatados
        """
        filepath = filepath or self.cnpj_file

        if not filepath.exists():
            self.logger.warning(f"Arquivo {filepath} não encontrado")
            return []

        cnpjs = []
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                cnpj = line.strip()
                # Remove linhas vazias e comentários
                if cnpj and not cnpj.startswith('#'):
                    # Limpa formatação do CNPJ
                    cnpj_limpo = cnpj.replace('.', '').replace('/', '').replace('-', '').replace(' ', '')
                    if cnpj_limpo.isdigit() and len(cnpj_limpo) == 14:
                        cnpjs.append(cnpj)
                    else:
                        self.logger.warning(f"CNPJ inválido ignorado: {cnpj}")

        self.logger.info(f"Carregados {len(cnpjs)} CNPJs do arquivo {filepath}")
        return cnpjs

    def format_cnpj(self, cnpj: str) -> str:
        """
        Formata CNPJ para exibição

        Args:
            cnpj: CNPJ sem formatação

        Returns:
            CNPJ formatado (00.000.000/0001-00)
        """
        # Remove qualquer formatação existente
        cnpj_limpo = cnpj.replace('.', '').replace('/', '').replace('-', '').replace(' ', '')

        if len(cnpj_limpo) != 14:
            return cnpj

        # Formata: 00.000.000/0001-00
        return f"{cnpj_limpo[:2]}.{cnpj_limpo[2:5]}.{cnpj_limpo[5:8]}/{cnpj_limpo[8:12]}-{cnpj_limpo[12:]}"

    def process_cnpj(self, cnpj: str) -> Dict[str, Any]:
        """
        Processa um CNPJ individual

        Args:
            cnpj: CNPJ a processar

        Returns:
            Dict com resultados do processamento
        """
        cnpj_formatado = self.format_cnpj(cnpj)
        self.logger.info(f"Processando CNPJ: {cnpj_formatado}")

        resultado = {
            'cnpj': cnpj_formatado,
            'cnpj_original': cnpj,
            'sucesso': False,
            'timestamp': datetime.now().isoformat(),
            'mensagens': [],
            'quantidade_mensagens': 0,
            'erro': None,
            'tempo_processamento': 0
        }

        tempo_inicio = time.time()

        try:
            # 1. Trocar perfil para o CNPJ
            self.logger.info(f"Trocando perfil para {cnpj_formatado}...")
            troca_result = self.automation.switch_profile(cnpj=cnpj)

            if not troca_result['success']:
                resultado['erro'] = f"Falha ao trocar perfil: {troca_result['message']}"
                self.logger.error(resultado['erro'])
                return resultado

            # Aguarda troca de perfil
            time.sleep(3)

            # 2. Acessar área de mensagens
            self.logger.info("Acessando mensagens...")
            msg_result = self.automation.access_messages()

            if not msg_result['success']:
                resultado['erro'] = f"Falha ao acessar mensagens: {msg_result['message']}"
                self.logger.error(resultado['erro'])
                return resultado

            # Aguarda carregamento
            time.sleep(2)

            # 3. Extrair mensagens não lidas
            self.logger.info("Extraindo mensagens não lidas...")
            extract_result = self.extractor.extract_unread_messages()

            if extract_result['success']:
                resultado['mensagens'] = extract_result.get('messages', [])
                resultado['quantidade_mensagens'] = extract_result.get('count', 0)
                resultado['sucesso'] = True

                self.logger.info(f"✓ {cnpj_formatado}: {resultado['quantidade_mensagens']} mensagens não lidas")
            else:
                resultado['erro'] = extract_result.get('message', 'Erro desconhecido')
                self.logger.warning(f"Nenhuma mensagem encontrada para {cnpj_formatado}")

        except Exception as e:
            resultado['erro'] = str(e)
            self.logger.error(f"Erro ao processar {cnpj_formatado}: {str(e)}")

        finally:
            resultado['tempo_processamento'] = round(time.time() - tempo_inicio, 2)

        return resultado

    def process_all(self, cnpjs: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Processa todos os CNPJs

        Args:
            cnpjs: Lista de CNPJs (se None, carrega do arquivo)

        Returns:
            Dict com resultados consolidados
        """
        # Carrega CNPJs se não fornecidos
        if cnpjs is None:
            cnpjs = self.load_cnpjs()

        if not cnpjs:
            return {
                'success': False,
                'message': 'Nenhum CNPJ para processar',
                'results': []
            }

        # Inicializa estatísticas
        self.stats['total_cnpjs'] = len(cnpjs)
        self.stats['tempo_inicio'] = datetime.now()
        self.results = []

        self.logger.info(f"Iniciando processamento de {len(cnpjs)} CNPJs...")

        # Processa cada CNPJ
        for idx, cnpj in enumerate(cnpjs, 1):
            self.logger.info(f"\n[{idx}/{len(cnpjs)}] Processando CNPJ {cnpj}...")

            resultado = self.process_cnpj(cnpj)
            self.results.append(resultado)

            # Atualiza estatísticas
            self.stats['processados'] += 1

            if resultado['sucesso']:
                if resultado['quantidade_mensagens'] > 0:
                    self.stats['com_mensagens'] += 1
                    self.stats['total_mensagens'] += resultado['quantidade_mensagens']
            else:
                self.stats['erros'] += 1

            # Pequena pausa entre CNPJs
            if idx < len(cnpjs):
                time.sleep(2)

        self.stats['tempo_fim'] = datetime.now()
        tempo_total = (self.stats['tempo_fim'] - self.stats['tempo_inicio']).total_seconds()

        self.logger.info(f"\n{'='*60}")
        self.logger.info(f"PROCESSAMENTO CONCLUÍDO!")
        self.logger.info(f"{'='*60}")
        self.logger.info(f"Total de CNPJs: {self.stats['total_cnpjs']}")
        self.logger.info(f"Processados com sucesso: {self.stats['processados'] - self.stats['erros']}")
        self.logger.info(f"CNPJs com mensagens: {self.stats['com_mensagens']}")
        self.logger.info(f"Total de mensagens: {self.stats['total_mensagens']}")
        self.logger.info(f"Erros: {self.stats['erros']}")
        self.logger.info(f"Tempo total: {tempo_total:.2f}s")
        self.logger.info(f"{'='*60}\n")

        return {
            'success': True,
            'message': f'Processamento concluído: {self.stats["com_mensagens"]} CNPJs com mensagens',
            'stats': self.stats,
            'results': self.results
        }

    def generate_report(self, results: Optional[Dict[str, Any]] = None) -> Path:
        """
        Gera relatório consolidado

        Args:
            results: Resultados do processamento (opcional)

        Returns:
            Caminho do arquivo de relatório
        """
        if results is None:
            results = {
                'stats': self.stats,
                'results': self.results
            }

        self.logger.info("Gerando relatório consolidado...")

        # Gera relatório HTML
        filepath = self.reporter.generate_cnpj_report(results)

        self.logger.info(f"Relatório salvo em: {filepath}")
        return filepath

    def run(self, cnpj_file: Optional[Path] = None) -> Dict[str, Any]:
        """
        Executa fluxo completo de processamento

        Args:
            cnpj_file: Arquivo com lista de CNPJs (opcional)

        Returns:
            Dict com resultados e caminho do relatório
        """
        try:
            # Inicializa componentes
            self.automation = DETAutomation(self.config)
            self.extractor = DETExtractor(self.automation, self.config)
            self.reporter = DETReporter(self.config)

            # Inicia navegador
            self.logger.info("Iniciando navegador...")
            start_result = self.automation.start_browser()
            if not start_result['success']:
                return {
                    'success': False,
                    'message': 'Falha ao iniciar navegador',
                    'error': start_result['message']
                }

            # Acessa DET
            self.logger.info("Acessando portal DET...")
            det_result = self.automation.access_det()
            if not det_result['success']:
                return {
                    'success': False,
                    'message': 'Falha ao acessar DET',
                    'error': det_result['message']
                }

            # Aguarda login manual
            self.logger.info("\n" + "="*60)
            self.logger.info("ATENÇÃO: Faça login manualmente no portal DET")
            self.logger.info("O processamento iniciará em 30 segundos...")
            self.logger.info("="*60 + "\n")
            time.sleep(30)

            # Carrega CNPJs
            cnpjs = self.load_cnpjs(cnpj_file)

            # Processa todos
            results = self.process_all(cnpjs)

            # Gera relatório
            report_path = self.generate_report(results)

            return {
                'success': True,
                'message': 'Processamento concluído com sucesso',
                'stats': self.stats,
                'report_path': str(report_path),
                'results': self.results
            }

        except Exception as e:
            self.logger.error(f"Erro no processamento: {str(e)}")
            return {
                'success': False,
                'message': f'Erro no processamento: {str(e)}'
            }

        finally:
            # Fecha navegador
            if self.automation:
                self.automation.stop_browser()
