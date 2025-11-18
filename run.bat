@echo off
echo ========================================
echo   ROBO SIMPLES - INICIANDO...
echo ========================================
echo.

REM Verifica se o ambiente virtual existe
if not exist "venv\Scripts\activate.bat" (
    echo [ERRO] Ambiente virtual nao encontrado!
    echo.
    echo Execute o arquivo install.bat primeiro para instalar o robo.
    echo.
    pause
    exit /b 1
)

echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo.
echo ========================================
echo   ROBO INICIADO!
echo ========================================
echo.
echo Acesse no navegador: http://localhost:5000
echo.
echo Pressione Ctrl+C para parar o robo
echo.
echo ========================================
echo.

REM Tenta abrir o navegador automaticamente
timeout /t 2 /nobreak >nul
start http://localhost:5000

REM Inicia o servidor Flask
python app.py

pause
