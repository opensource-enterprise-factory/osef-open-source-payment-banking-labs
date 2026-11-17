# PNI-05 — Orchestration et événements de paiement

**OSEF Academy · Proposition pédagogique originale v0.1 (17 novembre 2026)**  
**Niveau visé :** P3 Integrator · **Architectures :** ARC-07, ARC-10 · **Issues/labs de départ :** OPB-009, OPB-013.

> Formation communautaire non certifiante. Activités uniquement sur machines isolées et acteurs/données fictifs ; aucun accès à un système bancaire, PSP, switch, wallet, HSM ou rail réel. La présente fiche n'est pas un support OPPL et ne reprend pas ses méthodes confidentielles.

## Objectifs et acquis observables
- Comprendre idempotence, corrélation, publication d'événement et éventuelle cohérence.
- identifier les risques de rejeu et d'ordre.

## Prérequis
- Lire [le parcours](README.md), [SECURITY.md](../../../SECURITY.md) et [CONTRIBUTING.md](../../../CONTRIBUTING.md).
- Git et bases de programmation ou de modélisation ; pour le code, un outil/langage choisi par le contributeur, avec version fixée.
- Délimiter un laboratoire totalement fictif avant toute exécution.

## Travail à réaliser
1. Définir un orchestrateur fictif.
2. documenter commandes/événements et schémas.
3. simuler redelivery, out-of-order et panne d'un worker.

## Livrables et preuve
Contrats événementiels, matrice de tests de redelivery et ADR d'orchestration.

Pour chaque test : préciser **entrée synthétique, résultat attendu, commande exécutée, résultat observé, date, versions et éventuel échec**. Les composants de référence décrits par les blueprints sont des **candidats**, non des intégrations OSEF validées.

## Critères de revue
- [ ] Objectif métier, périmètre, acteurs et limites décrits.
- [ ] Contrats, schémas et hypothèses versionnés et sourcés.
- [ ] Aucune donnée personnelle ou financière réelle, aucun secret ni connexion à des tiers.
- [ ] Au moins un scénario positif et un scénario négatif pertinents ont été **effectivement testés**, ou leur absence est explicitement déclarée.
- [ ] Problèmes, décisions d'architecture, licences et risques documentés.
- [ ] Instructions et scripts commentés ; logs/artefacts expurgés.
- [ ] PR ou issue liée avec statut honnête, revue indépendante si disponible.

## Plan de cours approfondi — proposition v0.2

**Nature :** chapitres et séquences à enseigner, pas une preuve de cours déjà dispensés. Les composants des blueprints sont candidats et la mise en œuvre reste entièrement en laboratoire fictif.

### Objectifs pédagogiques observables
1. Définir les transitions d'un orchestrateur fictif.
2. Distinguer publication et traitement d'un événement.
3. Tester redelivery et ordre inversé.

### Chapitres et notions
1. **Chapitre 1 — Commande versus événement.** Définir la notion, illustrer avec une situation fictive et examiner son impact sur les interfaces et données.
2. **Chapitre 2 — Orchestrateur et dépendances.** Définir la notion, illustrer avec une situation fictive et examiner son impact sur les interfaces et données.
3. **Chapitre 3 — Rejeu, ordre et idempotence.** Définir la notion, illustrer avec une situation fictive et examiner son impact sur les interfaces et données.
4. **Chapitre 4 — Cohérence et reprise.** Définir la notion, illustrer avec une situation fictive et examiner son impact sur les interfaces et données.

### Parcours d'une séance
1. Identifier le cas d'usage et la vue **Business** de l'architecture concernée.
2. Étudier objets, états et règles via la vue **Data**.
3. Établir contrats, responsabilités et cas d'erreur dans la vue **Application**.
4. Définir prérequis, isolation, versions et contrôles de la vue **Technology**.
5. Réaliser le TP proposé et commenter les résultats réels ou les blocages.
6. Réviser le schéma BDAT après la démonstration et publier les écarts.

### TP guidé
1. Définir deux événements versionnés.
2. Simuler deux notifications répétées.
3. Produire une ADR sur cohérence et retries.

**Préparation du TP :** lire [le catalogue des labs](../../../labs/README.md), choisir un exercice réalisable et consigner versions, licences et état réel des composants. **Un lab encore au stade d'issue n'est pas considéré exécutable.**

### Épreuve d'évaluation proposée
- **Concepts :** justifier les notions et les frontières de responsabilité du scénario.
- **Conception :** fournir schéma B/D/A/T, contrats d'interface et jeux de données inventées.
- **Pratique :** un succès et une erreur/reprise pertinente, avec résultat réellement observé ; sinon signaler « non exécuté ».
- **Revue :** rattacher les preuves à une exigence de l'architecture et à une issue/PR ; citer les limites.

**Critères spécifiques :**
- [ ] Pas de double effet.
- [ ] Ordre d'événements documenté.
- [ ] Décision justifiée.
- [ ] Le rapport distingue hypothèses, actions exécutées et éléments non vérifiés.
- [ ] Aucun système financier, client réel, secret ou rail de production n'est sollicité.

[Correspondance compétence ↔ cours](../CORRESPONDANCE-COMPETENCES-COURS.md) · [Atlas des vues BDAT](../../architecture/blueprints/BDAT-4-VUES-README.md) · [Modèle de preuve](../MODELE-PREUVE-COMPETENCE.md)

---

## Ressources OSEF
- [Atlas des architectures BDAT](../../architecture/blueprints/BDAT-README.md)
- [Catalogue des labs](../../../labs/README.md)
- [Évaluation du parcours](EVALUATION.md)
- [Politique sécurité](../../../SECURITY.md)

**English summary:** Proposed open-source digital payments and interoperability learning unit, Orchestration et événements de paiement. Synthetic transactions only; evidence-based review required.
