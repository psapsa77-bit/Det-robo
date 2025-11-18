"""
Configurações do DET Robot
"""
import os
from pathlib import Path
from typing import Optional
from dataclasses import dataclass


@dataclass
class DETConfig:
    """Configurações centralizadas do DET Robot"""

    # URLs
    DET_URL: str = "https://det.trabalho.gov.br/"

    # Timeouts (segundos)
    DEFAULT_TIMEOUT: int = 10
    PAGE_LOAD_TIMEOUT: int = 30
    ELEMENT_WAIT_TIMEOUT: int = 15

    # Diretórios
    BASE_DIR: Path = Path(__file__).parent.parent
    EXPORTS_DIR: Path = BASE_DIR / "exports"
    LOGS_DIR: Path = BASE_DIR / "logs"
    SCREENSHOTS_DIR: Path = BASE_DIR / "screenshots"

    # Chrome Options
    HEADLESS: bool = False
    WINDOW_SIZE: tuple = (1920, 1080)

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Extração de dados
    MAX_MESSAGES_TO_EXTRACT: int = 50
    EXTRACT_ATTACHMENTS: bool = True

    # Relatórios
    REPORT_FORMAT: str = "html"  # html, pdf, json
    INCLUDE_SCREENSHOTS: bool = True

    def __post_init__(self):
        """Cria diretórios necessários após inicialização"""
        self.EXPORTS_DIR.mkdir(exist_ok=True)
        self.LOGS_DIR.mkdir(exist_ok=True)
        self.SCREENSHOTS_DIR.mkdir(exist_ok=True)

    @classmethod
    def from_env(cls) -> 'DETConfig':
        """Cria configuração a partir de variáveis de ambiente"""
        return cls(
            DET_URL=os.getenv('DET_URL', cls.DET_URL),
            HEADLESS=os.getenv('HEADLESS', '').lower() == 'true',
            LOG_LEVEL=os.getenv('LOG_LEVEL', cls.LOG_LEVEL),
        )

    def to_dict(self) -> dict:
        """Converte configurações para dicionário"""
        return {
            'det_url': self.DET_URL,
            'default_timeout': self.DEFAULT_TIMEOUT,
            'headless': self.HEADLESS,
            'log_level': self.LOG_LEVEL,
            'exports_dir': str(self.EXPORTS_DIR),
            'logs_dir': str(self.LOGS_DIR),
        }
