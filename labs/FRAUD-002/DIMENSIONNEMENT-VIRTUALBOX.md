# FRAUD-002 — Dimensionnement et déploiement VirtualBox : deux options

> **Décision d'architecture à prendre, pas un déploiement déjà réalisé.** Mise à jour : 18 novembre 2026.
>
> Les ressources ci-dessous sont des **hypothèses de dimensionnement OSEF pour une démonstration**, **pas des minima officiels de Tazama ni des garanties de performance**. Aucun benchmark Tazama n'a encore été exécuté dans cette VM. **Ne pas utiliser en production, ni de données bancaires réelles.**

## Contexte observé sur la VM existante

Précontrôle communiqué depuis `osef-fraud-01` (Ubuntu 22.04.5 LTS, VirtualBox) :

| Élément | Mesure rapportée |
|---|---|
| vCPU | 2 |
| RAM totale | 3,8 Gio |
| RAM disponible à l'instant T | 3,1 Gio |
| Swap | 0 |
| Disque racine | 25 Go ; ~20 Go libres |
| Docker Engine | 29.10.0 |
| Docker Compose | v5.8.0 |
| FRAUD-001 | Ports 8090–8092 actifs en loopback et sur l'IP host-only 192.168.255.10 |
| Tazama cloné | `/home/lionel/tazama-stack` au commit `83e4b12c16986aedfff843ed84b7045ac912ec0a` |
| Composition Tazama | **13 services** d'après `docker compose config --services` : PostgreSQL, NATS, Valkey, TMS, event-director, admin-service, tazama-demo, typology-processor, event-adjudicator, event-flow, rule-901, rule-902 et batch-ppa |

**FRAUD-001 a passé T01–T10 selon le journal transmis par l'exécutant.** Préserver le volume SQLite, les secrets de laboratoire et les preuves avant toute opération sur l'hyperviseur.

## Comparatif de décision

| Critère | **Option A : deux VM** | **Option B : une VM redimensionnée** |
|---|---|---|
| Architecture | `osef-fraud-01` pour FRAUD-001 ; `osef-fraud-02` pour Tazama | FRAUD-001 et Tazama partagent `osef-fraud-01` |
| VM FRAUD-001 | Conserver 2 vCPU, 4 Gio, 25 Go | Remplacer son enveloppe par 4 à 6 vCPU, 12–16 Gio, 80–100 Go |
| VM FRAUD-002 | Nouvelle VM, **4 vCPU, 12 Gio RAM, 80 Go SSD**, swap 4 Gio optionnel | Pas de deuxième VM |
| Impact sur FRAUD-001 | Faible si VM 01 préservée et démarrée séparément | Arrêt obligatoire pendant redimensionnement ; compétition CPU/RAM/disque à l'exécution |
| Ressources sur le PC hôte | Pour deux VM simultanées : ~16 Gio de RAM invité au total + Windows/hyperviseur | Une VM de 12–16 Gio + Windows/hyperviseur |
| Réseau entre labs | Host-only isolé ; API accessibles uniquement aux VM autorisées | Docker networks séparés ; relier les services via API/ports contrôlés |
| Sauvegarde et restauration | Snapshots/exports indépendants | Une seule VM ; erreurs d'hôte pouvant toucher les deux labs |
| Complexité | Plus de gestion VM et de réseau | Plus simple à exploiter, mais risque de couplage |
| Recommandation | **Préférée si le laptop a ≥32 Gio de RAM et une capacité CPU suffisante** | **Alternative** si l'on souhaite limiter le nombre de VM, avec ressources suffisantes |

**Dimensionnements de départ à mesurer :** 4 vCPU/12 Gio/80 Go pour Tazama Core en démonstration. 8 Gio RAM/40 Go peuvent être essayés sur un profil réduit et sans charges, **sans garantie**, mais 3,8 Gio RAM ne constituent pas un point de départ recommandé pour 13 services.

### Contraintes du laptop physique

- Sur un laptop **16 Go RAM**, ne pas réserver 12–16 Go à Ubuntu sans mesurer la mémoire nécessaire à Windows : envisager une machine distante ou un essai limité séquentiel.
- Avec **32 Go RAM**, une VM Tazama de 12 Gio est une hypothèse de départ raisonnable ; le fonctionnement simultané de deux VM reste fonction de la charge Windows et du CPU réel.
- La **quantité de RAM physique du laptop n'est pas confirmée** à ce jour ; la recommandation finale dépendra de cette mesure.
- 4 Gio de swap, si ajoutés, sont une **marge de secours**, pas un remplacement de RAM. Surveiller la latence et `vmstat` ; ne pas prétendre que le swap rend la configuration suffisante.

## Option A — Deux VM : séparation recommandée

```text
PC Windows 11 + Oracle VirtualBox
  ├─ osef-fraud-01 : Ubuntu 22.04.5 (existant, garder tel quel)
  │    └─ FRAUD-001 : PSP A / Relay + SQLite / PSP B (8090–8092)
  └─ osef-fraud-02 : Ubuntu 22.04/24.04 (nouvelle VM)
       └─ FRAUD-002 : Tazama Core (Docker Compose, profil Public DockerHub)
           └─ PostgreSQL / NATS / Valkey / TMS / règles / adjudication
```

### Préparation VirtualBox

1. Sauvegarder les preuves de FRAUD-001 et effectuer une sauvegarde/export **hors du disque de la VM** ; un snapshot seul n'est pas une sauvegarde durable.
2. Créer `osef-fraud-02` sur Ubuntu Server 22.04 LTS ou 24.04 LTS, **4 vCPU, 12 Gio de RAM, 80 Go VDI dynamique**. Choisir un volume SSD côté hôte si disponible.
3. Réseau : **NAT** pour télécharger les images ; ajouter **Host-only** si une communication contrôlée avec `osef-fraud-01` ou Windows est nécessaire. Ne pas activer les redirections vers Internet.
4. Installer Docker Engine et Compose avec les procédures officielles, puis exécuter le précontrôle OSEF sur la nouvelle VM.
5. Cloner la version Tazama examinée, noter le commit, inspecter les fichiers Compose et les publications de ports avant le démarrage. Ne pas copier les secrets de FRAUD-001.
6. Dans un premier temps, démarrer **uniquement FRAUD-002** : pour tester les deux ensembles à la fois, vérifier la RAM disponible sur le PC hôte et les conflits réseau.
7. Avant d'intégrer les labs, autoriser explicitement la connectivité vers une **API précise** : pas d'exposition de PostgreSQL/NATS/Valkey sur le réseau partagé et pas d'accès Internet entrant.

### Critères de passage Option A

- [ ] VM `osef-fraud-02` démarrée et `preflight.sh` exécuté.
- [ ] CPU, mémoire, espace disque et swap surveillés pendant les 13 services.
- [ ] Aucune modification/perturbation de FRAUD-001.
- [ ] Tests Tazama officiels passés sur jeux fictifs et version fixée.
- [ ] Ports exposés et pare-feu documentés avant interconnexion.

## Option B — Une seule VM redimensionnée

```text
PC Windows 11 + Oracle VirtualBox
  └─ osef-fraud-01 : Ubuntu 22.04.5 (VM existante redimensionnée)
       ├─ FRAUD-001 : 3 conteneurs, ports 8090–8092
       └─ FRAUD-002 : Tazama Core, 13 services prévus
          → ports et réseaux à vérifier / isoler
```

### Procédure de migration sans perte intentionnelle de données

1. **Arrêt planifié** de FRAUD-001 (interruption de la démonstration). Enregistrer `docker compose ps` et les preuves T01–T10.
2. Sauvegarder hors VM le projet, **le volume SQLite** et les clés de lab dans un endroit protégé ; ne pas publier `.env`. Exporter la VM si possible.
3. Éteindre proprement Ubuntu : `sudo shutdown -h now`. **Ne jamais redimensionner un disque utilisé par une VM en fonctionnement.**
4. Dans VirtualBox, attribuer **4 à 6 vCPU et 12–16 Gio RAM** si le laptop le permet. Préférer **80–100 Go VDI dynamique** pour le disque ; vérifier l'espace disponible sur le disque physique de Windows.
5. Si le VDI existant est agrandi, **ne pas présumer que la partition et le système de fichiers le sont automatiquement**. Vérifier dans Ubuntu avec `lsblk -f`, `findmnt -no SOURCE,FSTYPE /` et `df -h /`. Suivre la procédure correspondant **au type de partition et de système de fichiers observé** (ext4/LVM/autre). Ne pas exécuter de commande `growpart`, `resize2fs` ou `lvextend` avant cette identification et une sauvegarde.
6. Démarrer la VM, vérifier `free -h`, `nproc`, `df -h /` et relancer `bash scripts/preflight.sh`.
7. Vérifier FRAUD-001 : `docker compose ps`, puis `bash scripts/test-lab.sh --extended`. **Le mode étendu arrête brièvement le relais** pour le test T09 ; à exécuter uniquement dans le lab.
8. Avant de lancer Tazama, identifier les **ports publiés** par les 13 services et les réseaux ; comparer aux ports FRAUD-001 8090–8092. Les services Tazama peuvent exposer plusieurs interfaces ; ne pas utiliser une publication `0.0.0.0` sans justification ni protection.
9. Déployer Tazama avec un nom de projet distinct (`tazama-core`) et un réseau séparé ; ne pas utiliser `docker system prune --volumes`, `docker compose down --volumes` sur FRAUD-001 ni supprimer les volumes hors périmètre.
10. Mesurer l'usage combiné pendant les tests, sans confondre un démarrage réussi et une stabilité démontrée.

### Critères de passage Option B

- [ ] Export/sauvegarde réalisé et restaurable.
- [ ] RAM/CPU/capacité disque visibles dans Ubuntu après redimensionnement.
- [ ] FRAUD-001 relancé avec T01–T10 réussis.
- [ ] Aucun conflit de ports, secrets, volumes ou réseaux.
- [ ] Tazama Core testé sans échec mémoire ni impact inacceptable sur FRAUD-001.
- [ ] Prévoir un rollback : restauration de la VM sauvegardée si redimensionnement ou tests échouent.

## Vérifications non destructives communes avant un déploiement Tazama

À lancer **dans la VM candidate**, avec l'instance Tazama clonée :

```bash
# Observer CPU / mémoire / disque.
nproc
free -h
df -h /
lsblk -f

# Relever les ports déjà à l'écoute.
ss -ltn

# Comparer les ports prévus de la stack Tazama, en évitant d'imprimer les secrets.
cd /home/lionel/tazama-stack/core
FILES=(
  -f docker-compose.base.infrastructure.yaml
  -f docker-compose.base.override.yaml
  -f docker-compose.hub.cfg.yaml
  -f docker-compose.hub.core.yaml
  -f docker-compose.hub.rules.yaml
)
docker compose "${FILES[@]}" config --format json |
python3 -c 'import json,sys; d=json.load(sys.stdin); [(print(n, "ports:", [(p.get("host_ip"),p.get("published"),p.get("target")) for p in s.get("ports",[])], "memory:", s.get("deploy",{}).get("resources",{}).get("limits",{}).get("memory","non définie"))) for n,s in d["services"].items()]'

# Cette commande ne crée pas de conteneurs.
```

**Attention :** la stack officielle `core/tazama-core.sh` peut exécuter `docker compose ... down --volumes` sur des projets Tazama pendant un redéploiement. Lire les choix et les commandes affichées avant validation. Ne pas utiliser ses fonctions de purge générale sans inventaire préalable de tous les projets Docker.

### Mesures à enregistrer après démarrage (seulement si la VM est dimensionnée)

```bash
free -h
df -h /
docker stats --no-stream
docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
```

Laisser tourner le lab pendant les scénarios de test et recueillir les pics et les échecs, sans secrets dans les logs. **Aucune valeur de RAM par conteneur ni de débit transactionnel n'est encore mesurée**.

## Choix recommandé et prochain jalon

**Option A** si le laptop peut accueillir une seconde VM et si la séparation des labs importe. **Option B** si une seule VM est plus pratique, à condition de sauvegarder FRAUD-001, d'agrandir proprement son disque et de vérifier la cohabitation.

**Décision finale en attente :** mémoire RAM physique du PC Windows, CPU disponible, espace disque réel, choix de l'option. Ces critères permettront d'arrêter la configuration sans inventer la capacité du laptop.

### Sources vérifiables

- [Tazama Stack — dépôt et avertissement sandbox](https://github.com/tazama-lf/tazama-stack)
- [README Core officiel](https://github.com/tazama-lf/tazama-stack/blob/83e4b12c16986aedfff843ed84b7045ac912ec0a/core/README.md)
- [Lanceur exact au commit inspecté](https://github.com/tazama-lf/tazama-stack/blob/83e4b12c16986aedfff843ed84b7045ac912ec0a/core/tazama-core.sh)
- [VirtualBox — manuel officiel](https://www.virtualbox.org/manual/)
- [Docker Engine — installation Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- [FRAUD-001 — issue #43](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/43)
- [FRAUD-002 — issue #50](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/50)
