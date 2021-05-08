import pandas as pd
from main import *


with open("files.txt", "w",encoding="utf-8") as f:

   for file in All:
       
        f.write('#####\t'+file+' : \n')

        # lecture du fichier
        src = lecture(file)

        #ecriture des colonnes du fichier
        col = src.columns
        for c in col:
            f.write(c+';\n')

        f.write('\n')
