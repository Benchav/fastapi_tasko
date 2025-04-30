import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

# Carga las variables de entorno desde .env
load_dotenv()

# Lee la variable de entorno que contiene el JSON como string
firebase_creds = {
    "type": os.getenv("type"),
    "project_id": os.getenv("project_id"),
    "private_key_id": os.getenv("private_key_id"),
    "private_key": os.getenv("private_key").replace('\\n', '\n'),
    "client_email": os.getenv("client_email"),
    "client_id": os.getenv("client_id"),
    "auth_uri": os.getenv("auth_uri"),
    "token_uri": os.getenv("token_uri"),
    "auth_provider_x509_cert_url": os.getenv("auth_provider_x509_cert_url"),
    "client_x509_cert_url": os.getenv("client_x509_cert_url"),
    "universe_domain": os.getenv("universe_domain")
}

cred = credentials.Certificate(firebase_creds)
initialize_app(cred)
db = firestore.client()

# Ejemplo: referencia a colección de usuarios
usuarios_col = db.collection("usuarios")
tareas_col = db.collection("tareas")

