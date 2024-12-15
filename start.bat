@echo off
setlocal enabledelayedexpansion
set "PYTHON=python"
echo "Launching..."
cd %CD%
set "USER=%USERNAME%"
echo Current User = %USER%
call .\venv\scripts\activate.bat
echo "venv activated"
python --version
echo.
python -s syslogserver.py