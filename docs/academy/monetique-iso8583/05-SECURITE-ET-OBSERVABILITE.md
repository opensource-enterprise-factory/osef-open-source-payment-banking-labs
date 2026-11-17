# OSEF-MON-05 — Sécurité des messages, journalisation et observabilité

**Statut : fiche pédagogique proposée — à tester avec des contributeurs**  
**Niveau cible :** P3 Integrator  
**Parcours :** [Ingénieur monétique & ISO 8583](README.md)  
**Architecture :** [ARC-02](../../architecture/blueprints/ARC-02.md)  
**Démonstrateur :** [OPB-D03-001](../../../labs/03-card-payments/OPB-D03-001/START-HERE.md)

> **Lab uniquement.** Aucun matériel confidentiel OPPL, aucune donnée de carte ou bancaire réelle, aucun réseau financier ni certification de production.

## Prérequis
Fiches 01–04 ; bases d'API, secrets et logs.

## Compétences observables
- Identifier les risques de divulgation dans logs/artefacts et les frontières de confiance.
- Définir les métriques de laboratoire utiles sans exporter de champs sensibles.
- Expliquer les limites d'un simulateur sans HSM, EMV et PKI de production.

## Exercices à réaliser
1. Produire un threat model simple : acteur, actif, menace, contrôle et preuve.
2. Ajouter au plan de tests la vérification que les sorties publiques n'exposent aucun payload sensible.
3. Définir taux d'erreur, latence de traitement local, nombre de trames rejetées, sans prétendre mesurer un réseau bancaire.

## Preuves attendues
Threat model, checklist sécurité, spécification des logs et des métriques.

La preuve doit préciser : auteur/pseudo GitHub, date, version de l'environnement, action réellement effectuée, résultat observé, problèmes non résolus et lien vers l'issue ou la PR. Ne pas inventer une sortie de test.

## Critères d'acceptation proposés
- [ ] Aucune donnée client, PAN/PIN/CVV ou secret réel.
- [ ] Les limites des mesures sont indiquées.
- [ ] Les règles de SECURITY.md sont explicitement respectées.
- [ ] Un autre contributeur a examiné le livrable, ou l'absence de revue est signalée.
- [ ] Les risques, licences et limites sont identifiés.
- [ ] Le contenu ne divulgue ni données financières ni secrets.

## Ressources amont à examiner
- https://owasp.org/API-Security/
- https://opentelemetry.io/docs/

Les sources sont des **points de départ à consulter** : leur présence ne démontre ni version compatible, ni conformité de l'implémentation OSEF.

## Pour l'évaluateur
Utiliser la [grille d'évaluation commune](EVALUATION.md) : attribuer les points uniquement pour des preuves consultables et reproductibles. Si un contrôle n'a pas été exécuté, noter **non vérifié**, pas **réussi**.

**English summary:** Proposed, non-accredited ISO 8583 educational unit: Sécurité des messages, journalisation et observabilité. Synthetic data only. Provide evidence of actual execution and independent review.
