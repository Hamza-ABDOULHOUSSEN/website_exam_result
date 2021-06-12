import pandas as pd
from main import fichiers_Classes_xlsx, dirPath

classes = fichiers_Classes_xlsx

def bonif(file):
    ### lecture du fichier excel
    cl = pd.read_excel(file, skiprows=1)

    bon_ecrit = cl['bonification_ecrit'].values    # liste des bonification ecrite dans l'ordre de la colonne
    bon_oral = cl['bonification_oral'].values   # liste des bonification orale dans l'ordre de la colonne

    for i in range(len(bon_ecrit)):
        if bon_ecrit[i] != bon_oral[i]:
            return False
    
    return True

for file in classes:
    print(bonif(dirPath+file))

print("Les bonifications ecrites et orales sont les mêmes")
