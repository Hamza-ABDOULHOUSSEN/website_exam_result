from flask import Flask, request, render_template, g
from wtforms import Form, StringField, SelectField, IntegerField, validators
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
        res = list(zip(coordinates, scolarship, wishes))
        tags = ["Coordonnées", "Scolarité", "Vœux"]

    return res, tags, query


def buildCoordinates(req):
    # req permet de dire sur quoi on fait la recherche. INE, id ou nom prenom
    identite = "SELECT candidat_id, INE, Civ, Nom, Prenom, Autres_Prenoms, Date_Naissance, Ville_Naissance, Adresse1, Code_Postal, Commune, Pays.pays, Email, Telephone, Portable FROM Candidat JOIN Pays ON Pays.code_pays = Candidat.Pays_id " + req + " ORDER BY nom"
    c = GetDB().cursor()
    c.execute(identite)
    content = []
    for t in c.fetchall():
        id = "ID : " + str(t[0])
        INE = "INE : " + str(t[1])
        nom = str(t[2]) + ". " + str(t[3]) + " " + str(t[4])
        if t[5] is not None:
            nom += " " + t[5]
        naissance = "Né le " + str(t[6]) + " à " + str(t[7])
        adresse = "Adresse : " + str(t[8]) + ", " + str(t[9]) + " " + str(t[10]) + ", " + str(t[11])
        mail = "Email : " + str(t[12])
        telephone = "Téléphone fixe : "
        if t[13] is None:
            telephone += "Aucun"
        else:
            telephone += str(t[13])
        portable = "Téléphone portable : "
        if t[14] is None:
            portable += "Aucun"
        else:
            portable += str(t[14])

        content.append((id, INE, nom, naissance, adresse, mail, telephone, portable))
    return content


def buildScolarship(req):
    scolar = "SELECT Nom, Classe, Filliere, Puissance, E.etablissement, E.CP, E.Ville, Epreuve1, LV, Ville_ecrit, B.serie, Bac_Mention, Sujet_TIPE, Candidat.Boursier FROM Candidat JOIN Etablissement E on Candidat.Etablissement_id = E.code_etablissement JOIN Bac B on B.bac_id = Candidat.Bac_id " + req + " ORDER BY Nom"
    c = GetDB().cursor()
    c.execute(scolar)
    content = []
    for t in c.fetchall():
        filliere = "Filliere : " + str(t[2])
        classe = "Classe : " + str(t[1])
        puissance = "Année : " + str(t[3])
        etablissement = "Etablissement : " + str(t[4]) + ", " + str(t[5]) + ", " + str(t[6])
        epreuve = "Epreuve : " + str(t[7]) + " - " + str(t[8]) + " à " + str(t[9])
        bac = "Baccalauréat : " + str(t[10]) + " - Mention : "
        if t[11] != "":
            bac += str(t[11])
        else:
            bac += "Aucune"

        tipe = "Sujet TIPE : " + str(t[12])
        boursier = "Boursier : " + str(t[13])

        content.append((filliere, classe, puissance, etablissement, epreuve, bac, tipe, boursier))
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
    for id in c.fetchall():
        wishesReq = f"SELECT E.nom, Voeux.ordre FROM Voeux JOIN Ecole E on Voeux.ecole_id = E.ecole_id WHERE Voeux.candidat_id = '{id[0]}' ORDER BY Voeux.ordre"
        d.execute(wishesReq)
        content.append([t[0] for t in d.fetchall()])

    return content


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
