@echo off
for /r %%F in (*.ui) do (
  python -m PyQt5.uic.pyuic "%%F" -o "%%~dpnF.py"
)
@REM for /r %%F in (*.qrc) do (
@REM   pyside6-rcc "%%F" | sed "0,/PySide6/s//PyQt6/" > "%%~dpnF.py"
@REM )