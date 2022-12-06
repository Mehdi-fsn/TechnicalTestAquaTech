from flask import Flask, request
from flask_cors import CORS
from bdd.main import session
from bdd.tablesDeclare import capteurNiveauEau, capteurPression
from generator import generatorEau, generatorPression


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<script>alert('bad')</script>"

# Route permettant d'insérer les données génrérées dans la BDD
@app.route("/generator", methods=["GET", "POST"])
def generator():
    # Session mysql
    sessionl = session()

    # Vérification si les données ont déja été générées
    verif = sessionl.query(capteurNiveauEau).filter(capteurNiveauEau.date == '2022-11-28 00:00:00')
    for v in verif:
        if(int(v.cm)):
            return {"result" : "error"}
    
    # Insertion des données du capteur de niveau d'eau
    gEau = generatorEau()

    sessionl.bulk_save_objects(
        [
            capteurNiveauEau(
                date = data.get("date"),
                cm= data.get("vCurrent")
            )
            for data in gEau
        ]
    )
    sessionl.commit()

    #  Restart de la session
    sessionl.begin()    
    
    # Insertion des données du capteur de Pression
    gPression = generatorPression()

    sessionl.bulk_save_objects(
        [
            capteurPression(
                date = data.get("date"),
                bar= data.get("vCurrent")
            )
            for data in gPression
        ]
    )
    
    sessionl.commit()

    return {
        "result" : "success"
    }

@app.route("/getDataEau", methods=["GET", "POST"])
def getDataEau():
    sessionl = session()

    datemin = request.form['date_min']
    datemax = request.form['date_max']

    datas = sessionl.query(capteurNiveauEau).filter(capteurNiveauEau.date.between(datemin, datemax))
    
    result = []
    for data in datas:
        result.append(data.as_dict())
    return result

@app.route("/getDataPression", methods=["GET", "POST"])
def getDataPression():
    sessionl = session()

    datemin = request.form['date_min']
    datemax = request.form['date_max']

    datas = sessionl.query(capteurPression).filter(capteurPression.date.between(datemin, datemax))
    
    result = []
    for data in datas:
        result.append(data.as_dict())
    return result

@app.route("/refresh", methods=["GET", "POST"])
def delete():
    sessionl = session()
    
    sessionl.query(capteurPression).delete()
    sessionl.query(capteurNiveauEau).delete()
    
    sessionl.commit()
    
    generator()
    
    return {"result" : "success"}


