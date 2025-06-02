import os
import firebase_admin
from firebase_admin import credentials

def initialize_firebase():
    use_emulator = os.getenv("USE_FIREBASE_EMULATOR", "false").lower() == "true"

    if use_emulator:
        os.environ["FIRESTORE_EMULATOR_HOST"] = os.getenv("FIRESTORE_EMULATOR_HOST", "localhost:8080")
        os.environ["FIREBASE_AUTH_EMULATOR_HOST"] = os.getenv("FIREBASE_AUTH_EMULATOR_HOST", "localhost:9099")
        firebase_admin.initialize_app()
    else:
        cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
