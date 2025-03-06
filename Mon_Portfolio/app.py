from flask import Flask, render_template, request, redirect, flash, url_for, send_from_directory
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret_key"  # Pour les messages flash

# 📌 Forcer le rechargement des images (ajout timestamp)
app.jinja_env.globals.update(time=lambda: int(datetime.now().timestamp()))

# 📊 Fonction pour créer un graphique Plotly
def create_plotly_graph():
    df = pd.DataFrame({'x': np.arange(10), 'y': np.random.randint(1, 20, 10)})
    fig = px.line(df, x="x", y="y", title="Graphique Interactif Plotly")
    return fig.to_html(full_html=False)

# 📊 Fonction pour créer des graphiques Matplotlib
def create_matplotlib_graphs():
    x = np.arange(10)
    y = np.random.randint(1, 20, 10)

    # Vérifier et créer le dossier static/images
    if not os.path.exists("static/images"):
        os.makedirs("static/images")

    # Scatter plot
    scatter_path = "static/images/scatter_plot.png"
    plt.figure(figsize=(5, 3))
    plt.scatter(x, y, color='red', label='Scatter Plot')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.savefig(scatter_path)
    plt.close()

    # Bar plot
    bar_path = "static/images/bar_plot.png"
    plt.figure(figsize=(5, 3))
    plt.bar(x, y, color='blue', label='Bar Plot')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.savefig(bar_path)
    plt.close()

    return scatter_path, bar_path

@app.route('/')
def home():
    plotly_graph = create_plotly_graph()
    scatter_path, bar_path = create_matplotlib_graphs()
    return render_template("home.html", plotly_graph=plotly_graph, scatter_path=scatter_path, bar_path=bar_path)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    flash(f"Merci {name}, votre message a été envoyé avec succès !", "success")
    return redirect('/contact')

# 📌 Route pour afficher les fichiers statiques
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
