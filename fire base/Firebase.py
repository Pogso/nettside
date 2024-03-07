import firebase_admin
from firebase_admin import credentials, db

# Replace 'path/to/your/credentials.json' with the path to your Firebase service account key file
cred = credentials.Certificate('fire base\credentials.json')
firebase_admin.initialize_app(cred, {"databaseURL":"https://fir-54d98-default-rtdb.europe-west1.firebasedatabase.app/"})

# Access the Firestore database
ref = db.reference('/')

# Example: Adding data to Firestore
Konsert = [
    {"navn": "rororo din båt", "tid": "03.24.2024", "sted": "Molde"},
    {"navn": "ta din åre fatt", "tid": "03.29.2024", "sted": "Kristiansund"},
    {"navn": "Vuggende, vuggende", "tid": "04.5.2024", "sted": "Oslo"}
]



Konsert_ref = ref.child('Konserter')

# Push each item in the 'Consert' list as a separate document with unique identifiers
for idx, data in enumerate(Konsert, start=1):
    Konsert_ref.child(f'Konsert {idx}').set(data)
