import pandas as pd
from main import *

def uniq(file,col):

    ### lecture fichier excel
    df = lecture(file)

    # parc: les nombres d'occurence de chaque valeur
    parc = df[col].value_counts().values    # nombre d'occurence des différentes valeurs dans la colonne
    n = len(parc)
    
    for i in range(n):
        if parc[i] != 1:        # chaque element ne doit etre qu'une fois dans la colonne
            return False

    return True


for file in fichiers_admis:
    col = 'Can _cod'
    print(file+'\t'+col+'\t\t'+ str(uniq(file,col)))

for file in fichiers_CMT:
    col = "Numéro d'inscription"
    print(file+'\t'+col+'\t\t'+ str(uniq(file,col)))

for file in fichiers_Classes_xlsx:
    col = 'login'
    print(file+'\t'+col+'\t\t'+ str(uniq(file,col)))

for file in fichiers_Classes_csv:
    col = 'scei'
    print(file+'\t'+col+'\t\t'+ str(uniq(file,col)))

for file in fichiers_Ecrit+fichiers_Oral:
    col = 'Can _cod'
    print(file+'\t'+col+'\t\t'+ str(uniq(file,col)))

files = ['Inscription.xlsx', 'ResultatEcrit_DD_MM_YYYY_ATS.xlsx', 'ResultatOral_DD_MM_YYYY_ATS.xlsx', 'listeEcoles.xlsx', 'listeEtablissements.xlsx', 'listeEtatsReponsesAppel.xlsx']
cols = ['CODE_CANDIDAT', "Numéro d'inscription", "Numéro d'inscription",'Ecole', 'Rne', 'Ata _cod']
for i in range(6):
    file = files[i]
    col = cols[i]
    print(file+'\t'+col+'\t\t'+ str(uniq(file,col)))

