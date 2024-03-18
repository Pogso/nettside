import firebase_admin
from firebase_admin import credentials, db
from flask import Flask,redirect,url_for,render_template,request

cred = credentials.Certificate('fire base\credentials.json')
firebase_admin.initialize_app(cred, {"databaseURL":"https://fir-54d98-default-rtdb.europe-west1.firebasedatabase.app/"})

ref =db.reference('/')

app=Flask(__name__, template_folder="./template")


@app.route('/')
def Input():
    return render_template('main.html')

@app.route('/konserter')
def Konserter():
    konserter1 = ref.get()

    return render_template('Konserter.html', konserter2=konserter1)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        navn = request.form['Navn']
        sted = request.form['sted']
        tid = request.form['tid']
            
        Konsert = {
            'navn': navn,
            'sted': sted,
            'tid': tid
        }

        ref.push(Konsert)
        print("Data pushed to Firebase")


    return render_template('main.html')
app.run()