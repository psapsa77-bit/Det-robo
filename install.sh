#!/bin/bash

echo "========================================"
echo "  INSTALADOR DO ROBÔ SIMPLES"
echo "========================================"
echo ""

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "[ERRO] Python3 não encontrado!"
    echo ""
    echo "Por favor, instale o Python 3.7 ou superior:"
    echo "  Ubuntu/Debian: sudo apt-get install python3 python3-pip python3-venv"
    echo "  Fedora: sudo dnf install python3 python3-pip"
    echo "  Mac: brew install python3"
    echo ""
    exit 1
fi

echo "[OK] Python3 encontrado!"
echo ""

# Verifica se Google Chrome está instalado
if command -v google-chrome &> /dev/null || command -v google-chrome-stable &> /dev/null || command -v chromium &> /dev/null || command -v chromium-browser &> /dev/null; then
    echo "[OK] Google Chrome/Chromium encontrado!"
else
    echo "[AVISO] Google Chrome não encontrado!"
    echo "O Chrome é necessário para o robô funcionar."
    echo "  Ubuntu/Debian: sudo apt-get install google-chrome-stable"
    echo "  Fedora: sudo dnf install google-chrome-stable"
    echo "  Mac: brew install --cask google-chrome"
    echo ""
fi

echo ""
echo "Criando ambiente virtual..."
python3 -m venv venv

if [ $? -ne 0 ]; then
    echo "[ERRO] Falha ao criar ambiente virtual!"
    exit 1
fi

echo "[OK] Ambiente virtual criado!"
echo ""

echo "Ativando ambiente virtual..."
source venv/bin/activate

echo "Instalando dependências..."
echo ""
pip install --upgrade pip
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "[ERRO] Falha ao instalar dependências!"
    exit 1
fi

echo ""
echo "========================================"
echo "  INSTALAÇÃO CONCLUÍDA COM SUCESSO!"
echo "========================================"
echo ""
echo "Para iniciar o robô, execute: ./run.sh"
echo "  (ou: bash run.sh)"
echo ""
