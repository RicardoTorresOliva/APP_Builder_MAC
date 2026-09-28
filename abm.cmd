@echo off
rem Lanzador del CLI de ABM (Windows). En macOS/Linux usa ./abm
set PYTHONUTF8=1
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 "%~dp0scripts\abm.py" %*
) else (
  python "%~dp0scripts\abm.py" %*
)
exit /b %errorlevel%
