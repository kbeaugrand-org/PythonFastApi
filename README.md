# Windows Service in Python

## How To Build the service

```
 pyinstaller -F --hidden-import=win32timezone WindowsService.py
```

## How To install the service

```
.\dist\WindowsService.exe --startup auto install
```