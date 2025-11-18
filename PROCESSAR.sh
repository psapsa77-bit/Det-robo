#!/bin/bash

# Cores
BLUE='\033[0;34m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "============================================================"
echo "   DET ROBOT - PROCESSADOR AUTOMATIZADO DE CNPJs"
echo "============================================================"
echo -e "${NC}"
echo ""
echo "Este script irá processar todos os CNPJs do arquivo cnpjs.txt"
echo ""

# Verificar se ambiente virtual existe
if [ ! -d "venv" ]; then
    echo -e "${RED}[ERRO] Ambiente virtual não encontrado!${NC}"
    echo ""
    echo "Por favor, execute bash INSTALAR_LINUX.sh primeiro"
    echo ""
    exit 1
fi

# Ativar ambiente virtual
source venv/bin/activate

# Verificar se arquivo cnpjs.txt existe
if [ ! -f "cnpjs.txt" ]; then
    echo -e "${RED}[AVISO] Arquivo cnpjs.txt não encontrado!${NC}"
    echo ""
    echo "Criando arquivo de exemplo..."
    echo "# Adicione seus CNPJs aqui (um por linha)" > cnpjs.txt
    echo ""
    echo "Por favor:"
    echo "  1. Edite o arquivo cnpjs.txt"
    echo "  2. Adicione seus CNPJs (um por linha)"
    echo "  3. Execute este script novamente"
    echo ""
    exit 1
fi

# Executar processador
echo ""
echo "Iniciando processamento..."
echo ""
python3 PROCESSAR_CNPJS.py

echo ""
