@echo off
title DET Robot - Processador de CNPJs
color 0B

echo.
echo ============================================================
echo    DET ROBOT - PROCESSADOR AUTOMATIZADO DE CNPJs
echo ============================================================
echo.
echo Este script ira processar todos os CNPJs do arquivo cnpjs.txt
echo.

REM Verificar se ambiente virtual existe
if not exist "venv" (
    echo [ERRO] Ambiente virtual nao encontrado!
    echo.
    echo Por favor, execute INSTALAR_WINDOWS.bat primeiro
    echo.
    pause
    exit /b 1
)

REM Ativar ambiente virtual
call venv\Scripts\activate.bat

REM Verificar se arquivo cnpjs.txt existe
if not exist "cnpjs.txt" (
    echo [AVISO] Arquivo cnpjs.txt nao encontrado!
    echo.
    echo Criando arquivo de exemplo...
    echo # Adicione seus CNPJs aqui (um por linha^) > cnpjs.txt
    echo.
    echo Por favor:
    echo   1. Edite o arquivo cnpjs.txt
    echo   2. Adicione seus CNPJs (um por linha^)
    echo   3. Execute este script novamente
    echo.
    pause
    exit /b 1
)

REM Executar processador
echo.
echo Iniciando processamento...
echo.
python PROCESSAR_CNPJS.py

echo.
pause
