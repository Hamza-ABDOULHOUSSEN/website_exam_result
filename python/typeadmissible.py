import pandas as pd
import numpy as np

dirPath = "../data/public/"
classes = ['Classes_MP_CMT_spe_XXXX.xlsx', 'Classes_PC_CMT_spe_XXXX.xlsx', 'Classes_PSI_CMT_spe_XXXX.xlsx', 'Classes_PT_CMT_spe_XXXX.xlsx', 'Classes_TSI_CMT_spe_XXXX.xlsx']
fichiers_admissible = ['ADMISSIBLE_MP.xlsx', 'ADMISSIBLE_PC.xlsx', 'ADMISSIBLE_PSI.xlsx', 'ADMISSIBLE_PT.xlsx', 'ADMISSIBLE_TSI.xlsx']
fichiers_admissible_spe = ['ADMISSIBLE_MP-SPE.xlsx', 'ADMISSIBLE_PC-SPE.xlsx', 'ADMISSIBLE_PSI-SPE.xlsx', 'ADMISSIBLE_PT-SPE.xlsx', 'ADMISSIBLE_TSI-SPE.xlsx']
fichiers_admis = ['ADMIS_MP.xlsx', 'ADMIS_PC.xlsx', 'ADMIS_PSI.xlsx', 'ADMIS_PT.xlsx', 'ADMIS_TSI.xlsx']
fichiers_admis_spe = ['ADMIS_MP-SPE.xlsx', 'ADMIS_PC-SPE.xlsx', 'ADMIS_PSI-SPE.xlsx', 'ADMIS_PT-SPE.xlsx', 'ADMIS_TSI-SPE.xlsx']



def comparetypeadmis(classe,file,filespe):
    ### lire le fichier excel
    df = pd.read_excel(file)
    dfspe = pd.read_excel(filespe)
    cl = pd.read_excel(classe, skiprows=1)

    # logA = liste des logins des candidats de type admissible A
    logA = cl['login'][cl['type_admissible'] == 'A'].values

    # logB = liste des logins des candidats de type admissible B
    logB = cl['login'][cl['type_admissible'] == 'B'].values

    cand_MP = df['Can _cod'].values
    cand_MPSPE = dfspe['Can _cod'].values

    for cod in logA:
        if not(cod in cand_MP):
            return False
    
    for cod in logB:
        if (cod in cand_MP) or not(cod in cand_MPSPE):
            return False

    #verification cardinal
    if not(len(logA)+len(logB) == len(cand_MPSPE)):
        print("pas le bon cardinal")

    return True

n = len(classes)
for i in range(n):
    print(comparetypeadmis(dirPath+classes[i], dirPath+fichiers_admis[i], dirPath+fichiers_admis_spe[i]))
print("")
for i in range(n):
    print(comparetypeadmis(dirPath+classes[i], dirPath+fichiers_admissible[i], dirPath+fichiers_admissible_spe[i]))

print("")
print("Les type admissible A sont les élèves admis de classe normale")
print("Les type admissible B sont les élèves admis de classe spé seulement")