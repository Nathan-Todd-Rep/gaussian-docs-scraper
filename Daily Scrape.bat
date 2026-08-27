@echo off
rem Unattended daily re-scrape, invoked by a Windows Task Scheduler entry
rem (not meant to be double-clicked interactively -- see Run Scraper.bat
rem for that). Re-scrapes the gaussian domain with --skip-summary (raw
rem passages only, no Ollama) and appends output to a log file so results
rem are auditable without needing to watch it run. Add more --config runs
rem below if/when other domains are ready for continuous re-scraping too.

rem Always run from this file's own folder, no matter how it was launched.
cd /d "%~dp0"

set PYTHON_CMD=
py --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=py
    goto :python_found
)
python --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=python
)

:python_found
if "%PYTHON_CMD%"=="" (
    echo [%date% %time%] Python not found on PATH -- skipping scheduled scrape. >> "%USERPROFILE%\.inkly\daily_scrape.log"
    exit /b 1
)

echo [%date% %time%] Starting daily scrape >> "%USERPROFILE%\.inkly\daily_scrape.log"

%PYTHON_CMD% scrape.py --config configs\gaussian.toml --skip-summary < NUL >> "%USERPROFILE%\.inkly\daily_scrape.log" 2>&1

echo [%date% %time%] Daily scrape finished >> "%USERPROFILE%\.inkly\daily_scrape.log"
