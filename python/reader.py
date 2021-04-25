import pandas as pd
import os

dirPath = "../data/public"
files = [file for file in os.listdir(dirPath)]
# variable temporaire pour garder tous les fichiers dans le répertoire data

keptFiles = []
for file in files:
    if file.endswith(".xlsx"):
        keptFiles.append((dirPath + "/" + file, file))
        # le première variable du tuple est pour garder le chemin absolu depuis le fichier
        # la seconde est pour garder le nom du fichier et s'en servir de clé pour retrouver le contenu dans la table
        # de hachage

del files  # on supprime cette variable car elle n'est plus utile

filesContents = {}

for file in keptFiles:
    print(f'[+] Lecture de \t {file[1]}')
    filesContents[file[1]] = pd.read_excel(file[0])

print("[*] Tous les fichiers ont été chargés en mémoire.")
