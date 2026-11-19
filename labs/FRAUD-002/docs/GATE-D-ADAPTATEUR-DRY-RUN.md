# FRAUD-002 — Gate D : premier adaptateur OSEF (dry-run hors ligne)

**Statut : prototype en PR, non déployé sur `osef-fraud-01` ; aucune émission de signal.**

Le script `scripts/tazama-adapter-dry-run.py` implémente la **première décision sûre** du contrat Gate D : inspecter un rapport JSON Tazama déjà sauvegardé et renvoyer une décision **sans aucune requête réseau** ni donnée transactionnelle affichée. Cette étape est volontairement limitée : elle n'est **pas encore** l'adaptateur Tazama → PSP A.

## Prérequis

- Python 3 disponible dans le laboratoire ; bibliothèque standard uniquement.
- Rapport **entièrement synthétique et expurgé**, jamais une capture brute contenant des comptes, MSISDN, identifiants clients ou secrets.
- Ne pas enregistrer de rapport réel dans Git.

## Utilisation après revue/fusion PR et `git pull --ff-only`

Depuis la racine du dépôt :

```bash
# Tests unitaires autonomes : aucun conteneur ni serveur requis.
python3 -m unittest discover -s labs/FRAUD-002/tests -p 'test_*.py' -v

# Tester un rapport anonymisé existant localement (chemin à remplacer par celui du fichier autorisé).
python3 labs/FRAUD-002/scripts/tazama-adapter-dry-run.py --report /chemin/vers/rapport-synthetique-expurge.json

# Simuler la réponse Tazama '204 No Content' sans fichier.
python3 labs/FRAUD-002/scripts/tazama-adapter-dry-run.py --http-status 204
```

Sortie attendue sur notre cas de rapport synthétique `NALT` :

```json
{"decision": "NO_PUBLISH", "reason": "NALT"}
```

Réponse HTTP 204 :

```json
{"decision": "NO_PUBLISH", "reason": "REPORT_NOT_READY"}
```

**Comportement fail-closed :** status Tazama inconnu, erreur HTTP, JSON illisible, structure inattendue, score élevé sans politique approuvée → **aucun partage**. Le script ne lit aucun secret, n'envoie aucun HTTP et ne traite pas de compte réel. Exit code `2` pour entrée indéterminée/erreur (afin de ne pas confondre avec un succès nominal).

### Limites et tâches suivantes

1. **D01/D03 partiels** : tests locaux du filtrage NALT, des réponses 204/401 et des rapports invalides ; les tests ne sont pas encore exécutés dans la VM.
2. **D02 à réaliser** : récupération bornée d'un rapport via l'API Tazama, authentification de la source, attente contrôlée 204→200 ; *pas encore de réseau dans ce prototype*.
3. **D04/D05 à réaliser** : provoquer et documenter une vraie alerte positive Tazama pour définir une politique explicite et versionnée de catégorie/sévérité ; aucune déduction à partir d'un simple score.
4. **D06/E01–E05 à réaliser** : jeton opaque stable et non ré-identifiant, idempotence, API PSP A, isolation PSP B, cas de sécurité/TTL, reprise et revue d'un second ingénieur.
5. Aucune utilisation en production dans une IMF.

Références : [Contrat Gate D](GATE-D-CONTRAT-TAZAMA-FRAUD-001.md) et [Intérêt IMF / production](INTERET-TAZAMA-IMF-AFRIQUE-FRANCOPHONE.md).
