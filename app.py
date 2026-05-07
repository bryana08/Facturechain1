import os
import random
import time
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(title="FactureChain Backend")

# --- CONFIGURATION SÉCURITÉ (CORS) ---
# Permet au navigateur d'accepter les réponses du serveur
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODÈLES DE DONNÉES ---
class LoginCredentials(BaseModel):
    username: str
    password: str

class Reclamation(BaseModel):
    motif: str
    description: str

# --- ROUTES API ---

# 1. Connexion
@app.post("/api/login")
async def login(credentials: LoginCredentials):
    if credentials.username == "admin" and credentials.password == "1234":
        return {"status": "success"}
    return {"status": "error", "message": "Identifiants invalides"}

# 2. Données de consommation (pour dash.html)
@app.get("/api/consommation")
async def get_consommation():
    # Simulation de données sécurisées
    return [
        {"mois": "Juin 2025", "reel": 180, "fact": 180, "montant": "19 800", "statut": "ok", "hash": "0x4a1e...b9d2"},
        {"mois": "Juillet 2025", "reel": 220, "fact": 225, "montant": "24 500", "statut": "ok", "hash": "0x7d3c...f8a1"},
        {"mois": "Août 2025", "reel": 258, "fact": 293, "montant": "35 580", "statut": "anomaly", "hash": "0x8c7f...a2d4"}
    ]

# 3. Envoi de réclamation (pour Réclamation.html)
@app.post("/api/envoyer-reclamation")
async def post_reclamation(data: Reclamation):
    # Simulation du temps de validation blockchain
    time.sleep(1.2)
    
    # Génération d'un Hash Polygon factice pour la démo
    tx_hash = "0x" + "".join(random.choices("abcdef0123456789", k=64))
    tracking_id = f"FC-2026-{random.randint(1000, 9999)}"
    
    return {
        "status": "success",
        "tx_hash": tx_hash,
        "tracking_id": tracking_id
    }

# --- SERVEUR DE FICHIERS STATIQUES ---

# Cette ligne permet à Render de trouver tes fichiers .html et .js
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
async def read_index():
    # Charge la page d'accueil par défaut
    return FileResponse('index.html')

# --- LANCEMENT DYNAMIQUE (IMPORTANT POUR RENDER) ---
if __name__ == "__main__":
    import uvicorn
    # Render utilise une variable d'environnement pour le port
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
