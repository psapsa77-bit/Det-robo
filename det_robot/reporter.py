"""
Módulo de Geração de Relatórios
"""
import json
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path

from det_robot.config import DETConfig


class DETReporter:
    """
    Gerador de relatórios profissionais

    Suporta:
    - Relatórios HTML com gráficos
    - Exportação JSON
    - Relatórios PDF (futuro)
    - Sumários executivos
    """

    def __init__(self, config: Optional[DETConfig] = None):
        """
        Inicializa gerador de relatórios

        Args:
            config: Configurações (opcional)
        """
        self.config = config or DETConfig()
        self.logger = logging.getLogger(__name__)

    def generate_html_report(self, data: Dict[str, Any], title: str = "Relatório DET") -> Dict[str, Any]:
        """
        Gera relatório HTML

        Args:
            data: Dados para o relatório
            title: Título do relatório

        Returns:
            Dict com caminho do arquivo gerado
        """
        try:
            self.logger.info(f"Gerando relatório HTML: {title}")

            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'relatorio_det_{timestamp}.html'
            filepath = self.config.EXPORTS_DIR / filename

            html_content = self._build_html_template(data, title)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)

            self.logger.info(f"Relatório HTML gerado: {filepath}")

            return {
                'success': True,
                'filepath': str(filepath),
                'filename': filename,
                'format': 'html'
            }

        except Exception as e:
            self.logger.error(f"Erro ao gerar relatório HTML: {str(e)}")
            return {
                'success': False,
                'message': f'Erro ao gerar relatório: {str(e)}'
            }

    def export_json(self, data: Dict[str, Any], filename: Optional[str] = None) -> Dict[str, Any]:
        """
        Exporta dados para JSON

        Args:
            data: Dados para exportar
            filename: Nome do arquivo (opcional)

        Returns:
            Dict com caminho do arquivo gerado
        """
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = filename or f'dados_det_{timestamp}.json'
            filepath = self.config.EXPORTS_DIR / filename

            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            self.logger.info(f"JSON exportado: {filepath}")

            return {
                'success': True,
                'filepath': str(filepath),
                'filename': filename,
                'format': 'json'
            }

        except Exception as e:
            self.logger.error(f"Erro ao exportar JSON: {str(e)}")
            return {
                'success': False,
                'message': f'Erro ao exportar JSON: {str(e)}'
            }

    def generate_summary(self, data: Dict[str, Any]) -> str:
        """
        Gera sumário executivo textual

        Args:
            data: Dados para resumir

        Returns:
            String com sumário formatado
        """
        lines = [
            "=" * 60,
            "SUMÁRIO EXECUTIVO - DET ROBOT",
            "=" * 60,
            "",
            f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
            "",
        ]

        if 'messages' in data:
            lines.append(f"📧 Mensagens: {len(data['messages'])}")

        if 'profiles' in data:
            lines.append(f"🏢 Perfis: {len(data['profiles'])}")

        lines.extend(["", "=" * 60])

        return "\n".join(lines)

    def _build_html_template(self, data: Dict[str, Any], title: str) -> str:
        """
        Constrói template HTML do relatório

        Args:
            data: Dados do relatório
            title: Título

        Returns:
            HTML completo
        """
        html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #1e3a8a;
            border-bottom: 3px solid #1e3a8a;
            padding-bottom: 10px;
        }}
        .meta {{
            color: #666;
            font-size: 0.9em;
            margin-bottom: 20px;
        }}
        .section {{
            margin: 30px 0;
        }}
        .section h2 {{
            color: #3b82f6;
            border-left: 4px solid #3b82f6;
            padding-left: 10px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background: #1e3a8a;
            color: white;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            text-align: center;
            color: #666;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>⚡ {title}</h1>
        <div class="meta">
            Gerado em: {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}<br>
            DET Robot v1.0
        </div>

        <div class="section">
            <h2>Dados Extraídos</h2>
            <pre>{json.dumps(data, indent=2, ensure_ascii=False)}</pre>
        </div>

        <div class="footer">
            <p>Relatório gerado automaticamente por DET Robot</p>
            <p>© 2024 DET Robot - Automação Profissional</p>
        </div>
    </div>
</body>
</html>
        """
        return html

    def generate_cnpj_report(self, data: Dict[str, Any]) -> Path:
        """
        Gera relatório HTML consolidado de processamento de CNPJs

        Args:
            data: Dados do processamento com stats e results

        Returns:
            Path do arquivo gerado
        """
        try:
            self.logger.info("Gerando relatório consolidado de CNPJs...")

            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'relatorio_cnpjs_{timestamp}.html'
            filepath = self.config.EXPORTS_DIR / filename

            stats = data.get('stats', {})
            results = data.get('results', [])

            # Calcula tempo total
            tempo_total = 0
            if stats.get('tempo_inicio') and stats.get('tempo_fim'):
                tempo_inicio = stats['tempo_inicio']
                tempo_fim = stats['tempo_fim']
                if isinstance(tempo_inicio, str):
                    tempo_inicio = datetime.fromisoformat(tempo_inicio)
                if isinstance(tempo_fim, str):
                    tempo_fim = datetime.fromisoformat(tempo_fim)
                tempo_total = (tempo_fim - tempo_inicio).total_seconds()

            html = self._build_cnpj_report_html(stats, results, tempo_total)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)

            self.logger.info(f"Relatório consolidado gerado: {filepath}")
            return filepath

        except Exception as e:
            self.logger.error(f"Erro ao gerar relatório de CNPJs: {str(e)}")
            raise

    def _build_cnpj_report_html(self, stats: Dict[str, Any], results: List[Dict[str, Any]], tempo_total: float) -> str:
        """
        Constrói HTML do relatório de CNPJs

        Args:
            stats: Estatísticas do processamento
            results: Resultados por CNPJ
            tempo_total: Tempo total em segundos

        Returns:
            HTML completo
        """
        # Filtra CNPJs com mensagens
        cnpjs_com_mensagens = [r for r in results if r.get('quantidade_mensagens', 0) > 0]
        cnpjs_sem_mensagens = [r for r in results if r.get('quantidade_mensagens', 0) == 0 and r.get('sucesso')]
        cnpjs_com_erro = [r for r in results if not r.get('sucesso')]

        # Conta total de mensagens
        total_msgs = sum(r.get('quantidade_mensagens', 0) for r in results)

        html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório DET - Processamento de CNPJs</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
            font-weight: 300;
        }}
        .header .subtitle {{
            margin-top: 10px;
            opacity: 0.9;
            font-size: 1.1em;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 40px;
            background: #f8fafc;
        }}
        .stat-card {{
            background: white;
            padding: 25px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-top: 4px solid #3b82f6;
        }}
        .stat-card.success {{
            border-top-color: #10b981;
        }}
        .stat-card.warning {{
            border-top-color: #f59e0b;
        }}
        .stat-card.error {{
            border-top-color: #ef4444;
        }}
        .stat-value {{
            font-size: 3em;
            font-weight: bold;
            color: #1e3a8a;
            margin: 10px 0;
        }}
        .stat-label {{
            color: #64748b;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .content {{
            padding: 40px;
        }}
        .section {{
            margin-bottom: 50px;
        }}
        .section h2 {{
            color: #1e3a8a;
            font-size: 1.8em;
            border-left: 5px solid #3b82f6;
            padding-left: 15px;
            margin-bottom: 25px;
        }}
        .cnpj-card {{
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 25px;
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }}
        .cnpj-card:hover {{
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            transform: translateY(-2px);
        }}
        .cnpj-card.has-messages {{
            border-left: 5px solid #10b981;
            background: #f0fdf4;
        }}
        .cnpj-card.no-messages {{
            border-left: 5px solid #94a3b8;
            background: #f8fafc;
        }}
        .cnpj-card.error {{
            border-left: 5px solid #ef4444;
            background: #fef2f2;
        }}
        .cnpj-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }}
        .cnpj-number {{
            font-size: 1.4em;
            font-weight: bold;
            color: #1e3a8a;
        }}
        .badge {{
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: 600;
        }}
        .badge.success {{
            background: #d1fae5;
            color: #065f46;
        }}
        .badge.info {{
            background: #dbeafe;
            color: #1e40af;
        }}
        .badge.error {{
            background: #fee2e2;
            color: #991b1b;
        }}
        .messages-list {{
            margin-top: 15px;
            padding-left: 20px;
        }}
        .message-item {{
            background: white;
            padding: 15px;
            border-radius: 6px;
            margin-bottom: 10px;
            border-left: 3px solid #3b82f6;
        }}
        .message-subject {{
            font-weight: 600;
            color: #1e3a8a;
            margin-bottom: 5px;
        }}
        .message-meta {{
            font-size: 0.85em;
            color: #64748b;
        }}
        .footer {{
            background: #1e293b;
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .no-messages-text {{
            color: #64748b;
            font-style: italic;
        }}
        .error-text {{
            color: #dc2626;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>⚡ DET Robot - Relatório de Processamento</h1>
            <div class="subtitle">
                Análise de Mensagens Não Lidas por CNPJ<br>
                Gerado em {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}
            </div>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-label">Total de CNPJs</div>
                <div class="stat-value">{stats.get('total_cnpjs', 0)}</div>
            </div>
            <div class="stat-card success">
                <div class="stat-label">Com Mensagens</div>
                <div class="stat-value">{stats.get('com_mensagens', 0)}</div>
            </div>
            <div class="stat-card warning">
                <div class="stat-label">Total Mensagens</div>
                <div class="stat-value">{total_msgs}</div>
            </div>
            <div class="stat-card error">
                <div class="stat-label">Erros</div>
                <div class="stat-value">{stats.get('erros', 0)}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Tempo Total</div>
                <div class="stat-value">{int(tempo_total)}s</div>
            </div>
        </div>

        <div class="content">
"""

        # Seção: CNPJs com mensagens
        if cnpjs_com_mensagens:
            html += f"""
            <div class="section">
                <h2>📧 CNPJs com Mensagens Não Lidas ({len(cnpjs_com_mensagens)})</h2>
"""
            for resultado in cnpjs_com_mensagens:
                html += f"""
                <div class="cnpj-card has-messages">
                    <div class="cnpj-header">
                        <div class="cnpj-number">{resultado['cnpj']}</div>
                        <div class="badge success">
                            {resultado['quantidade_mensagens']} mensagem(ns)
                        </div>
                    </div>
"""
                if resultado.get('mensagens'):
                    html += """
                    <div class="messages-list">
"""
                    for msg in resultado['mensagens']:
                        # Verifica se msg é dict ou string
                        if isinstance(msg, dict):
                            subject = msg.get('subject', 'Sem assunto')
                            sender = msg.get('sender', 'Remetente desconhecido')
                            date = msg.get('date', '')
                            html += f"""
                        <div class="message-item">
                            <div class="message-subject">{subject}</div>
                            <div class="message-meta">De: {sender} | {date}</div>
                        </div>
"""
                        else:
                            html += f"""
                        <div class="message-item">
                            <div class="message-subject">{msg}</div>
                        </div>
"""
                    html += """
                    </div>
"""
                html += """
                </div>
"""
            html += """
            </div>
"""

        # Seção: CNPJs sem mensagens
        if cnpjs_sem_mensagens:
            html += f"""
            <div class="section">
                <h2>✓ CNPJs sem Mensagens ({len(cnpjs_sem_mensagens)})</h2>
"""
            for resultado in cnpjs_sem_mensagens:
                html += f"""
                <div class="cnpj-card no-messages">
                    <div class="cnpj-header">
                        <div class="cnpj-number">{resultado['cnpj']}</div>
                        <div class="badge info">Sem mensagens</div>
                    </div>
                    <div class="no-messages-text">Nenhuma mensagem não lida encontrada</div>
                </div>
"""
            html += """
            </div>
"""

        # Seção: CNPJs com erro
        if cnpjs_com_erro:
            html += f"""
            <div class="section">
                <h2>⚠️ CNPJs com Erros ({len(cnpjs_com_erro)})</h2>
"""
            for resultado in cnpjs_com_erro:
                html += f"""
                <div class="cnpj-card error">
                    <div class="cnpj-header">
                        <div class="cnpj-number">{resultado['cnpj']}</div>
                        <div class="badge error">Erro</div>
                    </div>
                    <div class="error-text">❌ {resultado.get('erro', 'Erro desconhecido')}</div>
                </div>
"""
            html += """
            </div>
"""

        html += f"""
        </div>

        <div class="footer">
            <p><strong>DET Robot v2.0</strong> - Automação Profissional</p>
            <p>Relatório gerado automaticamente em {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}</p>
        </div>
    </div>
</body>
</html>
"""
        return html

