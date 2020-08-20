from classes.ScreenShooter import ScreenShooter

# pyinstaller -F c:\pydir\project\py-screen-shooter\main.py --hiddenimport=sg --name=screenshooter
# pyinstaller -F main.py --hiddenimport=sg --name=screenshooter --icon=assets/icon.ico

shooter = ScreenShooter()
shooter.run()
