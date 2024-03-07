import firebase_admin
from firebase_admin import credentials, db
 
cred = credentials.Certificate('fire base\credentials.json')
firebase_admin.initialize_app(cred, {"databaseURL":"https://fir-54d98-default-rtdb.europe-west1.firebasedatabase.app/"})

ref = db.reference('/')


Konserter = [
{"navn": "rororo din bat", "tid": "03.24.2024", "sted": "Molde" },
{"navn": "ta din are fatt", "tid": "03.29.2024", "sted": "Kristiansund"}, 
{"navn": "Vuggende, vuggende", "tid": "04.5.2024", "sted": "Oslo"}]

for konsert in Konserter:
    ref.push(konsert)

print("funker")