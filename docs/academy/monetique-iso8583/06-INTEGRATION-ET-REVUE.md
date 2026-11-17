# OSEF-MON-06 — Contrat de simulation, démonstration et contribution amont

**Statut : fiche pédagogique proposée — à tester avec des contributeurs**  
**Niveau cible :** P3 Integrator / P4 Reviewer  
**Parcours :** [Ingénieur monétique & ISO 8583](README.md)  
**Architecture :** [ARC-02](../../architecture/blueprints/ARC-02.md)  
**Démonstrateur :** [OPB-D03-001](../../../labs/03-card-payments/OPB-D03-001/START-HERE.md)

> **Lab uniquement.** Aucun matériel confidentiel OPPL, aucune donnée de carte ou bancaire réelle, aucun réseau financier ni certification de production.

## Prérequis
Fiches 01–05, tests unitaires et revue de code.

## Compétences observables
- Spécifier les interfaces d'un hôte fictif, sans connexion aux réseaux de paiement.
- Préparer une démonstration reproductible, un rapport d'évaluation et une revue indépendante.
- Identifier une amélioration amont pertinente et respecter la politique de contribution du projet concerné.

## Exercices à réaliser
1. Réaliser le blueprint ARC-02, puis proposer un schéma de contrat pour le composant fictif.
2. Assembler un dossier de démonstration : prérequis, commandes, tests, erreurs, décisions et limites.
3. Ouvrir une PR OSEF documentée ; l'éventuelle contribution upstream reste optionnelle et sans garantie d'acceptation.

## Preuves attendues
README de démo, diagramme, scripts commentés, résultats de tests, lien PR et revue.

La preuve doit préciser : auteur/pseudo GitHub, date, version de l'environnement, action réellement effectuée, résultat observé, problèmes non résolus et lien vers l'issue ou la PR. Ne pas inventer une sortie de test.

## Critères d'acceptation proposés
- [ ] Démonstration purement locale, réexécutable par un tiers.
- [ ] Issues et PR ont des statuts exacts.
- [ ] Aucune prétention de certification, d'homologation ou de prêt-production.
- [ ] Un autre contributeur a examiné le livrable, ou l'absence de revue est signalée.
- [ ] Les risques, licences et limites sont identifiés.
- [ ] Le contenu ne divulgue ni données financières ni secrets.

## Ressources amont à examiner
- https://github.com/moov-io/iso8583/blob/master/CONTRIBUTING.md
- https://docs.github.com/en/pull-requests

Les sources sont des **points de départ à consulter** : leur présence ne démontre ni version compatible, ni conformité de l'implémentation OSEF.

## Pour l'évaluateur
Utiliser la [grille d'évaluation commune](EVALUATION.md) : attribuer les points uniquement pour des preuves consultables et reproductibles. Si un contrôle n'a pas été exécuté, noter **non vérifié**, pas **réussi**.

**English summary:** Proposed, non-accredited ISO 8583 educational unit: Contrat de simulation, démonstration et contribution amont. Synthetic data only. Provide evidence of actual execution and independent review.
