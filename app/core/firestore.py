import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

# Carga las variables de entorno desde .env
load_dotenv()

# Lee la variable de entorno que contiene el JSON como string
firebase_key_json = os.getenv("FIREBASE_KEY_JSON")

if not firebase_key_json:
    raise ValueError("No se encontró la variable de entorno FIREBASE_KEY_JSON")

try:
    # Convierte el string en un diccionario
    firebase_key_dict = json.loads(firebase_key_json)
except json.JSONDecodeError:
    raise ValueError("La variable FIREBASE_KEY_JSON no contiene un JSON válido")

# Inicializa Firebase si no está ya inicializado
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_key_dict)
    firebase_admin.initialize_app(cred)

# Cliente de Firestore
db = firestore.client()

# Ejemplo: referencia a colección de usuarios
usuarios_col = db.collection("usuarios")
tareas_col = db.collection("tareas")

