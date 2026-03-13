"""
login_outlook.py
────────────────
À exécuter UNE SEULE FOIS en local pour obtenir et sauvegarder
le token OAuth Outlook. Le token sera rechargé automatiquement
par l'app Streamlit lors des prochains lancements.

Usage :
    python login_outlook.py
"""

import os
from O365 import Account
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID     = os.getenv('AZURE_CLIENT_ID')
CLIENT_SECRET = os.getenv('AZURE_CLIENT_SECRET')
TENANT_ID     = os.getenv('AZURE_TENANT_ID')

if not all([CLIENT_ID, CLIENT_SECRET, TENANT_ID]):
    print("❌ Variables d'environnement manquantes. Vérifiez votre fichier .env")
    exit(1)

credentials = (CLIENT_ID, CLIENT_SECRET)
account = Account(credentials, tenant_id=TENANT_ID)

print("🔐 Lancement du flow d'authentification OAuth Microsoft 365...")
print("   → Un lien va s'afficher. Ouvrez-le dans votre navigateur.")
print("   → Connectez-vous avec votre compte Maison Kayser.")
print("   → Copiez l'URL de redirection et collez-la ici.\n")

if account.authenticate(scopes=['basic', 'message_all']):
    print("\n✅ Authentification réussie !")
    print("   Le token est sauvegardé localement (o365_token.txt).")
    print("   Vous pouvez maintenant lancer l'app : streamlit run app.py")
else:
    print("\n❌ Échec de l'authentification. Vérifiez vos credentials Azure.")
