#!/bin/bash

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "==============================================="
echo "   DET ROBOT - VERIFICAÇÃO DE INSTALAÇÃO"
echo "==============================================="
echo -e "${NC}"
echo ""

# Verificar se venv existe
echo -e "${BLUE}[1/5] Verificando ambiente virtual...${NC}"
if [ -d "venv" ]; then
    echo -e "${GREEN}[OK] Ambiente virtual encontrado${NC}"
else
    echo -e "${RED}[ERRO] Ambiente virtual não encontrado!${NC}"
    echo "Execute INSTALAR_LINUX.sh primeiro"
    exit 1
fi
echo ""

# Ativar venv
source venv/bin/activate

# Verificar Flask
echo -e "${BLUE}[2/5] Verificando Flask...${NC}"
python -c "import flask; print('Flask version:', flask.__version__)" 2>/dev/null
if [ $? -eq 0 ]; then
    echo -e "${GREEN}[OK] Flask instalado corretamente${NC}"
else
    echo -e "${RED}[ERRO] Flask não está instalado!${NC}"
    exit 1
fi
echo ""

# Verificar Selenium
echo -e "${BLUE}[3/5] Verificando Selenium...${NC}"
python -c "import selenium; print('Selenium version:', selenium.__version__)" 2>/dev/null
if [ $? -eq 0 ]; then
    echo -e "${GREEN}[OK] Selenium instalado corretamente${NC}"
else
    echo -e "${RED}[ERRO] Selenium não está instalado!${NC}"
    exit 1
fi
echo ""

# Verificar módulo det_robot
echo -e "${BLUE}[4/5] Verificando módulo det_robot...${NC}"
python -c "from det_robot import DETConfig, DETAutomation; print('Módulo det_robot OK')" 2>/dev/null
if [ $? -eq 0 ]; then
    echo -e "${GREEN}[OK] Módulo det_robot funcional${NC}"
else
    echo -e "${RED}[ERRO] Módulo det_robot não está acessível!${NC}"
    exit 1
fi
echo ""

# Listar todas as dependências instaladas
echo -e "${BLUE}[5/5] Listando todas as dependências...${NC}"
pip list | grep -E "(Flask|selenium|werkzeug|jinja2)"
echo ""

# Sucesso
echo -e "${GREEN}"
echo "==============================================="
echo "   VERIFICAÇÃO CONCLUÍDA COM SUCESSO!"
echo "==============================================="
echo -e "${NC}"
echo ""
echo "Tudo está pronto! Execute: bash ABRIR.sh"
echo ""
