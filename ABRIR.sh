#!/bin/bash

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "==============================================="
echo "   DET ROBOT - INICIANDO SISTEMA"
echo "==============================================="
echo "   Versão: 1.0.0"
echo "   Porta: 5000"
echo "==============================================="
echo -e "${NC}"

# Verificar se ambiente virtual existe
if [ ! -f "venv/bin/activate" ]; then
    echo -e "${RED}[ERRO] Ambiente virtual não encontrado!${NC}"
    echo ""
    echo "Execute primeiro: bash INSTALAR_LINUX.sh"
    echo ""
    exit 1
fi

# Ativar ambiente virtual
echo -e "${BLUE}[1/3] Ativando ambiente virtual...${NC}"
source venv/bin/activate

if [ $? -ne 0 ]; then
    echo -e "${RED}[ERRO] Falha ao ativar ambiente virtual!${NC}"
    exit 1
fi
echo -e "${GREEN}[OK] Ambiente ativado${NC}"
echo ""

# Verificar se porta 5000 está disponível
echo -e "${BLUE}[2/3] Verificando disponibilidade da porta...${NC}"
if lsof -Pi :5000 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo -e "${YELLOW}[AVISO] Porta 5000 já está em uso!${NC}"
    echo ""
    echo "Possível causa: DET Robot já está rodando"
    echo ""
    read -p "Deseja continuar mesmo assim? (s/N): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Ss]$ ]]; then
        exit 1
    fi
fi
echo ""

# Iniciar servidor
echo -e "${BLUE}[3/3] Iniciando DET Robot...${NC}"
echo ""
echo -e "${GREEN}"
echo "==============================================="
echo "   SISTEMA INICIADO COM SUCESSO!"
echo "==============================================="
echo -e "${NC}"
echo ""
echo "  Interface Web: ${GREEN}http://localhost:5000${NC}"
echo ""
echo "  Comandos:"
echo "    - Pressione Ctrl+C para parar"
echo "    - Feche o terminal para encerrar"
echo ""
echo "  Documentação: docs/COMO_USAR.md"
echo ""
echo "==============================================="
echo ""

# Aguardar 2 segundos e abrir navegador
sleep 2

# Tentar abrir navegador automaticamente
if command -v xdg-open &> /dev/null; then
    xdg-open http://localhost:5000 &> /dev/null &
elif command -v open &> /dev/null; then
    open http://localhost:5000 &> /dev/null &
fi

# Iniciar Flask
python3 app.py

# Se chegou aqui, houve erro ou usuário parou
echo ""
echo "Sistema encerrado."
