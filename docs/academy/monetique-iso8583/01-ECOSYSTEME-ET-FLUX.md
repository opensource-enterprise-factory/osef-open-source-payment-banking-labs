# OSEF-MON-01 — Acteurs, responsabilités et cycle d'un paiement carte

**Statut : fiche pédagogique proposée — à tester avec des contributeurs**  
**Niveau cible :** P1 Explorer  
**Parcours :** [Ingénieur monétique & ISO 8583](README.md)  
**Architecture :** [ARC-02](../../architecture/blueprints/ARC-02.md)  
**Démonstrateur :** [OPB-D03-001](../../../labs/03-card-payments/OPB-D03-001/START-HERE.md)

> **Lab uniquement.** Aucun matériel confidentiel OPPL, aucune donnée de carte ou bancaire réelle, aucun réseau financier ni certification de production.

## Prérequis
Lecture du README, de SECURITY.md et du blueprint ARC-02.

## Compétences observables
- Différencier émetteur, acquéreur, commerçant et rôle d'un switch dans un scénario fictif.
- Dessiner le flux conceptuel d'une demande, d'une réponse et d'une situation indéterminée.
- Identifier les frontières entre autorisation, compensation et règlement sans les simuler.

## Exercices à réaliser
1. Tracer un diagramme de séquence avec TPE fictif, acquéreur simulé, hôte fictif.
2. Décrire cinq événements possibles : demande, acceptation, refus, délai dépassé, doublon.
3. Rédiger une matrice « qui sait quoi ? » par acteur et par étape.

## Preuves attendues
Diagramme source Mermaid, glossaire de 12 termes minimum et note de limites.

La preuve doit préciser : auteur/pseudo GitHub, date, version de l'environnement, action réellement effectuée, résultat observé, problèmes non résolus et lien vers l'issue ou la PR. Ne pas inventer une sortie de test.

## Critères d'acceptation proposés
- [ ] Les rôles des acteurs sont explicités sans réseau réel.
- [ ] Le timeout n'est pas automatiquement assimilé à un refus.
- [ ] Le document distingue les faits du standard et les hypothèses du lab.
- [ ] Un autre contributeur a examiné le livrable, ou l'absence de revue est signalée.
- [ ] Les risques, licences et limites sont identifiés.
- [ ] Le contenu ne divulgue ni données financières ni secrets.

## Ressources amont à examiner
- https://github.com/moov-io/iso8583
- https://www.iso.org/standard/79451.html

Les sources sont des **points de départ à consulter** : leur présence ne démontre ni version compatible, ni conformité de l'implémentation OSEF.

## Pour l'évaluateur
Utiliser la [grille d'évaluation commune](EVALUATION.md) : attribuer les points uniquement pour des preuves consultables et reproductibles. Si un contrôle n'a pas été exécuté, noter **non vérifié**, pas **réussi**.

**English summary:** Proposed, non-accredited ISO 8583 educational unit: Acteurs, responsabilités et cycle d'un paiement carte. Synthetic data only. Provide evidence of actual execution and independent review.
