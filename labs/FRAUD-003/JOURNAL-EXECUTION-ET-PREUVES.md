# FRAUD-003 — Journal d'exécution et preuves techniques

> **Règle de suivi :** enregistrer au fur et à mesure les commandes, sorties expurgées, conclusions, limites, incidents, corrections par PR et critères de passage des Gates. Les observations viennent des sorties terminal **fournies par l'opérateur** : elles ne sont pas des mesures exécutées directement par le rédacteur sur la VM. Ne jamais publier de secrets, de fichier `.env`, de données personnelles ni de rapports bruts sensibles.

## Session du 20 novembre 2026 — Gate 0, précontrôles

**Machine déclarée :** Ubuntu dans VirtualBox, VM `osef-fraud-01` ; dépôt `/home/lionel/osef-open-source-payment-banking-labs`.

### Contrôle Git

Commande rapportée :

```bash
git status -sb
git rev-parse --short HEAD
git remote -v
```

Résultat observé sous `root` :

```text
## main...origin/main
627fc07
origin  https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs.git (fetch)
origin  https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs.git (push)
```

**Limites :** l'état `main...origin/main` compare seulement les références Git locales et ne prouve pas que `main` est synchronisée avec GitHub au 20/11. Les écritures FRAUD-003 de la PR #79 ne sont **pas** présentes dans ce checkout tant que la PR n'a pas été fusionnée puis synchronisée.

### Incident de propriété Git — **ouvert**

Observation en session `lionel` : `fatal: detected dubious ownership`. Vérification en session `root` :

```text
root:root 755 /home/lionel/osef-open-source-payment-banking-labs
root:root 755 /home/lionel/osef-open-source-payment-banking-labs/.git
root:root 644 /home/lionel/osef-open-source-payment-banking-labs/.git/config
```

Une commande ultérieure a encore affiché `root:root .` et `root:root .git`, et les diagnostics ont continué avec l'invite `root@osef-fraud-01`. **Aucune preuve ultérieure de correction de propriété et de succès de Git sous `lionel` n'a été fournie.** Ne pas considérer l'incident résolu et ne pas contourner aveuglément avec `safe.directory`.

**Contrôle de clôture :** vérifier l'absence de montage protégé sous le dépôt, corriger les propriétaires si approprié, puis obtenir `stat -c '%U:%G %n' . .git` et `git status -sb` en tant que `lionel`. Ne pas faire de modifications Git sous `root`.

### FRAUD-001 : services et réseau

Commande rapportée : `docker compose ps` dans `labs/FRAUD-001`.

Observations :
- `fraud-001-psp-a-1` : `Up`, accès loopback `127.0.0.1:8091` et Host-only `192.168.255.10:8091`.
- `fraud-001-psp-b-1` : `Up`, accès `127.0.0.1:8092` et `192.168.255.10:8092`.
- `fraud-001-relay-1` : `Up (healthy)`, accès `127.0.0.1:8090` et `192.168.255.10:8090`.

### FRAUD-002 : Tazama

Commande rapportée : `python3 labs/FRAUD-002/scripts/tazama-safe.py ps`.

Observations :
- `[OK] 13 services, 8 ports localhost et Tazama Demo sur 192.168.255.10:3011 ; aucune collision 8090–8092.`
- `admin-service`, `batch-ppa`, `core-postgres`, `event-adjudicator`, `event-director`, `event-flow`, `nats`, `rule-901`, `rule-902`, `tazama-demo`, `tms-service`, `typology-processor` et `valkey` : `Up`.
- `batch-ppa`, `core-postgres`, `tazama-demo`, `valkey` : `healthy`.
- Script signale : **aucune limite mémoire déclarée** ; ne pas lancer de nouveaux services avant contrôle RAM/CPU/disque.

### HTTP : cinq réponses positives — 20/11/2026 09:23 UTC

Commandes en lecture seule :

```bash
curl -sS -i --max-time 5 http://127.0.0.1:8090/health
curl -sS -i --max-time 5 http://127.0.0.1:8091/health
curl -sS -i --max-time 5 http://127.0.0.1:8092/health
curl -sS -i --max-time 5 http://127.0.0.1:5000/
curl -sS -i --max-time 5 http://127.0.0.1:5100/
```

| Endpoint | Observé |
|---|---|
| Relais 8090 | `200 OK`, `{"status":"ok","role":"relay"}` |
| PSP A 8091 | `200 OK`, `{"status":"ok","role":"psp-a"}` |
| PSP B 8092 | `200 OK`, `{"status":"ok","role":"psp-b"}` |
| Tazama TMS 5000 | `200 OK`, `{"status":"UP"}` |
| Tazama Admin 5100 | `200 OK`, `{"status":"UP"}` |

**Interprétation :** disponibilité HTTP des interfaces interrogées, **pas** nouveau test transactionnel complet ni garantie de bon fonctionnement sous charge.

### Inspection du code FRAUD-001 — routes et autorisations

Commandes sans modification :

```bash
grep -nE '@app\.(get|post|put|delete|patch)' labs/FRAUD-001/app.py
grep -nE 'class .*BaseModel|transaction_token|category|severity|recipient|expires_in_hours' labs/FRAUD-001/app.py
sed -n '1,94p' labs/FRAUD-001/app.py
sed -n '95,194p' labs/FRAUD-001/app.py
```

Résultats lus dans le code fourni :

| Route | Rôle conditionnel et comportement |
|---|---|
| `GET /health` | Retourne `role` et `status` |
| `POST /signals` | Relais seulement, clé `PSP_A_KEY` ; SQLite, jeton unique, HTTP 409 si doublon |
| `GET /signals` | Relais seulement, clé `PSP_B_KEY` ; filtre `recipient = psp-b` et `expires_at > now`, limite 100 |
| `GET /audit` | Relais seulement, clé `ADMIN_KEY` ; journal d'événements |
| `POST /submit` | PSP A seulement, `LAB_USER_KEY` ; relais HTTP avec clé `PSP_A_KEY` |
| `GET /inbox` | PSP B seulement, `LAB_USER_KEY` ; consultation relayée avec clé `PSP_B_KEY` |
| `GET /` | Interface web HTML de laboratoire |

Schéma `Signal` observé : `transaction_token` avec motif `^demo-[A-Za-z0-9-]{8,64}$` ; `category` ∈ `suspicious-transfer`, `account-takeover`, `social-engineering` ; `severity` ∈ `low`, `medium`, `high` ; `recipient` = `psp-b` ; `expires_in_hours` entier de 1 à 24.

**Observations de sécurité :**
- `hmac.compare_digest` utilisé pour les vérifications de clés ; clés chargées depuis variables d'environnement.
- Le compte de démonstration à l'entrée des deux PSP repose sur la même variable `LAB_USER_KEY` ; les clés internes de rôles sont séparées au relais.
- L'audit enregistre `timestamp`, `actor`, `action`, `outcome` ; aucune charge utile ni clé n'est insérée par la fonction `audit`.
- Une expiration filtre les résultats lus mais **ne prouve pas la purge physique** des données SQLite.
- Le relais est **bipartite**, pas un système de trois institutions ; ses permissions ne doivent pas être étendues par hypothèse.

**Décision d'architecture proposée, non encore approuvée :** construire un service FRAUD-003 distinct avec identités institutionnelles séparées, politique d'accès par propriétaire et dossier, et persistance indépendante. L'utilisation de Tazama Case Management reste à étudier ; ne pas présumer l'existence d'une API compatible.

## Étape suivante — dimensionnement avant toute nouvelle création de conteneurs

Les mesures CPU/RAM/disque ont été **fournies et analysées** pour un instantané de la VM (voir session ci-dessous). La capacité de fonctionnement sous charge et la décision de déploiement FRAUD-003 restent **à valider**, notamment parce qu'aucun plafond mémoire des services existants n'est déclaré.

```bash
# Diagnostic en lecture seule uniquement
nproc
free -h
df -h /
docker stats --no-stream --format 'table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}'
```

## Session du 20 novembre 2026 — Gate 0, ressources et capacité (sortie opérateur)

Commandes exécutées : `nproc`, `free -h`, `df -h /`, `docker stats --no-stream --format 'table {{.Name}}\\t{{.CPUPerc}}\\t{{.MemUsage}}'`. Aucune action modificatrice.

| Ressource | Résultat effectivement communiqué |
|---|---|
| vCPU | `4` |
| Mémoire système | `11Gi total`, `1.0Gi used`, `9.2Gi free`, `1.4Gi buff/cache`, `10Gi available` |
| Swap | `0B` |
| Partition racine | `/dev/sda2` : `79G` total, `8.5G` utilisés, `67G` disponibles, `12%` utilisés |
| Conteneurs visibles | 16 (13 Tazama + 3 FRAUD-001) |
| Limite Docker affichée | `11.68GiB` pour chaque conteneur : valeur maximale système affichée, **pas une limite mémoire individuelle configurée** |

### Instantané par service (CPU ; mémoire)

| Service | CPU instantané | RAM |
|---|---:|---:|
| batch-ppa | 0.00 % | 57.98 MiB |
| tazama-demo | 0.00 % | 158.7 MiB |
| typology-processor | 0.00 % | 61.39 MiB |
| admin-service | 0.00 % | 57.43 MiB |
| tms-service | 0.00 % | 63.38 MiB |
| event-adjudicator | 0.00 % | 52.29 MiB |
| event-flow | 0.00 % | 45.62 MiB |
| rule-902 | 0.00 % | 46.25 MiB |
| event-director | 0.00 % | 55.43 MiB |
| rule-901 | 0.00 % | 50.9 MiB |
| core-postgres | 0.00 % | 52.52 MiB |
| nats | 0.19 % | 6.062 MiB |
| valkey | 28.87 % | 11.29 MiB |
| fraud-001-psp-a-1 | 0.65 % | 47.87 MiB |
| fraud-001-psp-b-1 | 0.71 % | 48.27 MiB |
| fraud-001-relay-1 | 33.07 % | 35.95 MiB |

**Interprétation bornée :** la mémoire disponible (`10Gi`) et le disque libre (`67G`) donnent une marge pour envisager un prototype très léger. Les pics ponctuels CPU de Valkey et du relais ne suffisent pas à établir une saturation ou une capacité sous charge. Aucun swap n'est configuré ; aucun plafond de RAM dédié aux conteneurs existants n'est prouvé. Le chiffre 11.68 GiB affiché par `docker stats` ne doit pas être interprété comme une allocation réservée par conteneur.

**Décision Gate 0 (provisoire) :** faisabilité plausible d'un **prototype FRAUD-003 léger** sur la même VM, avec budget de ressources explicite, ports distincts, non-régression FRAUD-001/002 et arrêt contrôlé. **Pas de feu vert pour déployer les trois simulateurs ni pour un test en charge sans revue Gate 1**, vérification de la propriété Git sous `lionel` et approbation des paramètres techniques.

**Preuves restant à obtenir :** mesures sur une période représentative de charge, comportement des services existants pendant le lab, limites de ressources dans les fichiers Compose proposés, backup si nouvelles données persistantes, et revue technique.

---

## Checklist vivante Gate 0

- [x] Services FRAUD-001/002 repérés et états Docker observés.
- [x] Disponibilité HTTP des cinq interfaces testées.
- [x] Routes et validations du modèle FRAUD-001 examinées sur la copie locale.
- [x] Limitations de réutilisation bipartite documentées.
- [ ] Propriété Git corrigée et accès utilisateur `lionel` vérifié.
- [x] Mesures CPU/RAM/disque et charge Docker récoltées et interprétées (instantané seulement ; tests en charge non réalisés).
- [ ] Contrats comparés au code fusionné et validés en revue.
- [ ] Décision d'isolation et architecture Gate 1 approuvées.
- [ ] PR documentaire fusionnée ; code de `main` synchronisé en sécurité.

## Session du 20 novembre 2026 — Gate 2 : huit tests unitaires réussis sur la VM

**Preuve :** sortie terminal transmise par l'opérateur sur `osef-fraud-01`, en utilisant le worktree `/tmp/osef-fraud003-pr79-test` au commit `b3eba12` de la PR #79. Tests exécutés dans `python:3.12-slim` avec `--network host` et dépôt monté en lecture seule ; la tentative précédente en réseau Docker par défaut était bloquée par la résolution DNS pendant `pip install`.

Commande exécutée :

```bash
cd /tmp/osef-fraud003-pr79-test
docker run --rm --network host -v "$(pwd):/work:ro" -w /work python:3.12-slim \
  sh -c 'pip install --quiet --retries 1 --timeout 10 -r labs/FRAUD-003/requirements.txt && python -m unittest discover -s labs/FRAUD-003/tests -p "test_*.py" -v'
```

**Résultat observé : `Ran 8 tests in 1.961s` ; `OK`.** Les huit scénarios réussis sont : lecture isolée des trois institutions, doublon intra-institution, expiration, santé HTTP, validation d'identifiants et TTL, authentification refusée, clés invalides au démarrage, et rejet des champs sensibles inattendus.

**Avertissements non bloquants :** `pip` en tant que root à l'intérieur du conteneur temporaire ; avertissement de dépréciation `StarletteDeprecationWarning` concernant `httpx` / `starlette.testclient`. La compatibilité exacte des versions doit être suivie.

**Limites :** seuls les tests par `TestClient` sont prouvés ; l'image du service `labs/FRAUD-003/Dockerfile`, le lancement Compose, l'API sur `127.0.0.1:8113` et les essais de bout en bout sont encore non testés. La PR reste non fusionnée et non revue.

**Étape suivante :** recette Docker locale isolée sur VM, preuves de création/lecture des trois institutions, contrôle croisé 404, puis revue finale et décision de fusion.

---

## Protocole de consignation pour chaque prochaine séance

Documenter : **date**, **Gate**, **commande en lecture seule ou script versionné**, **résultat réellement observé**, **pass/fail/non testé**, **limites**, **issue/PR**, **prochaine décision**. Ne jamais cocher un test à partir d'une sortie attendue ou d'une hypothèse.

La progression technique précède ici les séances d'approfondissement métier et la préparation finale du meetup, conformément à la préférence d'exécution du laboratoire. Les trois dimensions restent dans le standard OSEF : [parcours intégré](PARCOURS-TECHNIQUE-METIER-MEETUP.md).
