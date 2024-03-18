import firebase_admin
from firebase_admin import credentials, db
from flask import Flask,redirect,url_for,render_template,request

cred = credentials.Certificate('stikk-ut-nettside\stikk-ut.json')
firebase_admin.initialize_app(cred, {"databaseURL":"https://stikk-ut-e35ce-default-rtdb.europe-west1.firebasedatabase.app/"})

ref =db.reference('/')

app=Flask(__name__, template_folder="./html-css")


@app.route('/')
def Input():
    reference = ref.get()
    return render_template('stikk-ut.html', StikkUt1=reference) if reference else render_template('stikk-ut.html', StikkUt1={"Error": False})

@app.route('/stikk-ut')
def StikkUt():
    reference = ref.get()

    return render_template('stikk-ut.html', StikkUt1={"key": "value"})

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        navn = request.form['Navn']
        sted = request.form['sted']
        tid = request.form['tid']
        bilde = request.form['bilde']
        beskrivelse = request.form['beskrivelse']
            
        StikkUt = {
            'navn': navn,
            'sted': sted,
            'tid': tid,
            'bilde' : bilde,
            'beskrivelse' : beskrivelse
            
        }

        ref.push(StikkUt)
        print("Data pushed to Firebase")


    return render_template('legg-inn.html')
app.run(debug=True)