import pandas as pd
from main import *


# On verifie que tous les elements de petit sont dans grand

def contient(grand,petit):
    (file,col) = grand
    (filebis,colbis) = petit

    dfg = lecture(file)
    liste_element_grand = dfg[col][:]

    dfp = lecture(filebis)
    n,_ = dfp.shape

    bool = True

    for i in range(n):
        if not(dfp[colbis][i] in liste_element_grand):
            print(dfp[colbis][i])
            bool = False
    
    return bool

# Exemple
liste_grand = [('listeEtablissements.xlsx', 'Etab')]
liste_petit = [('Inscription.xlsx', 'ETABLISSEMENT')]
grand = liste_grand[0]
petit = liste_petit[0]
# contient(grand,petit)