import sys
import shutil
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

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
    messagebox.showinfo("Backup complete","A file named " + file+".bkp" + ' was created in the "backup" folder. Open the "backup" folder to retrieve it. Delete the .bkp extension to restore it.')
while check==0:
    path="./backup/"+file+".bkp"+str(n)
    if os.path.isfile(path):
        n=n+1
    else:
        shutil.copy(file,path)
        check=1
        messagebox.showinfo("Backup complete","A file named " + file+".bkp" + str(n) + ' was created in the "backup" folder. Open the "backup" folder to retrieve it. Delete the .bkp'+str(n)+ ' extension to restore it.')

