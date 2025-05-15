@echo off
setlocal

echo === INSTALLATION AUTOMATIQUE POUR WINDOWS ===

:: Répertoire temporaire
set "TEMP_DIR=%~dp0temp_installs"
mkdir "%TEMP_DIR%" >nul 2>&1

:: Téléchargement Python si non installé
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Téléchargement de Python...
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe -OutFile '%TEMP_DIR%\python.exe'"
    echo Installation de Python...
    "%TEMP_DIR%\python.exe" /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1
) else (
    echo [OK] Python déjà installé.
)

:: Redémarrer le terminal pour actualiser le PATH
set PATH=%PATH%;C:\Python311\Scripts\;C:\Python311\

:: pip install
where pip >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    python -m ensurepip --upgrade
)

:: Téléchargement de Git si nécessaire
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Téléchargement de Git...
    powershell -Command "Invoke-WebRequest -Uri https://github.com/git-for-windows/git/releases/download/v2.44.0.windows.1/Git-2.44.0-64-bit.exe -OutFile '%TEMP_DIR%\git.exe'"
    echo Installation de Git...
    "%TEMP_DIR%\git.exe" /SILENT
) else (
    echo [OK] Git déjà installé.
)

:: Téléchargement Node.js si nécessaire
where node >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Téléchargement de Node.js...
    powershell -Command "Invoke-WebRequest -Uri https://nodejs.org/dist/v20.12.2/node-v20.12.2-x64.msi -OutFile '%TEMP_DIR%\node.msi'"
    echo Installation de Node.js...
    msiexec /i "%TEMP_DIR%\node.msi" /qn
) else (
    echo [OK] Node.js déjà installé.
)

:: Installer Jupyter et ipykernel
echo Installation de Jupyter et ipykernel...
pip install --upgrade pip
pip install jupyter ipykernel

echo === INSTALLATION COMPLETE ===
pause
