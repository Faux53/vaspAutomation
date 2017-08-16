import glob, os, shutil, re

os.system('phonopy diamond.conf -d')

folder = '/Users/andrewadams/Desktop/vasp/dir'

#uses glob to find a sequence pattern
for find in glob.glob(os.path.join(folder, '*.*')):
    #splits the string from file names, removes the extra stuff so we can give the new directory a different name, look at folder and how many characters it has then add that number with 8 and replace 43 with it.
    sequence = find.rsplit('.', 1)[0][43:]
    #adds the name required
    dispadd = 'disp-' + sequence
    #joins the new named sequence with the folder
    joiner = (os.path.join(folder, dispadd))
    #this is just so that it doesnt error when it sees something that isnt the glob pattern
    try:
        os.mkdir(joiner)
    except OSError:
        pass
    #moves the poscar in the new paths
    shutil.move(find, os.path.join(joiner, os.path.basename(find)))

os.chdir('/Users/andrewadams/Desktop/vasp/dir')

os.system('for d in */; do cp POTCAR "$d"; done; ')

os.system('for d in */; do cp KPOINTS "$d"; done; ')

os.system('for d in */; do cp INCAR "$d"; done; ')

os.system('phonopy -f disp-001/vasprun.xml disp-002/vasprun.xml')

os.system('phonopy -p --factor=64.6528 band.conf')

#beer
