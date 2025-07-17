import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancep-default-rtdb.firebaseio.com/",
    'storageBucket': 'https://console.firebase.google.com/u/0/project/faceattendancep/database/faceattendancep-default-rtdb/data/~2F'
})
