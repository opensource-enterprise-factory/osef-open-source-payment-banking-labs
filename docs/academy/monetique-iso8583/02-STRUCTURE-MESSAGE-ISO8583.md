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

## Séquence de cours détaillée — proposition pédagogique v0.2

**Périmètre :** approfondissement théorique et travaux dirigés sur messages et hôtes de **laboratoire fictifs**. Les supports de cours magistraux, les heures et les résultats des tests ne sont pas présumés validés.

### Objectifs d'apprentissage évaluables
1. Expliquer le lien bitmap/champs.
2. Comparer les champs fictifs 3,4,11 au profil choisi.
3. Décrire les limites d'une spec donnée.

### Chapitres à enseigner
1. **Chapitre 1 — Rôle du MTI.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.
2. **Chapitre 2 — Bitmap primaire et champs actifs.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.
3. **Chapitre 3 — Profils, formats et longueurs.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.
4. **Chapitre 4 — Contraintes de données de test.** Expliquer le principe, analyser un exemple de lab et expliciter les limites techniques.

### Séance-type proposée
1. Mise en situation métier à partir de **ARC-02-B**.
2. Analyse des messages et données via **ARC-02-D**.
3. Étude des responsabilités logicielles **ARC-02-A** et des contraintes **ARC-02-T**.
4. Travail dirigé documenté ci-dessous.
5. Correction collective : expliquer une anomalie, documenter l'attendu et le réellement observé.

### TP guidé
1. Lire ARC-02-D puis la spécification du prototype.
2. Établir table de données fictives.
3. Décrire la sérialisation attendue sans données de carte.

**Point de départ :** [OPB-D03-001](../../../labs/03-card-payments/OPB-D03-001/README.md). Le code de référence **n'a pas de résultat de compilation et de tests confirmé** : le formateur doit commencer par le vérifier et ne pas attribuer une réussite a priori.

### Évaluation proposée
- **Questions de compréhension :** expliquer au moins un acteur, un champ/protocole ou un scénario d'échec pertinent.
- **Étude d'architecture :** relier une exigence de la vue B, D, A ou T à la fonctionnalité étudiée.
- **Épreuve pratique :** soumettre un jeu de données inventé, un scénario nominal et un scénario négatif, ou signaler exactement ce qui n'a pas été exécuté.
- **Preuve :** code/diagramme, environnement, versions, commandes commentées, sorties expurgées et éventuelle revue.

**Critères ciblés :**
- [ ] Champs de lab inventés.
- [ ] Longueurs et formats justifiés.
- [ ] Profil non présenté comme universel.
- [ ] Les supports originaux OSEF restent séparés de toute documentation OPPL confidentielle.
- [ ] La validation est réservée à une revue fondée sur les preuves.

[Correspondance compétence ↔ cours](../CORRESPONDANCE-COMPETENCES-COURS.md) · [Atlas des 40 vues BDAT](../../architecture/blueprints/BDAT-4-VUES-README.md) · [Modèle de preuve](../MODELE-PREUVE-COMPETENCE.md)

---

## Pour l'évaluateur
Utiliser la [grille d'évaluation commune](EVALUATION.md) : attribuer les points uniquement pour des preuves consultables et reproductibles. Si un contrôle n'a pas été exécuté, noter **non vérifié**, pas **réussi**.

**English summary:** Proposed, non-accredited ISO 8583 educational unit: MTI, bitmap, champs et spécification de message. Synthetic data only. Provide evidence of actual execution and independent review.
