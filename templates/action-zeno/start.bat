@echo off
setlocal

:: Define the path to the PowerShell script
set "PSScriptPath=%CD%\zeno-html-video-create.ps1"

:: Run the PowerShell script
powershell -ExecutionPolicy Bypass -File "%PSScriptPath%"

endlocal
