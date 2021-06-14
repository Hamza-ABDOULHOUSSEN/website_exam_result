import sqlite3
import pandas as pd
import math
import sys

sys.path.append("python")

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
# MP_Spe_Info_Si
req_spe_info_si = "insert into MP_Spe_Info_SI (candidat_id, Spe_Info_SI) values (?,?)"
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

### TABLE BAC et CODE_SERIE_BAC
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

### TABLE CODE_CONCOURS
Dic_Filliere = []
def filliere(filliere,code):
    if not(filliere in Dic_Filliere):
        code = int(code)
        Dic_Filliere.append(filliere)
        c.execute(req_code_concours, (filliere,code) )
    return filliere

### TABLE PROFESSION
Dic_Prof = []
def prof(code,profession):
    code = int(code)
    if not( code in Dic_Prof):
        Dic_Prof.append(code)
        c.execute(req_profession, (code,profession) )
    return code

### TABLE PAYS
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

### TABLE ETABLISSEMENT
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

### TABLE CANDIDAT
# Parcours de Inscription.xlsx
for i in range(taille['Inscription.xlsx']):
    c.execute(req, (int(file['Inscription.xlsx']['CODE_CANDIDAT'][i]) , ine(file['Inscription.xlsx']['NUMERO_INE'][i]) ,  civ(file['Inscription.xlsx']['CIVILITE'][i]) , file['Inscription.xlsx']['NOM'][i] , file['Inscription.xlsx']['PRENOM'][i] , file['Inscription.xlsx']['AUTRES_PRENOMS'][i] , file['Inscription.xlsx']['DATE_NAISSANCE'][i] , file['Inscription.xlsx']['VILLE_NAISSANCE'][i] , pays(file['Inscription.xlsx']['CODE_PAYS_NAISSANCE'][i],file['Inscription.xlsx']['PAYS_NAISSANCE'][i]) ,  francais(file['Inscription.xlsx']['FRANCAIS'][i]) , natio(file['Inscription.xlsx']['CODE_PAYS_NATIONALITE'][i],file['Inscription.xlsx']['AUTRE_NATIONALITE'][i]) , file['Inscription.xlsx']['ADRESSE1'][i] , file['Inscription.xlsx']['ADRESSE2'][i] , int(file['Inscription.xlsx']['CP'][i]) , file['Inscription.xlsx']['VILLE'][i] , pays(file['Inscription.xlsx']['CODE_PAYS'][i],file['Inscription.xlsx']['LIBELLE_PAYS'][i]) , file['Inscription.xlsx']['EMAIL'][i] , file['Inscription.xlsx']['TELEPHONE'][i] , file['Inscription.xlsx']['TEL_PORTABLE'][i] , filliere(file['Inscription.xlsx']['VOIE'][i],file['Inscription.xlsx']['CODE_CONCOURS'][i]) , file['Inscription.xlsx']['CLASSE'][i] , file['Inscription.xlsx']['PUISSANCE'][i] , etab(file['Inscription.xlsx']['CODE_ETABLISSEMENT'][i],file['Inscription.xlsx']['ETABLISSEMENT'][i]) , file['Inscription.xlsx']['EPREUVE1'][i] , file['Inscription.xlsx']['OPTION1'][i] , file['Inscription.xlsx']['LIBELLE_VILLE_ECRIT'][i] , bac(file['Inscription.xlsx']['ANNEE_BAC'][i] , file['Inscription.xlsx']['MOIS_BAC'][i] , file['Inscription.xlsx']['SERIE'][i], file['Inscription.xlsx']['CODE_SERIE'][i]), mention(file['Inscription.xlsx']['MENTION'][i]) , bacdep(file['Inscription.xlsx']['CAN_DEP_BAC'][i]) , file['Inscription.xlsx']['SUJET_TIPE'][i] , prof(file['Inscription.xlsx']['COD_CSP_PERE'][i],file['Inscription.xlsx']['LIB_CSP_PERE'][i]) , prof(file['Inscription.xlsx']['COD_CSP_MERE'][i],file['Inscription.xlsx']['LIB_CSP_MERE'][i]) , boursier(file['Inscription.xlsx']['QUALITE'][i])) )

    if file['Inscription.xlsx']['VOIE'][i] == 'MP':
        c.execute(req_spe_info_si, (int(file['Inscription.xlsx']['CODE_CANDIDAT'][i]), file['Inscription.xlsx']['OPTION2'][i]) )

### TABLE CANDIDAT
# INSERTION CANDIDAT ATS
tab = file['ADMISSIBLE_ATS.xlsx']
for i in range(taille['ADMISSIBLE_ATS.xlsx']):
    c.execute(req_ajout_ats, (int(tab['Can _cod'][i]), civ(tab['Civ _lib'][i]), tab['Nom'][i], tab['Prenom'][i], tab['Can _ad 1'][i], tab['Can _ad 2'][i], int(tab['Can _cod _pos'][i]), tab['Can _com'][i], ajout_pays(tab['Can _pay _adr'][i]), tab['Can _mel'][i], tab['Can _tel'][i], tab['Can _por'][i]) )


### TABLE ETABLISSEMENT
# Parcours de listeEtablissements.xlsx
for i in range(taille['listeEtablissements.xlsx']):
    code_etablissement = file['listeEtablissements.xlsx']['Rne'][i]
    etablissement = file['listeEtablissements.xlsx']['Etab'][i]
    if code_etablissement in Dic_etab and Dic_etab[code_etablissement] == etablissement:
        c.execute(req_etab_upd, (file['listeEtablissements.xlsx']['Type _etab'][i], file['listeEtablissements.xlsx']['Ville _etab'][i], int(file['listeEtablissements.xlsx']['Code _postal _etab'][i]), ajout_pays(file['listeEtablissements.xlsx']['Pays _atab'][i]), code_etablissement ) )
    elif not(code_etablissement in Dic_etab):
        Dic_etab[code_etablissement] = etablissement
        c.execute(req_etab_new, (code_etablissement, etablissement, file['listeEtablissements.xlsx']['Type _etab'][i], file['listeEtablissements.xlsx']['Ville _etab'][i], int(file['listeEtablissements.xlsx']['Code _postal _etab'][i]), ajout_pays(file['listeEtablissements.xlsx']['Pays _atab'][i])) )


### TABLE Ecole
for i in range(taille['listeEcoles.xlsx']):
    c.execute(req_ecole, (int(file['listeEcoles.xlsx']['Ecole'][i]), file['listeEcoles.xlsx']['Nom _ecole'][i]) )

### TABLE Voeux
for fichier in fichiers_Voeux:
    for i in range(taille[fichier]):
        c.execute(req_voeux, (int(file[fichier]['Can _cod'][i]), int(file[fichier]['Eco _cod'][i]), int(file[fichier]['Voe _ord'][i])) )

### TABLE EtatReponse
for i in range(taille['listeEtatsReponsesAppel.xlsx']):
    c.execute(req_etat_rep, (int(file['listeEtatsReponsesAppel.xlsx']['Ata _cod'][i]), file['listeEtatsReponsesAppel.xlsx']['Ata _lib'][i]) )


### TABLE rang_ecrit
## requetes
req_rang_ecrit = "insert into rang_ecrit (candidat_id, rang_ecrit) values (?,?)"

tab = file['ADMISSIBLE_PT-SPE.xlsx']
for i in range(taille['ADMISSIBLE_PT-SPE.xlsx']):
    c.execute(req_rang_ecrit, (int(tab['Can _cod'][i]), int(tab['rang'][i])) )

for k in range(4):  # ajout du rang_ecrit des fichiers admissible normal ATS, MP, PC et PSI
    tab=file[fichiers_admissible_normal[k]]
    for i in range(taille[fichiers_admissible_normal[k]]):
        if not math.isnan(tab['rang'][i]):
            c.execute(req_rang_ecrit, (int(tab['Can _cod'][i]), int(tab['rang'][i])) )

### TABLE resultat
## requetes
req_resultat = "insert into resultat (candidat_id, rang, total, moyenne) values (?,?,?,?)"
req_rang_oral_total = "insert into rang_oral (candidat_id, total_oral) values (?,?)"
 
for fichier in fichiers_Classes_csv:
    tab = file[fichier]
    for i in range(taille[fichier]):
        if not math.isnan(tab['rang_classe'][i]) or not math.isnan(tab['total_points'][i]) or not math.isnan(tab['moyenne_generale'][i]):
            c.execute(req_resultat, (int(tab['scei'][i]), int(tab['rang_classe'][i]), float(tab['total_points'][i].replace(',','.')), float(tab['moyenne_generale'][i].replace(',','.'))) )
        if type(tab['total_oral'][i]) == str:
            c.execute(req_rang_oral_total, (int(tab['scei'][i]), float(tab['total_oral'][i].replace(',','.'))) )

### TABLE Note_Ecrit
##requetes
req_ecrit_ATS = "insert into Ecrit_Note_ATS (candidat_id, Math, Phy, Fr, Ang, SI, total_ecrit, moyenne_ecrit) values (?,?,?,?,?,?,?,?)"
req_ecrit_MP = "insert into Ecrit_Note_MP (candidat_id, Math1, Math2, Phy1, Phy2, Chimie, Fr, LV1, IPT, Spe, total_ecrit) values (?,?,?,?,?,?,?,?,?,?,?)"
req_ecrit_PC = "insert into Ecrit_Note_PC (candidat_id, Math1, Math2, Phy1, Phy2, Chimie, Fr, LV1, IPT, total_ecrit) values (?,?,?,?,?,?,?,?,?,?)"
req_ecrit_PSI = "insert into Ecrit_Note_PSI (candidat_id, Math1, Math2, Phy1, Phy2, Chimie, Fr, LV1, IPT, SI, total_ecrit) values (?,?,?,?,?,?,?,?,?,?,?)"
req_ecrit_PT = "insert into Ecrit_Note_PT (candidat_id, Math1, Math2, Phy1, Phy2, Info_Model, SI, Fr, LV1, total_ecrit) values (?,?,?,?,?,?,?,?,?,?)"
req_ecrit_TSI = "insert into Ecrit_Note_TSI (candidat_id, Math1, Math2, Phy1, Phy2, Fr, LV1, SI, Info, total_ecrit) values (?,?,?,?,?,?,?,?,?,?)"

### TABLE Note_Oral
##requetes
req_oral_A = "insert into Oral_Note_A (candidat_id, Math, Phy_SI, Entr, Ang) values (?,?,?,?,?)"
req_oral_A_TSI = "insert into Oral_Note_A_TSI (candidat_id, Math1, Math2, Phy1, Phy2, LV, TP_Phy, S2I) values (?,?,?,?,?,?,?,?)"

req_oral_B = "insert into Oral_Note_B (candidat_id, Math, QCM_Phy_Info, Entr, QCM_Ang) values (?,?,?,?,?)"

req_oral_ATS = "insert into Oral_Note_ATS (candidat_id, Math, Phy, Genie_Elec, Genie_Meca, LV) values (?,?,?,?,?,?)"

req_oral_opt = "insert into Oral_Note_Opt (candidat_id, QCM_Phy_Info, QCM_Ang) values (?,?,?)"


### TABLE CENTRE
Dic_centre = {}
Dic_jury = {}
centre_id = -1
jury_id = -1

##requetes
req_centre = "insert into Centre (centre_id, Centre) values (?,?)"
req_jury = "insert into Jury (jury_id, Jury, centre_id) values (?,?,?)"
req_centre_jury = "insert into Centre_Jury (candidat_id, jury_id) values (?,?)"

def centre(centre,jury):
    global centre_id
    global jury_id
    if jury in Dic_jury:
        return Dic_jury[jury]
    else:
        jury_id +=1
        Dic_jury[jury] = jury_id
        if not (centre in Dic_centre):
            # ajout du nouveau centre
            centre_id += 1
            Dic_centre[centre] = centre_id
            c.execute(req_centre, (centre_id,centre))   
        # ajout du nouveau jury
        c.execute(req_jury, (jury_id, jury, Dic_centre[centre]) )
        return jury_id

def note(x):
    if not(0<=x and x<=20):
        return None
    else:
        return float(x)

### TABLE Note_Oral_A
# Les MP et PC passent Physique
for fichier in ['CMT_Oraux_YYYY_MP.xlsx', 'CMT_Oraux_YYYY_PC.xlsx']:
    tab = file[fichier]
    for i in range(taille[fichier]):
        if (0<=tab['Maths'][i] and tab['Maths'][i]<=20):
            c.execute(req_oral_A, (int(tab["Numéro d'inscription"][i]), note(tab['Maths'][i]), note(tab['Phys.'][i]), note(tab['Entretien'][i]), note(tab['Anglais'][i])) )
        if type(tab['Centre'][i]) != float and file[fichier]['Centre'][i] != ' ':
            c.execute(req_centre_jury, (int(tab["Numéro d'inscription"][i]), centre(tab['Centre'][i],tab['Jury'][i])) )

# Les PSI et PT passent SI    
for fichier in ['CMT_Oraux_YYYY_PSI.xlsx', 'CMT_Oraux_YYYY_PT.xlsx']:
    tab = file[fichier]
    for i in range(taille[fichier]):
        if (0<=tab['Maths'][i] and tab['Maths'][i]<=20):
            c.execute(req_oral_A, (int(tab["Numéro d'inscription"][i]), note(tab['Maths'][i]), note(tab['S.I.'][i]), note(tab['Entretien'][i]), note(tab['Anglais'][i])) )
        if type(tab['Centre'][i]) != float and file[fichier]['Centre'][i] != ' ':
            c.execute(req_centre_jury, (int(tab["Numéro d'inscription"][i]), centre(tab['Centre'][i],tab['Jury'][i])) )
        
### TABLE Note_Ecrit_MP & TABLE Note_Oral_MP_A & TABLE Note_Oral_MP_B
### TABLE Note_Oral_Opt

tab = file['Classes_MP_CMT_spe_XXXX.xlsx']
for i in range(taille['Classes_MP_CMT_spe_XXXX.xlsx']):
    c.execute(req_ecrit_MP, (int(tab['login'][i]), note(tab['600 (Mathématiques 1)'][i]), note(tab['601 ( Mathématiques 2)'][i]), note(tab['602 (Physique 1)'][i]), note(tab['603 (Physique 2)'][i]), note(tab['604 (Chimie)'][i]), note(tab['605 (Français)'][i]), note(tab['28 (Langue)'][i]), note(tab['1050 (Informatique)'][i]), note(tab['599 (Informatique ou Sciences industrielles)'][i]), float(tab['total_ecrit'][i])) )

    if tab['type_admissible'][i] == 'A': 
        if not math.isnan(tab['1 (QCM info/physique)'][i]):
            c.execute(req_oral_opt, (int(tab['login'][i]), note(tab['1 (QCM info/physique)'][i]), note(tab['3 (QCM anglais)'][i])) )

    else:
        c.execute(req_oral_B, (int(tab['login'][i]), note(tab['401 (Mathématiques (affichée))'][i]), note(tab['1 (QCM info/physique)'][i]), note(tab['2 (Entretien nouvelles technologies)'][i]), note(tab['3 (QCM anglais)'][i])) )

### TABLE Note_Ecrit_PC
tab = file['Classes_PC_CMT_spe_XXXX.xlsx']
for i in range(taille['Classes_PC_CMT_spe_XXXX.xlsx']):
    c.execute(req_ecrit_PC, (int(tab['login'][i]), note(tab['600 (Mathématiques 1)'][i]), note(tab['601 ( Mathématiques 2)'][i]), note(tab['602 (Physique 1)'][i]), note(tab['603 (Physique 2)'][i]), note(tab['604 (Chimie)'][i]), note(tab['605 (Français)'][i]), note(tab['28 (Langue)'][i]), note(tab['1050 (Informatique)'][i]), float(tab['total_ecrit'][i])) )

    if tab['type_admissible'][i] == 'A':
        if not math.isnan(tab['1 (QCM info/physique)'][i]):
            c.execute(req_oral_opt, (int(tab['login'][i]), note(tab['1 (QCM info/physique)'][i]), note(tab['3 (QCM anglais)'][i])) )

    else:
        c.execute(req_oral_B, (int(tab['login'][i]), note(tab['401 (Mathématiques (affichée))'][i]), note(tab['1 (QCM info/physique)'][i]), note(tab['2 (Entretien nouvelles technologies)'][i]), note(tab['3 (QCM anglais)'][i])) )

### TABLE Note_Ecrit_PSI
tab = file['Classes_PSI_CMT_spe_XXXX.xlsx']
for i in range(taille['Classes_PSI_CMT_spe_XXXX.xlsx']):
    c.execute(req_ecrit_PSI, (int(tab['login'][i]), note(tab['600 (Mathématiques 1)'][i]), note(tab['601 ( Mathématiques 2)'][i]), note(tab['602 (Physique 1)'][i]), note(tab['603 (Physique 2)'][i]), note(tab['604 (Chimie)'][i]), note(tab['605 (Français)'][i]), note(tab['28 (Langue)'][i]), note(tab['1050 (Informatique)'][i]), note(tab['606 (Sciences industrielles)'][i]), float(tab['total_ecrit'][i])) )

    if tab['type_admissible'][i] == 'A':
        if not math.isnan(tab['1 (QCM info/physique)'][i]):
            c.execute(req_oral_opt, (int(tab['login'][i]), note(tab['1 (QCM info/physique)'][i]), note(tab['3 (QCM anglais)'][i])) )

    else:
        c.execute(req_oral_B, (int(tab['login'][i]), note(tab['401 (Mathématiques (affichée))'][i]), note(tab['1 (QCM info/physique)'][i]), note(tab['2 (Entretien nouvelles technologies)'][i]), note(tab['3 (QCM anglais)'][i])) )

### TABLE Note_Ecrit_PT
tab = file['Classes_PT_CMT_spe_XXXX.xlsx']
for i in range(taille['Classes_PT_CMT_spe_XXXX.xlsx']):
    c.execute(req_ecrit_PT, (int(tab['login'][i]), note(tab['700 (Mathématiques B)'][i]), note(tab['701 (Mathématiques C)'][i]), note(tab['702 (Physique A)'][i]), note(tab['703 (Physique B)'][i]), note(tab['704 (Informatique modélisation)'][i]), note(tab['705 (Sciences industrielles A)'][i]), note(tab['706 (Français B)'][i]), note(tab['707 (Langue A)'][i]), float(tab['total_ecrit'][i])) )

    if tab['type_admissible'][i] == 'A':
        if not math.isnan(tab['1 (QCM info/physique)'][i]):
            c.execute(req_oral_opt, (int(tab['login'][i]), note(tab['1 (QCM info/physique)'][i]), note(tab['3 (QCM anglais)'][i])) )

    else:
        c.execute(req_oral_B, (int(tab['login'][i]), note(tab['401 (Mathématiques (affichée))'][i]), note(tab['1 (QCM info/physique)'][i]), note(tab['2 (Entretien nouvelles technologies)'][i]), note(tab['3 (QCM anglais)'][i])) )

### TABLE Note_Ecrit_TSI
tab = file['Classes_TSI_CMT_spe_XXXX.xlsx']
for i in range(taille['Classes_TSI_CMT_spe_XXXX.xlsx']):
    c.execute(req_ecrit_TSI, (int(tab['login'][i]), note(tab['800 (Mathématiques 1)'][i]), note(tab['801 (Mathématiques 2)'][i]), note(tab['802 (Physique 1)'][i]), note(tab['803 (Physique 2)'][i]), note(tab['804 (Français)'][i]), note(tab['805 (Langue)'][i]), note(tab['806 (Sciences industrielles)'][i]), note(tab['807 (Informatique)'][i]), float(tab['total_ecrit'][i])) )
    c.execute(req_rang_ecrit, (int(tab['login'][i]), int(tab['rang_admissible'][i])) )
    if tab['type_admissible'][i] == 'A':
        c.execute(req_oral_A_TSI, (int(tab['login'][i]), note(tab['13 (Mathématiques 1)'][i]), note(tab['14 (Mathématiques 2)'][i]), note(tab['15 (Physique-chimie 1)'][i]), note(tab['16 (Physique-chimie 2)'][i]), note(tab['17 (Langue vivante)'][i]), note(tab['18 (TP Physique-chimie)'][i]), note(tab['19 (S2I)'][i])) )
    else:
        c.execute(req_oral_B, (int(tab['login'][i]), note(tab['4 (Mathématiques)'][i]), note(tab['1 (QCM info/physique)'][i]), note(tab['2 (Entretien nouvelles technologies)'][i]), note(tab['3 (QCM anglais)'][i])) )

def moyenne_ats(i):
    tab = file['ResultatEcrit_DD_MM_YYYY_ATS.xlsx']
    if note(tab['Mathématiques'][i])==None or note(tab['Sc. Physiques'][i])==None or note(tab['Français'][i])==None or note(tab['Anglais'][i])==None or note(tab['Sciences Industrielles'][i])==None:
        return None
    else:
        return float(tab['Moyenne'][i])

def total_ats(i):
    tab = file['ResultatEcrit_DD_MM_YYYY_ATS.xlsx']
    if note(tab['Mathématiques'][i])==None or note(tab['Sc. Physiques'][i])==None or note(tab['Français'][i])==None or note(tab['Anglais'][i])==None or note(tab['Sciences Industrielles'][i])==None:
        return None
    else:
        return float(tab['Total'][i])

### TABLE Note_Ecrit_ATS
tab = file['ResultatEcrit_DD_MM_YYYY_ATS.xlsx']
for i in range(1,taille['ResultatEcrit_DD_MM_YYYY_ATS.xlsx']):
    if note(tab['Mathématiques'][i])!=None and note(tab['Sc. Physiques'][i])!=None and note(tab['Français'][i])!=None and note(tab['Anglais'][i])!=None and note(tab['Sciences Industrielles'][i])!=None:
        c.execute(req_ecrit_ATS, (int(tab["Numéro d'inscription"][i]), note(tab['Mathématiques'][i]), note(tab['Sc. Physiques'][i]), note(tab['Français'][i]), note(tab['Anglais'][i]), note(tab['Sciences Industrielles'][i]), total_ats(i), moyenne_ats(i)) )

### TABLE Note_Oral_ATS
tab = file['ResultatOral_DD_MM_YYYY_ATS.xlsx']
for i in range(1,taille['ResultatOral_DD_MM_YYYY_ATS.xlsx']):
    if note(tab['Mathématiques'][i]) and note(tab['Sciences Physiques'][i]) and note(tab['Génie électrique'][i]) and note(tab['Génie mécanique'][i]) and note(tab['Langue au choix (oral commun)'][i]):
        c.execute(req_oral_ATS, (tab["Numéro d'inscription"][i], note(tab['Mathématiques'][i]), note(tab['Sciences Physiques'][i]), note(tab['Génie électrique'][i]), note(tab['Génie mécanique'][i]), note(tab['Langue au choix (oral commun)'][i])) )
    
    if not math.isnan(tab['Rang'][i]):
        c.execute(req_resultat, (tab["Numéro d'inscription"][i], int(tab['Rang'][i]), float(tab['Total'][i]), float(tab['Moyenne'][i])) )
    else:
        c.execute(req_resultat, (tab["Numéro d'inscription"][i], i, float(tab['Total'][i]), float(tab['Moyenne'][i])) )

### TABLE rang_oral
##requetes
req_rang_oral_rang = "UPDATE rang_oral SET rang_oral = ? WHERE candidat_id = ?"

for fichier in fichiers_Oral:
    tab = file[fichier]
    for i in range(taille[fichier]):
        if not math.isnan(tab['rang'][i]):
            c.execute(req_rang_oral_rang, (int(tab['rang'][i]), int(tab['Can _cod'][i])) )

### TABLE Candidat Statut_admission
## requetes
req_admission_upd = "UPDATE Candidat SET Statut_admission = ? WHERE candidat_id = ?"
req_type_adm = "insert into type_admissible (candidat_id,type_admissible) values (?,?)"

# pour retenir les candidats dont l'admission est deja etablit 
liste_admission = []
liste_type_admission = []

for fichier in fichiers_admis_spe:
    tab = file[fichier]
    for i in range(taille[fichier]):
        c.execute(req_admission_upd, ("ADMIS", int(tab['Can _cod'][i])) )
        
        liste_admission.append(tab['Can _cod'][i])

fichier = 'ADMIS_ATS.xlsx'
tab = file[fichier]
for i in range(taille[fichier]):
    c.execute(req_admission_upd, ("ADMIS", int(tab['Can _cod'][i])) )
    liste_admission.append(tab['Can _cod'][i])


for fichier in fichiers_admissible_normal:
    tab = file[fichier]
    for i in range(taille[fichier]):
        c.execute(req_type_adm, (int(tab['Can _cod'][i]), "A") )
        liste_type_admission.append(tab['Can _cod'][i])

for fichier in fichiers_admissible_spe:
    tab = file[fichier]
    for i in range(taille[fichier]):
        if not(tab['Can _cod'][i] in liste_admission):
            c.execute(req_admission_upd, ("ADMISSIBLE", int(tab['Can _cod'][i])) )
        if not(tab['Can _cod'][i] in liste_type_admission):
            c.execute(req_type_adm, (int(tab['Can _cod'][i]), "B") )
        
fichier = 'ADMISSIBLE_ATS.xlsx'
tab = file[fichier]
for i in range(taille[fichier]):
    if not(tab['Can _cod'][i] in liste_admission):
        c.execute(req_admission_upd, ("ADMISSIBLE", int(tab['Can _cod'][i])) )


conn.commit()
conn.close()
