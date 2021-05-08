import pandas as pd
from main import *

fichiers_admis = ['ADMIS_MP-SPE.xlsx', 'ADMIS_MP.xlsx', 'ADMIS_PC-SPE.xlsx', 'ADMIS_PC.xlsx', 'ADMIS_PSI-SPE.xlsx', 'ADMIS_PSI.xlsx', 'ADMIS_PT-SPE.xlsx', 'ADMIS_PT.xlsx', 'ADMIS_TSI-SPE.xlsx', 'ADMIS_TSI.xlsx']
fichiers_admissible = ['ADMISSIBLE_MP-SPE.xlsx', 'ADMISSIBLE_MP.xlsx', 'ADMISSIBLE_PC-SPE.xlsx', 'ADMISSIBLE_PC.xlsx', 'ADMISSIBLE_PSI-SPE.xlsx', 'ADMISSIBLE_PSI.xlsx', 'ADMISSIBLE_PT-SPE.xlsx', 'ADMISSIBLE_PT.xlsx', 'ADMISSIBLE_TSI-SPE.xlsx', 'ADMISSIBLE_TSI.xlsx']

def admis_admissible(file_admis, file_admissible):
    # lecture des fichiers excel
    admis = pd.read_excel(file_admis)
    admissible = pd.read_excel(file_admissible)


    candadmis = admis['Can _cod'].values    # liste des id des candidats admis
    candadmissible = admissible['Can _cod'].values  # liste des id des candidats admissible

    for cod in candadmis:
        if not(cod in candadmissible):
            return False

    if len(candadmis) == len(candadmissible):
        print("Tous les admissibles sont admis")
    
    return True


for i in range(len(fichiers_admis)):
    file_admis = dirPath+fichiers_admis[i]
    file_admissible = dirPath+fichiers_admissible[i]
    print( admis_admissible(file_admis, file_admissible))

print("Tous les admis sont admissible")
