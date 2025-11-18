@echo off
title DET Robot - Instalador
color 0B

echo.
echo ===============================================
echo    DET ROBOT - INSTALADOR PROFISSIONAL
echo ===============================================
echo    Versao: 1.0.0
echo    Sistema: Windows
echo ===============================================
echo.

REM Verificacao de privilegios administrativos
net session >nul 2>&1
if %errorLevel% == 0 (
    echo [OK] Executando com privilegios de administrador
) else (
    echo [INFO] Executando sem privilegios de administrador
)
echo.

REM Verificar Python
echo [1/6] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado!
    echo.
    echo Por favor, instale Python 3.7 ou superior:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANTE: Marque "Add Python to PATH" durante instalacao!
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [OK] Python %PYTHON_VERSION% encontrado
echo.

REM Verificar Google Chrome
echo [2/6] Verificando Google Chrome...
if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" (
    echo [OK] Google Chrome encontrado
) else if exist "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" (
    echo [OK] Google Chrome encontrado
) else (
    echo [AVISO] Google Chrome nao encontrado!
    echo.
    echo O Chrome e NECESSARIO para o DET Robot funcionar.
    echo Baixe em: https://www.google.com/chrome/
    echo.
    echo Deseja continuar mesmo assim? (S/N)
    choice /C SN /N /M "Sua escolha: "
    if errorlevel 2 exit /b 1
)
echo.

REM Limpar instalacao anterior
echo [3/6] Limpando instalacao anterior...
if exist "venv" (
    echo Removendo ambiente virtual antigo...
    rmdir /s /q venv 2>nul
)
echo [OK] Limpeza concluida
echo.

REM Criar ambiente virtual
echo [4/6] Criando ambiente virtual...
python -m venv venv
if errorlevel 1 (
    echo [ERRO] Falha ao criar ambiente virtual!
    echo.
    echo Possivel solucao:
    echo   pip install --upgrade pip
    echo   pip install virtualenv
    echo.
    pause
    exit /b 1
)
echo [OK] Ambiente virtual criado
echo.

REM Ativar ambiente virtual
echo [5/6] Ativando ambiente virtual...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERRO] Falha ao ativar ambiente virtual!
    pause
    exit /b 1
)
echo [OK] Ambiente virtual ativado
echo.

REM Instalar dependencias
echo [6/6] Instalando dependencias...
echo.
echo Atualizando pip...
python -m pip install --upgrade pip

echo.
echo Instalando pacotes necessarios...
echo   - Flask (servidor web)
echo   - Selenium (automacao)
echo   - Outras dependencias...
echo.

REM Tenta instalar do requirements.txt com output verbose
echo Executando: pip install -r requirements.txt
echo.
pip install -r requirements.txt -v

if errorlevel 1 (
    echo.
    echo [ERRO] Falha ao instalar dependencias do requirements.txt!
    echo.
    echo Tentando instalacao individual com versoes flexiveis...
    echo.

    pip install "flask>=3.0.0" -v
    set FLASK_STATUS=%errorlevel%

    pip install "selenium>=4.15.0" -v
    set SELENIUM_STATUS=%errorlevel%

    if %FLASK_STATUS% neq 0 (
        echo.
        echo [ERRO] Falha ao instalar Flask!
        echo.
        echo Detalhes do erro acima. Possiveis solucoes:
        echo   1. Verifique sua conexao com a internet
        echo   2. Execute: pip install --upgrade pip setuptools wheel
        echo   3. Tente instalar manualmente: pip install flask selenium
        echo.
        pause
        exit /b 1
    )

    if %SELENIUM_STATUS% neq 0 (
        echo.
        echo [ERRO] Falha ao instalar Selenium!
        echo.
        echo Detalhes do erro acima. Possiveis solucoes:
        echo   1. Verifique sua conexao com a internet
        echo   2. Execute: pip install --upgrade pip setuptools wheel
        echo   3. Tente instalar manualmente: pip install flask selenium
        echo.
        pause
        exit /b 1
    )
)

echo.
echo [OK] Todas as dependencias instaladas
echo.

REM Criar diretorios necessarios
echo Criando estrutura de diretorios...
if not exist "exports" mkdir exports
if not exist "logs" mkdir logs
if not exist "screenshots" mkdir screenshots
echo [OK] Diretorios criados
echo.

REM Sucesso
echo ===============================================
echo    INSTALACAO CONCLUIDA COM SUCESSO!
echo ===============================================
echo.
echo Proximos passos:
echo   1. Execute: ABRIR.bat
echo   2. Acesse: http://localhost:5000
echo   3. Consulte: docs\COMO_USAR.md
echo.
echo ===============================================
echo.

pause
