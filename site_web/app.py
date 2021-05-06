from flask import Flask, request, render_template, g
from wtforms import Form, StringField, SelectField, IntegerField, validators
from wtforms.validators import input_required
import sqlite3

path = "../python/CMT_database.db"


class QueryForm(Form):
    id = IntegerField('ID candidat')
    name = StringField('Nom candidat')
    FirstName = StringField('Prénom candidat')
    field = SelectField('Filière suivie')


app = Flask(__name__)


@app.route('/')
def index():
    render_template("index.html")


@app.route('/query', methods = ["GET"])
def query():
    form = QueryForm(request.form)
    result = []
    arguments = request.args
    req = BuildRequest(arguments)

    render_template("query.html", form = form, result = result)


def BuildRequest(args):
    req = 'SELECT * FROM Candidat'
    req += 'WHERE'
    added = False
    if args["name"]:
        name = args["name"]
        req += f"Nom = '{name}'"
        added = True
    if args["FirstName"]:
        FirstName = args["FirstName"]
        if added:
            req += " AND "
        req += f"Prenom = '{FirstName}'"
        added = True
    if args["id"]:
        id = int(args["id"])
        if added:
            req += " AND "
        req += f"candidat_id = '{id}'"
        added = True
    if args["field"]:
        field = args["field"]
        if added:
            req += " AND "
        req += f"Filiere = '{field}'"
    return req


def GetDB():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(path)
    return db


@app.teardown_appcontext
def CloseConnection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
