# OSEF-MON-04 — Rejets, erreurs de format, doublons et états incertains

**Statut : fiche pédagogique proposée — à tester avec des contributeurs**  
**Niveau cible :** P2 Builder / P3 Integrator  
**Parcours :** [Ingénieur monétique & ISO 8583](README.md)  
**Architecture :** [ARC-02](../../architecture/blueprints/ARC-02.md)  
**Démonstrateur :** [OPB-D03-001](../../../labs/03-card-payments/OPB-D03-001/START-HERE.md)

> **Lab uniquement.** Aucun matériel confidentiel OPPL, aucune donnée de carte ou bancaire réelle, aucun réseau financier ni certification de production.

## Prérequis
Fiches 01–03 et compréhension des assertions de test.

## Compétences observables
- Distinguer une trame mal formée d'un refus de traitement métier fictif.
- Concevoir des scénarios d'erreurs, timeout et doublon sans inventer de sémantique normative.
- Éviter de déduire la réussite ou l'échec d'une opération sur simple absence de réponse.

## Exercices à réaliser
1. Étendre les tests de messages tronqués et champs incompatibles avec une spécification choisie.
2. Décrire une machine à états du service fictif, et une règle de résolution d'un statut indéterminé.
3. Proposer un test d'idempotence pour un faux hôte local (travail de conception si composant non disponible).

## Preuves attendues
Matrice de tests (entrée, attendu, observé, statut), diagramme de machine à états.

La preuve doit préciser : auteur/pseudo GitHub, date, version de l'environnement, action réellement effectuée, résultat observé, problèmes non résolus et lien vers l'issue ou la PR. Ne pas inventer une sortie de test.

## Critères d'acceptation proposés
- [ ] Les retours d'erreur sont vérifiés et ne font pas planter le lab sans explication.
- [ ] Un timeout reste un état incertain jusqu'à résolution.
- [ ] Les scénarios de reversal ne sont pas présentés comme des opérations financières exécutées.
- [ ] Un autre contributeur a examiné le livrable, ou l'absence de revue est signalée.
- [ ] Les risques, licences et limites sont identifiés.
- [ ] Le contenu ne divulgue ni données financières ni secrets.

## Ressources amont à examiner
- https://github.com/moov-io/iso8583

Les sources sont des **points de départ à consulter** : leur présence ne démontre ni version compatible, ni conformité de l'implémentation OSEF.

## Pour l'évaluateur
Utiliser la [grille d'évaluation commune](EVALUATION.md) : attribuer les points uniquement pour des preuves consultables et reproductibles. Si un contrôle n'a pas été exécuté, noter **non vérifié**, pas **réussi**.

**English summary:** Proposed, non-accredited ISO 8583 educational unit: Rejets, erreurs de format, doublons et états incertains. Synthetic data only. Provide evidence of actual execution and independent review.
