# OSEF-MON-03 — Encoder, décoder et vérifier un message fictif en Go

**Statut : fiche pédagogique proposée — à tester avec des contributeurs**  
**Niveau cible :** P2 Builder  
**Parcours :** [Ingénieur monétique & ISO 8583](README.md)  
**Architecture :** [ARC-02](../../architecture/blueprints/ARC-02.md)  
**Démonstrateur :** [OPB-D03-001](../../../labs/03-card-payments/OPB-D03-001/START-HERE.md)

> **Lab uniquement.** Aucun matériel confidentiel OPPL, aucune donnée de carte ou bancaire réelle, aucun réseau financier ni certification de production.

## Prérequis
Fiches 01–02, Git, Go et tests unitaires de base.

## Compétences observables
- Préparer un module Go reproductible et consigner les versions utilisées.
- Construire un aller-retour Pack/Unpack sur un jeu synthétique.
- Fournir les résultats réellement obtenus, réussites comme échecs.

## Exercices à réaliser
1. Reproduire d'abord les instructions START-HERE dans un dossier isolé ; vérifier la compatibilité avec l'API Moov actuelle.
2. En cas d'erreur de compilation, localiser le décalage API et proposer un correctif limité en PR.
3. Figer le module et les checksums, exécuter les tests, consigner la sortie expurgée.

## Preuves attendues
go.mod / go.sum après validation, code commenté, preuve de go test, trace d'exécution avec version de Go.

La preuve doit préciser : auteur/pseudo GitHub, date, version de l'environnement, action réellement effectuée, résultat observé, problèmes non résolus et lien vers l'issue ou la PR. Ne pas inventer une sortie de test.

## Critères d'acceptation proposés
- [ ] Compilation et tests observés, pas simplement présumés.
- [ ] Égalité des champs attendus documentée.
- [ ] Aucun appel à un réseau financier ni journalisation de payload réel.
- [ ] Un autre contributeur a examiné le livrable, ou l'absence de revue est signalée.
- [ ] Les risques, licences et limites sont identifiés.
- [ ] Le contenu ne divulgue ni données financières ni secrets.

## Ressources amont à examiner
- https://github.com/moov-io/iso8583
- https://go.dev/doc/modules/managing-dependencies

Les sources sont des **points de départ à consulter** : leur présence ne démontre ni version compatible, ni conformité de l'implémentation OSEF.

## Pour l'évaluateur
Utiliser la [grille d'évaluation commune](EVALUATION.md) : attribuer les points uniquement pour des preuves consultables et reproductibles. Si un contrôle n'a pas été exécuté, noter **non vérifié**, pas **réussi**.

**English summary:** Proposed, non-accredited ISO 8583 educational unit: Encoder, décoder et vérifier un message fictif en Go. Synthetic data only. Provide evidence of actual execution and independent review.
