from flask import Flask, render_template
import pandas as pd
import requests
from io import StringIO

app = Flask(__name__)

SHEET_URL = "https://docs.google.com/spreadsheets/d/1F8Ouf2vOdHbNtoTtgWdSz4UJzpMCJQP_DOTC45Af4CI/gviz/tq?tqx=out:csv"

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/registro')
def registro():
    return render_template("registro.html")

@app.route("/hunters")
def homeHunters():
    return render_template("indexHunters.html")

@app.route("/hunters/dashboard")
def dashboard():
    response = requests.get(SHEET_URL, verify=False)
    df = pd.read_csv(StringIO(response.text))

    # Insertar columna de ícono de carnet (HTML)
    df.insert(0, 'Icono', '<span class="icon-col">🪪</span>')

    # Convertir DataFrame a HTML, sin escapar los tags
    table_html = df.to_html(classes='data-table', index=False, escape=False)

    return render_template("dashboard.html", table_html=table_html)

if __name__ == "__main__":
    app.run(debug=True)
