from app.core.analitic_date import Analitic
from app.models.dados import res as result
from flask import render_template, request
from app import app
import json

@app.route("/")
def home(): 
    return render_template("basic.html")

@app.route('/page-busca')
def page_de_busca():
    return render_template("page_de_busca.html")

@app.route("/painel-de-analise")
def painel_de_analise():
            
    return render_template("painel_de_analise.html")

@app.route("/painel-grafico")
def painel_grafico():
            
    return render_template("painel_grafico.html")



@app.route("/analisar-portarias", methods=['POST'])
def analisar_portaria():
    if_ = request.form['if']
    date = request.form['date']
    
    #res = result
    if_analisar = Analitic()
    res = if_analisar.analitic(if_, date)
    
    
   
    print(res)
        
    return render_template("analitic.html", res=res)
