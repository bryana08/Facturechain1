// Détection automatique de l'URL du serveur (fonctionne en local et sur Render)
const API_URL = window.location.origin + "/api";

document.addEventListener('DOMContentLoaded', () => {
    
    // ==========================================
    // 1. GESTION DE LA CONNEXION (login.html)
    // ==========================================
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const user = document.getElementById('username').value;
            const pass = document.getElementById('password').value;

            try {
                const response = await fetch(`${API_URL}/login`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ username: user, password: pass })
                });
                const result = await response.json();
                
                if (result.status === "success") {
                    // Redirection vers le tableau de bord
                    window.location.href = "dash.html";
                } else {
                    alert("Identifiants incorrects (admin / 1234)");
                }
            } catch (err) {
                console.error("Erreur de connexion:", err);
                alert("Impossible de joindre le serveur FactureChain.");
            }
        });
    }

    // ==========================================
    // 2. CHARGEMENT DU DASHBOARD (dash.html)
    // ==========================================
    const tableBody = document.getElementById('tableBody');
    if (tableBody) {
        async function chargerDonnees() {
            try {
                const res = await fetch(`${API_URL}/consommation`);
                const data = await res.json();
                
                // On vide le message de chargement
                tableBody.innerHTML = ""; 

                data.forEach(d => {
                    // Calcul automatique de l'écart
                    const ecart = ((d.fact - d.reel) / d.reel * 100).toFixed(1);
                    const ecartCouleur = ecart > 5 ? '#E8460A' : '#06D6A0';
                    
                    // On définit la classe du badge
                    const badgeClass = d.statut === "anomaly" ? "badge anomaly" : "badge ok";

                    tableBody.innerHTML += `
                        <tr>
                            <td>${d.mois}</td>
                            <td>${d.reel} kWh</td>
                            <td>${d.fact} kWh</td>
                            <td style="color:${ecartCouleur}; font-weight:bold;">${ecart}%</td>
                            <td>${d.montant} FCFA</td>
                            <td><span class="${badgeClass}">${d.statut.toUpperCase()}</span></td>
                            <td style="font-family:'Space Mono'; font-size:10px; color:#8B96A8;">${d.hash}</td>
                        </tr>`;
                });
            } catch (err) {
                console.error("Erreur dashboard:", err);
                tableBody.innerHTML = "<tr><td colspan='7'>Erreur lors du chargement des données.</td></tr>";
            }
        }
        chargerDonnees();
    }

    // ==========================================
    // 3. ENVOI DE RÉCLAMATION (Réclamation.html)
    // ==========================================
    const formReclame = document.getElementById('formReclamation');
    if (formReclame) {
        formReclame.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const btn = e.target.querySelector('button');
            const originalText = btn.innerText;
            
            // Effet visuel de chargement
            btn.innerText = "ANCRAGE BLOCKCHAIN EN COURS...";
            btn.disabled = true;
            
            const payload = {
                motif: document.getElementById('motif').value,
                description: document.getElementById('description').value
            };

            try {
                const res = await fetch(`${API_URL}/envoyer-reclamation`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(payload)
                });
                
                const result = await res.json();
                
                if (result.status === "success") {
                    // Mise à jour de l'overlay de succès
                    document.querySelector('.tx-box').innerHTML = `TX HASH POLYGON :<br>${result.tx_hash}`;
                    document.querySelector('.tracking-num').innerText = `ID DE SUIVI : ${result.tracking_id}`;
                    
                    // Affichage de l'overlay
                    document.getElementById('successOverlay').style.display = 'flex';
                }
            } catch (err) {
                alert("Erreur lors de l'envoi de la réclamation.");
            } finally {
                btn.innerText = originalText;
                btn.disabled = false;
            }
        });
    }
});
