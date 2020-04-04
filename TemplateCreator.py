import csv
import tkinter as tk
from tkinter import filedialog, messagebox
import sys

app = tk.Tk()

app.withdraw()

INIFileTypes = [('Configure File', '.ini')]

csvFileTypes = [('Comma Separated Values File', '.csv')]

structString = ''

dataTable = []

entryCount = 0 

currentFile = filedialog.askopenfilename(parent=app, title='What file do you want to convert?', filetypes=csvFileTypes)

outputFile = filedialog.asksaveasfile(parent=app, title='Where do you wish to save the data file?', filetypes=INIFileTypes).name

with open(currentFile) as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    for row in reader:
        entryCount += 1
        structString += '[' + row[19] + '_' + row[18] + ']\n'
        dataTable.append(structString)
        structString = ''
with open(outputFile, mode='w') as iniFile:
    for x in dataTable:
        iniFile.write(x)
    iniFile.write('NoOfEntries=' + str(entryCount))
messagebox.showwarning('File Operation', 'File Completion Complete')
    
        
        
