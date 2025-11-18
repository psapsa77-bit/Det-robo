#!/bin/bash

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "==============================================="
echo "   DET ROBOT - INSTALADOR PROFISSIONAL"
echo "==============================================="
echo "   Versão: 1.0.0"
echo "   Sistema: Linux/Mac"
echo "==============================================="
echo -e "${NC}"

# Verificar Python
echo -e "${BLUE}[1/6] Verificando Python...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERRO] Python3 não encontrado!${NC}"
    echo ""
    echo "Por favor, instale Python 3.7 ou superior:"
    echo "  Ubuntu/Debian: sudo apt-get install python3 python3-pip python3-venv"
    echo "  Fedora: sudo dnf install python3 python3-pip"
    echo "  Mac: brew install python3"
    echo ""
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo -e "${GREEN}[OK] $PYTHON_VERSION encontrado${NC}"
echo ""

# Verificar Chrome
echo -e "${BLUE}[2/6] Verificando Google Chrome...${NC}"
if command -v google-chrome &> /dev/null || command -v google-chrome-stable &> /dev/null || \
   command -v chromium &> /dev/null || command -v chromium-browser &> /dev/null; then
    echo -e "${GREEN}[OK] Google Chrome/Chromium encontrado${NC}"
else
    echo -e "${YELLOW}[AVISO] Google Chrome não encontrado!${NC}"
    echo ""
    echo "O Chrome é NECESSÁRIO para o DET Robot funcionar."
    echo "  Ubuntu/Debian: sudo apt-get install google-chrome-stable"
    echo "  Fedora: sudo dnf install google-chrome-stable"
    echo "  Mac: brew install --cask google-chrome"
    echo ""
    read -p "Deseja continuar mesmo assim? (s/N): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Ss]$ ]]; then
        exit 1
    fi
fi
echo ""

# Limpar instalação anterior
echo -e "${BLUE}[3/6] Limpando instalação anterior...${NC}"
if [ -d "venv" ]; then
    echo "Removendo ambiente virtual antigo..."
    rm -rf venv
fi
echo -e "${GREEN}[OK] Limpeza concluída${NC}"
echo ""

# Criar ambiente virtual
echo -e "${BLUE}[4/6] Criando ambiente virtual...${NC}"
python3 -m venv venv

if [ $? -ne 0 ]; then
    echo -e "${RED}[ERRO] Falha ao criar ambiente virtual!${NC}"
    echo ""
    echo "Possível solução:"
    echo "  pip3 install --upgrade pip"
    echo "  pip3 install virtualenv"
    echo ""
    exit 1
fi
echo -e "${GREEN}[OK] Ambiente virtual criado${NC}"
echo ""

# Ativar ambiente virtual
echo -e "${BLUE}[5/6] Ativando ambiente virtual...${NC}"
source venv/bin/activate

if [ $? -ne 0 ]; then
    echo -e "${RED}[ERRO] Falha ao ativar ambiente virtual!${NC}"
    exit 1
fi
echo -e "${GREEN}[OK] Ambiente virtual ativado${NC}"
echo ""

# Instalar dependências
echo -e "${BLUE}[6/6] Instalando dependências...${NC}"
echo ""
echo "Atualizando pip..."
pip install --upgrade pip

echo ""
echo "Instalando pacotes necessários..."
echo "  - Flask (servidor web)"
echo "  - Selenium (automação)"
echo "  - Outras dependências..."
echo ""

# Tenta instalar do requirements.txt com output verbose
echo "Executando: pip install -r requirements.txt"
echo ""
pip install -r requirements.txt -v

if [ $? -ne 0 ]; then
    echo ""
    echo -e "${RED}[ERRO] Falha ao instalar dependências do requirements.txt!${NC}"
    echo ""
    echo "Tentando instalação individual com versões flexíveis..."

    pip install "flask>=3.0.0" -v
    FLASK_STATUS=$?

    pip install "selenium>=4.15.0" -v
    SELENIUM_STATUS=$?

    if [ $FLASK_STATUS -ne 0 ] || [ $SELENIUM_STATUS -ne 0 ]; then
        echo ""
        echo -e "${RED}[ERRO] Falha crítica na instalação!${NC}"
        echo ""
        echo "Detalhes do erro acima. Possíveis soluções:"
        echo "  1. Verifique sua conexão com a internet"
        echo "  2. Execute: pip3 install --upgrade pip setuptools wheel"
        echo "  3. Tente instalar manualmente: pip3 install flask selenium"
        echo ""
        exit 1
    fi
fi

echo ""
echo -e "${GREEN}[OK] Todas as dependências instaladas${NC}"
echo ""

# Criar diretórios necessários
echo "Criando estrutura de diretórios..."
mkdir -p exports logs screenshots
chmod +x ABRIR.sh
echo -e "${GREEN}[OK] Diretórios criados${NC}"
echo ""

# Sucesso
echo -e "${GREEN}"
echo "==============================================="
echo "   INSTALAÇÃO CONCLUÍDA COM SUCESSO!"
echo "==============================================="
echo -e "${NC}"
echo ""
echo "Próximos passos:"
echo "  1. Execute: bash ABRIR.sh (ou ./ABRIR.sh)"
echo "  2. Acesse: http://localhost:5000"
echo "  3. Consulte: docs/COMO_USAR.md"
echo ""
echo "==============================================="
echo ""
