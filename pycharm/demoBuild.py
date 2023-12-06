import PyInstaller.__main__
import pathlib

import os


package_name="Speaker Reg Demo V0.1"

PyInstaller.__main__.run([
    '--clean',
    '--name=%s' % package_name,
    '--noconfirm',
    '--onefile',
    #'--windowed',
    '--console',
    #'--hidden-import=PyAudio',
    #'--icon=OMflexIcon.ico',
    #'--add-binary=libusb-1.64.dll;.',
    '--add-data=subject1.weight150.npy;.',
    '--add-data=subject2.weight150.npy;.',
    '--add-data=subject3.weight150.npy;.',
    '--add-data=1.bmp;.',
    '--add-data=2.bmp;.',
    '--add-data=3.bmp;.',
    'demo.py'
])