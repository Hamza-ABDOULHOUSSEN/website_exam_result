#!/bin/bash
echo "[+] Lancement de l'environnement virtuel"
source env/bin/activate
export FLASK_APP=site_web/app.py
echo "[+] Lancement du site internet"
flask run
