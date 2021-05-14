import sqlite3
import pandas as pd
import os
import sys
sys.path.append('../python')
from main import *

DATABASE = "CMT_database.db"
conn = sqlite3.connect(DATABASE)
c = conn.cursor()

# importation donnee
file = read_all()       # dictionnaire clé: nom du fichier , valeur: fichier lu avec pandas
taille = {}
for name in All:         # All = listes des fichiers
    (nb_ligne,_) = file[name].shape
    taille[name] = nb_ligne



### TABLE Candidat

## requetes
# Candidat
req = "insert into Candidat (candidat_id,INE, Civ, Nom, Prenom, Autres_Prenoms, Date_Naissance, Ville_Naissance, Pays_Naissance_id, Francais, Autre_Nationalite_id, Adresse1, Adresse2, Code_Postal, Commune, Pays_id, Email, Telephone, Portable, Filliere, Classe, Puissance, Etablissement_id, Epreuve1, LV, Ville_ecrit, Bac_id, Bac_Mention, Bac_dep, Sujet_TIPE, Profession_pere_code, Profession_mere_code, Boursier) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
req_ajout_ats = "insert into Candidat (candidat_id, Civ, Nom, Prenom, Adresse1, Adresse2, Code_Postal, Commune, Pays_id, Email, Telephone, Portable, Filliere) values (?,?,?,?,?,?,?,?,?,?,?,?,'ATS')"
# Bac
req_bac = "insert into Bac (bac_id, annee, mois, code_serie) values (?,?,?,?)"
req_code_serie_bac = "insert into Code_Serie_Bac (code_serie, serie) values (?,?)"
req_code_concours = "insert into Code_Concours (Filliere, code_concours) values (?,?)"
# Profession
req_profession = "insert into Profession (code_profession, profession) values (?,?)"
# Pays
req_pays = "insert into Pays (code_pays, pays) values (?,?)"
req_natio = "insert into Pays (code_pays, nationalite) values (?,?)"
req_pays_upd = "UPDATE Pays SET pays = ? WHERE code_pays = ?"
req_natio_upd = "UPDATE Pays SET nationalite = ? WHERE code_pays = ?"
# Etablissement
req_etab_ins = "insert into Etablissement (code_etablissement,etablissement) values (?,?)"
req_etab_new = "insert into Etablissement (code_etablissement,etablissement, Type, Ville, CP, Pays_id) values (?,?,?,?,?,?)"
req_etab_upd = "UPDATE Etablissement SET (Type, Ville, CP, Pays_id) = (?,?,?,?) WHERE code_etablissement = ?"
# Ecole 
req_ecole = "insert into Ecole (ecole_id,nom) values (?,?)"
# Voeux
req_voeux = "insert into Voeux (candidat_id,ecole_id,ordre) values (?,?,?)"
# EtatReponse
req_etat_rep = "insert into EtatReponse (code,reponse) values (?,?)"


def civ(n):
    if n == 1:
        return 'Mr'
    else:
        return 'Mme'

def bacdep(x):
    if type(x) == str:
        return x
    else:
        return "non indique"

def boursier(s):
    if s == ' ':
        return "non"
    if s == 'Boursier':
        return "oui"

def francais(x):
    if x==0:
        return "non"
    else:
        return "oui"

def ine(x):
    if type(x) != str:
        return 'non indique'
    else:
        return x

def mention(x):
    if x == 'S':
        return ""
    else:
        return x

# TABLE BAC et CODE_SERIE_BAC
Dic_Bac = {}
Dic_Bac_Serie = []
Bac_id = -1

def bac(annee,mois,serie,codeserie):
    annee = int(annee)
    mois = int(mois)
    codeserie = int(codeserie)
    global Bac_id
    if (annee,mois,codeserie) in Dic_Bac:
        return Dic_Bac[(annee,mois,codeserie)]
    else:
        Bac_id +=1
        Dic_Bac[(annee,mois,codeserie)] = Bac_id
        # ajout du nouveau type de Bac
        c.execute(req_bac, (Bac_id, annee, mois, codeserie))

        # ajout de la nouvelle serie
        if not(codeserie in Dic_Bac_Serie):
            Dic_Bac_Serie.append(codeserie)
            c.execute(req_code_serie_bac, (codeserie, serie))

        return Bac_id

# TABLE CODE_CONCOURS
Dic_Filliere = []
def filliere(filliere,code):
    if not(filliere in Dic_Filliere):
        code = int(code)
        Dic_Filliere.append(filliere)
        c.execute(req_code_concours, (filliere,code) )
    return filliere

# TABLE PROFESSION
Dic_Prof = []
def prof(code,profession):
    code = int(code)
    if not( code in Dic_Prof):
        Dic_Prof.append(code)
        c.execute(req_profession, (code,profession) )
    return code

# TABLE PAYS
Dic_pays = {}
Dic_nation = []

def pays(code,pays):
    code = int(code)
    if not(pays in Dic_pays):
        Dic_pays[pays] = code
        if code in Dic_nation:
            c.execute(req_pays_upd, (pays,code))
        else:
            c.execute(req_pays, (code,pays))
    return code

def natio(code,natio):
    code = int(code)
    if not(code in Dic_nation):
        Dic_nation.append(code) 
        if code in Dic_pays.values():
            c.execute(req_natio_upd, (natio,code))
        else:
            c.execute(req_natio, (code,natio))
    return code

# TABLE ETABLISSEMENT
pays_code_incr = -1
def ajout_pays(pays):
    global pays_code_incr
    if (pays in Dic_pays):
        return Dic_pays[pays]
    else:
        pays_code_incr += 1
        while (pays_code_incr in Dic_pays.values()) or (pays_code_incr in Dic_nation):
            pays_code_incr += 1

        Dic_pays[pays] = pays_code_incr
        c.execute(req_pays, (pays_code_incr,pays))
        return pays_code_incr

Dic_etab = {}
def etab(code_etablissement, etablissement):
    if not(code_etablissement in Dic_etab):
        Dic_etab[code_etablissement] = etablissement
        c.execute(req_etab_ins, (code_etablissement,etablissement))
    return code_etablissement

# TABLE CANDIDAT
# Parcours de Inscription.xlsx
for i in range(taille['Inscription.xlsx']):
    c.execute(req, (int(file['Inscription.xlsx']['CODE_CANDIDAT'][i]) , ine(file['Inscription.xlsx']['NUMERO_INE'][i]) ,  civ(file['Inscription.xlsx']['CIVILITE'][i]) , file['Inscription.xlsx']['NOM'][i] , file['Inscription.xlsx']['PRENOM'][i] , file['Inscription.xlsx']['AUTRES_PRENOMS'][i] , file['Inscription.xlsx']['DATE_NAISSANCE'][i] , file['Inscription.xlsx']['VILLE_NAISSANCE'][i] , pays(file['Inscription.xlsx']['CODE_PAYS_NAISSANCE'][i],file['Inscription.xlsx']['PAYS_NAISSANCE'][i]) ,  francais(file['Inscription.xlsx']['FRANCAIS'][i]) , natio(file['Inscription.xlsx']['CODE_PAYS_NATIONALITE'][i],file['Inscription.xlsx']['AUTRE_NATIONALITE'][i]) , file['Inscription.xlsx']['ADRESSE1'][i] , file['Inscription.xlsx']['ADRESSE2'][i] , int(file['Inscription.xlsx']['CP'][i]) , file['Inscription.xlsx']['VILLE'][i] , pays(file['Inscription.xlsx']['CODE_PAYS'][i],file['Inscription.xlsx']['LIBELLE_PAYS'][i]) , file['Inscription.xlsx']['EMAIL'][i] , file['Inscription.xlsx']['TELEPHONE'][i] , file['Inscription.xlsx']['TEL_PORTABLE'][i] , filliere(file['Inscription.xlsx']['VOIE'][i],file['Inscription.xlsx']['CODE_CONCOURS'][i]) , file['Inscription.xlsx']['CLASSE'][i] , file['Inscription.xlsx']['PUISSANCE'][i] , etab(file['Inscription.xlsx']['CODE_ETABLISSEMENT'][i],file['Inscription.xlsx']['ETABLISSEMENT'][i]) , file['Inscription.xlsx']['EPREUVE1'][i] , file['Inscription.xlsx']['OPTION1'][i] , file['Inscription.xlsx']['LIBELLE_VILLE_ECRIT'][i] , bac(file['Inscription.xlsx']['ANNEE_BAC'][i] , file['Inscription.xlsx']['MOIS_BAC'][i] , file['Inscription.xlsx']['SERIE'][i], file['Inscription.xlsx']['CODE_SERIE'][i]), mention(file['Inscription.xlsx']['MENTION'][i]) , bacdep(file['Inscription.xlsx']['CAN_DEP_BAC'][i]) , file['Inscription.xlsx']['SUJET_TIPE'][i] , prof(file['Inscription.xlsx']['COD_CSP_PERE'][i],file['Inscription.xlsx']['LIB_CSP_PERE'][i]) , prof(file['Inscription.xlsx']['COD_CSP_MERE'][i],file['Inscription.xlsx']['LIB_CSP_MERE'][i]) , boursier(file['Inscription.xlsx']['QUALITE'][i])) )

# TABLE CANDIDAT
# INSERTION CANDIDAT ATS
tab = file['ADMISSIBLE_ATS.xlsx']
for i in range(taille['ADMISSIBLE_ATS.xlsx']):
    c.execute(req_ajout_ats, (int(tab['Can _cod'][i]), civ(tab['Civ _lib'][i]), tab['Nom'][i], tab['Prenom'][i], tab['Can _ad 1'][i], tab['Can _ad 2'][i], int(tab['Can _cod _pos'][i]), tab['Can _com'][i], ajout_pays(tab['Can _pay _adr'][i]), tab['Can _mel'][i], tab['Can _tel'][i], tab['Can _por'][i]) )


# TABLE ETABLISSEMENT
# Parcours de listeEtablissements.xlsx
for i in range(taille['listeEtablissements.xlsx']):
    code_etablissement = file['listeEtablissements.xlsx']['Rne'][i]
    etablissement = file['listeEtablissements.xlsx']['Etab'][i]
    if code_etablissement in Dic_etab and Dic_etab[code_etablissement] == etablissement:
        c.execute(req_etab_upd, (file['listeEtablissements.xlsx']['Type _etab'][i], file['listeEtablissements.xlsx']['Ville _etab'][i], int(file['listeEtablissements.xlsx']['Code _postal _etab'][i]), ajout_pays(file['listeEtablissements.xlsx']['Pays _atab'][i]), code_etablissement ) )
    elif not(code_etablissement in Dic_etab):
        Dic_etab[code_etablissement] = etablissement
        c.execute(req_etab_new, (code_etablissement, etablissement, file['listeEtablissements.xlsx']['Type _etab'][i], file['listeEtablissements.xlsx']['Ville _etab'][i], int(file['listeEtablissements.xlsx']['Code _postal _etab'][i]), ajout_pays(file['listeEtablissements.xlsx']['Pays _atab'][i])) )


# TABLE Ecole
for i in range(taille['listeEcoles.xlsx']):
    c.execute(req_ecole, (int(file['listeEcoles.xlsx']['Ecole'][i]), file['listeEcoles.xlsx']['Nom _ecole'][i]) )

# TABLE Voeux
for fichier in fichiers_Voeux:
    for i in range(taille[fichier]):
        c.execute(req_voeux, (int(file[fichier]['Can _cod'][i]), int(file[fichier]['Eco _cod'][i]), int(file[fichier]['Voe _ord'][i])) )

# TABLE EtatReponse
for i in range(taille['listeEtatsReponsesAppel.xlsx']):
    c.execute(req_etat_rep, (int(file['listeEtatsReponsesAppel.xlsx']['Ata _cod'][i]), file['listeEtatsReponsesAppel.xlsx']['Ata _lib'][i]) )

# TABLE Note_Ecrit
req_ecrit_ATS = "insert into Ecrit_Note_ATS (candidat_id, Math, Phy, Fr, Ang, SI, total_ecrit, rang_ecrit) values (?,?,?,?,?,?,?,?)"
req_ecrit_MP = "insert into Ecrit_Note_MP (candidat_id, Math1, Math2, Phy1, Phy2, Chimie, Fr, LV1, IPT, Spe, total_ecrit, rang_ecrit) values (?,?,?,?,?,?,?,?,?,?,?,?)"
req_ecrit_PC = "insert into Ecrit_Note_PC (candidat_id, Math1, Math2, Phy1, Phy2, Chimie, Fr, LV1, IPT, total_ecrit, rang_ecrit) values (?,?,?,?,?,?,?,?,?,?,?)"
req_ecrit_PSI = "insert into Ecrit_Note_PSI (candidat_id, Math1, Math2, Phy1, Phy2, Chimie, Fr, LV1, IPT, SI, total_ecrit, rang_ecrit) values (?,?,?,?,?,?,?,?,?,?,?,?)"
req_ecrit_PT = "insert into Ecrit_Note_PT (candidat_id, Math1, Math2, Phy1, Phy2, Info_Model, SI, Fr, LV1, total_ecrit, rang_ecrit) values (?,?,?,?,?,?,?,?,?,?,?)"
req_ecrit_TSI = "insert into Ecrit_Note_TSI (candidat_id, Math1, Math2, Phy1, Phy2, Fr, LV1, SI, Info, total_ecrit, rang_ecrit) values (?,?,?,?,?,?,?,?,?,?,?)"
fichiers_Classes_xlsx = ['Classes_MP_CMT_spe_XXXX.xlsx', 'Classes_PC_CMT_spe_XXXX.xlsx', 'Classes_PSI_CMT_spe_XXXX.xlsx', 'Classes_PT_CMT_spe_XXXX.xlsx', 'Classes_TSI_CMT_spe_XXXX.xlsx']

tab = file['Classes_MP_CMT_spe_XXXX.xlsx']
for i in range(taille['Classes_MP_CMT_spe_XXXX.xlsx']):
    c.execute(req_ecrit_MP, (int(tab['login'][i]), tab['600 (Mathématiques 1)'][i], tab['601 ( Mathématiques 2)'][i], tab['602 (Physique 1)'][i], tab['603 (Physique 2)'][i], tab['604 (Chimie)'][i], tab['605 (Français)'][i], tab['28 (Langue)'][i], tab['1050 (Informatique)'][i], tab['599 (Informatique ou Sciences industrielles)'][i], tab['total_ecrit'][i], int(tab['rang_admissible'][i])) )

conn.commit()
conn.close()
