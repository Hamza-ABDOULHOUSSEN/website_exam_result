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
	"Statut"	TEXT,
	"Etablissement"	TEXT,
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
	PRIMARY KEY("candidat_id")
);

CREATE TABLE "Bac" (
	"bac_id"	INT,
	"annee"	INT,
	"mois"	INT,
	"serie"	TEXT,
	FOREIGN KEY("bac_id") REFERENCES "Candidat"("Bac_id"),
	PRIMARY KEY("bac_id")
);

CREATE TABLE "Code_Serie_Bac" (
	"serie"	TEXT,
	"code_serie"	INT,
	FOREIGN KEY("serie") REFERENCES "Bac"("serie"),
	PRIMARY KEY("serie")
);

CREATE TABLE "Code_Concours" (
	"Filliere"	TEXT,
	"code_concours"	INT,
	FOREIGN KEY("Filliere") REFERENCES "Candidat"("Filliere"),
	PRIMARY KEY("Filliere")
);

CREATE TABLE "Profession" (
	"code_profession"	TEXT,
	"profession"	TEXT,
	FOREIGN KEY("code_profession") REFERENCES "Candidat"("Profession_pere_code"),
	FOREIGN KEY("code_profession") REFERENCES "Candidat"("Profession_mere_code"),
	PRIMARY KEY("code_profession")
);

CREATE TABLE "Pays" (
	"code_pays"	INT,
	"pays"	TEXT,
	"nationalite"	TEXT,
	FOREIGN KEY("code_pays") REFERENCES "Candidat"("Pays_Naissance_id"),
	FOREIGN KEY("code_pays") REFERENCES "Candidat"("Autre_Nationalite_id"),
	FOREIGN KEY("code_pays") REFERENCES "Candidat"("Pays_id"),
	PRIMARY KEY("code_pays")
);
