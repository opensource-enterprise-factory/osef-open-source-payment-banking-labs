# FRAUD-002 — Gate D05 : qualifier une alerte ALRT sans publication

**Statut : implémentation en PR, tests sur VM à confirmer.** Concerne uniquement le profil de démonstration Tazama Public DockerHub observé dans FRAUD-002. **Aucune émission vers PSP A, aucun signal créé et aucun usage IMF en production.**

## Preuve métier Gate D04 (19 novembre 2026)

Transaction entièrement fictive dans Tazama Demo ; logs TMS : pacs.008 et pacs.002 transmis à Event Director ; rapport Admin Service lu et filtré pour ne pas exposer les données des comptes :

| Champ | Observé |
|---|---|
| Statut | `ALRT` |
| Typologie | `999-901-902@4.0.0` |
| Score | `600` |
| Seuil d'alerte | `300` |
| Seuil d'interdiction | `500` |
| Règle 901 | Bande `.03`, poids `400` |
| Règle 902 | Bande `.02`, poids `200` |
| EFRuP | Bande `none`, poids `0` |

Ces éléments sont cohérents avec la [configuration SQL officielle épinglée](https://github.com/tazama-lf/tazama-stack/blob/83e4b12c16986aedfff843ed84b7045ac912ec0a/core/postgres/migration/config/00-public-base.sql). **Le résultat ALRT est une alerte de surveillance, pas la preuve que le paiement a été bloqué ni une fraude avérée.**

## Décision Gate D05 — uniquement un candidat à revue

Le classificateur offline de `scripts/tazama-adapter-dry-run.py`, réutilisé par le lecteur HTTP local `scripts/tazama-read-only-dry-run.py`, reconnaît maintenant une alerte positive **seulement si** :

1. La réponse est un rapport confirmé `HTTP 200` et `message = Report was found`.
2. Le champ `data.report.status` est exactement `ALRT`.
3. Il y a exactement une typologie `999-901-902@4.0.0` avec workflow et seuils 300/500, EFRuP connu.
4. Les trois règles attendues EFRuP, 901, 902 sont présentes une seule fois, avec bandes et poids explicitement validés pour cette configuration.
5. Le score est numérique, supérieur ou égal à 300, et **égal à la somme des poids** vérifiés.

Alors la sortie (et seulement la sortie) devient :

```json
{"decision": "REVIEW_ONLY", "reason": "ALRT_CANDIDATE"}
```

Cela **ne signifie pas PUBLISH**, ne crée aucun jeton, ne choisit aucune catégorie, gravité ou destinataire et n'initie aucun POST. Les statuts `NALT`, HTTP 204, 401, erreurs, typologies non reconnues et incohérences restent `NO_PUBLISH`. Aucun seuil de gravité n'est déduit du score seul.

## Vérifications après revue et fusion de la PR

Sur `osef-fraud-01`, ne rien modifier à la main et ne pas lancer d'autre configuration :

```bash
cd /home/lionel/osef-open-source-payment-banking-labs
git status -sb
git checkout main
git pull --ff-only origin main

# Tous les tests de D01/D02/D05 sont locaux et n'émettent aucune requête réseau.
python3 -m unittest discover -s labs/FRAUD-002/tests -p 'test_*.py' -v

# Lecture seule du rapport ALRT déjà observé dans la VM :
python3 labs/FRAUD-002/scripts/tazama-read-only-dry-run.py \
  --msgid a8a4d16c08dc481ba85092c9abf895a4
```

Résultat attendu du dernier appel : `REVIEW_ONLY / ALRT_CANDIDATE`, sous réserve que le rapport soit toujours disponible et conforme.

## Conditions avant Gate D06

- [ ] Valider cette PR et obtenir les résultats d'exécution sur VM (sans captures de données sensibles).
- [ ] Réviser la politique d'autorisation : qui valide le type `suspicious-transfer`, le niveau `low/medium/high`, la durée de vie et le destinataire ?
- [ ] Concevoir un jeton de laboratoire **opaque**, stable pour les reprises mais non dérivé publiquement d'un identifiant de transaction ; stockage de correspondance protégé et durée de vie limitée.
- [ ] Tests de doublons, contrôles d'accès, indisponibilité PSP A/relais et audit ; aucune diffusion tant que ces garanties ne sont pas vérifiées.
- [ ] Décider comment gérer les futurs profils Tazama, versions et typologies : fail-closed par défaut.

Sources complémentaires : [contrat Gate D](GATE-D-CONTRAT-TAZAMA-FRAUD-001.md), [preuve Gate D04](GATE-D04-SCENARIO-ALERTE-POSITIVE.md), [API FRAUD-001](../../FRAUD-001/app.py).
