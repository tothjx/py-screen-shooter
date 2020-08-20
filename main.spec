from PyInstaller.utils.hooks import collect_submodules

hiddenimports_os = collect_submodules('os')
hiddenimports_sys = collect_submodules('sys')
hiddenimports_keyboard = collect_submodules('keyboard')
hiddenimports_datetime = collect_submodules('datetime')
hiddenimports_ImageGrab = collect_submodules('ImageGrab')
hiddenimports_ScreenShooter = collect_submodules('classes.ScreenShooter')

all_hidden_imports = hiddenimports_os + hiddenimports_sys + hiddenimports_keyboard + hiddenimports_datetime + hiddenimports_ImageGrab + hiddenimports_ScreenShooter

a = Analysis(['main.py'],
     pathex=['C:\\pydir\\project\\py-screen-shooter'],
     binaries=[],
     datas=[],
     hiddenimports=all_hidden_imports,
     hookspath=[],
     runtime_hooks=[],
     excludes=[],
     win_no_prefer_redirects=False,
     win_private_assemblies=False,
     cipher=None,
     noarchive=False)
