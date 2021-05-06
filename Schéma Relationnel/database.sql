CREATE TABLE Candidat(
    candidat_id   INTEGER PRIMARY KEY,
    INE           TEXT NOT NULL,
    Civ           TEXT NOT NULL,
    Nom           TEXT NOT NULL,
    Prenom        TEXT NOT NULL,
    Autres_Prenoms TEXT,  
    Date_Naissance     TEXT NOT NULL,
    Ville_Naissance TEXT,
    Pays_Naissance_id INT,
    Francais INT,
    Autre_Nationalite_id INT,   
    Adresse1      TEXT NOT NULL,
    Adresse2      TEXT,
    Code_Postal   INTEGER  NOT NULL,
    Commune       TEXT NOT NULL,
    Pays_id          INT NOT NULL,
    Email         TEXT NOT NULL,
    Telephone     TEXT,
    Portable      TEXT,
    Filliere      TEXT NOT NULL,
    Classe        TEXT,
    Puissance      TEXT,
    Statut        TEXT,
    Etablissement TEXT,

    Epreuve1        TEXT,
    LV              TEXT,
    Ville_ecrit     TEXT,
    Bac_id          INT,
    Bac_Mention     TEXT,
    Bac_dep         TEXT,

    Sujet_TIPE      TEXT,

    Profession_pere_code INT,
    Profession_mere_code INT,
    Boursier INT
);

CREATE TABLE Bac (
  bac_id INT PRIMARY KEY,
  annee INT,
  mois INT,
  serie TEXT,
  code_serie INT,
  FOREIGN KEY (bac_id) REFERENCES Candidat (Bac_id)
);