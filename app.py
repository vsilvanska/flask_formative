from flask import Flask, render_template, request, redirect, url_for
from flask import session
import csv

app = Flask(__name__)
app.secret_key = b'bahe004cc8de79cc96482b95db2d75473a3aa855b3270350267ccc92bddd46c5'

@app.route('/', methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():    
    with open("data.csv", "r", encoding="utf-8") as fichier_csv:
        data = list(csv.DictReader(fichier_csv, delimiter=";"))      
    return render_template('index.html', data=data)

@app.route("/index", methods=['GET', 'POST'])
def encode_nom():
    if request.method == 'GET':
        return render_template('index.html')
    
    elif request.method == 'POST':
        session['nom'] = request.form['nom']
        session['prenom'] = request.form['prenom']
        session['datedenaissance'] = request.form['datedenaissance']
        session['nomville'] = request.form['nomville']
        session['villeecole'] = request.form['villeecole']
        session['annee'] = request.form['annee']
        session['classe'] = request.form['classe']
        session['option'] = request.form['option']

        new_id = None

        with open("data.csv", "r", encoding="utf-8", newline="") as fichier_csv:
            data = list(csv.DictReader(fichier_csv, delimiter=";"))
            new_id = len(data) + 1  

        with open("data.csv", "a", encoding="utf-8", newline="") as fichier_csv:                      
            writer = csv.writer(fichier_csv, delimiter=';')            
            line = [new_id, session['nom'], session['prenom'], session['datedenaissance'],['nomecole'],['villecole'],['annee'],['classe'],['option']]
            writer.writerow(line)
    
        with open('data.csv', mode='w', newline='') as file:
            donnees = ['nom', 'prenom', 'datedenaissance', 'nomecole', 'villeecole', 'annee', 'classe', 'option']
            writer = csv.DictWriter(file, fieldnames=donnees, delimiter=";")
            writer.writeheader()
            writer.writerows(data)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'GET':
        line = []
        with open("data.csv", "r", encoding="utf-8", newline="") as fichier_csv:
            data = list(csv.DictReader(fichier_csv, delimiter=";"))

            for line in data:
                if line['id'] == id:
                    session['nom'] = request.form['nom']
                    session['prenom'] = request.form['prenom']
                    session['datedenaissance'] = request.form['datedenaissance']
                    session['nomville'] = request.form['nomville']
                    session['villeecole'] = request.form['villeecole']
                    session['annee'] = request.form['annee']
                    session['classe'] = request.form['classe']
                    session['option'] = request.form['option']

        return render_template('edit_mail.html',
                                    nom = nom,
                                    prenom = prenom,
                                    datedenaissance = datedenaissance,
                                    nomville = nomville,
                                    villeecole = villeecole,
                                    annee = annee,
                                    classe = classe,
                                    option = option,
                                )
     
    elif request.method == 'POST':
        session['nom'] = request.form['nom']
        session['prenom'] = request.form['prenom']
        session['datedenaissance'] = request.form['datedenaissance']
        session['nomville'] = request.form['nomville']
        session['villeecole'] = request.form['villeecole']
        session['annee'] = request.form['annee']
        session['classe'] = request.form['classe']
        session['option'] = request.form['option']
        data = []

        with open("data.csv", "r", encoding="utf-8", newline="") as fichier_csv:
            data = list(csv.DictReader(fichier_csv, delimiter=";"))

        return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)