"""
DET Robot - Sistema de Automação para Domicílio Eletrônico Trabalhista
=======================================================================

Módulo principal do DET Robot.

Funcionalidades:
- Automação de navegação no portal DET
- Extração de dados estruturados
- Geração de relatórios profissionais
- Processamento automatizado de múltiplos CNPJs
"""

__version__ = "2.0.0"
__author__ = "DET Robot Team"

from det_robot.config import DETConfig
from det_robot.automation import DETAutomation
from det_robot.extractor import DETExtractor
from det_robot.reporter import DETReporter
from det_robot.processor import CNPJProcessor

__all__ = [
    'DETConfig',
    'DETAutomation',
    'DETExtractor',
    'DETReporter',
    'CNPJProcessor',
]
