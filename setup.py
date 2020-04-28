#https://fernandofreitasalves.com/how-to-create-python-exe-with-msi-installer-and-cx_freeze/
# pentru msi rulezi python setup.py bdist_msi


from cx_Freeze import setup, Executable
import os
import sys

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

exe = [Executable("main.py", base=base, icon='Dapino.ico')]

os.environ['TCL_LIBRARY'] = r'C:\\Users\\dm\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\\Users\\dm\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tk8.6'

options = {
'build_exe': {
    'include_files': ['alarm-clock.png','cross-script.png','tick-circle.png','timer.ui'],
    'packages': ['pyqt5']
}
}

setup(name="ShutDown Software", version="1.0", description='To be added',
  options=options, executables=exe)