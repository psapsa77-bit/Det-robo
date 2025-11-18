@echo off
title DET Robot - Verificacao de Instalacao
color 0B

echo.
echo ===============================================
echo    DET ROBOT - VERIFICACAO DE INSTALACAO
echo ===============================================
echo.

REM Verificar se venv existe
echo [1/5] Verificando ambiente virtual...
if exist "venv" (
    echo [OK] Ambiente virtual encontrado
) else (
    echo [ERRO] Ambiente virtual nao encontrado!
    echo Execute INSTALAR_WINDOWS.bat primeiro
    pause
    exit /b 1
)
echo.

REM Ativar venv
call venv\Scripts\activate.bat

REM Verificar Flask
echo [2/5] Verificando Flask...
python -c "import flask; print('Flask version:', flask.__version__)" 2>nul
if errorlevel 1 (
    echo [ERRO] Flask nao esta instalado!
    pause
    exit /b 1
) else (
    echo [OK] Flask instalado corretamente
)
echo.

REM Verificar Selenium
echo [3/5] Verificando Selenium...
python -c "import selenium; print('Selenium version:', selenium.__version__)" 2>nul
if errorlevel 1 (
    echo [ERRO] Selenium nao esta instalado!
    pause
    exit /b 1
) else (
    echo [OK] Selenium instalado corretamente
)
echo.

REM Verificar modulo det_robot
echo [4/5] Verificando modulo det_robot...
python -c "from det_robot import DETConfig, DETAutomation; print('Modulo det_robot OK')" 2>nul
if errorlevel 1 (
    echo [ERRO] Modulo det_robot nao esta acessivel!
    pause
    exit /b 1
) else (
    echo [OK] Modulo det_robot funcional
)
echo.

REM Listar todas as dependencias instaladas
echo [5/5] Listando todas as dependencias...
pip list | findstr /I "Flask selenium werkzeug jinja2"
echo.

REM Sucesso
echo ===============================================
echo    VERIFICACAO CONCLUIDA COM SUCESSO!
echo ===============================================
echo.
echo Tudo esta pronto! Execute: ABRIR.bat
echo.

pause
