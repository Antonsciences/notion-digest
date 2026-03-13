# 📧 Notion Digest — Maison Eric Kayser Asie Ltd

Envoie par e-mail (Gmail SMTP) un récapitulatif hiérarchisé des tâches stockées dans Notion avec support parent-enfant.

---

## 📁 Fichiers du projet

```
├── app.py               ← Application Streamlit principale (Gmail)
├── requirements.txt     ← Dépendances Python
├── .env                 ← Vos secrets (ne JAMAIS committer)
├── .env.example         ← Template — copier et remplir
└── .gitignore           ← Exclut .env, tokens et fichiers temporaires
```

---

## 🚀 Installation & Lancement

### 1. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 2. Configurer les secrets

Copiez `.env.example` en `.env` et renseignez **vos valeurs personnelles** :

```bash
cp .env.example .env
```

Éditez `.env` :
- **GMAIL_ADDRESS** : votre adresse Gmail
- **GMAIL_APP_PASSWORD** : mot de passe d'application [voir ci-dessous]
- **NOTION_TOKEN** : token d'intégration Notion (commence par `ntn_`)
- **NOTION_DATABASE_ID** : UUID de votre base Notion
- **DEFAULT_RECIPIENT** : email de destination

#### Créer un mot de passe d'application Gmail
1. Allez sur [https://myaccount.google.com/security](https://myaccount.google.com/security)
2. Activez la **validation en 2 étapes**
3. Allez dans **Mots de passe des applications**
4. Générez un mot de passe pour "Mail" + "Windows/Mac/Linux"
5. Copiez le code 16 caractères dans `GMAIL_APP_PASSWORD`

### 3. Lancer l'application

```bash
streamlit run app.py
```

L'app s'ouvre sur [http://localhost:8501](http://localhost:8501)

---

## 🔐 Sécurité

- Le fichier `.env` ne doit **jamais** être commité dans Git ni partagé
- Les tokens et mots de passe sont exposés en clair — si compromis, les révoquer immédiatement :
  - Gmail : régénérer le mot de passe d'application
  - Notion : révoquer le token dans les paramètres d'intégration
- Le `.gitignore` exclut automatiquement `.env`

---

## ⚠️ Prérequis Notion

Votre intégration Notion doit avoir **accès à la base de données** :
1. Ouvrez votre base Notion en vue complète (page-niveau)
2. Cliquez sur `...` (menu haut-droit) → `+ Add connections`
3. Cherchez et sélectionnez votre intégration (créée sur [developers.notion.com](https://developers.notion.com))
4. Acceptez les permissions demandées

## 📊 Structure Notion attendue

La base doit contenir :
- **Au minimum** : une propriété de type **Title** pour le nom de la tâche
- **Optionnel** : une propriété de type **Relation** nommée `Parent task` pour les sous-tâches

La hiérarchie s'affiche ainsi :
```
• Tâche 1
  - Sous-tâche 1.1
  - Sous-tâche 1.2
• Tâche 2
```

---

## 🛠 Dépannage

| Erreur | Solution |
|---|---|
| **Erreur Notion 401/403** | Vérifier que le token `NOTION_TOKEN` est valide |
| **Erreur Notion 404** | L'intégration n'est pas invitée sur la base (voir prérequis) |
| **Authentification Gmail échouée** | Vérifier que `GMAIL_APP_PASSWORD` est le mot de passe **d'application**, pas le mot de passe Gmail |
| **Aucune tâche trouvée** | Vérifier que `NOTION_DATABASE_ID` est correct (UUID format) |
| **Sous-tâches non affichées** | S'assurer que la relation parent-enfant existe et que la propriété s'appelle `Parent task` |
| **Erreur SMTP** | Vérifier l'authentification Gmail et que la validation 2FA est activée |
