import sqlite3

DATABASE = "CMT_database.db"
conn = sqlite3.connect(DATABASE)
c = conn.cursor()


# TABLE Candidat
# INSERTION CANDIDAT 44232 en PC
# Le candidat 44232 est en ligne  1162

req = "insert into Candidat (candidat_id, Civ, Nom, Prenom, Adresse1, Code_Postal, Commune, Pays_id, Email, Portable, Filliere, Puissance, Statut_admission) values (44232,'Mr','Rolland','Marcel','64, rue Jules Fernandez','73721','Sainte Adrienne',0,'cecile49@fontaine.net','01 28 65 85 39','PC','3/2', 'ADMIS')"
c.execute(req)

req_resultat = "insert into resultat (candidat_id, rang, total) values (70066,1125,738.75)"
req_rang_oral_total = "insert into rang_oral (candidat_id, total_oral) values (70066,409)"
c.execute(req_resultat)
c.execute(req_rang_oral_total)

conn.commit()
conn.close()