from flask import Flask, render_template, request
import requests
import json

from urllib.request import urlopen

app = Flask(__name__)

@app.route('/')
def hello():
    cislo_sveta = "007"
    pole = ["Pondeli", "Utery", "Streda"]
    return render_template("main.html", promenna = cislo_sveta, pole = pole)

@app.route('/graph')
def graph():
    res = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m')
    response = json.loads(res.text)
    return render_template('graph.html',osaX=response['hourly']['time'][0:-5],osaY=response['hourly']['temperature_2m'][0:-5])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port =5000)
