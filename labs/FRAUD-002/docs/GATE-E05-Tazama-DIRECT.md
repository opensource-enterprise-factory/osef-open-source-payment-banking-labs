# FRAUD-002 — Gate E05 : lecture directe du rapport ALRT en mémoire

**Statut : PR en revue, tests de la liaison directe sur VM non encore exécutés.** La lecture du rapport réel en mode *lecture seule* a déjà confirmé séparément les chemins d'identité ; elle n'a pas encore servi d'entrée à un POST.

## Observations réelles du 19 novembre 2026

Pour le message synthétique `pacs.002` `a8a4d16c08dc481ba85092c9abf895a4`, vérification en direct de l'API Admin locale : `report.status=ALRT`, `data.transactionID` présent et égal au msgid demandé, `data.transaction.FIToFIPmtSts.GrpHdr.MsgId` également égal au msgid. Les champs racine de `data` sont : `dataCache`, `networkMap`, `report`, `transaction`, `transactionID`. La sortie de diagnostic n'exposait aucune donnée de client.

Un contrôle antérieur de ce même rapport a montré un score **600**, seuil d'alerte **300**, seuil d'interdiction **500**, règle 901 `.03` / 400, règle 902 `.02` / 200, EFRuP `none` / 0. Le score ne signifie pas qu'un paiement a été bloqué ni qu'une fraude réelle a été prouvée.

## Pourquoi un script supplémentaire

Le script D06-2 `tazama-controlled-submit.py` charge un **fichier local** : la recette D06-2 a réussi avec un **fixture fabriqué**, ce qui prouve PSP A → relais → PSP B mais pas la provenance Tazama de l'événement.

Le script `tazama-direct-lab-submit.py` réutilise directement :
- `tazama-read-only-dry-run._fetch_once` : **GET seulement** vers `http://127.0.0.1:5100/v1/admin/reports/getreportbymsgid`, sans proxy ni redirection et avec taille/timeout bornés.
- `tazama-controlled-submit.execute` : validation D05/D06, politique `OSEF-D06-LAB-20261119`, HMAC dédié, concordance des deux IDs, `POST` PSP A opt-in puis lecture PSP B.

Le JSON du rapport reste en RAM et n'est **jamais** écrit sur disque ni affiché. Les réponses stdout sont limitées à `decision` et `reason`. Sans `--send-synthetic-lab`, aucun envoi. Sans politique exacte, sans clé HMAC, sans identité cohérente, sur statut `NALT` ou erreur API : **NO_SEND**.

## Mise à jour et tests après revue/fusion

```bash
cd /home/lionel/osef-open-source-payment-banking-labs
git status -sb
git checkout main
git pull --ff-only origin main
python3 -m unittest discover -s labs/FRAUD-002/tests -p 'test_*.py' -v
```

**72 tests attendus** (59 déjà exécutés sur VM, 13 nouveaux). Ces tests injectent des réponses et ne réalisent pas de POST HTTP.

## Premier test réel : lecture directe et prévisualisation seulement

Dans la session terminal qui possède toujours `OSEF_FRAUD002_LAB_TOKEN_KEY` :

```bash
python3 labs/FRAUD-002/scripts/tazama-direct-lab-submit.py \
  --msgid a8a4d16c08dc481ba85092c9abf895a4 \
  --policy labs/FRAUD-002/fixtures/d06-lab-policy.json
```

Résultat attendu si tous les champs du rapport réel correspondent aux validations strictes :
`{"decision":"PREVIEW_ONLY","reason":"SEND_NOT_ENABLED"}`.

**Si `NO_SEND` : ne jamais contourner le contrôle de cohérence ni falsifier le rapport.** Inspecter la cause, puis corriger via PR GitHub si besoin. Cette étape ne requiert pas `LAB_USER_KEY`, uniquement la clé HMAC du laboratoire.

## Test direct avec émission — seulement après validation de la prévisualisation et revue humaine

```bash
python3 labs/FRAUD-002/scripts/tazama-direct-lab-submit.py \
  --msgid a8a4d16c08dc481ba85092c9abf895a4 \
  --policy labs/FRAUD-002/fixtures/d06-lab-policy.json \
  --send-synthetic-lab
```

Conditions : aucun secret affiché, clé HMAC stable (ne pas régénérer), `LAB_USER_KEY` valide déjà chargée, service PSP A/B/relai healthy, revue d'ingénieur, **un seul envoi**. Sortie possible `SENT_AND_RECEIVED / PSP_B_CONFIRMED`, `DUPLICATE / PSP_A_409`, ou un état d'échec explicite ; ne pas réessayer une émission incertaine sans lire l'inbox et l'audit. Le HMAC du msgid Tazama réel est distinct du jeton D06-2 généré à partir du fixture.

**Limites :** cette intégration valide un laboratoire synthétique sur une VM, pas la sécurité de Tazama en production. Le statut `ALRT` reste un signal de risque, pas une fraude avérée. Les contrôles Gate E TTL post-échéance, regressions, revue indépendante et traçabilité finale restent nécessaires.

## Tests de sécurité requis

- [ ] 72/72 tests unitaires exécutés sur VM.
- [ ] GET réel avec prévisualisation `PREVIEW_ONLY` ou diagnostic des contrôles de cohérence.
- [ ] Revue indépendante du code et de la politique.
- [ ] Émission directe opt-in, réception par PSP B et audit (si prérequis validés).
- [ ] Absence du signal TTL D06 après `2026-11-19T16:39:32.356955+00:00`.
- [ ] Rerun FRAUD-001 T01–T10 et Newman Tazama E2E, preuves expurgées.
