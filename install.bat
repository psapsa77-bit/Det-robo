@echo off
echo ========================================
echo   INSTALADOR DO ROBO SIMPLES
echo ========================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado!
    echo.
    echo Por favor, instale o Python 3.7 ou superior:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANTE: Marque a opcao "Add Python to PATH" durante a instalacao!
    echo.
    pause
    exit /b 1
)

echo [OK] Python encontrado!
echo.

REM Verifica se Google Chrome está instalado
if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" (
    echo [OK] Google Chrome encontrado!
) else if exist "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" (
    echo [OK] Google Chrome encontrado!
) else (
    echo [AVISO] Google Chrome nao encontrado!
    echo O Chrome e necessario para o robo funcionar.
    echo Baixe em: https://www.google.com/chrome/
    echo.
)

echo.
echo Criando ambiente virtual...
python -m venv venv
if errorlevel 1 (
    echo [ERRO] Falha ao criar ambiente virtual!
    pause
    exit /b 1
)

echo [OK] Ambiente virtual criado!
echo.

echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo Instalando dependencias...
echo.
pip install --upgrade pip
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo [ERRO] Falha ao instalar dependencias!
    pause
    exit /b 1
)

echo.
echo ========================================
echo   INSTALACAO CONCLUIDA COM SUCESSO!
echo ========================================
echo.
echo Para iniciar o robo, execute: run.bat
echo.
pause
