import tkinter as tk
from tkinter import filedialog as fd
import glob, os

root = tk.Tk()
root.withdraw()

def readSourceFile(): # Func to read Source Folder.

    global SourcePath
    SourcePath = fd.askdirectory()
    os.chdir(SourcePath)

    extension = 'mp4'  # Setting extension for mp4 files.
    global Videos
    Videos = glob.glob('*.{}'.format(extension)) # List of mp4 Files.

readSourceFile()

print(Videos)