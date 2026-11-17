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

## Séquence de cours détaillée — proposition pédagogique v0.2

**Périmètre :** approfondissement théorique et travaux dirigés sur messages et hôtes de **laboratoire fictifs**. Les supports de cours magistraux, les heures et les résultats des tests ne sont pas présumés validés.

### Objectifs d'apprentissage évaluables
1. Décrire trois risques sans utiliser de données carte.
2. Proposer des logs expurgés.
3. Spécifier un indicateur d'erreur local.

### Chapitres à enseigner
1. **Chapitre 1 — Frontières de confiance.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.
2. **Chapitre 2 — Confidentialité et gestion des logs.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.
3. **Chapitre 3 — Métriques et traces synthétiques.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.
4. **Chapitre 4 — Limites HSM/EMV/PKI.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.

### Séance-type proposée
1. Mise en situation métier à partir de **ARC-02-B**.
2. Analyse des messages et données via **ARC-02-D**.
3. Étude des responsabilités logicielles **ARC-02-A** et des contraintes **ARC-02-T**.
4. Travail dirigé documenté ci-dessous.
5. Correction collective : expliquer une anomalie, documenter l'attendu et le réellement observé.

### TP guidé
1. Construire modèle de menace ARC-08.
2. Établir allowlist des champs loggables.
3. Définir compteur de trames rejetées et limites de mesure.

**Point de départ :** [OPB-D03-001](../../../labs/03-card-payments/OPB-D03-001/README.md). Le code de référence **n'a pas de résultat de compilation et de tests confirmé** : le formateur doit commencer par le vérifier et ne pas attribuer une réussite a priori.

### Évaluation proposée
- **Questions de compréhension :** expliquer au moins un acteur, un champ/protocole ou un scénario d'échec pertinent.
- **Étude d'architecture :** relier une exigence de la vue B, D, A ou T à la fonctionnalité étudiée.
- **Épreuve pratique :** soumettre un jeu de données inventé, un scénario nominal et un scénario négatif, ou signaler exactement ce qui n'a pas été exécuté.
- **Preuve :** code/diagramme, environnement, versions, commandes commentées, sorties expurgées et éventuelle revue.

**Critères ciblés :**
- [ ] Aucune donnée réelle.
- [ ] Logs minimisés.
- [ ] Aucune prétention de conformité.
- [ ] Les supports originaux OSEF restent séparés de toute documentation OPPL confidentielle.
- [ ] La validation est réservée à une revue fondée sur les preuves.

[Correspondance compétence ↔ cours](../CORRESPONDANCE-COMPETENCES-COURS.md) · [Atlas des 40 vues BDAT](../../architecture/blueprints/BDAT-4-VUES-README.md) · [Modèle de preuve](../MODELE-PREUVE-COMPETENCE.md)

---

## Pour l'évaluateur
Utiliser la [grille d'évaluation commune](EVALUATION.md) : attribuer les points uniquement pour des preuves consultables et reproductibles. Si un contrôle n'a pas été exécuté, noter **non vérifié**, pas **réussi**.

**English summary:** Proposed, non-accredited ISO 8583 educational unit: Sécurité des messages, journalisation et observabilité. Synthetic data only. Provide evidence of actual execution and independent review.
