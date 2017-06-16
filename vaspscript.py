import os
import shutil

os.system('mkdir testingenv')

os.system('phonopy diamond.conf -d')

source = os.listdir('/Users/andrewadams/desktop/vasp')
destination = 'testingenv'
for files in source:
    if files.startswith('POSCAR'):
        shutil.move(source, destination)

source = os.listdir('/Users/andrewadams/desktop/vasp')
destination = 'testingenv'
for files in source:
    if files('disp.yaml'):
        shutil.move(source, destination)

os.system('cd /Users/andrewadams/desktop/vasp')

os.system('phonopy -f disp-001/vasprun.xml disp-002/vasprun.xml')

os.system('phonopy -f disp-001/vasprun.xml disp-002/vasprun.xml')

