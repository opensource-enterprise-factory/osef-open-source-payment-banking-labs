# FRAUD-002 — Gate E04 : gérer la lecture Tazama HTTP 204 sans modifier l'upstream

## Constat sur la VM (19 novembre 2026)

La collection officielle Newman 2.1 a réussi la création du message, l'envoi des messages synthétiques `pacs.008` et `pacs.002`, puis le GET du rapport Admin a retourné HTTP **204**. Le test officiel tentait directement `pm.response.json()` : erreur `JSONError`, bilan 4 requêtes, 13 assertions, 1 erreur de script.

La relecture manuelle **du même msgid** a donné HTTP **200**, rapport présent, statut **NALT**, identifiants concordants. Le lecteur OSEF D02 a classé `NO_PUBLISH / NALT`. Cela prouve une disponibilité ultérieure, pas la cause précise du délai.

## Correction proposée dans le lanceur OSEF

La collection officielle `tazama-lf/postman` et son environnement restent strictement intacts. Le script `scripts/test-tazama-e2e.sh` lance **deux dossiers existants** de la même collection :

1. `Message Creation sans pain.001/013` : génération et POST des transactions **une seule fois**. Newman exporte les globals synthétiques dans un répertoire temporaire à droits restreints.
2. `scripts/wait-tazama-newman-report.py` récupère **uniquement le msgid pacs.002** depuis ces globals, puis effectue des GET vers **127.0.0.1:5100** à intervalles bornés (30 essais, 2 secondes). Seul HTTP 204 est réessayé. HTTP 200 doit inclure le rapport et la concordance des deux identifiants. Tout autre HTTP, erreur d'identité ou payload malformé arrête le flux sans nouvelle transaction.
3. `DB update tests` : Newman recharge **les mêmes globals** et exécute toutes les assertions upstream sur ce rapport prêt.

Le répertoire temporaire est supprimé à la fin même en cas d'erreur. Aucun rapport brut ni secret d'API n'est écrit ; seuls les globals de la transaction **synthétique** sont temporairement exportés. Aucun `pacs.008`/`pacs.002` n'est réémis pendant l'attente. L'option `--user UID:GID` limite les droits du conteneur Newman pour la création du fichier temporaire.

**Important :** la découpe en dossiers fait apparaître deux résumés Newman distincts. Les assertions du premier et du second dossier doivent **toutes** réussir ; ne pas exiger que chaque résumé individuel indique 39 assertions. Le total cumulé à viser est **39**, si les attentes de la version de collection sont identiques au test antérieur.

## Tests à lancer après revue et fusion (aucune modification manuelle sur la VM)

```bash
cd /home/lionel/osef-open-source-payment-banking-labs
git checkout main
git pull --ff-only origin main
python3 -m unittest discover -s labs/FRAUD-002/tests -p 'test_*.py' -v
bash labs/FRAUD-002/scripts/test-tazama-e2e.sh
```

Attendus : 83 tests Python (72 anciens + 11 nouveaux), première phase Newman acceptée, `[OK] Tazama Admin report READY; identity verified`, seconde phase Newman avec aucune assertion ou script échoué, puis `[OK] Deux phases Newman terminées`.

**Échecs à investiguer sans contournement :**
- `REPORT_NOT_READY_AFTER_BOUNDED_POLL` : pas de rapport dans la fenêtre bornée, inspecter la santé et les logs des services.
- `REPORT_IDENTITY_OR_CONTENT_MISMATCH` : données inattendues, ne pas exécuter la phase 2.
- Erreur Newman sur dossier/globals/permissions : corriger la procédure dans GitHub via PR, ne pas éditer sur la VM.

Le statut `NALT` est valide pour cette collection et **ne justifie jamais l'émission d'un signal inter-PSP**. Ce scénario reste une recette synthétique, pas un exercice de paiement bancaire réel.

## Références

- [Documentation officielle Newman — options CLI](https://learning.postman.com/docs/collections/using-newman-cli/newman-options)
- [Collection Tazama upstream](https://github.com/tazama-lf/postman)
- [FRAUD-002 issue #50](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/50)
