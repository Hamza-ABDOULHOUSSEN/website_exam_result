import sqlite3
import pandas as pd

DATABASE = "CMT_database.db"
conn = sqlite3.connect(DATABASE)
c = conn.cursor()

dirPath = "../data/public/"

file = dirPath + 'Inscription.xlsx'

df = pd.read_excel(file, skiprows=1)

(nb_ligne,_) = df.shape



### TABLE Candidat xxx TABLE Bac

# Dictionnaire des differents bac
Dic_Bac = {}
Bac_id = -1

# requetes
req = "insert into Candidat (candidat_id,INE, Civ, Nom, Prenom, Autres_Prenoms, Date_Naissance, Ville_Naissance, Pays_Naissance_id, Francais, Autre_Nationalite_id, Adresse1, Adresse2, Code_Postal, Commune, Pays_id, Email, Telephone, Portable, Filliere, Classe, Puissance, Statut, Etablissement, Epreuve1, LV, Ville_ecrit, Bac_id, Bac_Mention, Bac_dep, Sujet_TIPE, Profession_pere_code, Profession_mere_code, Boursier) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
req_bac = "insert into Bac (bac_id, annee, mois, serie, code_serie) values (?,?,?,?,?)"

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

def b(s):
    if s == ' ':
        return 0
    if s == 'Boursier':
        return 1

def ine(x):
    if type(x) != str:
        return 'non indique'
    else:
        return x

def bac(annee,mois,serie,codeserie):
    global Bac_id
    if (annee,mois,serie) in Dic_Bac:
        return Dic_Bac[(annee,mois,serie)]
    else:
        Bac_id +=1
        Dic_Bac[(annee,mois,serie)] = Bac_id
        c.execute(req_bac, (Bac_id, annee, mois, serie, codeserie) )
        return Bac_id


for i in range(nb_ligne):
    c.execute(req, (int(df['CODE_CANDIDAT'][i]) , ine(df['NUMERO_INE'][i]) ,  civ(df['CIVILITE'][i]) , df['NOM'][i] , df['PRENOM'][i] , df['AUTRES_PRENOMS'][i] , df['DATE_NAISSANCE'][i] , df['VILLE_NAISSANCE'][i] , int(df['CODE_PAYS_NAISSANCE'][i]) ,  int(df['FRANCAIS'][i]) , int(df['CODE_PAYS_NATIONALITE'][i]) , df['ADRESSE1'][i] , df['ADRESSE2'][i] , int(df['CP'][i]) , df['VILLE'][i] , int(df['CODE_PAYS'][i]) , df['EMAIL'][i] , df['TELEPHONE'][i] , df['TEL_PORTABLE'][i] , df['VOIE'][i] , df['CLASSE'][i] , df['PUISSANCE'][i] , 'Admis' , df['CODE_ETABLISSEMENT'][i] , df['EPREUVE1'][i] , df['OPTION1'][i] , df['LIBELLE_VILLE_ECRIT'][i] , bac(int(df['ANNEE_BAC'][i]) , int(df['MOIS_BAC'][i]) , df['SERIE'][i], int(df['CODE_SERIE'][i])), df['MENTION'][i] , bacdep(df['CAN_DEP_BAC'][i]) , df['SUJET_TIPE'][i] , int(df['COD_CSP_PERE'][i]) , int(df['COD_CSP_MERE'][i]) , b(df['QUALITE'][i])) )


conn.commit()
conn.close()
