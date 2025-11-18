#!/bin/bash

echo "========================================"
echo "  ROBÔ SIMPLES - INICIANDO..."
echo "========================================"
echo ""

# Verifica se o ambiente virtual existe
if [ ! -f "venv/bin/activate" ]; then
    echo "[ERRO] Ambiente virtual não encontrado!"
    echo ""
    echo "Execute o arquivo install.sh primeiro para instalar o robô:"
    echo "  bash install.sh"
    echo ""
    exit 1
fi

echo "Ativando ambiente virtual..."
source venv/bin/activate

echo ""
echo "========================================"
echo "  ROBÔ INICIADO!"
echo "========================================"
echo ""
echo "Acesse no navegador: http://localhost:5000"
echo ""
echo "Pressione Ctrl+C para parar o robô"
echo ""
echo "========================================"
echo ""

# Aguarda 2 segundos
sleep 2

# Tenta abrir o navegador automaticamente
if command -v xdg-open &> /dev/null; then
    xdg-open http://localhost:5000 &> /dev/null &
elif command -v open &> /dev/null; then
    open http://localhost:5000 &> /dev/null &
fi

# Inicia o servidor Flask
python3 app.py
