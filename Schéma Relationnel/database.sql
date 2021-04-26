CREATE TABLE Candidat(
    candidat_id   INTEGER PRIMARY KEY,
    Civ           TEXT NOT NULL,
    Nom           TEXT NOT NULL,
    Prenom        TEXT NOT NULL,
    Naissance     TEXT NOT NULL,
    Adresse1      TEXT NOT NULL,
    Adresse2      TEXT NOT NULL,
    Code_Postal   INTEGER  NOT NULL,
    Commune       TEXT NOT NULL,
    Pays          TEXT NOT NULL,
    Email         TEXT NOT NULL,
    Telephone     TEXT,
    Portable      TEXT,
    Filliere      TEXT NOT NULL,
    Statut        TEXT,
    Etablissement TEXT
);

CREATE TABLE Classement_Note_MP(
    candidat_id  INTEGER PRIMARY KEY,
    Math1        DOUBLE,
    Math2        DOUBLE,
    Phy1         DOUBLE,
    Phy2         DOUBLE,
    Chimie       DOUBLE,
    Fr           DOUBLE,
    LV1          DOUBLE,
    IPT          DOUBLE,
    Spe          DOUBLE,
    bonification INTEGER,
    total_ecrit  DOUBLE,
    rang_ecrit   INTEGER,
    Math_oral    DOUBLE,
    Phy_oral     DOUBLE,
    Fr_oral      DOUBLE,
    Ang_oral     DOUBLE,
    total_oral   DOUBLE,
    total        DOUBLE,
    rang         INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Classement_Note_PSI(
    candidat_id  INTEGER PRIMARY KEY,
    Math1        DOUBLE,
    Math2        DOUBLE,
    Phy1         DOUBLE,
    Phy2         DOUBLE,
    Chimie       DOUBLE,
    Fr           DOUBLE,
    LV1          DOUBLE,
    IPT          DOUBLE,
    SI           DOUBLE,
    bonification INTEGER,
    total_ecrit  DOUBLE,
    rang_ecrit   INTEGER,
    Math_oral    DOUBLE,
    Phy_oral     DOUBLE,
    Fr_oral      DOUBLE,
    Ang_oral     DOUBLE,
    total_oral   DOUBLE,
    total        DOUBLE,
    rang         INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Classement_Note_PC(
    candidat_id  INTEGER PRIMARY KEY,
    Math1        DOUBLE,
    Math2        DOUBLE,
    Phy1         DOUBLE,
    Phy2         DOUBLE,
    Chimie       DOUBLE,
    Fr           DOUBLE,
    LV1          DOUBLE,
    IPT          DOUBLE,
    bonification INTEGER,
    total_ecrit  DOUBLE,
    rang_ecrit   INTEGER,
    Math_oral    DOUBLE,
    Phy_oral     DOUBLE,
    Fr_oral      DOUBLE,
    Ang_oral     DOUBLE,
    total_oral   DOUBLE,
    total        DOUBLE,
    rang         INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Classement_Note_PT(
    candidat_id  INTEGER PRIMARY KEY,
    Math1        DOUBLE,
    Math2        DOUBLE,
    Phy1         DOUBLE,
    Phy2         DOUBLE,
    Info_Model   DOUBLE,
    SI           DOUBLE,
    Fr           DOUBLE,
    LV1          DOUBLE,
    bonification INTEGER,
    total_ecrit  DOUBLE,
    rang_ecrit   INTEGER,
    Math_oral    DOUBLE,
    Phy_oral     DOUBLE,
    Fr_oral      DOUBLE,
    Ang_oral     DOUBLE,
    total_oral   DOUBLE,
    total        DOUBLE,
    rang         INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Classement_Note_TSI(
    candidat_id  INTEGER PRIMARY KEY,
    Math1        DOUBLE,
    Math2        DOUBLE,
    Phy1         DOUBLE,
    Phy2         DOUBLE,
    Fr           DOUBLE,
    LV1          DOUBLE,
    SI           DOUBLE,
    Info         DOUBLE,
    bonification INTEGER,
    total_ecrit  DOUBLE,
    rang_ecrit   INTEGER,
    Math1_oral   DOUBLE,
    Math2_oral   DOUBLE,
    Phy1_oral    DOUBLE,
    Phy2_oral    DOUBLE,
    LV_oral      DOUBLE,
    TP_Phy_oral  DOUBLE,
    S2I_oral     DOUBLE,
    total_oral   DOUBLE,
    total        DOUBLE,
    rang         INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Classement_Note_ATS(
    candidat_id      INTEGER PRIMARY KEY,
    Math             DOUBLE,
    Phy              DOUBLE,
    Fr               DOUBLE,
    Ang              DOUBLE,
    SI               DOUBLE,
    bonification     INTEGER,
    moyenne_ecrit    DOUBLE,
    total_ecrit      DOUBLE,
    rang_ecrit       INTEGER,
    Math_oral        DOUBLE,
    Phy_oral         DOUBLE,
    Genie_elec_oral  DOUBLE,
    Genie_meca_oral  DOUBLE,
    LV_oral          DOUBLE,
    Epreuve_ATS_oral DOUBLE,
    moyenne_oral     DOUBLE,
    total_oral       DOUBLE,
    rang_oral        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Etablissement(
    Etablissement TEXT PRIMARY KEY,
    Type          TEXT,
    Ville         TEXT,
    CP            INTEGER,
    Pays          TEXT,
    FOREIGN KEY (Etablissement) REFERENCES Candidat (Etablissement)
);

CREATE TABLE Ecole(
    ecole_id INTEGER PRIMARY KEY,
    nom      TEXT,
    FOREIGN KEY (ecole_id) REFERENCES Voeux (ecole_id)
);

CREATE TABLE Voeux(
    candidat_id INTEGER,
    ecole_id    INTEGER,
    ordre       INTEGER,
    PRIMARY KEY (candidat_id, ecole_id)
);

CREATE TABLE Admission_ATS(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_ATS(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admission_MP(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_MP(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_MP_SPE(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admission_PC(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_PC(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_PC_SPE(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admission_PSI(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_PSI(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_PSI_SPE(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admission_PT(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_PT(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_PT_SPE(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admission_TSI(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_TSI(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_TSI_SPE(
    candidat_id INTEGER PRIMARY KEY,
    rang        INTEGER,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);
