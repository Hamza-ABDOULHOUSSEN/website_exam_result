CREATE TABLE Candidat(
    candidat_id   int PRIMARY KEY,
    Civ           text NOT NULL,
    Nom           text NOT NULL,
    Prenom        text NOT NULL,
    Naissance     text NOT NULL,
    Adresse1      text NOT NULL,
    Adresse2      text NOT NULL,
    Code_Postal   int  NOT NULL,
    Commune       text NOT NULL,
    Pays          text NOT NULL,
    Email         text NOT NULL,
    Telephone     text,
    Portable      text,
    Filliere      text NOT NULL,
    Statut        text,
    Etablissement text
);

CREATE TABLE Classement_Note_MP(
    candidat_id  int PRIMARY KEY,
    Math1        double,
    Math2        double,
    Phy1         double,
    Phy2         double,
    Chimie       double,
    Fr           double,
    LV1          double,
    IPT          double,
    Spe          double,
    bonification int,
    total_ecrit  double,
    rang_ecrit   int,
    Math_oral    double,
    Phy_oral     double,
    Fr_oral      double,
    Ang_oral     double,
    total_oral   double,
    total        double,
    rang         int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Classement_Note_PSI(
    candidat_id  int PRIMARY KEY,
    Math1        double,
    Math2        double,
    Phy1         double,
    Phy2         double,
    Chimie       double,
    Fr           double,
    LV1          double,
    IPT          double,
    SI           double,
    bonification int,
    total_ecrit  double,
    rang_ecrit   int,
    Math_oral    double,
    Phy_oral     double,
    Fr_oral      double,
    Ang_oral     double,
    total_oral   double,
    total        double,
    rang         int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Classement_Note_PC(
    candidat_id  int PRIMARY KEY,
    Math1        double,
    Math2        double,
    Phy1         double,
    Phy2         double,
    Chimie       double,
    Fr           double,
    LV1          double,
    IPT          double,
    bonification int,
    total_ecrit  double,
    rang_ecrit   int,
    Math_oral    double,
    Phy_oral     double,
    Fr_oral      double,
    Ang_oral     double,
    total_oral   double,
    total        double,
    rang         int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Classement_Note_PT(
    candidat_id  int PRIMARY KEY,
    Math1        double,
    Math2        double,
    Phy1         double,
    Phy2         double,
    Info_Model   double,
    SI           double,
    Fr           double,
    LV1          double,
    bonification int,
    total_ecrit  double,
    rang_ecrit   int,
    Math_oral    double,
    Phy_oral     double,
    Fr_oral      double,
    Ang_oral     double,
    total_oral   double,
    total        double,
    rang         int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Classement_Note_TSI(
    candidat_id  int PRIMARY KEY,
    Math1        double,
    Math2        double,
    Phy1         double,
    Phy2         double,
    Fr           double,
    LV1          double,
    SI           double,
    Info         double,
    bonification int,
    total_ecrit  double,
    rang_ecrit   int,
    Math1_oral   double,
    Math2_oral   double,
    Phy1_oral    double,
    Phy2_oral    double,
    LV_oral      double,
    TP_Phy_oral  double,
    S2I_oral     double,
    total_oral   double,
    total        double,
    rang         int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Classement_Note_ATS(
    candidat_id      int PRIMARY KEY,
    Math             double,
    Phy              double,
    Fr               double,
    Ang              double,
    SI               double,
    bonification     int,
    moyenne_ecrit    double,
    total_ecrit      double,
    rang_ecrit       int,
    Math_oral        double,
    Phy_oral         double,
    Genie_elec_oral  double,
    Genie_meca_oral  double,
    LV_oral          double,
    Epreuve_ATS_oral double,
    moyenne_oral     double,
    total_oral       double,
    rang_oral        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Etablissement(
    Etablissement text PRIMARY KEY,
    Type          text,
    Ville         text,
    CP            int,
    Pays          text,
    FOREIGN KEY (Etablissement) REFERENCES Candidat (Etablissement)
);

CREATE TABLE Ecole(
    ecole_id int PRIMARY KEY,
    nom      text,
    FOREIGN KEY (ecole_id) REFERENCES Voeux (ecole_id)
);

CREATE TABLE Voeux(
    candidat_id int,
    ecole_id    int,
    ordre       int,
    PRIMARY KEY (candidat_id, ecole_id)
);

CREATE TABLE Admission_ATS(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_ATS(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admission_MP(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_MP(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_MP_SPE(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admission_PC(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_PC(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_PC_SPE(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admission_PSI(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_PSI(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_PSI_SPE(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admission_PT(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_PT(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_PT_SPE(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admission_TSI(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_TSI(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);

CREATE TABLE Admis_TSI_SPE(
    candidat_id int PRIMARY KEY,
    rang        int,
    FOREIGN KEY (candidat_id) REFERENCES Candidat (candidat_id)
);
