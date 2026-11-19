# FRAUD-002 — Gate D02 : lecture Tazama Admin en mode dry-run

**Statut : code en revue GitHub, non exécuté sur la VM à ce stade.** Prototype **sandbox-only** réservé à des données entièrement synthétiques. Aucun signal envoyé à FRAUD-001.

## Objectif

Lire en GET un résultat de transaction Tazama via l'API Admin Service locale, gérer une réponse **204 temporaire**, puis appliquer le classificateur **fail-closed** existant. La sortie reste une décision sans montant, compte, bénéficiaire, identifiant de transaction ou contenu du rapport.

## Sécurité par défaut

- Hôte fixé dans le code à `http://127.0.0.1:5100` ; **pas d'URL externe configurable**.
- Méthode HTTP `GET` uniquement, chemin fixé à `/v1/admin/reports/getreportbymsgid`.
- Identifiant message uniquement **32 caractères hexadécimaux** ; jamais de saisie d'URL.
- Redirections HTTP refusées et proxys d'environnement désactivés.
- Délai réseau de 5 secondes par requête, corps plafonné à 1 Mio.
- Maximum **4 tentatives**, pause d'une seconde seulement après HTTP 204.
- Aucun log du rapport, aucune donnée sensible retournée sur stdout ; la réponse JSON est évaluée en mémoire.
- **Aucune émission** à PSP A, au relais ou à PSP B, **aucune authentification de production**.
- Un statut inconnu, une erreur HTTP ou un rapport mal formé aboutit à `NO_PUBLISH`.

> **Attention** : le profil Tazama du lab est en mode sans authentification. Ne pas exposer Admin Service hors loopback, ne pas réutiliser ce lecteur dans une institution financière en production.

## Procédure de validation sur la VM (uniquement après revue et fusion PR)

Depuis `osef-fraud-01` :

```bash
cd /home/lionel/osef-open-source-payment-banking-labs
git status -sb
git checkout main
git pull --ff-only origin main

# Tester le classificateur et le lecteur HTTP avec des réponses simulées.
# Ces tests ne sollicitent pas Tazama.
python3 -m unittest discover -s labs/FRAUD-002/tests -p 'test_*.py' -v

# Cas déjà validé avec rapport HTTP 200 en API Tazama :
python3 labs/FRAUD-002/scripts/tazama-read-only-dry-run.py \
  --msgid a21c6eb6dc8c4c56b4efcaf079b315ce
```

**Résultat attendu** sur notre transaction fictive de 370 USD déjà observée :

```json
{"decision": "NO_PUBLISH", "reason": "NALT"}
```

Si le rapport est momentanément indisponible (HTTP 204), le programme essaie à nouveau trois fois au maximum ; ensuite :

```json
{"decision": "NO_PUBLISH", "reason": "REPORT_NOT_READY"}
```

Les autres réponses renvoient `NO_PUBLISH` avec une raison technique non sensible. Un code de sortie 2 est prévu pour les entrées invalides et erreurs de source. Aucun succès d'exécution sur la VM n'est affirmé avant réception des preuves.

## Tests unitaires ajoutés

`tests/test_tazama_read_only.py` couvre : NALT, 204→204→200, 204 persistant, 401, défaut réseau, statut inconnu, validation des identifiants, absence de fuite et borne sur le nombre de tentatives.

## Étapes suivantes

1. Valider D02 sur la VM avec une transaction synthétique et documenter la sortie.
2. Provoquer **une vraie alerte positive** Tazama et examiner son statut/contrat (D04/D05) ; ne pas assimiler un score élevé à une preuve d'alerte sans politique.
3. Préparer une PR distincte avec l'autorisation explicite de mapping, l'identifiant opaque non réidentifiant et les tests d'intégration contrôlés vers PSP A puis PSP B (D06/Gate E).
4. Revue par un second ingénieur, vérification des licences/versions et dossier final de clôture.

**Références :** [contrat de sécurité Gate D](GATE-D-CONTRAT-TAZAMA-FRAUD-001.md) ; [README FRAUD-002](../README.md) ; [code FRAUD-001](../../FRAUD-001/app.py).
