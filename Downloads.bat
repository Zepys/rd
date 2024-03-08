@echo off
curl -s -L -o setup.py https://gitlab.com/chamod12/lm_win-10_github_rdp/-/raw/main/setup.py
curl -s -L -o show.bat https://gitlab.com/chamod12/lm_win-10_github_rdp/-/raw/main/show.bat
certutil -urlcache -split -f "https://www.litemanager.com/soft/pro/ROMServer.exe"
pip install pyautogui --quiet
REM curl -s -L -o C:\Users\Public\Desktop\Telegram.exe https://telegram.org/dl/desktop/win64
REM curl -s -L -o C:\Users\Public\Desktop\Winrar.exe https://www.rarlab.com/rar/winrar-x64-621.exe
REM powershell -Command "Invoke-WebRequest 'https://github.com/chieunhatnang/VM-QuickConfig/releases/download/1.6.1/VMQuickConfig.exe' -OutFile 'C:\Users\Public\Desktop\VMQuickConfig.exe'"
REM C:\Users\Public\Desktop\Telegram.exe /VERYSILENT /NORESTART
REM del C:\Users\Public\Desktop\Telegram.exe
REM C:\Users\Public\Desktop\Winrar.exe /S
REM del C:\Users\Public\Desktop\Winrar.exe
REM del /f "C:\Users\Public\Desktop\Epic Games Launcher.lnk"
REM del /f "C:\Users\Public\Desktop\Unity Hub.lnk"
REM net user runneradmin TheDisa1a
REM python -c "import pyautogui as pag; pag.click(897, 64, duration=2)"

REM start "" /MAX "C:\Users\Public\Desktop\VMQuickConfig"
REM python -c "import pyautogui as pag; pag.click(147, 489, duration=2)"
REm python -c "import pyautogui as pag; pag.click(156, 552, duration=2)"
REM python -c "import pyautogui as pag; pag.click(587, 14, duration=2)"

start "" "ROMServer.exe"
python setup.py