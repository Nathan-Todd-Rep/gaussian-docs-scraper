@echo off
title Gaussian / Bioinformatics Docs Scraper

rem Always run from this file's own folder, no matter how it was launched.
cd /d "%~dp0"

echo ============================================
echo   Gaussian / Bioinformatics Docs Scraper
echo ============================================
echo.

rem --- Find a working Python command: try "py" first, then "python". ---
set PYTHON_CMD=

py --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=py
    goto :python_found
)

python --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=python
    goto :python_found
)

echo Python was not found on this computer.
echo.
echo Before this tool can run, Python needs to be installed:
echo   1. Go to https://www.python.org/downloads/
echo   2. Download and run the installer.
echo   3. IMPORTANT: on the first install screen, check the box
echo      that says "Add python.exe to PATH" before clicking Install.
echo   4. Once that finishes, double-click this file again.
echo.
pause
exit /b 1

:python_found
echo Found Python:
%PYTHON_CMD% --version
echo.

echo Installing required packages, this may take a minute the first time...
echo.
%PYTHON_CMD% -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo Something went wrong installing the required packages.
    echo Check your internet connection, then double-click this file to try again.
    echo.
    pause
    exit /b 1
)

echo.
echo Setup complete. Starting the scraper...
echo.
%PYTHON_CMD% scrape.py

if errorlevel 1 (
    echo.
    echo The scraper closed with an error.
    pause
)
