# OSEF FRAUD-001 — Lab d'interopérabilité antifraude entre PSP fictifs

> **Statut : prototype pédagogique proposé.** Les fichiers de démarrage sont publiés mais les tests Docker n'ont pas été exécutés sur une machine de référence par OSEF. À faire valider par un ingénieur avant publication d'un résultat. **Ce projet n'est pas une implémentation officielle de l'Open Financial Trust Alliance (OFTA), ni une plateforme de détection de fraude de production.**

- [Issue de pilotage #43](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/43)
- [Fiche de veille OFTA](../../docs/veille/2026-11-18/OFTA-FRAUD-INTEROPERABILITY.md)
- [Meetup associé #46](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/46)


## Exécution sur laptop Windows avec VirtualBox

Pour une VM Ubuntu Server 24.04 LTS unique avec les trois conteneurs Docker, voir le [guide VirtualBox + Ubuntu détaillé](VIRTUALBOX-UBUNTU.md). Il couvre la configuration de la VM, l'installation officielle de Docker, les commandes, les tests, la sécurité réseau et le dépannage. **Ce parcours n'est pas encore validé par un test matériel confirmé.**

## 1. Objectif et limites

Simuler le partage **d'un signal de risque non nominatif** d'un PSP A vers un PSP B à travers un service relais commun. Prouver par des tests qu'un échange autorisé fonctionne, qu'un doublon est refusé, qu'un acteur non autorisé ne peut pas lire le relais et qu'un audit minimal existe.

**Interdictions :** aucune donnée client, PAN/carte bancaire, MSISDN, identifiant réel de compte ou de transaction, IP de production, secret réel, passerelle de paiement, accès réseau bancaire, donnée de fraude réelle. Les identifiants de transactions doivent commencer par `demo-`. Ne pas exposer les services sur Internet. Pas de conformité PCI DSS, AML/KYC ou RGPD revendiquée.

## 2. Architecture de référence

```mermaid
flowchart LR
    Engineer["Ingénieur lab / curl"] -->|"X-Lab-Key, POST :8091/submit"| A["PSP A - FastAPI"]
    Engineer -->|"X-Lab-Key, GET :8092/inbox"| B["PSP B - FastAPI"]
    A -->|"X-API-Key A, POST /signals"| R["RELAY - FastAPI"]
    B -->|"X-API-Key B, GET /signals"| R
    R --> DB[("SQLite : signaux + audit")]
    Reviewer["Revue LAB autorisée"] -->|"X-API-Key admin, :8090/audit"| R
```

**Flux fonctionnel :**
1. L'ingénieur crée une alerte fictive via PSP A.
2. PSP A valide le JSON via Pydantic et contacte le relais avec son identité propre.
3. Le relais authentifie PSP A, vérifie le schéma, inscrit le signal et un événement d'audit dans SQLite.
4. PSP B s'authentifie auprès du relais et lit uniquement les signaux non expirés qui lui sont destinés.
5. L'ingénieur vérifie l'audit avec une clé admin distincte. Le relais interdit l'accès anonyme et n'autorise pas PSP A à consulter l'inbox de PSP B.
6. Le TTL est appliqué **à la lecture** : les alertes expirées restent physiquement dans SQLite. La purge physique est une amélioration obligatoire avant tout usage autre que cette démo.

## 3. Technologies open source retenues

| Couche | Choix | Justification | Limite |
|---|---|---|---|
| Environnement | Docker Engine + Compose v2 | Reproductibilité locale, isolation des trois services | Pas une architecture haute disponibilité |
| API PSP A / PSP B / relais | Python 3.12 + FastAPI + Uvicorn | API HTTP simple, OpenAPI auto-documenté | Pas de mTLS, ni service mesh |
| Schémas | Pydantic v2 | Typage strict des catégories et champs autorisés | Pas un standard OFTA |
| Appels internes | HTTPX | Client HTTP asynchrone | Trafic HTTP sur réseau Docker de lab |
| Persistance | SQLite | Démonstrateur minimal, aucun serveur DB séparé | Pas conçu pour transactions multi-nœuds |
| Audit | Table SQLite dédiée | Piste élémentaire acteur/action/résultat | Non immuable, logs non exhaustifs |
| Tests | Bash + curl + Python | Scénarios observables et accessibles aux ingénieurs | Ensemble de tests de base, à étendre |

**Choix délibéré :** pas de Kafka, Kubernetes, Keycloak, PostgreSQL ou moteur antifraude complexe pour ce premier lab. Ces briques deviennent pertinentes en phase 2, après validation des flux minimaux. Le moteur **Tazama** peut faire l'objet d'un lab distinct ; il n'est **pas** intégré ici.

Références des projets :
- FastAPI : https://fastapi.tiangolo.com/
- Pydantic : https://docs.pydantic.dev/
- Docker Compose : https://docs.docker.com/compose/
- HTTPX : https://www.python-httpx.org/
- SQLite : https://sqlite.org/
- OWASP API Security Top 10 : https://owasp.org/API-Security/

## 4. Prérequis de la machine

- Linux Ubuntu récent, ou Windows 11 + WSL2 Ubuntu avec Docker opérationnel.
- Docker Engine + plugin `docker compose` ; `git`, `bash`, `openssl`, `curl`, `python3`.
- **Ressources recommandées (dimensionnement de lab, non testé) :** 2 vCPU, 4 Gio RAM libres, 2 Gio de disque ; aucun GPU.
- Ports libres : **8090** (relais/admin), **8091** (PSP A), **8092** (PSP B), tous liés à `127.0.0.1`.
- Accès Internet pour installer les images et dépendances. Version des paquets Python actuellement bornée par versions majeures, pas figée au niveau patch : figer les versions et scanner les images avant les prochains sprints.

### Vérification

```bash
docker --version                # Le moteur Docker est-il installé ?
docker compose version         # Vérifie Compose v2.
docker info >/dev/null         # Vérifie l'accès au démon, sans sudo implicite.
git --version
openssl version
curl --version
python3 --version
```

**Attention :** si l'utilisateur n'a pas accès à Docker, faire régler les permissions par l'administrateur de la machine ; l'accès au socket Docker accorde des privilèges élevés.

## 5. Procédure de réalisation — pas à pas

### Étape A — récupérer le code

```bash
git clone https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs.git
cd osef-open-source-payment-banking-labs/labs/FRAUD-001

# Vérifier la liste des fichiers de l'expérience.
ls -la
```

Pour une installation déjà clonée, `git pull --ff-only` depuis une branche propre puis naviguer vers le dossier.

### Étape B — générer les secrets de lab

```bash
# Génère quatre clés aléatoires locales dans .env si absent ; n'écrase jamais un .env existant.
bash scripts/init-env.sh

# Valide la syntaxe du fichier Compose et la présence des variables.
docker compose config --quiet
```

Ne jamais copier le contenu du `.env` dans une issue, un support de meetup ou un chat public. **Ne pas committer ce fichier.** Pour renouveler les secrets : arrêter les conteneurs, sauvegarder/supprimer le `.env` puis relancer l'initialisation ; cela invalide les anciennes clés, sans constituer une révocation fine par PSP.

### Étape C — construire, démarrer et contrôler

```bash
# Reconstruit localement les trois images et démarre les conteneurs.
docker compose up --build -d

# L'état attendu est "running" et le relais "healthy".
docker compose ps

# Tous les services répondent localement.
curl --fail --silent http://127.0.0.1:8090/health
curl --fail --silent http://127.0.0.1:8091/health
curl --fail --silent http://127.0.0.1:8092/health

# Diagnostiquer un démarrage incomplet sans afficher les secrets.
docker compose logs --tail=60 relay psp-a psp-b
```

**Résultat attendu** pour chaque réponse : un JSON avec `"status":"ok"` et le rôle du conteneur.

### Étape D — exécuter les tests d'acceptation

```bash
# Vérifie le signal valide, le doublon, la clé client invalide,
# la lecture depuis PSP B, le schéma invalide et l'accès relais interdit.
bash scripts/test-lab.sh
```

**Important :** ce script est un point de départ. Les résultats doivent être réellement produits et conservés par l'ingénieur exécutant : leur succès n'a pas été vérifié ici sur Docker.

### Étape E — démonstration manuelle facultative

```bash
# Charge les variables sans afficher les valeurs des clés dans le terminal.
set -a
source .env
set +a

# Envoie un signal 100 % synthétique via PSP A, avec un jeton démo unique.
curl --fail-with-body -X POST http://127.0.0.1:8091/submit \
  -H "X-Lab-Key: $LAB_USER_KEY" \
  -H "Content-Type: application/json" \
  -d '{"transaction_token":"demo-transaction-20261118-001","category":"suspicious-transfer","severity":"high","recipient":"psp-b","expires_in_hours":1}'

# Vérifie la visibilité du signal côté PSP B (autorisé).
curl --fail-with-body http://127.0.0.1:8092/inbox \
  -H "X-Lab-Key: $LAB_USER_KEY"

# Audite les opérations depuis le relais local, avec une clé distincte.
curl --fail-with-body http://127.0.0.1:8090/audit \
  -H "X-API-Key: $ADMIN_KEY"
```

Si l'identifiant de démo a déjà été enregistré, la création répondra **409 Conflict**, conformément à la règle de dédoublonnage. Utiliser un nouveau `demo-...` pour recommencer.

### Étape F — nettoyage et réinitialisation

```bash
# Arrête les services sans supprimer la base SQLite pour inspection.
docker compose down

# ATTENTION : destructif, supprime aussi le volume SQLite et l'historique d'audit du lab.
# À exécuter seulement après avoir sauvegardé les preuves nécessaires.
docker compose down --volumes

# .env reste présent : le supprimer uniquement si les secrets doivent être renouvelés.
```

## 6. Scénarios obligatoires et résultats attendus

| Test | Entrée | Résultat attendu |
|---|---|---|
| T01 | Signal valide PSP A vers PSP B | HTTP 201 |
| T02 | Même jeton fictif soumis deux fois | HTTP 409 |
| T03 | Mauvaise clé client côté PSP A | HTTP 401 |
| T04 | Lecture via PSP B autorisé | HTTP 200 avec signal |
| T05 | Catégorie inconnue | HTTP 422 |
| T06 | Requête sans clé sur le relais | HTTP 401 |
| T07 | Consultation du journal par admin | HTTP 200 |
| T08 | Signal expiré à la lecture | N'apparaît plus dans l'inbox (automatisé avec `--extended`, à valider en VM) |
| T09 | Indisponibilité du relais | HTTP 503 et reprise contrôlée (automatisé avec `--extended`, à valider en VM) |
| T10 | Clé PSP A utilisée pour lire /signals | HTTP 401 (automatisé avec `--extended`, à valider en VM) |

**Évolution vérifiée dans le code :** T08–T10 figurent maintenant dans le script `test-lab.sh --extended`. Cela ne prouve pas leur réussite sur une VM donnée : l'ingénieur doit exécuter le script et joindre ses preuves avant de cocher la couverture complète.

## 7. Critères de validation et livrables de contribution

- [ ] Environnement démarré sur Linux ou WSL2, sans accès depuis l'extérieur du poste.
- [ ] T01 à T07 passent avec preuve (captures/logs expurgés).
- [ ] T08 à T10 sont exécutés, documentés et automatisés avant validation finale.
- [ ] Tous les événements et identifiants sont synthétiques.
- [ ] Documentation d'architecture, API, risques et limites réalisée.
- [ ] Diagramme des flux et séquence de traitement joints à la PR.
- [ ] Référent OSEF désigné, PR relue et environnement nettoyé.
- [ ] Aucun résultat ne prétend une conformité réglementaire ou un déploiement réel.

### Travail supplémentaire (phase 2, hors MVP)

TLS/mTLS entre services, authentification OAuth2/OIDC avec Keycloak, secrets Vault, isolation réseau renforcée, journal d'audit append-only, métriques Prometheus/Grafana, PostgreSQL, simulation de panne/résilience, gestion du consentement et des bases légales, purge TTL effective et gouvernance multi-acteurs. Étudier la compatibilité éventuelle avec un modèle public OFTA uniquement **après** publication et vérification de ses artefacts.

## 8. Dépannage

| Symptôme | Piste de diagnostic |
|---|---|
| `docker compose config` échoue | `.env` absent, lancer `bash scripts/init-env.sh` |
| Port 8090/8091/8092 occupé | Identifier le processus local, ne pas désactiver le binding loopback pour contourner |
| Relais unhealthy | `docker compose logs relay`, permissions volume SQLite |
| HTTP 401 | Utiliser la bonne clé pour l'endpoint ; ne pas publier le secret |
| HTTP 409 | Identifiant synthétique déjà soumis ; en générer un nouveau |
| HTTP 422 | Vérifier le JSON, les enums et le préfixe obligatoire `demo-` |
| HTTP 503 | Vérifier `docker compose ps`, la résolution interne `relay`, les logs |

## 9. Statut de vérification

- **Conçu / déposé :** architecture, scripts et API publiés dans le dépôt.
- **Non confirmé pour la VM de chaque contributeur :** bon fonctionnement de l'ensemble des scénarios T01–T10. Des preuves partielles pour les échanges via navigateur figurent plus bas ; elles ne suffisent pas à valider tous les tests étendus.
- **Responsable :** à désigner.
- **Contexte réglementaire :** chaque organisation doit faire sa propre analyse juridique avant tout échange réel. Le lab ne démontre aucune conformité sectorielle.

## 10. Références

- Linux Foundation, annonce de l'OFTA : https://www.linuxfoundation.org/press/linux-foundation-announces-the-open-financial-trust-alliance-to-strengthen-coordinated-protection-against-fraud-scams-and-financial-crime
- FastAPI : https://fastapi.tiangolo.com/
- Docker Compose : https://docs.docker.com/compose/
- Pydantic : https://docs.pydantic.dev/
- OWASP API Security Top 10 : https://owasp.org/API-Security/


## Démonstration dans le navigateur

Reconstruire les images depuis le dossier du lab avec `docker compose up --build -d`. Dans le navigateur de la VM, ouvrir le [relais](http://localhost:8090/), le [PSP A](http://localhost:8091/) et le [PSP B](http://localhost:8092/).

Pour ouvrir ces pages sur Windows lorsque Docker tourne dans VirtualBox, ouvrir un tunnel depuis PowerShell et laisser la session ouverte. Adapter l’adresse de la VM si nécessaire.

```powershell
ssh -N -o ExitOnForwardFailure=yes -L 127.0.0.1:8090:127.0.0.1:8090 -L 127.0.0.1:8091:127.0.0.1:8091 -L 127.0.0.1:8092:127.0.0.1:8092 lionel@192.168.255.10
```

1. Dans le PSP A, saisir `LAB_USER_KEY` du fichier `.env`, envoyer un signal (T01), puis rejouer le même jeton (T02). Les boutons T03 et T05 couvrent la clé invalide et le format invalide.
2. Dans le PSP B, saisir `LAB_USER_KEY` et copier le jeton du PSP A pour le retrouver (T04). Garder le même onglet pour T08. Après expiration réelle ou expiration forcée de ce même signal fictif dans SQLite depuis la VM, exécuter T08. Le test observe le retrait de la boîte de réception.
3. Dans le relais, tester la lecture sans clé (T06), consulter l’audit avec `ADMIN_KEY` (T07), puis tester l’interdiction de lire avec `PSP_A_KEY` (T10).
4. Pour T09, garder le PSP B ouvert, exécuter `docker compose stop relay` dans la VM, puis cliquer sur **Lire pendant l’arrêt**. Redémarrer avec `docker compose start relay`, attendre que le relais soit `healthy` et relancer la lecture.

Les champs de clés sont masqués. Les clés sont envoyées uniquement dans les en-têtes des requêtes au service affiché et ne sont pas enregistrées par l’interface. Chaque onglet affiche les statuts HTTP, le contenu JSON et l’historique local des actions.


### Accéder directement aux trois services depuis Windows

Depuis Ubuntu, dans le dossier du lab, indique l’IPv4 privée de la VM sur l’adaptateur Host-only VirtualBox. Pour `osef-fraud-01` :

```bash
FRAUD_HOST_ONLY_IP=192.168.255.10 docker compose -f compose.yaml -f compose.host-only.yaml up --build -d
for port in 8090 8091 8092; do
  curl -fsS "http://192.168.255.10:$port/health" && echo
done
```

Ouvre le [relais](http://192.168.255.10:8090/), le [PSP A](http://192.168.255.10:8091/) et le [PSP B](http://192.168.255.10:8092/) sur Windows. L’adresse doit déjà être attribuée à la VM. Cette option publie les trois ports sur l’interface privée et conserve les ports locaux utilisés par les scripts. Pour recréer les services en conservant l’accès privé, réutilise les deux fichiers Compose et la variable. Pour revenir à l’accès local seul, exécute `docker compose up -d`.

Le réseau privé doit être réservé aux machines de démonstration autorisées. Utilise uniquement des données et des clés de lab.


### Parcours web validé le 18 novembre 2026

Lionel Sakiti a exécuté ce parcours depuis le navigateur Windows sur le réseau privé VirtualBox de la VM `osef-fraud-01`, avec un signal fictif.

1. **T01 — Envoyer depuis le PSP A (8091).** Saisir la clé de démonstration, puis cliquer sur **Envoyer**. HTTP **201** et `accepted` confirment l’enregistrement du signal. Copier le jeton du formulaire.

   ![T01 — Signal accepté par le PSP A, HTTP 201](evidence/t01-psp-a-emission.png)

2. **T04 — Retrouver le signal dans le PSP B (8092).** Saisir la même clé de démonstration et coller le jeton, puis cliquer sur **Lire les signaux**. HTTP **200** et le même jeton dans la réponse confirment l’échange. La réponse identifie `psp-a` comme émetteur et `psp-b` comme destinataire.

   ![T04 — Même signal retrouvé par le PSP B, HTTP 200](evidence/t04-psp-b-reception.png)

3. **T07 — Consulter le journal sur le relais (8090).** Saisir la clé d’audit et cliquer sur **Voir l’audit**. HTTP **200** et les entrées `psp-a / create / accepted` et `psp-b / read / authorized` montrent que le relais journalise les opérations.

   ![T07 — Création et lecture visibles dans le journal du relais, HTTP 200](evidence/t07-relais-audit.png)


## Tests étendus T08 à T10

Dans le dossier du lab, avec les trois services déjà démarrés, exécuter :

```bash
bash scripts/test-lab.sh --extended
```

Le script exécute d’abord T01 à T07. Ensuite, T10 vérifie le refus de lecture pour le PSP A. T09 arrête brièvement le relais, vérifie le HTTP 503 du PSP B, redémarre le relais et exige un HTTP 200 contenant le même jeton. T08 force l’expiration de ce seul signal fictif dans SQLite et vérifie qu’il disparaît de la boîte de réception. Prévoir cette interruption pendant une fenêtre de test du lab. Le mode sans argument exécute T01 à T07.


### Remarque pour Ubuntu VirtualBox et les droits Docker

Le script `test-lab.sh --extended` appelle `docker compose` pour arrêter et redémarrer le relais et modifier l'expiration du signal synthétique. Si `docker info` échoue sans droits d'administrateur, **ne pas ouvrir les permissions du socket Docker** : utiliser `sudo -v` puis lancer `sudo bash scripts/test-lab.sh --extended` dans le premier terminal. Le `.env` reste local et les tests n'utilisent que des données fictives. Pour le second terminal, `tail -n +1 -F /tmp/fraud-001-tests.log` permet de suivre le log du premier terminal si celui-ci est lancé avec `tee`.

### Suivre les tests automatisés en direct

Avec les trois services actifs, ouvrir deux terminaux sur la VM. Dans le premier, depuis `labs/FRAUD-001`, lancer la suite, afficher sa sortie et conserver un log :

```bash
(
  set -o pipefail
  bash scripts/test-lab.sh --extended 2>&1 | tee /tmp/fraud-001-tests.log
)
```

Dans le second terminal, suivre le fichier depuis le début :

```bash
tail -n +1 -F /tmp/fraud-001-tests.log
```

`Ctrl+C` dans le deuxième terminal arrête l’affichage. Le fichier est remplacé lors de la prochaine exécution et peut être relu avec `less /tmp/fraud-001-tests.log`.

Pour suivre l’état des conteneurs à la place, lancer depuis `labs/FRAUD-001` :

```bash
watch -n 1 docker compose ps -a
```

Pendant T09, le relais s’arrête brièvement. Le script affiche le HTTP 503 attendu, puis un HTTP 200 avec le même jeton après redémarrage. La suite réussit si elle se termine par `OK : scénarios T01 à T10 terminés.` Pour une démo, projeter le log à côté des interfaces web.

## Démarrage automatique après reboot de la VM VirtualBox

**Politique OSEF : les changements de configuration sont préparés dans une branche et intégrés via Pull Request GitHub. Ne pas créer ou modifier directement les fichiers de configuration dans la VM.**

Le `compose.yaml` versionné active `restart: unless-stopped` pour `relay`, `psp-a` et `psp-b`. Docker relancera les conteneurs **existants** au redémarrage du démon, sauf s'ils ont été arrêtés volontairement. Cette politique n'exécute **pas** `docker compose up` à chaque démarrage : une initialisation `up -d` est requise après avoir récupéré et intégré la PR. Une fois les ports Host-only créés, Docker conserve leurs publications au redémarrage.

### Après fusion de la PR (une seule fois sur Ubuntu)

```bash
cd /home/lionel/osef-open-source-payment-banking-labs
git status -sb                      # vérifier l'absence de changements locaux à préserver
git checkout main
git pull --ff-only origin main

cd labs/FRAUD-001
# Les fichiers sont versionnés ; aucune édition locale.
# La variable IP n'est utilisée que par Compose au moment de créer/recréer les conteneurs.
FRAUD_HOST_ONLY_IP=192.168.255.10 \
  docker compose -f compose.yaml -f compose.host-only.yaml up -d

# Vérifier les politiques et ports effectifs.
docker inspect --format '{{.Name}} {{.HostConfig.RestartPolicy.Name}}' \
  $(FRAUD_HOST_ONLY_IP=192.168.255.10 docker compose -f compose.yaml -f compose.host-only.yaml ps -q)

FRAUD_HOST_ONLY_IP=192.168.255.10 \
  docker compose -f compose.yaml -f compose.host-only.yaml ps
```

### Conditions requises et vérification

- `sudo systemctl enable --now docker` assure le démarrage du démon Docker avec Ubuntu.
- L'interface VirtualBox Host-only `enp0s8` doit conserver `192.168.255.10/24` via Netplan et être opérationnelle. Si Docker redémarre avant l'interface ou si l'adresse n'est plus présente, les ports explicitement liés à `192.168.255.10` peuvent ne pas être publiés correctement. Vérifier `ip -br addr show enp0s8` et `docker compose ps` après le test de reboot.
- Depuis Windows, vérifier `Test-NetConnection 192.168.255.10 -Port 8090`, `8091` et `8092`, puis ouvrir les pages HTTP dans un navigateur.
- Si `docker compose down` a **supprimé** les conteneurs, ou après un arrêt volontaire avec `docker stop`, le redémarrage automatique ne suffit plus. Relancer explicitement la commande `up -d` ci-dessus.
- Ne jamais utiliser `down --volumes` pour FRAUD-001 ; le volume SQLite contient les signaux fictifs et l'audit.
- **Important :** T09 dans `test-lab.sh --extended` arrête le relais de manière intentionnelle et le redémarre lui-même. Le test doit être surveillé et rejoué après la fusion afin de vérifier qu'il fonctionne avec la politique `unless-stopped`.

### Règle de gestion de configuration

1. Modifier les fichiers exclusivement **dans une branche GitHub dédiée**.
2. Ouvrir une Pull Request, faire vérifier les changements et les risques, puis fusionner.
3. Sur la VM, **synchroniser la branche approuvée avec Git**, sans créer de fichier de configuration ni exécuter d'édition manuelle sur place.
4. Appliquer la configuration versionnée avec `docker compose` et documenter les preuves d'exécution dans GitHub.

