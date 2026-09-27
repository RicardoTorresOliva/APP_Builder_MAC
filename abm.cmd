@echo off
rem Lanzador del CLI de ABM (Windows). En macOS/Linux usa ./abm
where py >nul 2>nul && (py -3 "%~dp0scripts\abm.py" %*) || (python "%~dp0scripts\abm.py" %*)
