#!/bin/bash

# Instalador Simplificado DET Robot
# Para ambientes onde você quer pular verificações

echo "==================================="
echo "DET ROBOT - INSTALADOR SIMPLES"
echo "==================================="
echo ""

# Verificar Python
echo "Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "ERRO: Python3 não encontrado!"
    exit 1
fi
echo "OK: $(python3 --version)"
echo ""

# Criar ambiente virtual
echo "Criando ambiente virtual..."
rm -rf venv 2>/dev/null
python3 -m venv venv
echo "OK"
echo ""

# Ativar ambiente virtual
echo "Ativando ambiente virtual..."
source venv/bin/activate
echo "OK"
echo ""

# Atualizar pip
echo "Atualizando pip..."
pip install --upgrade pip --quiet
echo "OK"
echo ""

# Instalar dependências
echo "Instalando Flask e Selenium..."
pip install "flask>=3.0.0" "selenium>=4.15.0" --quiet

if [ $? -eq 0 ]; then
    echo "OK: Pacotes instalados com sucesso!"
else
    echo "Tentando com output detalhado..."
    pip install "flask>=3.0.0" "selenium>=4.15.0"

    if [ $? -ne 0 ]; then
        echo "ERRO: Falha na instalação!"
        echo ""
        echo "Tente manualmente:"
        echo "  source venv/bin/activate"
        echo "  pip install flask selenium"
        exit 1
    fi
fi
echo ""

# Criar diretórios
echo "Criando diretórios..."
mkdir -p exports logs screenshots
chmod +x ABRIR.sh VERIFICAR.sh 2>/dev/null
echo "OK"
echo ""

# Testar importações
echo "Testando instalação..."
python -c "import flask; import selenium; from det_robot import DETConfig; print('Tudo OK!')" 2>/dev/null

if [ $? -eq 0 ]; then
    echo ""
    echo "==================================="
    echo "INSTALAÇÃO CONCLUÍDA!"
    echo "==================================="
    echo ""
    echo "Para iniciar: bash ABRIR.sh"
    echo ""
else
    echo "AVISO: Módulos instalados mas pode haver problemas"
    echo "Execute: bash VERIFICAR.sh para mais detalhes"
    echo ""
fi
