#!/bin/bash
echo "[+] Création de l'environnement virtuel"
python3 -m venv env
echo "[+] Ouverture de l'environnement virtuel"
source env/bin/activate
echo "[+] Installation des dépendances"
pip3 install -r requirements.txt
deactivate
