CREATE TABLE "Candidat" (
	"candidat_id"	INT,
	"INE"	TEXT NOT NULL,
	"Civ"	TEXT NOT NULL,
	"Nom"	TEXT NOT NULL,
	"Prenom"	TEXT NOT NULL,
	"Autres_Prenoms"	TEXT,
	"Date_Naissance"	TEXT NOT NULL,
	"Ville_Naissance"	TEXT,
	"Pays_Naissance_id"	INT,
	"Francais"	TEXT,
	"Autre_Nationalite_id"	INT,
	"Adresse1"	TEXT NOT NULL,
	"Adresse2"	TEXT,
	"Code_Postal"	INTEGER NOT NULL,
	"Commune"	TEXT NOT NULL,
	"Pays_id"	INT NOT NULL,
	"Email"	TEXT NOT NULL,
	"Telephone"	TEXT,
	"Portable"	TEXT,
	"Filliere"	TEXT NOT NULL,
	"Classe"	TEXT,
	"Puissance"	TEXT,
	"Etablissement_id"	TEXT,
	"Epreuve1"	TEXT,
	"LV"	TEXT,
	"Ville_ecrit"	TEXT,
	"Bac_id"	INT,
	"Bac_Mention"	TEXT,
	"Bac_dep"	TEXT,
	"Sujet_TIPE"	TEXT,
	"Profession_pere_code"	INT,
	"Profession_mere_code"	INT,
	"Boursier"	TEXT,
	FOREIGN KEY("Bac_id") REFERENCES "Bac"("bac_id"),
	FOREIGN KEY("Filliere") REFERENCES "Code_Concours"("Filliere"),
	FOREIGN KEY("Profession_pere_code") REFERENCES "Profession"("code_profession"),
	FOREIGN KEY("Profession_mere_code") REFERENCES "Profession"("code_profession"),
	FOREIGN KEY("Pays_Naissance_id") REFERENCES "Pays"("code_pays"),
	FOREIGN KEY("Autre_Nationalite_id") REFERENCES "Pays"("code_pays"),
	FOREIGN KEY("Pays_id") REFERENCES "Pays"("code_pays"),
	FOREIGN KEY("Etablissement_id") REFERENCES "Etablissement"("code_etablissement"),
	PRIMARY KEY("candidat_id")
);

CREATE TABLE "Bac" (
	"bac_id"	INT,
	"annee"	INT,
	"mois"	INT,
	"serie"	TEXT,
	FOREIGN KEY("serie") REFERENCES "Code_Serie_Bac"("serie"),
	PRIMARY KEY("bac_id")
);

CREATE TABLE "Code_Serie_Bac" (
	"serie"	TEXT,
	"code_serie"	INT,
	PRIMARY KEY("serie")
);

CREATE TABLE "Code_Concours" (
	"Filliere"	TEXT,
	"code_concours"	INT,
	PRIMARY KEY("Filliere")
);

CREATE TABLE "Profession" (
	"code_profession"	TEXT,
	"profession"	TEXT,
	PRIMARY KEY("code_profession")
);

CREATE TABLE "Pays" (
	"code_pays"	INT,
	"pays"	TEXT,
	"nationalite"	TEXT,
	PRIMARY KEY("code_pays")
);

CREATE TABLE "Etablissement" (
	"code_etablissement"	TEXT,
	"etablissement"	TEXT,
	"Type"	TEXT,
	"Ville"	TEXT,
	"CP"	INT,
	"Pays_id"	INT,
	FOREIGN KEY("Pays_id") REFERENCES "Pays"("code_pays"),
	PRIMARY KEY("code_etablissement")
);
