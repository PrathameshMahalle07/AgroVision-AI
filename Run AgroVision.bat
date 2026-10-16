@echo off
setlocal
cd /d "%~dp0"

where npm >nul 2>nul
if errorlevel 1 (
  echo Node.js and npm were not found. Install Node.js, then try again.
  pause
  exit /b 1
)

if not exist node_modules (
  echo Installing project dependencies for the first run...
  call npm install --legacy-peer-deps
  if errorlevel 1 (
    echo Dependency installation failed.
    pause
    exit /b 1
  )
)

start "" powershell.exe -NoProfile -Command "Start-Sleep -Seconds 5; Start-Process 'http://localhost:3000'"
call npm run dev
pause
