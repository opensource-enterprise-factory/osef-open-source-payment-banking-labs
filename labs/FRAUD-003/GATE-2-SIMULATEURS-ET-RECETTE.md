# FRAUD-003 — Gate 2 : trois institutions fictives, isolation et recette

> **Statut : code proposé en PR #79, non fusionné et non exécuté sur la VM.** Les résultats ci-dessous sont des **attendus**, pas des succès observés. Pas de connectivité réelle à Tazama, FRAUD-001, un PSP ou une banque.

## Périmètre réalisé dans le code

Un **service FastAPI distinct** simule trois institutions virtuelles : `demo-bank-a`, `demo-psp-b`, `demo-mobile-c`. Ce sont trois **identités et espaces de données séparés dans un service commun**, pas trois conteneurs indépendants. Le moteur de corrélation, la communication inter-établissements et l'investigation ne sont pas encore implémentés (Gates 3 à 5).

- `POST /signals` — enregistrer uniquement un signal synthétique pour l'institution authentifiée.
- `GET /signals` — lister exclusivement les signaux actifs appartenant à cette institution (maximum 100).
- `GET /signals/{signal_id}` — récupérer son propre signal ; renvoyer 404 pour un signal absent **ou détenu par une autre institution**, afin de ne pas divulguer son existence.
- `GET /health` — disponibilité HTTP uniquement.
- `409` — doublon de `signal_id` **au sein d'une institution** ; le même identifiant fictif chez deux institutions ne constitue pas une collision inter-tenant.
- `422` — rejet des champs inattendus ou non conformes, y compris numéro de carte ou données personnelles ajoutées au JSON.
- `401` — clé manquante ou invalide.
- `expires_at` — les signaux expirés ne sont plus visibles à la lecture ; **aucune purge physique prouvée**.
- Audit SQLite interne : création, doublon, liste et consultation ; pas d'endpoint public d'audit à ce Gate.
- Configuration fail-closed : impossible de démarrer avec des clés absentes, trop courtes ou identiques.

## Choix et limites de conception

- Chaque institution possède une clé indépendante, lue depuis une variable d'environnement. Pas de `LAB_USER_KEY` partagé de FRAUD-001.
- L'API et SQLite sont **propres à FRAUD-003** ; le code, les volumes et les ports des laboratoires FRAUD-001/002 restent inchangés.
- Accès local : `127.0.0.1:8113`, sans publication Host-only par défaut.
- Ressources proposées dans `compose.yaml` : maximum `384m` de RAM, `0.75` CPU, `128` processus ; conteneur sans privilège, système de fichiers en lecture seule, volume de données distinct.
- Stockage SQLite seulement pour le premier Gate, non pour une preuve de montée en charge ou de résilience à plusieurs nœuds.
- Les tests de contrôle d'accès s'appuient ici sur la clé de l'institution ; une identité de personne, un dossier collaboratif, une authentification forte ou une révocation centralisée ne sont **pas encore** implémentés.
- Les valeurs `scenario_ref` sont des références de scénarios fabriqués ; elles ne doivent pas être déduites d'un identifiant de client ou de compte.
- Aucun partage transversal ne se produit. Le Gate 3 devra introduire une projection minimale **approuvée** avant toute corrélation entre établissements.

## Tests de code à exécuter après revue/fusion

Les prérequis Python du laboratoire sont dans `requirements.txt`. Sur un environnement Python isolé disponible, lancer **uniquement les tests**, sans installation improvisée des dépendances sur l'OS :

```bash
# Depuis la racine du dépôt synchronisé sur main après fusion.
# N'utilise aucun conteneur ni API Tazama/FRAUD-001.
python3 -m unittest discover -s labs/FRAUD-003/tests -p 'test_*.py' -v
```

La suite couvre : disponibilité, trois identités séparées, refus de lecture croisée, 401, 409, 422, expiration et rejet du démarrage avec des secrets invalides. **Elle n'a pas encore été exécutée sur la VM** et nécessite l'installation préalable des dépendances dans un environnement autorisé.

## Déploiement de labo — À lancer seulement après revue Gate 1 et fusion

Le Compose et le Dockerfile sont déjà versionnés. Il n'est **pas** nécessaire de créer manuellement un `.env` sur la VM ; générer les secrets **uniquement en mémoire dans une session de laboratoire autorisée**, après s'être assuré que les droits Git de l'utilisateur standard sont corrects.

```bash
# Depuis la racine du dépôt OSEF en tant qu'utilisateur non root.
# Inspecter le statut, puis synchroniser uniquement la PR déjà fusionnée.
git status -sb
git pull --ff-only origin main

# Trois clés indépendantes pour les seuls simulateurs fictifs.
# Ne pas les afficher ni les copier dans une issue ou un journal.
export FRAUD003_BANK_A_KEY="$(openssl rand -hex 32)"
export FRAUD003_PSP_B_KEY="$(openssl rand -hex 32)"
export FRAUD003_MOBILE_C_KEY="$(openssl rand -hex 32)"

# Lire les configurations résultantes sans imprimer les valeurs des secrets.
# Attention : ne pas utiliser docker compose config ni docker inspect
# dans des journaux publiés si les secrets risquent d'être inclus.
cd labs/FRAUD-003

# Construire et démarrer uniquement le nouveau service OSEF FRAUD-003.
docker compose up --build -d

# Santé du service. Ne modifie aucune donnée.
curl -fsS http://127.0.0.1:8113/health
```

Ne pas ajouter de nouveaux secrets dans Git. Les clés générées en session seront **perdues à la fermeture du terminal** ; prévoir un stockage de secrets approuvé avant un usage persistant et éviter de recréer des conteneurs sans les clés correctes.

### Arrêt sans perte du volume

```bash
# Depuis labs/FRAUD-003, ne touche pas aux autres projets Docker.
docker compose down
# Ne PAS ajouter --volumes : cela supprimerait les données de ce laboratoire.
```

## Console web pédagogique — ajout proposé, recette non exécutée

Le dashboard est servi par la même application sur `GET /`, son script local sur `GET /ui.js`. Il n'utilise aucun CDN, ne contient pas de secret préchargé, n'enregistre aucune clé en cookie/localStorage et affiche seulement les données obtenues par l'API authentifiée. Les routes `/signals` restent protégées. Les résultats de tests ne persistent pas après fermeture/rechargement de la page.

**Parcours manuel de recette web :**
1. Ouvrir `http://127.0.0.1:8113/` depuis la VM (ou via tunnel SSH) après démarrage du service.
2. Sélectionner une institution fictive et saisir **sa** clé de lab ; cliquer « Consulter les signaux ».
3. Cliquer « Exécuter les tests API » : disponibilité 200, clé et institution associées, création 201, lecture 200, doublon 409, champ rejeté 422, inexistant 404 et absence de clé 401 ; les résultats s'affichent PASS/FAIL dans le navigateur.
4. Changer d'institution : la page efface la clé et les résultats, il faut saisir la clé propre à cette institution.
5. Ne publier aucune capture contenant une clé ou une donnée sensible.

**Attention :** ce parcours **écrit un signal synthétique** dans SQLite ; la page ne possède pas d'historique serveur des PASS/FAIL et ne remplace pas les tests d'isolation entre trois institutions. Les tests additionnels `tests/test_web_console.py` contrôlent le HTML, le JS, les en-têtes anti-cache/CSP et l'absence d'exposition de l'API sans clé. Ces tests **n'ont pas encore été exécutés sur la VM**.

## Critères de recette Gate 2

- [x] Huit tests unitaires initiaux réussis sur la VM : `Ran 8 tests in 1.961s — OK` (sortie de l'opérateur).
- [ ] Tests de la nouvelle console web exécutés sur la VM.
- [ ] Service construit avec Compose sans impact sur FRAUD-001/002.
- [ ] Les trois clés sont distinctes et aucune valeur n'est publiée.
- [ ] Chaque institution peut créer/lire son signal fictif.
- [ ] L'accès à la liste et à l'identifiant d'une autre institution est refusé, sans fuite.
- [ ] 401 sur clé invalide/absente ; 422 sur JSON non conforme ; 409 sur doublon local.
- [ ] Un signal expiré disparaît de l'API à la lecture.
- [ ] Tests unitaires réussis, résultats et logs **réellement observés**, expurgés et consignés.
- [ ] Ressources observées durant le fonctionnement et non-régression des labs précédents.
- [ ] Revue du code, des clés, du contrôle d'accès et de la politique de partage avant Gate 3.

**Gate 2 ne peut être déclaré validé sans exécution des tests et preuves sur l'environnement cible.**
