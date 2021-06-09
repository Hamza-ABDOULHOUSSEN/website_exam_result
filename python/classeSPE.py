import pandas as pd
from main import dirPath, fichiers_admis_normal, fichiers_admis_spe, fichiers_admissible_normal, fichiers_admissible_spe


def include(filespe, file):

    ### lecture du fichier excel
    df = pd.read_excel(file)
    dfspe = pd.read_excel(filespe)

    n = len(df['Can _cod'])
    values = dfspe['Can _cod'].values   # liste des id des candidats admis en spe

    for i in range(n):
        cod = df['Can _cod'][i]

        if not(cod in values):
            return "Il y a un candidat de classe normale qui n'est pas en classe spé"
    
    return "Tous les candidats de classes normales sont en classe spé"

nadmis = len(fichiers_admis_spe)
nadmissible = len(fichiers_admissible_spe)

print("Fichier ADMIS")
for i in range(0,nadmis):
    print( include(dirPath+fichiers_admis_spe[i], dirPath+fichiers_admis_normal[i+1]) ) #decalage car il y a les ATS en normal mais pas en spe

print("")
print("Fichier ADMISSIBLE")
for i in range(0,nadmissible):
    print( include(dirPath+fichiers_admissible_spe[i], dirPath+fichiers_admissible_normal[i+1]) )


    