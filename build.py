import os
import ctypes
import shutil
import subprocess

if not ctypes.windll.shell32.IsUserAnAdmin():
    print('Not enough priviledge, restart as admin...')
    exit()
else:
    print('Elevated privilege acquired')

subprocess.run([
    'cmake', '-G', 'Visual Studio 17 2022', '-A', 'x64',
    '-DCMAKE_TOOLCHAIN_FILE=./vcpkg/scripts/buildsystems/vcpkg.cmake',
    '-DVCPKG_TARGET_TRIPLET=x64-windows-static',
    '-S', '.', '-B', 'build-x64'
    ], shell=True, check=True)


subprocess.run([
    'cmake', '--build', 'build-x64',
    '--config', 'Release'
    ], shell=True, check=True)