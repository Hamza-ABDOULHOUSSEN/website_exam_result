CREATE TABLE "Candidat" (
	"candidat_id"	INT,
	"INE"	TEXT,
	"Civ"	TEXT NOT NULL,
	"Nom"	TEXT NOT NULL,
	"Prenom"	TEXT NOT NULL,
	"Autres_Prenoms"	TEXT,
	"Date_Naissance"	TEXT,
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
  "Statut_admission" TEXT,
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
	"code_serie"	INT,
	FOREIGN KEY("code_serie") REFERENCES "Code_Serie_Bac"("code_serie"),
	PRIMARY KEY("bac_id")
);

CREATE TABLE "Code_Serie_Bac" (
	"code_serie"	INT,
	"serie"	TEXT,
	PRIMARY KEY("code_serie")
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

CREATE TABLE "MP_Spe_Info_SI" (
	candidat_id	INT,
	Spe_Info_SI	TEXT,
	FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
	PRIMARY KEY(candidat_id)
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

CREATE TABLE "Voeux" (
	"candidat_id"	INT,
	"ecole_id"	INT,
	"ordre"	INT,
	FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
	FOREIGN KEY("ecole_id") REFERENCES "Ecole"("ecole_id"),
	PRIMARY KEY("candidat_id","ecole_id","ordre")
);

CREATE TABLE "Ecole" (
	"ecole_id"	INT,
	"nom"	TEXT,
	PRIMARY KEY("ecole_id")
);

CREATE TABLE "EtatReponse" (
	"code"	INT,
	"reponse"	TEXT,
	PRIMARY KEY("code")
);

CREATE TABLE "Ecrit_Note_ATS" (
  candidat_id INT,
  Math	FLOAT,
  Phy	FLOAT,
  Fr	FLOAT,
  Ang	FLOAT,
  SI	FLOAT,
  total_ecrit	FLOAT,
  moyenne_ecrit	FLOAT,
  FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
  PRIMARY KEY("candidat_id")
);

CREATE TABLE "Ecrit_Note_MP" (
  candidat_id INT,
  Math1	FLOAT,
  Math2	FLOAT,
  Phy1	FLOAT,
  Phy2	FLOAT,
  Chimie	FLOAT,
  Fr	FLOAT,
  LV1	FLOAT,
  IPT	FLOAT,
  Spe	FLOAT,
  total_ecrit	FLOAT,
  FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
  PRIMARY KEY("candidat_id")
);

CREATE TABLE "Ecrit_Note_PC" (
  candidat_id INT,
  Math1	FLOAT,
  Math2	FLOAT,
  Phy1	FLOAT,
  Phy2	FLOAT,
  Chimie	FLOAT,
  Fr	FLOAT,
  LV1	FLOAT,
  IPT	FLOAT,
  total_ecrit	FLOAT,
  FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
  PRIMARY KEY("candidat_id")
);

CREATE TABLE "Ecrit_Note_PSI" (
  candidat_id INT,
  Math1	FLOAT,
  Math2	FLOAT,
  Phy1	FLOAT,
  Phy2	FLOAT,
  Chimie	FLOAT,
  Fr	FLOAT,
  LV1	FLOAT,
  IPT	FLOAT,
  SI	FLOAT,
  total_ecrit	FLOAT,
  FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
  PRIMARY KEY("candidat_id")
);

CREATE TABLE "Ecrit_Note_PT" (
  candidat_id INT,
  Math1	FLOAT,
  Math2	FLOAT,
  Phy1	FLOAT,
  Phy2	FLOAT,
  Info_Model	FLOAT,
  SI	FLOAT,
  Fr	FLOAT,
  LV1	FLOAT,
  total_ecrit	FLOAT,
  FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
  PRIMARY KEY("candidat_id")
);

CREATE TABLE "Ecrit_Note_TSI" (
  candidat_id INT,
  Math1	FLOAT,
  Math2	FLOAT,
  Phy1	FLOAT,
  Phy2	FLOAT,
  Fr	FLOAT,
  LV1	FLOAT,
  SI	FLOAT,
  Info	FLOAT,
  total_ecrit	FLOAT,
  FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
  PRIMARY KEY("candidat_id")
);

CREATE TABLE "rang_ecrit" (
  candidat_id INT,
  rang_ecrit	INT,
  FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
  PRIMARY KEY("candidat_id")
);

CREATE TABLE "Oral_Note" (
  candidat_id INT,
  Math	FLOAT,
  Phy_SI	FLOAT,
  Entr	FLOAT,
  Ang	FLOAT,
  FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
  PRIMARY KEY("candidat_id")
);

CREATE TABLE "Oral_Note_TSI" (
  candidat_id INT,
  Math1	FLOAT,
  Math2	FLOAT,
  Phy1	FLOAT,
  Phy2	FLOAT,
  LV	FLOAT,
  TP_Phy	FLOAT,
  S2I	FLOAT,
  FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
  PRIMARY KEY("candidat_id")
);

CREATE TABLE "Oral_Note_B" (
  candidat_id INT,
  Math	FLOAT,
  QCM_Phy_Info	FLOAT,
  Entr	FLOAT,
  QCM_Ang	FLOAT,
  FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
  PRIMARY KEY("candidat_id")
);

CREATE TABLE "Oral_Note_ATS" (
  candidat_id INT,
  Math	FLOAT,
  Phy	FLOAT,
  Genie_Elec	FLOAT,
  Genie_Meca	FLOAT,
  LV	FLOAT,
  FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
  PRIMARY KEY("candidat_id")
);

CREATE TABLE "Oral_Note_Opt" (
  candidat_id INT,
  QCM_Phy_Info	FLOAT,
  QCM_Ang	FLOAT,
  FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
  PRIMARY KEY("candidat_id")
);

CREATE TABLE "rang_oral" (
  candidat_id INT,
  rang_oral	INT,
  total_oral	FLOAT,
  FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
  PRIMARY KEY("candidat_id")
);

CREATE TABLE "resultat" (
  candidat_id INT,
  rang	INT,
  total	FLOAT,
  moyenne FLOAT,
  FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
  PRIMARY KEY("candidat_id")
);

CREATE TABLE "Centre_Jury" (
  candidat_id INT,
  jury_id	INT,
  FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
  FOREIGN KEY("jury_id") REFERENCES "Jury"("jury_id"),
  PRIMARY KEY("candidat_id")
);

CREATE TABLE "Jury" (
  jury_id INT,
  Jury	TEXT,
  centre_id INT,
  FOREIGN KEY("centre_id") REFERENCES "Centre"("centre_id"),
  PRIMARY KEY("jury_id")
);

CREATE TABLE "Centre" (
  centre_id INT,
  Centre	TEXT,
  PRIMARY KEY("centre_id")
);

CREATE TABLE "type_admissible" (
  candidat_id INT,
  type_admissible	TEXT,
  FOREIGN KEY("candidat_id") REFERENCES "Candidat"("candidat_id"),
  PRIMARY KEY("candidat_id")
);