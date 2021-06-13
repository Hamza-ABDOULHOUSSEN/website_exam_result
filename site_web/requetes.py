from flask import g
import sqlite3

DATABASE = "CMT_database.db"


def BuildRequest(args):
    if "INE" in args and "name" in args and "FirstName" in args and len(args) == 3:
        # on a fait une demande de candidat avec un ID
        INE = args["INE"]
        name = args["name"]
        FirstName = args["FirstName"]
        req = f"WHERE LOWER(INE) = LOWER('{INE}') " \
              f"AND LOWER(Nom) = LOWER('{name}') " \
              f"AND LOWER(Prenom) = LOWER('{FirstName}')"

        res = None
        tags = None

        if req != "":
            coordinates = buildCoordinates(req)
            scolarship = buildScolarship(req)
            wishes = buildWishes(req)
            jury = buildJury(req)
            notes_ecrit = buildNotesEcrit(req)
            notes_oral = buildNotesOral(req)
            etat_admis = buildEtatAdmis(req)
            res = list(zip(coordinates, scolarship, wishes, jury, notes_ecrit, notes_oral, etat_admis))
            tags = ["Coordonnées", "Scolarité", "Vœux", "Jury et centre d'examen", "Notes écrit", "Notes des oraux",
                    "Résultat et admissibilité"]
        return res, tags, "all"


def buildCoordinates(req):
    # req permet de dire sur quoi on fait la recherche. INE, ID ou nom prenom
    identite = f"SELECT C.candidat_id, C.INE, C.Civ, C.Nom, C.Prenom, C.Autres_Prenoms, C.Date_Naissance, C.Ville_Naissance, Pays_naissance.pays, C.Francais, Pays_autre.pays, " \
               f"C.Adresse1, C.Code_Postal, C.Commune, PAddr.pays, C.Email, C.Telephone, C.Portable, P1.profession, P2.profession " \
               f"FROM Candidat AS C " \
               f"JOIN Pays PAddr ON PAddr.code_pays = C.Pays_id " \
               f"JOIN Pays Pays_naissance ON Pays_naissance.code_pays = C.Pays_Naissance_id " \
               f"JOIN Pays Pays_autre ON Pays_autre.code_pays  = C.Autre_Nationalite_id " \
               f"JOIN Profession P1 on P1.code_profession = C.Profession_pere_code " \
               f"JOIN Profession P2 on P2.code_profession = C.Profession_mere_code " \
               f"{req} " \
               f"ORDER BY Nom"

    c = GetDB().cursor()
    c.execute(identite)
    content = []
    for t in c.fetchall():
        ID = f"ID : {str(t[0])}"
        INE = f"INE : {str(t[1])}"
        nom = f"{str(t[2])}. {str(t[3])} {str(t[4])}"
        if t[5] is not None:
            nom += " " + str(t[5])
        naissance = f"Né le {str(t[6])} à {str(t[7])}, {str(t[8])}"
        francais = f"Français : {str(t[9])}"
        autre_nationalite = f"Autre nationalité : "
        if t[10] is None:
            autre_nationalite += "Aucune"
        else:
            autre_nationalite += str(t[10])
        adresse = f"Adresse n°1 : {str(t[11])}, {str(t[12])}, {str(t[13])}, {str(t[14])}"
        mail = f"Email : {str(t[15])}"
        telephone = "Téléphone fixe : "
        if t[16] is None:
            telephone += "Aucun"
        else:
            telephone += str(t[16])
        portable = "Téléphone portable : "
        if t[17] is None:
            portable += "Aucun"
        else:
            portable += str(t[17])
        CSP_pere = f"Catégorie socio-professionnelle du père : {str(t[18])}"
        CSP_mere = f"Catégorie socio-professionnelle de la mère : {str(t[19])}"

        content.append((ID, INE, nom, naissance, francais, autre_nationalite, adresse, mail, telephone, portable,
                        CSP_pere, CSP_mere))
    return content


def buildScolarship(req):
    scolar = f"SELECT Nom, Classe, Filliere, Puissance, E.etablissement, E.Ville, E.CP, Epreuve1, LV, Ville_ecrit, Code_Serie_Bac.serie, Bac_Mention, Sujet_TIPE, Boursier " \
             f"FROM Candidat " \
             f"JOIN Etablissement E ON Candidat.Etablissement_id = E.code_etablissement " \
             f"JOIN Bac B ON Candidat.Bac_id = B.bac_id " \
             f"JOIN Code_Serie_Bac ON B.code_serie = Code_Serie_Bac.code_serie" \
             f" {req} " \
             f"ORDER BY Nom"
    c = GetDB().cursor()
    c.execute(scolar)
    content = []
    for t in c.fetchall():
        classe = "Classe : " + str(t[1])
        filliere = "Filliere : " + str(t[2])
        puissance = "Année : " + str(t[3])
        etablissement = "Etablissement : " + str(t[4])
        if t[5] is not None:
            etablissement += ", " + str(t[5])
        if t[6] is not None:
            etablissement += ", " + str(t[6])
        epreuve = "Epreuve : " + str(t[7]) + " - " + str(t[8]) + " à " + str(t[9])
        bac = "Baccalauréat : " + str(t[10]) + " - Mention : "
        if t[11] != "":
            bac += str(t[11])
        else:
            bac += "Aucune"

        TIPE = "Sujet TIPE : " + str(t[12])
        boursier = "Boursier : " + str(t[13])

        content.append((filliere, classe, puissance, etablissement, epreuve, bac, TIPE, boursier))
    return content


def buildWishes(req):
    # puisqu'une personne a fait plusieurs voeux, il faut prendre en compte ce cas
    # on en peut pas simplement faire un join avec la table des voeux, c'est surtout
    # important dans le cas où on peut avoir plusieurs personnes pour un même nom - prénom
    ids = "SELECT candidat_id, nom FROM Candidat " + req + " ORDER BY nom"
    c = GetDB().cursor()
    d = GetDB().cursor()
    c.execute(ids)
    content = []
    for ID in c.fetchall():
        wishesReq = f"SELECT E.nom, Voeux.ordre " \
                    f"FROM Voeux " \
                    f"JOIN Ecole E ON Voeux.ecole_id = E.ecole_id " \
                    f"WHERE Voeux.candidat_id = '{ID[0]}' " \
                    f"ORDER BY Voeux.ordre"

        d.execute(wishesReq)
        content.append([t[0] for t in d.fetchall()])

    return content


def buildJury(req):
    req = req.replace("candidat_id", "Candidat.candidat_id")
    req = req.replace("Nom", "Candidat.Nom")
    req = req.replace("Prenom", "Candidat.Prenom")
    req = req.replace("INE", "Candidat.INE")
    candidatReq = f"SELECT Nom, candidat_id " \
                  f"FROM Candidat " \
                  f"{req} " \
                  f"ORDER BY Nom"
    jury_centre = []

    candidat = GetDB().cursor()
    jury = GetDB().cursor()
    candidat.execute(candidatReq)
    for personne in candidat.fetchall():
        added = False
        juryReq = f"SELECT Jury, Centre " \
                  f"FROM Centre_Jury " \
                  f"JOIN Candidat C on Centre_Jury.candidat_id = C.candidat_id " \
                  f"JOIN Jury J on Centre_Jury.jury_id = J.jury_id " \
                  f"JOIN Centre C2 on J.centre_id = C2.centre_id " \
                  f"WHERE C.candidat_id = '{personne[1]}'"
        jury.execute(juryReq)
        for j in jury.fetchall():
            added = True
            jury_centre.append((
                "Jury : " + str(j[0]),
                "Centre d'examen : " + str(j[1])
            ))
        if not added:
            jury_centre.append(())

    return jury_centre


def buildNotesEcrit(req):
    noteReq = "SELECT candidat_id, Nom, Filliere FROM Candidat " + req + " ORDER BY Nom"
    c = GetDB().cursor()
    d = GetDB().cursor()
    notes = []
    c.execute(noteReq)
    added = False
    for t in c.fetchall():
        if t[2] == "ATS":
            d.execute(f"SELECT * FROM Ecrit_Note_ATS WHERE candidat_id = '{t[0]}'")
            for note_individu in d.fetchall():
                added = True
                notes.append((
                    ("Math", note_individu[0]),
                    ("Physique", note_individu[1]),
                    ("Français", note_individu[2]),
                    ("Anglais", note_individu[3]),
                    ("SI", note_individu[4]),
                    ("Total", note_individu[5]),
                ))
        elif t[2] == "MP":
            d.execute(f"SELECT * FROM Ecrit_Note_MP WHERE candidat_id = '{t[0]}'")
            for note_individu in d.fetchall():
                added = True
                notes.append((
                    ("Math 1", note_individu[1]),
                    ("Math 2", note_individu[2]),
                    ("Physique 1", note_individu[3]),
                    ("Physique 2", note_individu[4]),
                    ("Chimie", note_individu[5]),
                    ("Français", note_individu[6]),
                    ("LV1", note_individu[7]),
                    ("IPT", note_individu[8]),
                    ("Spe", note_individu[9]),
                    ("Total", note_individu[10])
                ))
        elif t[2] == "PC":
            d.execute(f"SELECT * FROM Ecrit_Note_PC WHERE candidat_id = '{t[0]}'")
            for note_individu in d.fetchall():
                notes.append((
                    ("Math 1", note_individu[1]),
                    ("Math 2", note_individu[2]),
                    ("Physique 1", note_individu[3]),
                    ("Physique 2", note_individu[4]),
                    ("Chimie", note_individu[5]),
                    ("Français", note_individu[6]),
                    ("LV1", note_individu[7]),
                    ("IPT", note_individu[8]),
                    ("Total", note_individu[9])
                ))
                added = True
        elif t[2] == "PSI":
            d.execute(f"SELECT * FROM Ecrit_Note_PSI WHERE candidat_id = '{t[0]}'")
            for note_individu in d.fetchall():
                added = True
                notes.append((
                    ("Math 1", note_individu[1]),
                    ("Math 2", note_individu[2]),
                    ("Physique 1", note_individu[3]),
                    ("Physique 2", note_individu[4]),
                    ("Chimie", note_individu[5]),
                    ("Français", note_individu[6]),
                    ("LV1", note_individu[7]),
                    ("IPT", note_individu[8]),
                    ("SI", note_individu[9]),
                    ("Total", note_individu[10])
                ))
        elif t[2] == "PT":
            d.execute(f"SELECT * FROM Ecrit_Note_PT WHERE candidat_id = '{t[0]}'")
            for note_individu in d.fetchall():
                added = True
                notes.append((
                    ("Math 1", note_individu[1]),
                    ("Math 2", note_individu[2]),
                    ("Physique 1", note_individu[3]),
                    ("Physique 2", note_individu[4]),
                    ("Informatique et modélisation", note_individu[5]),
                    ("SI", note_individu[6]),
                    ("Français", note_individu[7]),
                    ("LV1", note_individu[8]),
                    ("Total", note_individu[9])
                ))
        elif t[2] == "TSI":
            d.execute(f"SELECT * FROM Ecrit_Note_TSI WHERE candidat_id = '{t[0]}'")
            for note_individu in d.fetchall():
                added = True
                notes.append((
                    ("Math 1", note_individu[1]),
                    ("Math 2", note_individu[2]),
                    ("Physique 1", note_individu[3]),
                    ("Physique 2", note_individu[4]),
                    ("Français", note_individu[5]),
                    ("LV1", note_individu[6]),
                    ("SI", note_individu[7]),
                    ("Total", note_individu[8])
                ))
        if not added:
            notes.append(())
    return notes

def buildNotesOral(req):
    # req = req.replace("candidat_id", "C.candidat_id")
    # req = req.replace("Nom", "C.Nom")
    # req = req.replace("Prenom", "C.Prenom")
    # req = req.replace("INE", "C.INE")
    filiereReq = f"SELECT candidat_id, Nom, Filliere FROM Candidat " \
                 f"{req} " \
                 f"ORDER BY Nom "
    filiereDB = GetDB().cursor()
    filiereDB.execute(filiereReq)

    noteDB = GetDB().cursor()
    notes = []
    for candidat in filiereDB.fetchall():
        if candidat[2] == "ATS":
            noteReq = f"SELECT * FROM Oral_Note_ATS WHERE candidat_id = '{candidat[0]}'"
            noteDB.execute(noteReq)
            for note in noteDB.fetchall():
                notes.append((
                    ("Math", note[1]),
                    ("Physique", note[2]),
                    ("Génie Electrique", note[3]),
                    ("Génie mécanique", note[4]),
                    ("Langue vivante", note[5])
                ))
        elif candidat[2] == "TSI":
            noteReq = f"SELECT * FROM Oral_Note_A_TSI WHERE candidat_id = '{candidat[0]}'"
            noteDB.execute(noteReq)
            for note in noteDB.fetchall():
                notes.append((
                    ("Math 1", note[1]),
                    ("Math 2", note[2]),
                    ("Physique 1", note[3]),
                    ("Physique 2", note[4]),
                    ("Langue vivante", note[5]),
                    ("TP physique", note[6]),
                    ("Sciences industrielles de l'ingénieur", note[7])
                ))
        else:
            note_candidat = []
            noteReq = f"SELECT * FROM Oral_Note_A WHERE candidat_id = '{candidat[0]}'"
            noteDB.execute(noteReq)

            if candidat[1] in ["MP", "PC"]:
                matiere = "Physique"
            else:
                matiere = "Sciences de l'ingénieur"

            for note in noteDB.fetchall():
                note_candidat.append(("Math A", note[1]))
                note_candidat.append((matiere, note[2]))
                note_candidat.append(("Entretien", note[3]))
                note_candidat.append(("Anglais", note[4]))

            noteReq = f"SELECT * FROM Oral_Note_B WHERE candidat_id = '{candidat[0]}'"
            noteDB.execute(noteReq)

            for note in noteDB.fetchall():
                note_candidat.append(("Math B", note[1]))
                note_candidat.append(("QCM Physique Info", note[2]))
                note_candidat.append(("Entretien", note[3]))
                note_candidat.append(("QCM Anglais", note[4]))

            noteReq = f"SELECT * FROM Oral_Note_Opt WHERE candidat_id = '{candidat[0]}'"
            noteDB.execute(noteReq)

            for note in noteDB.fetchall():
                note_candidat.append(("QCM Physique Info", note[1]))
                note_candidat.append(("QCM Anglais", note[2]))

            notes.append(note_candidat)

    return notes

def buildEtatAdmis(req):
    admisReq = f"SELECT candidat_id, Nom, Statut_admission " \
               f"FROM Candidat " \
               f"{req} " \
               f"ORDER BY Nom"
    admisDB = GetDB().cursor()
    rangDB = GetDB().cursor()

    # plusieurs curseurs sont nécéssaires car tous les
    # candidats ne sont pas présents dans toutes les tables
    admisDB.execute(admisReq)
    statuts = []
    for candidat in admisDB.fetchall():
        rangEcritReq = f"SELECT rang_ecrit FROM rang_ecrit WHERE candidat_id = '{candidat[0]}'"
        rangOralReq = f"SELECT rang_oral FROM rang_oral WHERE candidat_id = '{candidat[0]}'"
        rangTotalReq = f"SELECT * FROM resultat WHERE candidat_id = '{candidat[0]}'"
        type_admissible = candidat[2]
        rangEcrit = ""
        rangOral = ""
        rangTotal = ""
        noteTotale = ""
        moyenneTotale = ""

        rangDB.execute(rangEcritReq)
        for rang in rangDB.fetchall():
            rangEcrit = rang[0]

        rangDB.execute(rangOralReq)
        for rang in rangDB.fetchall():
            rangOral = rang[0]

        rangDB.execute(rangTotalReq)
        for resume in rangDB.fetchall():
            rangTotal = resume[1]
            noteTotale = resume[2]
            moyenneTotale = resume[3]

        result = []
        if not type_admissible:
            type_admissible = "NON ADMIS"

        result.append(("Type admissible", str(type_admissible)))

        if not rangEcrit:
            rangEcrit = "Aucun"
        result.append(("Rang écrit", rangEcrit))

        if not rangOral:
            rangOral = "Aucun"
        result.append(("Rang oral", rangOral))

        if not rangTotal:
            rangTotal = "Aucun"
        result.append(("Rang total", rangTotal))

        if not noteTotale:
            noteTotale = "Aucun"
        result.append(("Note totale", noteTotale))

        if not moyenneTotale:
            moyenneTotale = "Aucun"
        result.append(("Moyenne totale", moyenneTotale))

        statuts.append(result)

    return statuts


def buildGlobalResults():
    filieres = ["ATS", "MP", "PC", "PSI", "PT", "TSI"]
    count = buildTotalCount(filieres)
    admissible, admis = buildAdmissibiliteCount(filieres, count)
    return count, admissible, admis


def buildTotalCount(filieres):
    count_filiere = []
    DB = GetDB().cursor()
    for filiere in filieres:  # boucle pour récupérer le nombre de candidat par filière
        count_filiere.append((
            filiere,
            DB.execute(f"SELECT COUNT(*) FROM Candidat WHERE Filliere = '{filiere}'").fetchall()[0][0]
        ))
    count_filiere.append(("Total", DB.execute("SELECT COUNT(*) FROM Candidat").fetchall()[0][0]))

    return count_filiere


def buildAdmissibiliteCount(filieres, counts):
    countsAdmissible = []
    countsAdmis = []
    DB = GetDB().cursor()
    for i in range(len(filieres)):
        countAdmissible = int(DB.execute(f"SELECT COUNT(*) "
                                         f"FROM Candidat "
                                         f"WHERE (Statut_admission = 'ADMISSIBLE' "
                                         f"OR Statut_admission = 'ADMIS') "
                                         f"AND (Filliere = '{filieres[i]}')"
                                         ).fetchall()[0][0])
        pourcentageAdmissible = int(10000 * countAdmissible / int(counts[i][1])) / 100
        countsAdmissible.append((filieres[i], str(countAdmissible), str(pourcentageAdmissible)))

        countAdmis = int(DB.execute(f"SELECT COUNT(*) "
                                    f"FROM Candidat "
                                    f"WHERE Statut_admission = 'ADMIS' "
                                    f"AND Filliere = '{filieres[i]}'"
                                    ).fetchall()[0][0])
        pourcentageAdmis = int(10000 * countAdmis / int(counts[i][1])) / 100
        countsAdmis.append((filieres[i], str(countAdmis), str(pourcentageAdmis)))

    countTotalAdmissible = DB.execute(f"SELECT COUNT(*) "
                                      f"FROM Candidat "
                                      f"WHERE Statut_admission = 'ADMISSIBLE' "
                                      f"OR Statut_admission = 'ADMIS'"
                                      ).fetchall()[0][0]

    countTotalAdmis = DB.execute(f"SELECT COUNT(*) "
                                 f"FROM Candidat "
                                 f"WHERE Statut_admission = 'ADMIS'"
                                 ).fetchall()[0][0]

    countsAdmissible.append(
        ("Total", countTotalAdmissible, str(int(10000 * countTotalAdmissible / counts[-1][1]) / 100)))

    countsAdmis.append(
        ("Total", countTotalAdmis, str(int(10000 * countTotalAdmis / counts[-1][1]) / 100)))

    return countsAdmissible, countsAdmis


def buildVoeuxDemande():
    filieres = ["ATS", "MP", "PC", "PSI", "PT", "TSI"]

    countCandidat = int(GetDB().cursor().execute("SELECT COUNT(Nom) FROM Candidat").fetchall()[0][0])
    ecoleReq = "SELECT DISTINCT * FROM Ecole"
    ecoleDB = GetDB().execute(ecoleReq)
    voeuxDB = GetDB()
    voeuxCount = []

    for ecole in ecoleDB.fetchall():
        voeuxTotalReq = f"SELECT COUNT(Voeux.candidat_id) FROM Voeux WHERE ecole_id = '{ecole[0]}'"
        voeuxFiliereCount = []

        for f in filieres:
            voeuxFiliereReq = f"SELECT COUNT(Voeux.candidat_id) " \
                              f"FROM Voeux " \
                              f"JOIN Ecole E on E.ecole_id = Voeux.ecole_id " \
                              f"JOIN Candidat C on Voeux.candidat_id = C.candidat_id " \
                              f"WHERE E.ecole_id = '{ecole[0]}' AND C.Filliere = '{f}'"
            countFiliere = int(voeuxDB.execute(voeuxFiliereReq).fetchall()[0][0])
            voeuxFiliereCount.append(countFiliere)
        somme = sum(voeuxFiliereCount)
        ecoleList = [ecole[1]] + voeuxFiliereCount + [somme] + [int(10000 * somme / countCandidat) / 100]
        voeuxCount.append(ecoleList)

    element8 = lambda x: x[7]
    voeuxCount.sort(key = element8, reverse = True)
    return voeuxCount


def buildNomEcole():
    ecoleReq = "SELECT nom FROM Ecole"
    nom = [t[0] for t in GetDB().execute(ecoleReq).fetchall()]
    nom.sort()
    nom.insert(0, "Toutes les écoles")
    ids = list(range(0, len(nom) + 1))
    return list(zip(ids, nom))


def buildNomMatiereEcrit():
    matieres = ["Mathématiques 1", "Mathématiques 2", "Physique 1", "Physique 2",
                "Chimie", "Français", "LV1", "IPT", "SI",
                "Informatique et modélisation", "Informatique", "Mathématiques",
                "Physique", "Anglais", "Spe"]

    res = ["Toutes les matières", "Tous les écrits", "Tous les oraux"]

    for m in matieres:
        res += ["Ecrit - " + m]

    return res

def buildNomMatiereOral():
    matieres = ["Mathématiques", "Physique_SI", "Entretien", "Anglais", "QCM Physique Informatique",
                "QCM Anglais", "Mathématiques 1", "Mathématiques 2", "Physique 1", "Physique 2",
                "LV", "TP Physique", "S2I", "Physique", "Génie Electrique", "Génie Mécanique"]

    res = []

    for m in matieres:
        res += ["Oral - " + m]

    return res


def buildNomMatiere():
    return buildNomMatiereEcrit() + buildNomMatiereOral()


def buildStatsEcrit():
    filieresEcrit = [["PSI", "PC", "PT", "TSI", "MP"],
                     ["PSI", "PC", "PT", "TSI", "MP"],
                     ["PSI", "PC", "PT", "TSI", "MP"],
                     ["PSI", "PC", "PT", "TSI", "MP"],
                     ["PSI", "PC", "MP"],
                     ["PSI", "PC", "PT", "TSI", "MP", "ATS"],
                     ["PSI", "PC", "PT", "TSI", "MP"],
                     ["PSI", "PC", "MP"],
                     ["PSI", "PT", "TSI", "ATS"],
                     ["PT"],
                     ["TSI"],
                     ["ATS"],
                     ["ATS"],
                     ["ATS"],
                     ["MP"]]

    matieresNom = buildNomMatiereEcrit()

    matieresAbrev = ["Math1",
                     "Math2",
                     "Phy1",
                     "Phy2",
                     "Chimie",
                     "Fr",
                     "LV1",
                     "IPT",
                     "SI",
                     "Info_Model",
                     "Info",
                     "Math",
                     "Phy",
                     "Ang",
                     "Spe"]

    filieresOral = [["A", "B", "ATS"],
                     ["A"],
                     ["A","B"],
                     ["A"],
                     ["B","Opt"],
                     ["B","Opt"],
                     ["A_TSI"],
                     ["A_TSI"],
                     ["A_TSI"],
                     ["A_TSI"],
                     ["A_TSI","ATS"],
                     ["A_TSI"],
                     ["A_TSI"],
                     ["ATS"],
                     ["ATS"],
                     ["ATS"]]

    matieresNomOral = buildNomMatiereOral()

    matieresAbrevOral = ["Math",
                         "Phy_SI",
                         "Entr",
                         "Ang",
                         "QCM_Phy_Info",
                         "QCM_Ang",
                         "Math1",
                         "Math2",
                         "Phy1",
                         "Phy2",
                         "LV",
                         "TP_Phy",
                         "S2I",
                         "Phy",
                         "Genie_Elec",
                         "Genie_Meca"]


    res = []

    c = GetDB().cursor()
    d = GetDB().cursor()

    for i in range(len(filieresEcrit)):
        moy = 0;
        nb = 0;

        for f in filieresEcrit[i]:
            c.execute("SELECT sum(" + matieresAbrev[i] + ") FROM Ecrit_Note_" + f)
            d.execute("SELECT count(" + matieresAbrev[i] + ") FROM Ecrit_Note_" + f)
            moy += c.fetchall()[0][0]
            nb += d.fetchall()[0][0]

        moy = round(moy / nb, 2)

        res += [[matieresNom[i+3], moy, nb]]

    for i in range(len(filieresOral)):
        moy = 0;
        nb = 0;

        for f in filieresOral[i]:
            c.execute("SELECT sum(" + matieresAbrevOral[i] + ") FROM Oral_Note_" + f)
            d.execute("SELECT count(" + matieresAbrevOral[i] + ") FROM Oral_Note_" + f)
            moy += c.fetchall()[0][0]
            nb += d.fetchall()[0][0]

        moy = round(moy / nb, 2)

        res += [[matieresNomOral[i], moy, nb]]

    return res


def GetDB():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
