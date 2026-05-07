
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

# --- ROUTES DES PAGES HTML ---

@app.get("/")
async def read_index():
    # Affiche la page d'accueil. Vérifie que ton fichier s'appelle bien index.html
    return FileResponse('index.html')

@app.get("/login")
async def read_login():
    return FileResponse('login.html')

@app.get("/dash")
async def read_dash():
    return FileResponse('dash.html')

@app.get("/reclamation")
async def read_reclamation():
    return FileResponse('Réclamation.html')

# --- CONFIGURATION DES FICHIERS (JS, CSS) ---
# Ceci permet à tes pages de trouver main.js
app.mount("/static", StaticFiles(directory="."), name="static")

# --- TES ROUTES API (Garde-les !) ---

class LoginCredentials(BaseModel):
    username: str
    password: str

@app.post("/api/login")
async def login(credentials: LoginCredentials):
    if credentials.username == "admin" and credentials.password == "1234":
        return {"status": "success"}
    return {"status": "error", "message": "Identifiants incorrects"}

# Route pour les données du dashboard
@app.get("/api/consommation")
async def get_consommation():
    return [
        {"mois": "Juin", "reel": 180, "fact": 180, "montant": "19 800", "statut": "ok", "hash": "0x4a1e...b9d2"},
        {"mois": "Juillet", "reel": 220, "fact": 225, "montant": "24 500", "statut": "ok", "hash": "0x7d3c...f8a1"}
    ]

# --- LANCEMENT RENDER ---
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
