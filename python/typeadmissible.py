import pandas as pd

dirPath = "../data/public/"
classes = ['Classes_MP_CMT_spe_XXXX.xlsx', 'Classes_PC_CMT_spe_XXXX.xlsx', 'Classes_PSI_CMT_spe_XXXX.xlsx', 'Classes_PT_CMT_spe_XXXX.xlsx', 'Classes_TSI_CMT_spe_XXXX.xlsx']
fichiers_admissible = ['ADMISSIBLE_MP.xlsx', 'ADMISSIBLE_PC.xlsx', 'ADMISSIBLE_PSI.xlsx', 'ADMISSIBLE_PT.xlsx', 'ADMISSIBLE_TSI.xlsx']
fichiers_admissible_spe = ['ADMISSIBLE_MP-SPE.xlsx', 'ADMISSIBLE_PC-SPE.xlsx', 'ADMISSIBLE_PSI-SPE.xlsx', 'ADMISSIBLE_PT-SPE.xlsx', 'ADMISSIBLE_TSI-SPE.xlsx']
fichiers_admis = ['ADMIS_MP.xlsx', 'ADMIS_PC.xlsx', 'ADMIS_PSI.xlsx', 'ADMIS_PT.xlsx', 'ADMIS_TSI.xlsx']
fichiers_admis_spe = ['ADMIS_MP-SPE.xlsx', 'ADMIS_PC-SPE.xlsx', 'ADMIS_PSI-SPE.xlsx', 'ADMIS_PT-SPE.xlsx', 'ADMIS_TSI-SPE.xlsx']



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