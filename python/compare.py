import pandas as pd
from main import *

# On compare les elements de liste_triple1 avec liste_triple2
# pour t1=(file, coluniq, col2) et t2=(filebis, coluniqbis, col2bis)
# Si il y a l'element 'x' dans coluniq de file et coluniqbis de filebis
# alors on verifie qu'il y a le même element dans col2 de file et col2bis de filebis

def compare(t1, t2):
    (file, coluniq, col2) = t1
    (filebis, coluniqbis, col2bis) = t2

    df1 = lecture(file)
    n1,_ = df1.shape

    dic = {}

    for i in range(n1):
        if df1[coluniq][i] in dic:
            print("les elements de la colonne ne sont pas uniques")
            print("element en double :")
            print(df1[coluniq][i])
            print(dic[df1[coluniq][i]])
            if dic[df1[coluniq][i]] != df1[col2][i]:
                print(df1[col2][i])
            print()

        dic[df1[coluniq][i]] = df1[col2][i]

    df2 = lecture(filebis)
    n2,_ = df2.shape

    bool = True

    for i in range(n2):
        if df2[coluniqbis][i] in dic and dic[df2[coluniqbis][i]] != df2[col2bis][i]:
            print(df2[coluniqbis][i])
            print("dans file1 :")
            print(dic[df2[coluniqbis][i]])
            print("dans file2 :") 
            print(df2[col2bis][i])
            print()
            
            bool = False

    return bool

## Exemple
liste_triple1 = [('listeEtablissements.xlsx', 'Rne', 'Etab')]
liste_triple2 = [('Inscription.xlsx', 'CODE_ETABLISSEMENT', 'ETABLISSEMENT')]
t1 = liste_triple1[0]
t2 = liste_triple2[0]
# compare(t1,t2)
