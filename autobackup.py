import sys
import shutil
import os

file=str(sys.argv[1])
n=0
check=0
file=os.path.basename(file)
bkpdir="./backup"
if not os.path.exists(bkpdir):
    os.mkdir('backup')

path="./backup/"+file+".bkp"
if os.path.isfile(path):
    n=n+1
else:
    shutil.copy(file,path)
    check=1
while check==0:
    path="./backup/"+file+".bkp"+str(n)
    if os.path.isfile(path):
        n=n+1
    else:
        shutil.copy(file,path)
        check=1        
    
