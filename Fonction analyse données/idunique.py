import pandas as pd
import numpy as np

fichiers = ['ADMISSIBLE_ATS.xlsx', 'ADMISSIBLE_PC.xlsx', 'ADMISSIBLE_PT.xlsx', 'ADMIS_MP-SPE.xlsx', 'ADMIS_PSI-SPE.xlsx', 'ADMIS_TSI-SPE.xlsx', 'ADMISSIBLE_MP-SPE.xlsx', 'ADMISSIBLE_PSI-SPE.xlsx', 'ADMISSIBLE_TSI-SPE.xlsx', 'ADMIS_MP.xlsx', 'ADMIS_PSI.xlsx', 'ADMIS_TSI.xlsx', 'ADMISSIBLE_MP.xlsx', 'ADMISSIBLE_PSI.xlsx', 'ADMISSIBLE_TSI.xlsx', 'ADMIS_PC-SPE.xlsx', 'ADMIS_PT-SPE.xlsx', 'ADMISSIBLE_PC-SPE.xlsx', 'ADMISSIBLE_PT-SPE.xlsx', 'ADMIS_ATS.xlsx', 'ADMIS_PC.xlsx', 'ADMIS_PT.xlsx']

def uniq(file):

    ### lire le fichier excel
    df = pd.read_excel(file)
    ### On ne garde que la colonne des id
    df.drop( df.columns[1:] , axis=1)

    parc = []
    n = len(df['Can _cod'])
    
    for i in range(n):
        cod = df['Can _cod'][i]

        if cod in parc:
            return False
        else:
            parc.append(cod)
    
    return True

for file in fichiers:
    print( uniq(file) )
