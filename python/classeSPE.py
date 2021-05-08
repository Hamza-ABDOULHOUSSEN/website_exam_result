import pandas as pd

dirPath = "../data/public/"
fichiers_admis = ['ADMIS_MP-SPE.xlsx', 'ADMIS_MP.xlsx', 'ADMIS_PC-SPE.xlsx', 'ADMIS_PC.xlsx', 'ADMIS_PSI-SPE.xlsx', 'ADMIS_PSI.xlsx', 'ADMIS_PT-SPE.xlsx', 'ADMIS_PT.xlsx', 'ADMIS_TSI-SPE.xlsx', 'ADMIS_TSI.xlsx']
fichiers_admissible = ['ADMISSIBLE_MP-SPE.xlsx', 'ADMISSIBLE_MP.xlsx', 'ADMISSIBLE_PC-SPE.xlsx', 'ADMISSIBLE_PC.xlsx', 'ADMISSIBLE_PSI-SPE.xlsx', 'ADMISSIBLE_PSI.xlsx', 'ADMISSIBLE_PT-SPE.xlsx', 'ADMISSIBLE_PT.xlsx', 'ADMISSIBLE_TSI-SPE.xlsx', 'ADMISSIBLE_TSI.xlsx']

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

nadmis = len(fichiers_admis)
nadmissible = len(fichiers_admissible)

print("Fichier ADMIS")
for i in range(0,nadmis,2):
    print( include(dirPath+fichiers_admis[i], dirPath+fichiers_admis[i+1]) )

print("")
print("Fichier ADMISSIBLE")
for i in range(0,nadmissible,2):
    print( include(dirPath+fichiers_admissible[i], dirPath+fichiers_admissible[i+1]) )
    