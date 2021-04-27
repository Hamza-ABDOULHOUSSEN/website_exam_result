import pandas as pd
import numpy as np

dirPath = "../data/public/"

### lire le fichier excel
df = pd.read_excel(dirPath+'ADMIS_MP.xlsx')

### afficher le fichier
#print (df)

### afficher les premières lignes
#df.head()

### afficher la taille (nb ligne, nb colonne)
#print(df.shape)

### afficher les entêtes des colonnes
#print(df.columns)

### eliminer des colonnes inutiles
df.drop( df.columns[1:] , axis=1)

### statistique
# df.describe()

### remplacer par une valeur par defaut
# df.fillna( df['age'].mean) (exemple)

### supprimer les lignes avec données manquantes
# df.dropna(axis=0)

### compter l'occurence de chaque terme
tab = df['Can _cod'].value_counts()