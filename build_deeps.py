import os
import ctypes
import shutil
import subprocess

if not ctypes.windll.shell32.IsUserAnAdmin():
    print('Not enough priviledge, restart as admin...')
    exit()
else:
    print('Elevated privilege acquired')

subprocess.run(['git', 'clone', 'https://github.com/Microsoft/vcpkg.git'], shell=True, check=True)

os.chdir('vcpkg')
subprocess.run(['bootstrap-vcpkg.bat'], shell=True, check=True)

subprocess.run(['vcpkg', 'install', 'wxwidgets:x64-windows-static'], shell=True, check=True)