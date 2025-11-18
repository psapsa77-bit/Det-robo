@echo off
title DET Robot - Sistema de Automacao
color 0B

echo.
echo ===============================================
echo    DET ROBOT - INICIANDO SISTEMA
echo ===============================================
echo    Versao: 1.0.0
echo    Porta: 5000
echo ===============================================
echo.

REM Verificar se ambiente virtual existe
if not exist "venv\Scripts\activate.bat" (
    echo [ERRO] Ambiente virtual nao encontrado!
    echo.
    echo Execute primeiro: INSTALAR_WINDOWS.bat
    echo.
    pause
    exit /b 1
)

REM Ativar ambiente virtual
echo [1/3] Ativando ambiente virtual...
call venv\Scripts\activate.bat
echo [OK] Ambiente ativado
echo.

REM Verificar se porta 5000 esta disponivel
echo [2/3] Verificando disponibilidade da porta...
netstat -ano | find ":5000" >nul
if %errorlevel% == 0 (
    echo [AVISO] Porta 5000 ja esta em uso!
    echo.
    echo Possivel causa: DET Robot ja esta rodando
    echo.
    echo Deseja continuar mesmo assim? (S/N)
    choice /C SN /N /M "Sua escolha: "
    if errorlevel 2 exit /b 1
)
echo.

REM Iniciar servidor
echo [3/3] Iniciando DET Robot...
echo.
echo ===============================================
echo    SISTEMA INICIADO COM SUCESSO!
echo ===============================================
echo.
echo   Interface Web: http://localhost:5000
echo.
echo   Comandos:
echo     - Pressione Ctrl+C para parar
echo     - Feche esta janela para encerrar
echo.
echo   Documentacao: docs\COMO_USAR.md
echo.
echo ===============================================
echo.

REM Aguardar 3 segundos e abrir navegador
timeout /t 3 /nobreak >nul
start http://localhost:5000

REM Iniciar Flask
python app.py

REM Se chegou aqui, houve erro ou usuario parou
echo.
echo Sistema encerrado.
pause
