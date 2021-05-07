import sqlite3
import pandas as pd

DATABASE = "CMT_database.db"
conn = sqlite3.connect(DATABASE)
c = conn.cursor()

dirPath = "../data/public/"

file = dirPath + 'Inscription.xlsx'

df = pd.read_excel(file, skiprows=1)

(nb_ligne,_) = df.shape



### TABLE Candidat

# requetes
req = "insert into Candidat (candidat_id,INE, Civ, Nom, Prenom, Autres_Prenoms, Date_Naissance, Ville_Naissance, Pays_Naissance_id, Francais, Autre_Nationalite_id, Adresse1, Adresse2, Code_Postal, Commune, Pays_id, Email, Telephone, Portable, Filliere, Classe, Puissance, Statut, Etablissement, Epreuve1, LV, Ville_ecrit, Bac_id, Bac_Mention, Bac_dep, Sujet_TIPE, Profession_pere_code, Profession_mere_code, Boursier) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
req_bac = "insert into Bac (bac_id, annee, mois, serie) values (?,?,?,?)"
req_code_serie_bac = "insert into Code_Serie_Bac (serie, code_serie) values (?,?)"
req_code_concours = "insert into Code_Concours (Filliere, code_concours) values (?,?)"
req_profession = "insert into Profession (code_profession, profession) values (?,?)"

req_pays = "insert into Pays (code_pays, pays) values (?,?)"
req_natio = "insert into Pays (code_pays, nationalite) values (?,?)"
req_pays_upd = "UPDATE Pays SET pays = ? WHERE code_pays = ?"
req_natio_upd = "UPDATE Pays SET nationalite = ? WHERE code_pays = ?"

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
    global Bac_id
    if (annee,mois,serie) in Dic_Bac:
        return Dic_Bac[(annee,mois,serie)]
    else:
        Bac_id +=1
        Dic_Bac[(annee,mois,serie)] = Bac_id
        # ajout du nouveau type de Bac
        c.execute(req_bac, (Bac_id, annee, mois, serie))

        # ajout de la nouvelle serie
        if not(serie in Dic_Bac_Serie):
            Dic_Bac_Serie.append(serie)
            c.execute(req_code_serie_bac, (serie,int(codeserie)))

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
Dic_pays = []
Dic_nation = []

def pays(code,pays):
    code = int(code)
    if not(code in Dic_pays):
        Dic_pays.append(code) 
        if code in Dic_nation:
            c.execute(req_pays_upd, (pays,code))
        else:
            c.execute(req_pays, (code,pays))
    return code

def natio(code,natio):
    code = int(code)
    if not(code in Dic_nation):
        Dic_nation.append(code) 
        if code in Dic_pays:
            c.execute(req_natio_upd, (natio,code))
        else:
            c.execute(req_natio, (code,natio))
    return code

# Parcours de Inscription.xlsx
for i in range(nb_ligne):
    c.execute(req, (int(df['CODE_CANDIDAT'][i]) , ine(df['NUMERO_INE'][i]) ,  civ(df['CIVILITE'][i]) , df['NOM'][i] , df['PRENOM'][i] , df['AUTRES_PRENOMS'][i] , df['DATE_NAISSANCE'][i] , df['VILLE_NAISSANCE'][i] , pays(df['CODE_PAYS_NAISSANCE'][i],df['PAYS_NAISSANCE'][i]) ,  francais(df['FRANCAIS'][i]) , natio(df['CODE_PAYS_NATIONALITE'][i],df['AUTRE_NATIONALITE'][i]) , df['ADRESSE1'][i] , df['ADRESSE2'][i] , int(df['CP'][i]) , df['VILLE'][i] , pays(df['CODE_PAYS'][i],df['LIBELLE_PAYS'][i]) , df['EMAIL'][i] , df['TELEPHONE'][i] , df['TEL_PORTABLE'][i] , filliere(df['VOIE'][i],df['CODE_CONCOURS'][i]) , df['CLASSE'][i] , df['PUISSANCE'][i] , 'Admis' , df['CODE_ETABLISSEMENT'][i] , df['EPREUVE1'][i] , df['OPTION1'][i] , df['LIBELLE_VILLE_ECRIT'][i] , bac(df['ANNEE_BAC'][i] , df['MOIS_BAC'][i] , df['SERIE'][i], df['CODE_SERIE'][i]), mention(df['MENTION'][i]) , bacdep(df['CAN_DEP_BAC'][i]) , df['SUJET_TIPE'][i] , prof(df['COD_CSP_PERE'][i],df['LIB_CSP_PERE'][i]) , prof(df['COD_CSP_MERE'][i],df['LIB_CSP_MERE'][i]) , boursier(df['QUALITE'][i])) )


conn.commit()
conn.close()
