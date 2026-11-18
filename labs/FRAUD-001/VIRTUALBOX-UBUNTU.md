# FRAUD-001 — Exécuter le laboratoire dans une VM Ubuntu sous VirtualBox (Windows 11)

> **Guide de lab** — procédure proposée pour un poste personnel ; **aucun test de bout en bout sur VirtualBox n'est encore confirmé par OSEF**. Utiliser seulement des données synthétiques. Aucun raccordement à un système de paiement réel.

- [Issue FRAUD-001 #43](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/43)
- [Guide principal et tests](README.md)
- [Documentation VirtualBox](https://www.virtualbox.org/manual/)
- [Installation Docker Engine pour Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

## 1. Architecture

```text
Laptop Windows 11
└── Oracle VirtualBox (réseau de la VM : NAT)
    └── Ubuntu Server 24.04 LTS — une seule VM
        └── Docker Engine + Docker Compose v2
            ├── psp-a :8000 -> 127.0.0.1:8091 dans Ubuntu
            ├── relay :8000 -> 127.0.0.1:8090 dans Ubuntu
            │   └── volume Docker SQLite (signaux fictifs + audit)
            └── psp-b :8000 -> 127.0.0.1:8092 dans Ubuntu
```

Les **trois conteneurs** fonctionnent dans une seule VM : **ne pas créer trois VM** pour ce MVP. Les ports sont liés à la boucle locale **de la VM** et ne sont donc pas directement accessibles sur `localhost` depuis Windows. Utiliser un terminal **dans Ubuntu** pour les premiers tests. Ne pas remplacer `127.0.0.1` par `0.0.0.0` pour contourner cette restriction.

## 2. Matériel de départ (estimations, pas mesures de performance)

| Ressource VM | Recommandation |
|---|---|
| OS invité | Ubuntu Server 24.04 LTS 64-bit |
| CPU | 2 vCPU |
| Mémoire | 4 Gio de RAM |
| Disque virtuel | 30 Gio, allocation dynamique |
| Réseau | NAT |
| GPU | Aucun |
| Réseau de l'application | Interne Docker et ports en boucle locale du système invité |

Si le PC hôte ne dispose pas de RAM suffisante, ajuster la VM sans priver Windows de mémoire. Activer VT-x/AMD-V dans le BIOS/UEFI si nécessaire. Docker Linux classique **ne requiert pas de virtualisation imbriquée** pour faire tourner ces conteneurs à l'intérieur de la VM.

## 3. Préparer la VM dans VirtualBox

1. Télécharger Ubuntu Server 24.04 LTS depuis https://ubuntu.com/download/server ; vérifier le checksum fourni sur le site officiel si disponible.
2. Créer une VM VirtualBox Linux/Ubuntu (64-bit), avec le profil de ressources ci-dessus.
3. Monter l'ISO dans le lecteur optique virtuel ; laisser **Carte 1 : NAT**. Une seconde carte réseau et les dossiers partagés ne sont pas nécessaires.
4. Installer Ubuntu Server ; créer un utilisateur non root et activer SSH seulement si une administration distante est réellement nécessaire.
5. Ouvrir une session de terminal **dans la VM Ubuntu** et exécuter les étapes suivantes.

## 4. Vérification du système Ubuntu

```bash
# Mise à jour de l'index des paquets puis installation des utilitaires de lab.
sudo apt update
sudo apt install -y ca-certificates curl git openssl python3

# Vérifier architecture, mémoire, disque et connectivité.
uname -m
free -h
df -h /
curl -I https://github.com
```

## 5. Installer Docker Engine + Compose (dépôt officiel Docker)

> Respecter la version courante du [guide Docker pour Ubuntu](https://docs.docker.com/engine/install/ubuntu/) en cas de changement de procédure. Ne pas mélanger l'installation officielle avec d'anciens paquets `docker.io` ou des variantes Snap.

```bash
# Enregistrer la clé officielle du dépôt Docker pour Ubuntu.
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Déclarer le dépôt officiel correspondant à la distribution et à l'architecture.
sudo tee /etc/apt/sources.list.d/docker.sources > /dev/null <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "$VERSION_CODENAME")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

# Installer Engine, CLI, containerd, Buildx et Compose.
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Vérifier le démon et Compose. Utiliser sudo pour éviter d'ajouter l'utilisateur
# au groupe docker, qui confère des privilèges proches de root.
sudo systemctl status docker --no-pager
sudo docker version
sudo docker compose version
```

**Privilèges :** `sudo docker` est volontaire. Ne pas modifier les permissions de `/var/run/docker.sock` ni exposer l'API Docker à distance.

## 6. Récupérer et lancer FRAUD-001

```bash
# Cloner le dépôt OSEF public.
git clone https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs.git
cd osef-open-source-payment-banking-labs/labs/FRAUD-001

# Générer quatre secrets strictement locaux dans .env.
bash scripts/init-env.sh

# Confirmer la configuration Compose sans imprimer les secrets.
sudo docker compose config --quiet

# Construire les images et démarrer les 3 services.
sudo docker compose up --build -d

# Observer les conteneurs et le statut de santé du relais.
sudo docker compose ps

# Contrôler les trois endpoints depuis l'Ubuntu invité.
curl --fail --silent http://127.0.0.1:8090/health
curl --fail --silent http://127.0.0.1:8091/health
curl --fail --silent http://127.0.0.1:8092/health
```

**Attendu :** trois réponses JSON avec `"status":"ok"` et le nom du rôle ; les services doivent être démarrés, le relais doit devenir `healthy`. **Résultat réel à renseigner par l'ingénieur**, pas présumé réussi.

## 7. Exécuter les scénarios

```bash
# Tests de base T01–T07 : création, doublon, authentification, lecture,
# validation JSON, refus d'accès anonyme et audit.
bash scripts/test-lab.sh

# Si un test échoue, consulter les logs récents sans publier les clés du .env.
sudo docker compose logs --tail=100 relay psp-a psp-b
```

Les tests T08 à T10 (expiration, relais indisponible, séparation des rôles) restent à automatiser selon le [README principal](README.md). Ne pas cocher leur réussite sans les avoir exécutés et documentés.

### Exemple de vérification manuelle

```bash
# Charger les clés de lab localement, ne jamais les copier dans GitHub.
set -a
source .env
set +a

# Construire un nouveau signal fictif ; changer le jeton pour une nouvelle exécution.
curl --fail-with-body -X POST http://127.0.0.1:8091/submit \
  -H "X-Lab-Key: $LAB_USER_KEY" \
  -H "Content-Type: application/json" \
  -d '{"transaction_token":"demo-virtualbox-20261118-001","category":"suspicious-transfer","severity":"high","recipient":"psp-b","expires_in_hours":1}'

# Consulter depuis PSP B.
curl --fail-with-body http://127.0.0.1:8092/inbox \
  -H "X-Lab-Key: $LAB_USER_KEY"
```

Une deuxième soumission avec un même `transaction_token` devrait renvoyer **409 Conflict**.

## 8. Arrêter et nettoyer

```bash
# Arrêter les services : préserve le volume SQLite et l'historique d'audit.
sudo docker compose down

# DANGER — uniquement après sauvegarde des preuves : efface le volume de lab.
# sudo docker compose down --volumes
```

**Confidentialité :** ne jamais joindre le fichier `.env`, les clés, les volumes ou des données réelles à une issue ou une PR.

## 9. Dépannage VirtualBox

| Symptôme | Vérification |
|---|---|
| Ubuntu 64-bit absent ou VM ne démarre pas | Vérifier VT-x/AMD-V, paramètres de virtualisation, conflits hyperviseur selon le système |
| Ubuntu manque de mémoire | Réduire la consommation du système hôte, ajuster les 4 Gio proposés |
| `docker: command not found` | Installation Docker incomplète ; consulter l'étape 5 |
| `permission denied` Docker | Utiliser `sudo docker ...` ; ne pas ouvrir le socket Docker |
| `docker compose config` échoue | `.env` absent ou invalide ; relancer `bash scripts/init-env.sh` |
| Port 8090/8091/8092 occupé | Rechercher le service occupant le port **dans la VM** |
| L'URL localhost ne marche pas dans Windows | C'est attendu : les ports sont liés à localhost **dans Ubuntu** |
| Retour 401 | Clé erronée, utiliser celle du bon service |
| Retour 409 | Jeton `demo-` déjà soumis, changer le jeton |
| Retour 422 | JSON incorrect, catégorie ou token hors schéma |
| Retour 503 | Relais indisponible : `sudo docker compose ps` et `logs` |

## 10. Fiche de validation à reporter dans l'issue #43

- OS invité/version : …
- VirtualBox/version : …
- CPU/RAM/disque alloués : …
- Versions Docker/Compose : …
- `sudo docker compose ps` : …
- Résultats T01–T07 : …
- Résultats T08–T10 : non exécutés / exécutés avec preuves …
- Anomalies, corrections proposées, commit/PR : …
- Captures/rapports expurgés : …

**Rappel :** le fonctionnement et les performances sur ce matériel ne sont confirmés qu'après exécution et dépôt des preuves. Aucun déploiement bancaire réel n'est autorisé par ce guide.
