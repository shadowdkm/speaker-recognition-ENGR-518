# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['demo.py'],
    pathex=[],
    binaries=[],
    datas=[('subject1.weight150.npy', '.'), ('subject2.weight150.npy', '.'), ('subject3.weight150.npy', '.'), ('1.bmp', '.'), ('2.bmp', '.'), ('3.bmp', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Speaker Reg Demo V0.1',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
