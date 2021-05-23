from flask import Flask, request, render_template, g
from wtforms import Form, StringField, IntegerField
from wtforms.validators import input_required
import sqlite3

DATABASE = "CMT_database.db"


class IdForm(Form):
    id = IntegerField('ID du candidat', validators = [input_required()])


class NameForm(Form):
    name = StringField('Nom du candidat', validators = [input_required()])
    FirstName = StringField('Prénom du candidat', validators = [input_required()])


class IneForm(Form):
    INE = StringField('INE du candidat', validators = [input_required()])


app = Flask(__name__)


@app.route('/', methods = ["GET"])
def index():
    return render_template("index.html")


@app.route('/candidats', methods = ["GET"])
def candidates():
    idForm = IdForm(request.form)
    nameForm = NameForm(request.form)
    ineForm = IneForm(request.form)
    arguments = request.args
    query = "none"
    result = None
    tags = None
    count = 0
    if len(arguments) != 0:
        result, tags, query = BuildRequest(arguments)
        count = len(result)
    return render_template("candidates.html", idForm = idForm, nameForm = nameForm, ineForm = ineForm,
                           result = result, tags = tags,
                           query = query, count = count)


@app.route('/resultats', methods = ["GET"])
def results():
    return render_template("results.html")


@app.route('/about', methods = ["GET"])
def about():
    return render_template("about.html")


@app.errorhandler(404)
def errorPage(e):
    return render_template("404.html"), 404


def BuildRequest(args):
    query = ""
    req = ""

    if "id" in args and len(args) == 1:
        # on a fait une demande de candidat avec un ID
        ID = args["id"]
        req = f"WHERE candidat_id = '{ID}'"
        query = "id"

    elif "name" in args and "FirstName" in args and len(args) == 2:
        name = args["name"]
        FirstName = args["FirstName"]
        req = f"WHERE Nom = '{name}' AND Prenom = '{FirstName}'"
        query = "name"

    elif "INE" in args and len(args) == 1:
        ine = args["INE"]
        req = f"WHERE INE = '{ine}'"
        query = "INE"

    res = None
    tags = None

    if req != "":
        coordinates = buildCoordinates(req)
        scolarship = buildScolarship(req)
        wishes = buildWishes(req)
        notes = buildNotes(req)
        res = list(zip(coordinates, scolarship, wishes, notes))
        tags = ["Coordonnées", "Scolarité", "Vœux", "Notes"]
    return res, tags, query


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
    scolar = f"SELECT Nom, Classe, Filliere, Puissance, E.etablissement, E.Ville, E.CP, Epreuve1, LV, Ville_ecrit, Code_Serie_Bac.serie, Bac_Mention, Sujet_TIPE, Boursier "\
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


def buildNotes(req):
    note = "SELECT candidat_id, Nom, Filliere FROM Candidat " + req + " ORDER BY Nom"
    c = GetDB().cursor()
    d = GetDB().cursor()
    notes = []
    c.execute(note)
    for t in c.fetchall():
        if t[2] == "ATS":
            d.execute(f"SELECT * FROM Ecrit_Note_ATS WHERE candidat_id = '{t[0]}'")
        elif t[2] == "MP":
            d.execute(f"SELECT * FROM Ecrit_Note_MP WHERE candidat_id = '{t[0]}'")
        elif t[2] == "PC":
            d.execute(f"SELECT * FROM Ecrit_Note_PC WHERE candidat_id = '{t[0]}'")
        elif t[2] == "PSI":
            d.execute(f"SELECT * FROM Ecrit_Note_PSI WHERE candidat_id = '{t[0]}'")
        elif t[2] == "PT":
            d.execute(f"SELECT * FROM Ecrit_Note_PT WHERE candidat_id = '{t[0]}'")
        elif t[2] == "TSI":
            d.execute(f"SELECT * FROM Ecrit_Note_TSI WHERE candidat_id = '{t[0]}'")

        notes.append(d.fetchall())

    return notes


def GetDB():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def CloseConnection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run()
