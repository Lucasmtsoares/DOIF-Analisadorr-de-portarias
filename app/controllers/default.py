from app.core.analitic_date import Analitic
from app.models.dados import res as result
from flask import render_template, request
from app import app
import json

@app.route("/")
def index(): 
    return render_template("basic.html")

@app.route("/analisar-portarias")
def analisar_portarias():
    res = result
    #x = Analitic()
    #res = x.analitic()
    
        
    return render_template("analitic.html", res=res)

@app.route("/analisar-portarias", methods=['POST'])
def analisar_portaria():
    if_ = request.form['if']
    date = request.form['date']
    
    #res = result
    if_analisar = Analitic()
    res = if_analisar.analitic(if_, date)
    
    
   
    print(res)
        
    return render_template("analitic.html", res=res)
