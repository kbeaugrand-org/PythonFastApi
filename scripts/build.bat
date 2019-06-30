@echo off

pyinstaller app-console.spec
pyinstaller app-service.spec

COPY .\scripts\install.bat .\dist\
COPY .\scripts\debug.bat .\dist\
COPY .\scripts\start.bat .\dist\
COPY .\scripts\remove.bat .\dist\