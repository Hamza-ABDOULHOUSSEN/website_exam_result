import pandas as pd
from main import *


# On verifie que tous les elements de petit sont dans grand
liste_non_inclu = []

def contient(grand,petit):
    global liste_non_inclu
    liste_non_inclu = []

    (file,col) = grand
    (filebis,colbis) = petit

    dfg = lecture(file)
    liste_element_grand = dfg[col].values

    dfp = lecture(filebis)
    n,_ = dfp.shape

    bool = True

    for i in range(n):
        if not(dfp[colbis][i] in liste_element_grand):
            liste_non_inclu.append( dfp[colbis][i] )
            bool = False
    
    return bool

# Exemple
liste_grand = [('listeEtablissements.xlsx', 'Etab')]
liste_petit = [('Inscription.xlsx', 'ETABLISSEMENT')]
grand = liste_grand[0]
petit = liste_petit[0]
# contient(grand,petit)

bigfile = 'Inscription.xlsx'
bigcol = 'CODE_CANDIDAT'
big = (bigfile,bigcol)

### verifications Inscription contient tous les candidats
#liste_non_inclu = []

#col = 'Can _cod'
#for file in ['ADMISSIBLE_PC-SPE.xlsx', 'ADMISSIBLE_PC.xlsx', 'ADMIS_PC-SPE.xlsx', 'ADMIS_PC.xlsx']: #fichier_admis
#    print(file)
#    print( contient(big, (file,col)) )

## certains candidats ne sont pas dans Inscription
