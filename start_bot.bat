@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=5539847661:AAEEc7xmrLHxYyhT16KSipkraj_2wtfAsM4

python bot_telegram.py

pause