@echo off
set DOWNLOAD_DIR=%USERPROFILE%\Downloads
start /b firefox  "file://%DOWNLOAD_DIR%\zenoprint.html" 
setlocal

:: Define the path to the PowerShell script
set "PSScriptPath=%DOWNLOAD_DIR%\zeno-html-video-create.ps1"

:: Run the PowerShell script
powershell -ExecutionPolicy Bypass -File "%PSScriptPath%"

endlocal
