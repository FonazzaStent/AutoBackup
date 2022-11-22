"""AutoBackup 1.0.1 - An extremely simple automatic incremental file
backup program.
Copyright (C) 2022  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

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

