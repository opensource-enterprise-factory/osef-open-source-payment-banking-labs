# FRAUD-001 — Guide de reprise pour un ingénieur

## Résultat à reproduire

Déployer un relais antifraude et deux prestataires de paiement fictifs. Le PSP A publie un signal, le relais le contrôle et l’enregistre dans SQLite, le PSP B retrouve le même jeton, puis le relais expose l’audit. Utiliser uniquement les données et les clés de démonstration.

| Service | Port hôte | Rôle |
|---|---:|---|
| Relais | 8090 | Contrôle des droits, validation, dédoublonnage, audit et persistance |
| PSP A | 8091 | Émission de signaux fictifs |
| PSP B | 8092 | Lecture des signaux qui lui sont destinés |

## 1. Préparer la VM

Pour un poste Windows, utiliser une VM Ubuntu VirtualBox avec une carte NAT pour les téléchargements et, si accès direct depuis Windows souhaité, une carte Host-only pour la démo. Utiliser l’IPv4 effectivement attribuée à cette carte, confirmée avec `ip -br -4 addr`. L’adresse du test OSEF était `192.168.255.10` et doit être adaptée sur une autre installation. Pour la préparation Ubuntu et Docker, suivre le [guide VirtualBox](VIRTUALBOX-UBUNTU.md) et l’[installation Docker pour Ubuntu](https://docs.docker.com/engine/install/ubuntu/).

```bash
# Confirmer les outils et l'accès au moteur Docker.
git --version
docker compose version
docker info --format '{{.ServerVersion}}'
command -v bash curl openssl python3
```

## 2. Déployer et vérifier les services

```bash
# Cloner une seule fois. Si le dépôt existe déjà, entrer dans son dossier et récupérer main.
git clone https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs.git
cd osef-open-source-payment-banking-labs/labs/FRAUD-001

# Générer les quatre clés locales, sans écraser un .env existant.
bash scripts/init-env.sh &&
docker compose config --quiet &&
docker compose up --build -d
```

Pour un accès direct depuis Windows, utiliser la variante suivante pour créer ou recréer les trois services. Remplacer l’IP d’exemple par celle de la VM. Les ports locaux restent disponibles pour les scripts.

```bash
FRAUD_HOST_ONLY_IP=192.168.255.10 docker compose \
  -f compose.yaml -f compose.host-only.yaml up --build -d
```

```bash
# Attendre trois services Up et un relais healthy.
docker compose ps
for port in 8090 8091 8092; do
  curl -fsS --max-time 5 "http://127.0.0.1:$port/health" && echo
done
```

## 3. Rejouer la démo web

Ouvrir les ports 8091, 8092 et 8090 avec l’adresse de la VM depuis Windows en mode Host-only, ou avec `localhost` depuis la VM. Pour consulter une clé, lancer par exemple `grep '^LAB_USER_KEY=' .env` dans un terminal privé et copier la valeur après le signe égal. Garder le fichier et les valeurs clés hors des captures, journaux partagés et commits.

1. **PSP A : T01.** Saisir `LAB_USER_KEY`, générer un nouveau jeton, envoyer le signal. Vérifier HTTP 201 et copier le jeton.
2. **PSP B : T04.** Saisir la même clé et rechercher le jeton. Vérifier HTTP 200 et la présence du même jeton.
3. **Relais : T07.** Saisir `ADMIN_KEY`, consulter l’audit, vérifier HTTP 200 et des entrées de création et de lecture.

Voir les [captures commentées](README.md#parcours-web-validé-le-18-novembre-2026). Les autres boutons permettent de rejouer les contrôles par service.

## 4. Exécuter et suivre T01 à T10

Avec les trois services démarrés, lancer depuis le dossier du lab :

```bash
# Exécuter les tests étendus et conserver le statut d'échec malgré tee.
(
  set -o pipefail
  bash scripts/test-lab.sh --extended 2>&1 | tee /tmp/fraud-001-tests.log
)
```

Dans un second terminal sur la même VM, lancer `tail -n +1 -F /tmp/fraud-001-tests.log`. Pour suivre les conteneurs dans le dossier du lab, lancer `watch -n 1 docker compose ps -a`. Le mode sans argument exécute T01 à T07. T09 du mode étendu arrête brièvement le relais et le redémarre. Prévenir les participants d’une démo qui utilise le même relais avant de le lancer.

| Test | Résultat attendu |
|---|---|
| T01 | Signal accepté, HTTP 201 |
| T02 | Doublon rejeté, HTTP 409 |
| T03 | Clé client invalide rejetée, HTTP 401 |
| T04 | Lecture PSP B, HTTP 200 et même jeton |
| T05 | Schéma invalide rejeté, HTTP 422 |
| T06 | Lecture directe sans clé refusée, HTTP 401 |
| T07 | Audit, HTTP 200 et journal non vide |
| T08 | Signal visible avant expiration, absent après, lecture HTTP 200 |
| T09 | 200 avant arrêt, 503 pendant l’arrêt, 200 après redémarrage avec le même jeton |
| T10 | Lecture directe avec la clé du PSP A refusée, HTTP 401 |

La suite étendue doit se terminer par `OK : scénarios T01 à T10 terminés.`

## 5. Vérifier T11 et conserver les preuves

La suite étendue laisse un signal fictif expiré après T08. Créer ensuite un nouveau signal avec T01 et vérifier sa lecture avec T04. Garder son jeton.

```bash
# Simulation en lecture seule. Le nombre dépend de l'historique du lab.
docker compose exec -T relay python - < scripts/purge-expired.py

# Une fois le périmètre vérifié, supprimer les signaux fictifs expirés.
docker compose exec -T relay python - --apply < scripts/purge-expired.py

# Vérifier le nombre de lignes expirées restantes.
docker compose exec -T relay python - < scripts/purge-expired.py
```

Vérifier le compteur à zéro, retrouver le jeton actif avec T04 et consulter à nouveau T07. Consigner le commit testé, les statuts de santé, le résumé T01 à T10, les compteurs T11 et les résultats des contrôles après purge. Ne joindre aucune clé. La [preuve de l’exécution de référence](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/43) rapporte 13 lignes purgées, puis zéro, un signal actif visible et l’audit consultable.

## 6. Dépanner et arrêter le lab

| Symptôme | Vérification |
|---|---|
| Git signale que le dossier n’est pas un dépôt | Entrer dans le clone, puis dans `labs/FRAUD-001`. |
| L’URL Windows ne répond pas | Vérifier l’IP Host-only et les publications dans `docker compose ps`. Une publication à `127.0.0.1` est locale à la VM. |
| HTTP 401 inattendu | Vérifier la clé du champ utilisé et sa valeur dans le `.env` du même déploiement. |
| HTTP 503 hors T09 | Vérifier `docker compose ps -a` et `docker compose logs --tail 50 relay`. |
| T11 échoue avec un fichier introuvable | Vérifier le dossier courant et la présence de `scripts/purge-expired.py` sur le commit testé. |

Pour suspendre le lab et reprendre avec les mêmes données, exécuter `docker compose stop`. Sur une VM partagée avec FRAUD-002, exécuter les commandes de ce guide depuis le dossier de FRAUD-001. Les deux labs partagent les ressources de la VM. Une démo FRAUD-002 qui appelle le relais peut voir une interruption pendant T09.

La validation de référence couvre le lab pédagogique sur VirtualBox. La tenue en charge, les autres scénarios de panne et un pilote avec des institutions relèvent de travaux ultérieurs.
