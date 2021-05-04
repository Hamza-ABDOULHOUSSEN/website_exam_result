import os
import pandas as pd

dirPath = "../data/public/"

All1 = os.listdir(dirPath)

# on retire les fichiers cachés
All = []
for a in All1:
    if a[0] != '.':
        All.append(a)
All.sort()

##### Cas à traiter :
# les fichiers csv
# les fichiers "Classes..." et "Inscription.xlsx"

with open("files.txt", "w",encoding="utf-8") as f:
   for file in All:
       
        f.write('#####\t'+file+' : \n')

       #lecture et ecriture des colonnes du fichier

        if file[-3:] == "csv":
            src = pd.read_csv(dirPath+file, sep =';')
            col = src.columns
            for c in col:
                f.write(c+'\n')

        elif file == "Inscription.xlsx" or file[:7] == "Classes":
            src = pd.read_excel(dirPath+file, skiprows=1)
            col = src.columns
            for c in col:
                f.write(c+'\n')

        else:
            src = pd.read_excel(dirPath+file)
            col = src.columns
            for c in col:
                f.write(c+'\n')

        f.write('\n')

