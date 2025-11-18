@echo off
title DET Robot - Instalador Simples

echo ===================================
echo DET ROBOT - INSTALADOR SIMPLES
echo ===================================
echo.

REM Verificar Python
echo Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python nao encontrado!
    pause
    exit /b 1
)
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo OK: Python %PYTHON_VERSION%
echo.

REM Criar ambiente virtual
echo Criando ambiente virtual...
if exist "venv" rmdir /s /q venv 2>nul
python -m venv venv
echo OK
echo.

REM Ativar ambiente virtual
echo Ativando ambiente virtual...
call venv\Scripts\activate.bat
echo OK
echo.

REM Atualizar pip
echo Atualizando pip...
python -m pip install --upgrade pip --quiet
echo OK
echo.

REM Instalar dependencias
echo Instalando Flask e Selenium...
pip install "flask>=3.0.0" "selenium>=4.15.0" --quiet

if errorlevel 1 (
    echo Tentando com output detalhado...
    pip install "flask>=3.0.0" "selenium>=4.15.0"

    if errorlevel 1 (
        echo ERRO: Falha na instalacao!
        echo.
        echo Tente manualmente:
        echo   venv\Scripts\activate.bat
        echo   pip install flask selenium
        pause
        exit /b 1
    )
) else (
    echo OK: Pacotes instalados com sucesso!
)
echo.

REM Criar diretorios
echo Criando diretorios...
if not exist "exports" mkdir exports
if not exist "logs" mkdir logs
if not exist "screenshots" mkdir screenshots
echo OK
echo.

REM Testar importacoes
echo Testando instalacao...
python -c "import flask; import selenium; from det_robot import DETConfig; print('Tudo OK!')" 2>nul

if errorlevel 1 (
    echo AVISO: Modulos instalados mas pode haver problemas
    echo Execute: VERIFICAR.bat para mais detalhes
    echo.
) else (
    echo.
    echo ===================================
    echo INSTALACAO CONCLUIDA!
    echo ===================================
    echo.
    echo Para iniciar: ABRIR.bat
    echo.
)

pause
