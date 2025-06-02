FROM node:18-alpine

# Installer Java uniquement une fois
RUN apk add --no-cache openjdk17

# Installer Firebase Tools globalement
RUN npm install -g firebase-tools

# Crée le dossier de travail
WORKDIR /firebase

# Copie uniquement le fichier de config Firebase
COPY ./firebase /firebase

# Point d’entrée
CMD ["firebase", "emulators:start", "--only", "auth,firestore,database", "--project", "local-dev", "--import=/firebase_data/data", "--export-on-exit"]
