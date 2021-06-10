import pandas as pd
from main import *

# On compare les elements de liste_triple1 avec liste_triple2
# pour t1=(file, coluniq, col2) et t2=(filebis, coluniqbis, col2bis)
# Si il y a l'element 'x' dans coluniq de file et coluniqbis de filebis
# alors on verifie qu'il y a le même element dans col2 de file et col2bis de filebis

liste_non_inclu = []

def compare(t1, t2):
    global liste_non_inclu
    liste_non_inclu = []

    (file, coluniq, col2) = t1
    (filebis, coluniqbis, col2bis) = t2

    df1 = lecture(file)
    n1,_ = df1.shape

    # on remplit un dictionnaire à partir des elements de la 1ere table
    dic = {}

    for i in range(n1):
        # colonne non unique
        if df1[coluniq][i] in dic:
            print("les elements de la colonne ne sont pas uniques")
            print("element en double :")
            print(df1[coluniq][i])
            print(dic[df1[coluniq][i]])
            if dic[df1[coluniq][i]] != df1[col2][i]:
                print(df1[col2][i])
            print()
            return None

        dic[df1[coluniq][i]] = df1[col2][i]

    df2 = lecture(filebis)
    n2,_ = df2.shape

    bool = True

    # on compare les elements de la 2nd table avec le dictionnaire
    # on les ajoutent dans liste_non_inclu

    for i in range(n2):
        if df2[coluniqbis][i] in dic and dic[df2[coluniqbis][i]] != df2[col2bis][i]:
            liste_non_inclu.append((df2[coluniqbis][i],dic[df2[coluniqbis][i]],df2[col2bis][i]))
            
            bool = False

    return bool

def affiche(liste):
    for (id, val1, val2) in liste:
        print(id)
        print("dans file1 :")
        print(val1)
        print("dans file2 :") 
        print(val2)
        print()

## Exemple
file1 = 'listeEtablissements.xlsx'
id1 = 'Rne'
col1 = 'Etab'
t1 = (file1,id1,col1)
file2 = 'Inscription.xlsx'
id2 = 'CODE_ETABLISSEMENT'
col2 = 'ETABLISSEMENT'
t2 = (file2,id2,col2)
#print(file1)
#print(file2)
# compare(t1,t2)
