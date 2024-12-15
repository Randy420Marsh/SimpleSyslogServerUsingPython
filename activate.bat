@echo off

SET current_path=%CD%

cd %current_path%

setlocal enabledelayedexpansion

REM Not needed
REM set python="C:\\Users\\%USERPROFILE%\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"
REM set python3="C:\\Users\\%USERPROFILE%\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"

REM set "PATH=%VIRTUAL_ENV%\Scripts;C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.42.34433\bin\Hostx64\x64;%PATH%"
REM Not needed

IF exist ./venv (cmd /k call .\venv\scripts\activate.bat)  ELSE (cmd /k python -m venv venv && cmd /k call .\venv\scripts\activate.bat)
