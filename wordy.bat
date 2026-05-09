@echo off
setlocal EnableExtensions EnableDelayedExpansion
cd /d "%~dp0"

set "VENV=.venv"
set "PYTHON=%VENV%\Scripts\python.exe"

if not exist "%PYTHON%" (
    echo Criando ambiente virtual...
    py -3 -m venv "%VENV%"
    if errorlevel 1 (
        echo Falha ao criar o ambiente virtual.
        exit /b 1
    )
)

echo Verificando dependencias instaladas...
for /f "usebackq delims=" %%A in (`"%PYTHON%" -c "import re, pathlib, importlib.metadata as md; t = pathlib.Path('requirements.txt').read_text(encoding='utf-16'); reqs = []; installed = {d.metadata['Name'].lower().replace('_','-') for d in md.distributions()}; [reqs.append(re.split(r'\s*(?:==|>=|<=|~=|!=|>|<|===)\s*', re.split(r'\s*;\s*', raw.split('#',1)[0].strip(), 1)[0].split(' @ ',1)[0].strip(), 1)[0].strip().lower().replace('_','-')) for raw in t.splitlines() if raw.split('#',1)[0].strip()]; print('OK' if all(r in installed for r in reqs) else 'MISSING')"`) do set "REQ_STATUS=%%A"

if /I "!REQ_STATUS!"=="MISSING" (
    echo Instalando dependencias faltantes...
    "%PYTHON%" -m pip install -r "requirements.txt"
    if errorlevel 1 (
        echo Falha ao instalar as dependencias.
        exit /b 1
    )
) else (
    echo Todas as dependencias ja estao instaladas.
)

echo Executando main.py...
"%PYTHON%" "main.py"
if errorlevel 1 (
    echo Falha ao executar o main.py.
)

powershell.exe -NoExit -Command "Write-Host 'Processo finalizado. Pressione Enter para fechar esta janela.'"
endlocal