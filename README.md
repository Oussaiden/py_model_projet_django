/mon_projet/
│
├── .env.dev                       # Variables pour Docker dev
├── .env.prod                      # Variables pour Cloud Run / Secret Manager
├── docker-compose.yml            # Pour Dev (Django + Postgres + Firebase Emulator)
├── cloudbuild.yaml               # (optionnel) CI/CD pour déploiement GCP
│
├── firebase/                     # Configs pour Firebase Emulator Suite
│   ├── firebase.json
│   └── firestore.rules
│
├── backend/                      # Dossier projet Django
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── manage.py
│   │
│   ├── ton_projet/               # Dossier du projet Django principal
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py           # Paramètres Dev + Prod auto-gérés
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── users/                    # App Django n°1 (gestion utilisateurs)
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── forms.py
│   │
│   ├── core/                     # App Django n°2 (logique métier principale)
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── utils.py
│   │
│   ├── templates/                # Fichiers HTML pour Django (si utilisé)
│   │   └── base.html
│   │
│   ├── static/                   # Fichiers statiques (JS/CSS/images)
│   │   └── style.css
│   │
│   └── media/                    # (optionnel) Fichiers uploadés par les utilisateurs
│
└── README.md                     # Documentation projet