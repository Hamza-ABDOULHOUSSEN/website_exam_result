import pandas as pd
import os


# region importation des fichiers
def parser(content):
    """Fonction qui prend une chaine de caractère en entrée et qui renvoie un table de hachage du contenu"""
    # la fonctions pd.read_csv() ne fonctionne pas car certaines lignes des fichiers cdv sont incomplètes
    lines = content.strip().split("\n")
    content = {}
    keys = lines[0].split(";")

    for key in keys:
        content[key] = []  # permet d'initialiser des listes pour des clés données pour les fichiers csv

    lines.pop(0)  # on retire la première ligne qui contient les clés de la table de hachage
    for line in lines:
        line = line.split(";")
        for i in range(len(keys)):
            content[keys[i]].append(line[i])
    return content


dirPath = "../data/public"
files = [file for file in os.listdir(dirPath)]
# variable temporaire pour garder tous les fichiers dans le répertoire data

xlsxFiles = []
csvFiles = []
for file in files:
    if file.endswith(".xlsx"):
        xlsxFiles.append((dirPath + "/" + file, file))
    if file.endswith(".csv"):
        csvFiles.append((dirPath + "/" + file, file))
        # le première variable du tuple est pour garder le chemin relatif depuis le script de lecture
        # la seconde est pour garder le nom du fichier et s'en servir de clé pour retrouver le contenu dans les tables
        # de hachage

del files  # on supprime cette variable car elle n'est plus utile

xlsxFilesContents = {}  # table de hachage pour garder le contenu des fichiers excel
csvFilesContents = {}  # table de hachage pour garder le contenu des fichiers csv

for file in xlsxFiles:
    print(f'[+] Lecture de \t {file[1]}')
    xlsxFilesContents[file[1]] = pd.read_excel(file[0])

for file in csvFiles:
    print(f'[+] Lecture de \t {file[1]}')
    with open(file[0]) as f:
        csvFilesContents[file[1]] = parser(f.read())

print("[*] Tous les fichiers ont été chargés en mémoire.")
# endregion
