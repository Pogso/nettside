import firebase_admin
from firebase_admin import credentials, db
from flask import Flask,redirect,url_for,render_template,request

cred = credentials.Certificate('stikk-ut-nettside\stikk-ut.json')
firebase_admin.initialize_app(cred, {"databaseURL":"https://stikk-ut-e35ce-default-rtdb.europe-west1.firebasedatabase.app/"})

ref =db.reference('/')

app=Flask(__name__, template_folder="./template")


@app.route('/submit')
def Input():
    return render_template('legg-inn.html')

@app.route('/')
def StikkUt():
    StikkUtTurer=[]
    finnTurer = ref.get()
    sortert_Turer = sorted(finnTurer.items(), key=lambda x: (x[1]["navn"], x[1]["sted"]))

    for i, turer2 in sortert_Turer:
        StikkUtTur = {
                "navn": turer2["navn"],
                "sted": turer2["sted"],
                "tid": turer2["tid"],
                "bilde" : turer2["bilde"],
                "beskrivelse" : turer2["beskrivelse"]
        }
        StikkUtTurer.append(StikkUtTur)



    return render_template('stikk-ut.html', StikkUt1=StikkUtTurer)

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