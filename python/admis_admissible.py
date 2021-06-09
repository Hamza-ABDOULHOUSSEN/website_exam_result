import pandas as pd
from main import *


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


for i in range(len(fichiers_admis_only)):
    file_admis = dirPath+fichiers_admis_only[i]
    file_admissible = dirPath+fichiers_admissible_only[i]
    print( admis_admissible(file_admis, file_admissible))

print("Tous les admis sont admissible")
