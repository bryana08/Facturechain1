# ⚡ FactureChain - Transparence Électrique via Blockchain

**FactureChain** est une plateforme décentralisée conçue pour résoudre les litiges de facturation énergétique au Cameroun. Le projet permet aux abonnés de vérifier l'intégrité de leurs données de consommation et d'ancrer leurs réclamations sur la blockchain Polygon pour garantir une transparence totale.

> **Projet présenté pour la Phase 2 (Demi-finale) du MIABE Hackathon 2026.**

---

## 🚀 Fonctionnalités Clés
- **Authentification Sécurisée** : Espace privé pour chaque abonné (Admin/User).
- **Dashboard Dynamique** : Visualisation en temps réel de la consommation (kWh) vs facturation.
- **Détection Automatique d'Anomalies** : Algorithme identifiant les écarts suspects entre l'index réel et facturé.
- **Réclamations Certifiées** : Enregistrement des litiges sur le réseau Polygon avec génération immédiate d'un Hash de transaction immuable.
- **Suivi de Résolution** : Timeline de traitement des plaintes pour éviter les silences administratifs.

## 🛠️ Stack Technique
- **Frontend** : HTML5, CSS3 (Design Navy & Orange), JavaScript (Fetch API).
- **Backend** : Python 3.10+ avec **FastAPI**.
- **Blockchain** : Simulation de Smart Contracts (Solidity/Polygon).
- **Déploiement** : Hébergé sur **Render**.

## 📦 Installation et Test Local (Ubuntu)

1. **Cloner le projet** :
   ```bash
   git clone [https://github.com/ton-pseudo/FactureChain.git](https://github.com/ton-pseudo/FactureChain.git)
   cd FactureChain



2.installer les dépendances 

pip install fastapi uvicorn


3.lancer le serveur 

python3 app.py



