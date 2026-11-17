# OSEF-MON-02 — MTI, bitmap, champs et spécification de message

**Statut : fiche pédagogique proposée — à tester avec des contributeurs**  
**Niveau cible :** P1 Explorer  
**Parcours :** [Ingénieur monétique & ISO 8583](README.md)  
**Architecture :** [ARC-02](../../architecture/blueprints/ARC-02.md)  
**Démonstrateur :** [OPB-D03-001](../../../labs/03-card-payments/OPB-D03-001/START-HERE.md)

> **Lab uniquement.** Aucun matériel confidentiel OPPL, aucune donnée de carte ou bancaire réelle, aucun réseau financier ni certification de production.

## Prérequis
Fiche 01 ; notions de représentation binaire et de chaînes de caractères.

## Compétences observables
- Expliquer la fonction du MTI, du bitmap et des définitions de champs.
- Reconnaître que le format exact dépend d'une spécification/version/profil donné.
- Construire une table de champs non sensibles et leurs contraintes de longueur/encodage.

## Exercices à réaliser
1. Étudier le code public OPB-D03-001 et l'usage de Spec87ASCII.
2. Représenter la liste des champs fictifs 3, 4 et 11 et leur lien avec le bitmap.
3. Construire une fiche de contrat : MTI, version choisie, champs, encodage, limites.

## Preuves attendues
Table de spécification pédagogique annotée et schéma expliquant le bitmap.

La preuve doit préciser : auteur/pseudo GitHub, date, version de l'environnement, action réellement effectuée, résultat observé, problèmes non résolus et lien vers l'issue ou la PR. Ne pas inventer une sortie de test.

## Critères d'acceptation proposés
- [ ] Aucune donnée de carte ni champ sensible dans les jeux de données.
- [ ] Chaque hypothèse de format est explicitée.
- [ ] Les champs du prototype ne sont pas présentés comme universels.
- [ ] Un autre contributeur a examiné le livrable, ou l'absence de revue est signalée.
- [ ] Les risques, licences et limites sont identifiés.
- [ ] Le contenu ne divulgue ni données financières ni secrets.

## Ressources amont à examiner
- https://github.com/moov-io/iso8583
- https://github.com/moov-io/iso8583/tree/master/specs

Les sources sont des **points de départ à consulter** : leur présence ne démontre ni version compatible, ni conformité de l'implémentation OSEF.

## Pour l'évaluateur
Utiliser la [grille d'évaluation commune](EVALUATION.md) : attribuer les points uniquement pour des preuves consultables et reproductibles. Si un contrôle n'a pas été exécuté, noter **non vérifié**, pas **réussi**.

**English summary:** Proposed, non-accredited ISO 8583 educational unit: MTI, bitmap, champs et spécification de message. Synthetic data only. Provide evidence of actual execution and independent review.
