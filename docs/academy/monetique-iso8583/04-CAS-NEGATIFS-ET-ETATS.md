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

## Séquence de cours détaillée — proposition pédagogique v0.2

**Périmètre :** approfondissement théorique et travaux dirigés sur messages et hôtes de **laboratoire fictifs**. Les supports de cours magistraux, les heures et les résultats des tests ne sont pas présumés validés.

### Objectifs d'apprentissage évaluables
1. Produire un cas d'erreur de décodage.
2. Concevoir une machine à états sûre.
3. Documenter un rejeu sans double effet.

### Chapitres à enseigner
1. **Chapitre 1 — Trame tronquée et champs incompatibles.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.
2. **Chapitre 2 — Refus simulé versus erreur de format.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.
3. **Chapitre 3 — Doublon et idempotence.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.
4. **Chapitre 4 — Timeout, état inconnu et correction.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.

### Séance-type proposée
1. Mise en situation métier à partir de **ARC-02-B**.
2. Analyse des messages et données via **ARC-02-D**.
3. Étude des responsabilités logicielles **ARC-02-A** et des contraintes **ARC-02-T**.
4. Travail dirigé documenté ci-dessous.
5. Correction collective : expliquer une anomalie, documenter l'attendu et le réellement observé.

### TP guidé
1. Exécuter des tests de trame tronquée lorsque possible.
2. Décrire les états et transitions autorisées.
3. Proposer un test de répétition sur un hôte mocké.

**Point de départ :** [OPB-D03-001](../../../labs/03-card-payments/OPB-D03-001/README.md). Le code de référence **n'a pas de résultat de compilation et de tests confirmé** : le formateur doit commencer par le vérifier et ne pas attribuer une réussite a priori.

### Évaluation proposée
- **Questions de compréhension :** expliquer au moins un acteur, un champ/protocole ou un scénario d'échec pertinent.
- **Étude d'architecture :** relier une exigence de la vue B, D, A ou T à la fonctionnalité étudiée.
- **Épreuve pratique :** soumettre un jeu de données inventé, un scénario nominal et un scénario négatif, ou signaler exactement ce qui n'a pas été exécuté.
- **Preuve :** code/diagramme, environnement, versions, commandes commentées, sorties expurgées et éventuelle revue.

**Critères ciblés :**
- [ ] Différences d'erreurs justifiées.
- [ ] UNKNOWN distinct du refus.
- [ ] Résultats observés ou non exécutés identifiés.
- [ ] Les supports originaux OSEF restent séparés de toute documentation OPPL confidentielle.
- [ ] La validation est réservée à une revue fondée sur les preuves.

[Correspondance compétence ↔ cours](../CORRESPONDANCE-COMPETENCES-COURS.md) · [Atlas des 40 vues BDAT](../../architecture/blueprints/BDAT-4-VUES-README.md) · [Modèle de preuve](../MODELE-PREUVE-COMPETENCE.md)

---

## Pour l'évaluateur
Utiliser la [grille d'évaluation commune](EVALUATION.md) : attribuer les points uniquement pour des preuves consultables et reproductibles. Si un contrôle n'a pas été exécuté, noter **non vérifié**, pas **réussi**.

**English summary:** Proposed, non-accredited ISO 8583 educational unit: Rejets, erreurs de format, doublons et états incertains. Synthetic data only. Provide evidence of actual execution and independent review.
