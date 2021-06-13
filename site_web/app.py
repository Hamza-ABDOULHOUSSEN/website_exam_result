from flask import Flask, request, render_template
from requetes import *
from formulaire import *

app = Flask(__name__)
with app.app_context():
    saveVoeuxDemandeJSON()


@app.route('/', methods = ["GET"])
def index():
    return render_template("index.html")


@app.route('/candidats', methods = ["GET"])
def candidates():
    identityForm = IdentityForm(request.form)
    arguments = request.args
    query = "none"
    result = None
    tags = None
    count = 0
    if len(arguments) != 0:
        result, tags, query = BuildRequest(arguments)
        count = len(result)
    return render_template("candidates.html", identityForm = identityForm,
                           result = result, tags = tags,
                           query = query, count = count)


@app.route('/resultats', methods = ["GET"])
def results():
    totalCount, admissibleCount, admisCount = buildGlobalResults()
    return render_template("results.html", totalCount = totalCount, admissibleCount = admissibleCount,
                           admisCount = admisCount)


@app.route('/statistiques/matiere', methods = ["GET"])
def stats_matiere():
    matieresNom = buildNomMatiere()
    matiereForm = MatiereSelectorForm(request.form)
    matiereForm.nomMatiere.choices = matieresNom

    stats = buildStatsEcrit()

    return render_template("statistiques_matiere.html", matieres = matiereForm, stats = stats)


@app.route('/statistiques/voeux', methods = ["GET"])
def stats_voeux():
    ecoleForm = EcoleSelectorForm(request.form)

    counts = loadVoeuxDemandeJSON()
    return render_template("statistiques_voeux.html", counts = counts, ecoles = ecoleForm)


@app.route('/statistiques/etablissement', methods = ["GET"])
def stats_etablissement():
    etabForm = EtabForm(request.form)
    arguments = request.args
    valid, AllInfo = buildInfoEtab(arguments)
    return render_template("statistiques_etab.html", EtabForm = etabForm, AllInfo = AllInfo, valid= valid, entete = ["Nombre de candidats", "Nombre d'admis", "Nombre d'admissibles", "Nombre de non admissibles", "Rang max", "Rang min", "Rang moyen"])


@app.route('/statistiques/provenance', methods = ["GET"])
def stats_provenance():
    etrangerCount, repartitionFrance = buildProvenance()
    return render_template('statistiques_provenance.html', etrangerCount = etrangerCount,
                           repartitionFrance = repartitionFrance)


@app.route('/about', methods = ["GET"])
def about():
    return render_template("about.html")


@app.errorhandler(404)
def errorPage(e):
    return render_template("404.html"), 404


@app.teardown_appcontext
def CloseConnection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run()
