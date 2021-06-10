import pandas as pd
from main import *


classes = fichiers_Classes_xlsx
fichiers_admissible = fichiers_admis_normal[1:] #On enleve les ATS
fichiers_admissible_spe = fichiers_admissible_spe
fichiers_admis = fichiers_admis_normal[1:] #On   enleve les ATS
fichiers_admis_spe = fichiers_admis_spe



def comparetypeadmis(classe,file,filespe):
    ### lecture du fichier excel
    df = pd.read_excel(file)
    dfspe = pd.read_excel(filespe)
    cl = pd.read_excel(classe, skiprows=1)

    # logA = liste des logins des candidats de type admissible A
    logA = cl['login'][cl['type_admissible'] == 'A'].values

    # logB = liste des logins des candidats de type admissible B
    logB = cl['login'][cl['type_admissible'] == 'B'].values

    cand = df['Can _cod'].values     # liste des id des candidats en normal
    candSPE = dfspe['Can _cod'].values   # liste des id des candidats en spe seulement

    for cod in logA:
        if not(cod in cand):
            return False
    
    for cod in logB:
        if (cod in cand) or not(cod in candSPE):
            return False

    #verification cardinal
    if not(len(logA)+len(logB) == len(candSPE)):
        print("pas le bon cardinal")

    return True

n = len(classes)
print("Pour les candidats admis:")
for i in range(n):
    print(comparetypeadmis(dirPath+classes[i], dirPath+fichiers_admis[i], dirPath+fichiers_admis_spe[i]))
print("")
print("Pour les candidats admissible:")
for i in range(n):
    print(comparetypeadmis(dirPath+classes[i], dirPath+fichiers_admissible[i], dirPath+fichiers_admissible_spe[i]))

print("")
print("Les type admissible A sont les élèves admis en normale")
print("Les type admissible B sont les élèves admis en spé seulement")