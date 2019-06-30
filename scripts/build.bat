pyinstaller -F --hidden-import=win32timezone --additional-hooks-dir .hooks main.py
pyinstaller -F --hidden-import=win32timezone service.py