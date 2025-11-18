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
