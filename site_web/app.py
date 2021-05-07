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
    count = 0
    if len(arguments) != 0:
        result, query = BuildRequest(arguments)
        count = len(result)
    return render_template("candidates.html", idForm = idForm, nameForm = nameForm, ineForm = ineForm,
                           result = result,
                           query = query, count = count)


@app.route('/resultats', methods = ["GET"])
def results():
    return render_template("results.html")


@app.route('/about', methods = ["GET"])
def about():
    return render_template("about.html")


def BuildRequest(args):
    if "id" in args and len(args) == 1:
        # on a fait une demande de candidat avec un ID
        ID = args["id"]
        req = f"SELECT * FROM Candidat WHERE candidat_id = '{ID}'"
        content = buildCoordinates(req)
        return content, "id"
    elif "name" in args and "FirstName" in args and len(args) == 2:
        name = args["name"]
        FirstName = args["FirstName"]
        req = f"SELECT * FROM Candidat WHERE Nom = '{name}' AND Prenom = '{FirstName}'"
        content = buildCoordinates(req)
        return content, "name"
    elif "INE" in args and len(args) == 1:
        ine = args["INE"]
        req = f"SELECT * FROM Candidat WHERE INE = '{ine}'"
        content = buildCoordinates(req)
        return content, "INE"
    else:
        return None


def buildCoordinates(req):
    c = GetDB().cursor()
    c.execute(req)
    content = [(t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8]) for t in c.fetchall()]
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
