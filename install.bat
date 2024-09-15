@echo off

:: Change directory to the location of the batch file
cd /d "%~dp0"

python src\setup.py

echo.
echo.
echo Setup complete! Check /sources for all the scripts you need to run in order to setup Slate for Windows

pause
