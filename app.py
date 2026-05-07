
import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

# 1. FORCE L'AFFICHAGE DE L'INDEX
@app.get("/")
async def read_index():
    # On essaye de charger index.html ou ind.html pour être sûr
    for name in ['index.html', 'ind.html']:
        if os.path.exists(name):
            return FileResponse(name)
    return {"error": "Fichier index.html introuvable sur le serveur"}

# 2. ROUTE POUR TOUTES LES AUTRES PAGES
@app.get("/{filename}")
async def get_site_file(filename: str):
    if os.path.exists(filename):
        return FileResponse(filename)
    return {"error": f"Fichier {filename} introuvable"}

# 3. ROUTES API
class LoginCredentials(BaseModel):
    username: str
    password: str

@app.post("/api/login")
async def login(credentials: LoginCredentials):
    if credentials.username == "admin" and credentials.password == "1234":
        return {"status": "success"}
    return {"status": "error"}

@app.get("/api/consommation")
async def get_consommation():
    return [{"mois": "Juin", "reel": 180, "fact": 180, "montant": "19 800", "statut": "ok", "hash": "0x4a1e...b9d2"}]

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
