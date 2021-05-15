import sqlite3

DATABASE = "CMT_database.db"
conn = sqlite3.connect(DATABASE)
c = conn.cursor()


# TABLE Candidat
# INSERTION CANDIDAT 44232 en PC
# Le candidat 44232 est en ligne  1162

req = "insert into Candidat (candidat_id, Civ, Nom, Prenom, Adresse1, Code_Postal, Commune, Pays_id, Email, Portable, Filliere, Puissance) values (44232,'Mr','Rolland','Marcel','64, rue Jules Fernandez','73721','Sainte Adrienne',0,'cecile49@fontaine.net','01 28 65 85 39','PC','3/2')"
c.execute(req)

conn.commit()
conn.close()