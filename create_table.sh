#!/bin/bash
rm CMT_database.db
source env/bin/activate
echo "[+] Génération de la base de données"
python3 Base\ de\ donnee/DB_generator.py
echo "[+] Remplissage de la base de données"
python3 Base\ de\ donnee/DB_insertion.py
echo "[+] Ajout des cas particuliers"
python3 Base\ de\ donnee/DB_insertion_particulier.py
deactivate