# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['rdp_handler/main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='RDPURLHandler',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets/icons/icon.icns'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='RDPURLHandler',
)
app = BUNDLE(
    coll,
    name='RDPURLHandler.app',
    icon='assets/icons/icon.icns',
    bundle_identifier=None,
    info_plist={
         'CFBundleName': 'RDPURLHandler',
         'CFBundleDisplayName': 'RDPURLHandler',
         'CFBundleIdentifier': 'com.yourcompany.rdpurlhandler',
         'CFBundleVersion': '1.0.0',
         'CFBundleShortVersionString': '1.0.0',
         'CFBundleExecutable': 'RDPURLHandler',
         'CFBundlePackageType': 'APPL',
         'CFBundleIconFile': 'icon.icns',
         'CFBundleURLTypes': [
             {
                 'CFBundleURLName': 'RDPURLHandler',
                 'CFBundleURLSchemes': ['rdp']
             }
         ],
         'NSHighResolutionCapable': True,
     })
