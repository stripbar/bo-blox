@echo off
:check_dependencies
REM Check if pygame and pyautogui are already installed
pip show pygame
if %errorlevel% neq 0 (
    echo pygame is not installed. Installing...
    REM Install pygame
    pip install pygame
) else (
    echo pygame is already installed.
)

pip show pyautogui
if %errorlevel% neq 0 (
    echo pyautogui is not installed. Installing...
    REM Install pyautogui
    pip install pyautogui
) else (
    echo pyautogui is already installed.
)

REM Run your Python script
:run_program
python main.py
goto run_program
