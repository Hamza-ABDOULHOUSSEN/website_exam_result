import pandas as pd
import os

dirPath = "../data/public/"

All1 = os.listdir(dirPath)
# on retire les fichiers cachés
All = []
for a in All1:
    if a[0] != '.' and a[0] != '~':
        All.append(a)
All.sort()
del All1

fichiers_admis = ['ADMISSIBLE_ATS.xlsx', 'ADMISSIBLE_MP-SPE.xlsx', 'ADMISSIBLE_MP.xlsx', 'ADMISSIBLE_PC-SPE.xlsx', 'ADMISSIBLE_PC.xlsx', 'ADMISSIBLE_PSI-SPE.xlsx', 'ADMISSIBLE_PSI.xlsx', 'ADMISSIBLE_PT-SPE.xlsx', 'ADMISSIBLE_PT.xlsx', 'ADMISSIBLE_TSI-SPE.xlsx', 'ADMISSIBLE_TSI.xlsx', 'ADMIS_ATS.xlsx', 'ADMIS_MP-SPE.xlsx', 'ADMIS_MP.xlsx', 'ADMIS_PC-SPE.xlsx', 'ADMIS_PC.xlsx', 'ADMIS_PSI-SPE.xlsx', 'ADMIS_PSI.xlsx', 'ADMIS_PT-SPE.xlsx', 'ADMIS_PT.xlsx', 'ADMIS_TSI-SPE.xlsx', 'ADMIS_TSI.xlsx']
fichiers_CMT = ['CMT_Oraux_YYYY_MP.xlsx', 'CMT_Oraux_YYYY_PC.xlsx', 'CMT_Oraux_YYYY_PSI.xlsx', 'CMT_Oraux_YYYY_PT.xlsx']
fichiers_Classes_xlsx = ['Classes_MP_CMT_spe_XXXX.xlsx', 'Classes_PC_CMT_spe_XXXX.xlsx', 'Classes_PSI_CMT_spe_XXXX.xlsx', 'Classes_PT_CMT_spe_XXXX.xlsx', 'Classes_TSI_CMT_spe_XXXX.xlsx']
fichiers_Classes_csv = ['Classes_MP_CMT_spe_XXXX_SCEI.csv', 'Classes_PC_CMT_spe_XXXX_SCEI.csv', 'Classes_PSI_CMT_spe_XXXX_SCEI.csv', 'Classes_PT_CMT_spe_XXXX_SCEI.csv', 'Classes_TSI_CMT_spe_XXXX_SCEI.csv']
fichiers_Ecrit = ['Ecrit_MP.xlsx', 'Ecrit_PC.xlsx', 'Ecrit_PSI.xlsx', 'Ecrit_PT.xlsx', 'Ecrit_TSI.xlsx']
fichiers_Oral = ['Oral_MP.xlsx', 'Oral_PC.xlsx', 'Oral_PSI.xlsx', 'Oral_PT.xlsx', 'Oral_TSI.xlsx']
fichiers_Voeux = ['listeVoeux_ATS.xlsx', 'listeVoeux_MP.xlsx', 'listeVoeux_PC.xlsx', 'listeVoeux_PSI.xlsx', 'listeVoeux_PT.xlsx', 'listeVoeux_TSI.xlsx']


def lecture(file):
    if file[-3:] == "csv":
        return pd.read_csv(dirPath+file, sep =';')

    elif file == "Inscription.xlsx" or file[:7] == "Classes":
        return pd.read_excel(dirPath+file, skiprows=1)

    else:
        return pd.read_excel(dirPath+file)


def read_all():
    
    FilesContents = {}  # dictionnaire pour garder le contenu des fichiers

    for file in All:
        FilesContents[file] = lecture(file)

    return FilesContents
