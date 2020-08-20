# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
hidden_imports_mn = ['classes.ScreenShooter']
hidden_imports_ss = ['os', 'sys', 'keyboard', 'datetime', 'PIL.ImageGrab']

mn_a = Analysis(['main.py'],
             pathex=['C:\\pydir\\project\\py-screen-shooter'],
             binaries=[],
             datas=[],
             hiddenimports=hidden_imports_mn,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

mn_pyz = PYZ(mn_a.pure, mn_a.zipped_data,
             cipher=block_cipher)

mn_exe = EXE(mn_pyz,
          mn_a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )

mn_coll = COLLECT(mn_exe,
               mn_a.binaries,
               mn_a.zipfiles,
               mn_a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')

ss_a = Analysis(['ScreenShooter.py'],
             pathex=['C:\\pydir\\project\\py-screen-shooter\\classes'],
             binaries=[],
             datas=[],
             hiddenimports=hidden_imports_ss,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

ss_pyz = PYZ(ss_a.pure, ss_a.zipped_data,
             cipher=block_cipher)

ss_exe = EXE(ss_pyz,
          ss_a.scripts,
          [],
          exclude_binaries=True,
          name='ScreenShooter',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )

ss_coll = COLLECT(ss_exe,
               ss_a.binaries,
               ss_a.zipfiles,
               ss_a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='ScreenShooter')

MERGE((mn_a, 'mn', 'mn'), (ss_a, 'ss', 'ss'))
