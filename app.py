from flask import Flask, render_template, request, redirect, flash
import requests
import re
import pandas as pd

app = Flask(__name__, template_folder='templates_folder')

url =  "https://raw.githubusercontent.com/ByCodersTec/desafio-ruby-on-rails/master/CNAB.txt"
response = requests.get(url)
responselist = re.split('\n', response.text)

tipo = responselist[0][0]
Data = responselist[0][1:9]
Valor = responselist[0][9:19]
CPF = responselist[0][19:30]
Cart = responselist[0][30:42]
Hora = responselist[0][42:48]
DonoDaLoja = responselist[0][48:62]
NomeLoja = responselist[2][62:81]

@app.route("/",methods = ['POST', 'GET'])
def index():
  print (request.args)
  return NomeLoja

@app.route("/api")
def setFile():
  return tipo

if __name__ == "__main__":
 app.run()