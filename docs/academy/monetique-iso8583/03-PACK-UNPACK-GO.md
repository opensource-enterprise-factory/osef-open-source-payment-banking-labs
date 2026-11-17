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

## Séquence de cours détaillée — proposition pédagogique v0.2

**Périmètre :** approfondissement théorique et travaux dirigés sur messages et hôtes de **laboratoire fictifs**. Les supports de cours magistraux, les heures et les résultats des tests ne sont pas présumés validés.

### Objectifs d'apprentissage évaluables
1. Comprendre la nécessité de fixer une version.
2. Démontrer une correspondance après décodage.
3. Distinguer erreur de compilation et erreur protocolaire.

### Chapitres à enseigner
1. **Chapitre 1 — Modules et dépendances Go.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.
2. **Chapitre 2 — Construction d'un message fictif.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.
3. **Chapitre 3 — Pack/Unpack et comparaison.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.
4. **Chapitre 4 — Tests unitaires et reproductibilité.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.

### Séance-type proposée
1. Mise en situation métier à partir de **ARC-02-B**.
2. Analyse des messages et données via **ARC-02-D**.
3. Étude des responsabilités logicielles **ARC-02-A** et des contraintes **ARC-02-T**.
4. Travail dirigé documenté ci-dessous.
5. Correction collective : expliquer une anomalie, documenter l'attendu et le réellement observé.

### TP guidé
1. Vérifier l'API de la dépendance Moov.
2. Exécuter go test sur machine isolée.
3. Comparer MTI et champ 4 et enregistrer toute anomalie.

**Point de départ :** [OPB-D03-001](../../../labs/03-card-payments/OPB-D03-001/README.md). Le code de référence **n'a pas de résultat de compilation et de tests confirmé** : le formateur doit commencer par le vérifier et ne pas attribuer une réussite a priori.

### Évaluation proposée
- **Questions de compréhension :** expliquer au moins un acteur, un champ/protocole ou un scénario d'échec pertinent.
- **Étude d'architecture :** relier une exigence de la vue B, D, A ou T à la fonctionnalité étudiée.
- **Épreuve pratique :** soumettre un jeu de données inventé, un scénario nominal et un scénario négatif, ou signaler exactement ce qui n'a pas été exécuté.
- **Preuve :** code/diagramme, environnement, versions, commandes commentées, sorties expurgées et éventuelle revue.

**Critères ciblés :**
- [ ] go.mod et go.sum vérifiés.
- [ ] Aucune sortie de tests inventée.
- [ ] Aucun champ sensible.
- [ ] Les supports originaux OSEF restent séparés de toute documentation OPPL confidentielle.
- [ ] La validation est réservée à une revue fondée sur les preuves.

[Correspondance compétence ↔ cours](../CORRESPONDANCE-COMPETENCES-COURS.md) · [Atlas des 40 vues BDAT](../../architecture/blueprints/BDAT-4-VUES-README.md) · [Modèle de preuve](../MODELE-PREUVE-COMPETENCE.md)

---

## Pour l'évaluateur
Utiliser la [grille d'évaluation commune](EVALUATION.md) : attribuer les points uniquement pour des preuves consultables et reproductibles. Si un contrôle n'a pas été exécuté, noter **non vérifié**, pas **réussi**.

**English summary:** Proposed, non-accredited ISO 8583 educational unit: Encoder, décoder et vérifier un message fictif en Go. Synthetic data only. Provide evidence of actual execution and independent review.
