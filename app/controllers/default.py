#from app.core.analitic_date import Analitic
from app.models.dados import res as result
from flask import render_template
from app import app
import json

@app.route("/")
def index(): 
    return render_template("basic.html")

@app.route("/processing", methods=['POST'])
def analisar_portarias():
    datas = result
        
    return render_template("analitic.html")

"""x = Analitic()
    b = x.analitic()
    print(b)"""