# FRAUD-002 — Gate D06-2 : essai de livraison inter-PSP contrôlé

**État : PR à revoir et tests VM non encore exécutés. Rien n'a été transmis.**

## Approbation pédagogique documentée

Le 19 novembre 2026, l'opérateur du laboratoire a explicitement approuvé le mapping **uniquement pour le test synthétique** :

- Alerte Tazama qualifiée `ALRT` → catégorie `suspicious-transfer`.
- Gravité choisie **`medium`** (convention de test, **pas** une déduction du score).
- Destinataire `psp-b`, expiration `1` heure.
- Référence interne de ce protocole : `OSEF-D06-LAB-20261119`.
- Aucune donnée personnelle, aucune transaction réelle, aucun PSP externe.

La politique est fournie en [fixtures/d06-lab-policy.json](../fixtures/d06-lab-policy.json). Elle ne constitue pas une validation institutionnelle ou une permission de publier d'autres données.

## Chaîne autorisée

`Rapport ALRT synthétique validé` → `tazama-signal-preview.prepare_signal` (qualification Gate D05, identité cohérente, politique approuvée, HMAC secret) → **opt-in explicite** `POST http://127.0.0.1:8091/submit` (`X-Lab-Key`) → relais FRAUD-001 via PSP A (`POST /signals`) → **vérification** `GET http://127.0.0.1:8092/inbox` sur PSP B (`X-Lab-Key`).

L'outil `scripts/tazama-controlled-submit.py` ne peut viser d'autres URL ; il désactive les proxies et les redirections, et masque les réponses HTTP. Il ne poste **rien** par défaut. L'émission nécessite explicitement `--send-synthetic-lab`, une clé HMAC distincte en environnement `OSEF_FRAUD002_LAB_TOKEN_KEY`, et `LAB_USER_KEY` (clé FRAUD-001 existante). Les valeurs ne doivent jamais figurer dans Git, dans les captures ou dans les journaux.

Le jeton `demo-<HMAC>` reste stable pour une même ID **et la même clé** ; si cette clé est modifiée entre deux tentatives, l'idempotence n'est plus assurée. Le relais rejette le même jeton avec HTTP 409. **Ne pas répéter un envoi après résultat incertain sans vérification de réception.**

## Réserve majeure : liaison au rapport Tazama réel

Le fixture `fixtures/d06-synthetic-alert.json` est **entièrement fabriqué à partir du scénario de test validé** et sert aux tests d'interface. Il **n'est pas** une capture de l'API Admin Tazama. Les chemins `data.transactionID` et `data.transaction.FIToFIPmtSts.GrpHdr.MsgId` imposés par la version D06-1 doivent **encore être vérifiés sur le vrai rapport**. La réussite avec le fixture ne valide PAS la liaison d'un rapport réel.

**Ne pas contourner les contrôles d'identifiant**, ne pas éditer de fichiers sur la VM et ne pas copier de vrais rapports avec données sensibles dans le dépôt. Une PR de correction du binding sera nécessaire si le rapport réel a une autre structure. L'objet de D06-2 est de valider dans un premier temps la chaîne FRAUD-001 avec des données fictives.

## Validation initiale, sans émission

Après revue/fusion de la PR et sur `osef-fraud-01` :

```bash
cd /home/lionel/osef-open-source-payment-banking-labs
git status -sb
git checkout main
git pull --ff-only origin main

# Tests unitaires uniquement : HTTP toujours simulé.
python3 -m unittest discover -s labs/FRAUD-002/tests -p 'test_*.py' -v

# Vérifier les trois composants existants avant tout POST.
python3 labs/FRAUD-002/scripts/tazama-safe.py ps
curl -fsS --max-time 5 http://127.0.0.1:8091/health
curl -fsS --max-time 5 http://127.0.0.1:8092/health
```

Résultats attendus : **59** tests unitaires (47 précédents + 12 nouveaux), endpoints `psp-a` / `psp-b` en bonne santé si FRAUD-001 est en service.

### Prévisualisation sans envoi

Les variables d'environnement d'exécution doivent être disponibles dans la session **sans être affichées ni conservées dans Git**. Utiliser une clé HMAC longue, stable, propre à ce laboratoire ; ne pas la confondre avec `LAB_USER_KEY`.

```bash
python3 labs/FRAUD-002/scripts/tazama-controlled-submit.py \
  --report labs/FRAUD-002/fixtures/d06-synthetic-alert.json \
  --policy labs/FRAUD-002/fixtures/d06-lab-policy.json \
  --msgid 0123456789abcdef0123456789abcdef
```

Sortie attendue si clés valides : `{"decision":"PREVIEW_ONLY","reason":"SEND_NOT_ENABLED"}`. **Aucun POST.**

### Envoi réel — uniquement après tests et contrôle des secrets

Avec les mêmes arguments, l'option `--send-synthetic-lab` déclenche **une seule** soumission vers PSP A, puis une lecture PSP B. Cette étape ne doit pas être exécutée avant la validation des prérequis, la confirmation des ports et l'examen de la PR par un second ingénieur :

```bash
python3 labs/FRAUD-002/scripts/tazama-controlled-submit.py \
  --report labs/FRAUD-002/fixtures/d06-synthetic-alert.json \
  --policy labs/FRAUD-002/fixtures/d06-lab-policy.json \
  --msgid 0123456789abcdef0123456789abcdef \
  --send-synthetic-lab
```

Résultats : `SENT_AND_RECEIVED / PSP_B_CONFIRMED` si PSP B voit le jeton ; `DUPLICATE / PSP_A_409` si ce jeton existe déjà ; `NO_SEND` sur absence d'autorisation, panne ou rejet. `SENT / RECEIPT_UNCONFIRMED` veut dire qu'un POST a réussi mais que sa réception par PSP B **n'est pas prouvée**.

## Recette finale Gate E

- [ ] 59/59 tests unitaires après fusion.
- [ ] Prévol health, accès en loopback, proxy/redirection bloqués.
- [ ] Flux synthétique PSP A → relais → PSP B prouvé avec audit.
- [ ] Rejet 401 sans clé, 409 pour duplicata, 503/panne et récupération.
- [ ] Vérifier TTL 1 heure selon horodatage (ne pas prétendre avoir observé l'expiration avant le délai).
- [ ] Aucune donnée de client ou d'opération réelle dans signal et audit.
- [ ] Régression FRAUD-001 T01–T10 ; Tazama Newman 39/39.
- [ ] Vérifier la structure effective des rapports Tazama pour le binding source avant toute revendication « Tazama réel → PSP B ».
- [ ] Revue par un second ingénieur et clôture de l'issue #50.
