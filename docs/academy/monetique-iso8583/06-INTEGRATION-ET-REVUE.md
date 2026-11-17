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

## Séquence de cours détaillée — proposition pédagogique v0.2

**Périmètre :** approfondissement théorique et travaux dirigés sur messages et hôtes de **laboratoire fictifs**. Les supports de cours magistraux, les heures et les résultats des tests ne sont pas présumés validés.

### Objectifs d'apprentissage évaluables
1. Définir interfaces d'un hôte de lab.
2. Justifier les choix techniques.
3. Produire un dossier de revue reproductible.

### Chapitres à enseigner
1. **Chapitre 1 — Contrat de démonstrateur.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.
2. **Chapitre 2 — Environnement et exécution locale.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.
3. **Chapitre 3 — ADR et limites.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.
4. **Chapitre 4 — Contribution GitHub et revue amont.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.

### Séance-type proposée
1. Mise en situation métier à partir de **ARC-02-B**.
2. Analyse des messages et données via **ARC-02-D**.
3. Étude des responsabilités logicielles **ARC-02-A** et des contraintes **ARC-02-T**.
4. Travail dirigé documenté ci-dessous.
5. Correction collective : expliquer une anomalie, documenter l'attendu et le réellement observé.

### TP guidé
1. Assembler B/D/A/T ARC-02.
2. Rédiger procédure de démo nominale et négative.
3. Préparer PR avec résultats et avertissements.

**Point de départ :** [OPB-D03-001](../../../labs/03-card-payments/OPB-D03-001/README.md). Le code de référence **n'a pas de résultat de compilation et de tests confirmé** : le formateur doit commencer par le vérifier et ne pas attribuer une réussite a priori.

### Évaluation proposée
- **Questions de compréhension :** expliquer au moins un acteur, un champ/protocole ou un scénario d'échec pertinent.
- **Étude d'architecture :** relier une exigence de la vue B, D, A ou T à la fonctionnalité étudiée.
- **Épreuve pratique :** soumettre un jeu de données inventé, un scénario nominal et un scénario négatif, ou signaler exactement ce qui n'a pas été exécuté.
- **Preuve :** code/diagramme, environnement, versions, commandes commentées, sorties expurgées et éventuelle revue.

**Critères ciblés :**
- [ ] Scripts commentés.
- [ ] Revue indépendante ou absence signalée.
- [ ] Version, licence et tests tracés.
- [ ] Les supports originaux OSEF restent séparés de toute documentation OPPL confidentielle.
- [ ] La validation est réservée à une revue fondée sur les preuves.

[Correspondance compétence ↔ cours](../CORRESPONDANCE-COMPETENCES-COURS.md) · [Atlas des 40 vues BDAT](../../architecture/blueprints/BDAT-4-VUES-README.md) · [Modèle de preuve](../MODELE-PREUVE-COMPETENCE.md)

---

## Pour l'évaluateur
Utiliser la [grille d'évaluation commune](EVALUATION.md) : attribuer les points uniquement pour des preuves consultables et reproductibles. Si un contrôle n'a pas été exécuté, noter **non vérifié**, pas **réussi**.

**English summary:** Proposed, non-accredited ISO 8583 educational unit: Contrat de simulation, démonstration et contribution amont. Synthetic data only. Provide evidence of actual execution and independent review.
