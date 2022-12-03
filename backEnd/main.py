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
@app.route("/generator")
def generator():
    # Session mysql
    sessionl = session()

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

@app.route("/getDataEau", methods=["GET"])
def getDataEau():
    # Session mysql
    sessionl = session()
    
    #  Selection de la table capteurNiveauEau
    datas = sessionl.query(capteurNiveauEau)
    
    #  Implémentation du fichier JSON qui contiendra les données à renvoyer
    result = []
    for data in datas:
        result.append(data.as_dict())
    return result

@app.route("/getDataPression", methods=["GET"])
def getDataPression():
    # Session mysql
    sessionl = session()
    
    #  Selection de la table capteurPression
    datas = sessionl.query(capteurPression)
    
    #  Implémentation du fichier JSON qui contiendra les données à renvoyer
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
