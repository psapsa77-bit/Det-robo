"""
DET Robot - Sistema de Automação para Domicílio Eletrônico Trabalhista
=======================================================================

Módulo principal do DET Robot.
"""

__version__ = "1.0.0"
__author__ = "DET Robot Team"

from det_robot.config import DETConfig
from det_robot.automation import DETAutomation
from det_robot.extractor import DETExtractor
from det_robot.reporter import DETReporter

__all__ = [
    'DETConfig',
    'DETAutomation',
    'DETExtractor',
    'DETReporter',
]
