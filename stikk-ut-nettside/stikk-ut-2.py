import firebase_admin
from firebase_admin import credentials, db
 
cred = credentials.Certificate('stikk-ut-nettside\stikk-ut.json')
firebase_admin.initialize_app(cred, {"databaseURL":"https://stikk-ut-e35ce-default-rtdb.europe-west1.firebasedatabase.app/"})

ref = db.reference('/')


turer = [
{"navn": "merete", "tid": "03.24.2024", "sted": "kammen", "bilde": "https://www.google.com/url?sa=i&url=https%3A%2F%2Ftechweez.com%2Fvivo-lowlight-selfie-1%2F&psig=AOvVaw3_DQ3wsNUGS34IlGGCswUP&ust=1710508157796000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCNDTxcrp84QDFQAAAAAdAAAAABAE", "beskrivelse": "veldig fin tur" },]

for tur in turer:
    ref.push(tur)

print("funker")