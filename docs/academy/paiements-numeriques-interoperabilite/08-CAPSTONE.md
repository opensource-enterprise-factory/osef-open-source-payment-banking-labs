# PNI-08 — Projet final : plateforme d'interopérabilité simulée

**OSEF Academy · Proposition pédagogique originale v0.1 (17 novembre 2026)**  
**Niveau visé :** P4 Reviewer / Architect · **Architectures :** ARC-03, ARC-05, ARC-06, ARC-09, ARC-10 · **Issues/labs de départ :** OPB-007, OPB-009, OPB-015, OPB-016, OPB-018, OPB-020.

> Formation communautaire non certifiante. Activités uniquement sur machines isolées et acteurs/données fictifs ; aucun accès à un système bancaire, PSP, switch, wallet, HSM ou rail réel. La présente fiche n'est pas un support OPPL et ne reprend pas ses méthodes confidentielles.

## Objectifs et acquis observables
- Concevoir et faire revoir une démonstration cohérente de paiement fictif de bout en bout, sans relation avec un réseau réel.

## Prérequis
- Lire [le parcours](README.md), [SECURITY.md](../../../SECURITY.md) et [CONTRIBUTING.md](../../../CONTRIBUTING.md).
- Git et bases de programmation ou de modélisation ; pour le code, un outil/langage choisi par le contributeur, avec version fixée.
- Délimiter un laboratoire totalement fictif avant toute exécution.

## Travail à réaliser
1. Assembler API + deux participants mockés + journal d'écritures + observabilité.
2. prouver succès, refus, timeout, doublon.
3. soutenir les décisions.

## Livrables et preuve
Code versionné, BDAT, séquences, tests observés, ADR, rapport et revue indépendante.

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
1. Articuler tous les composants de labo.
2. Démontrer succès, refus, timeout et doublon.
3. Défendre les choix lors d'une revue.

### Chapitres et notions
1. **Chapitre 1 — Architecture intégrée B/D/A/T.** Définir la notion, illustrer avec une situation fictive et examiner son impact sur les interfaces et données.
2. **Chapitre 2 — API, participants et ledger fictifs.** Définir la notion, illustrer avec une situation fictive et examiner son impact sur les interfaces et données.
3. **Chapitre 3 — Sécurité et observabilité.** Définir la notion, illustrer avec une situation fictive et examiner son impact sur les interfaces et données.
4. **Chapitre 4 — Soutenance, ADR et preuves.** Définir la notion, illustrer avec une situation fictive et examiner son impact sur les interfaces et données.

### Parcours d'une séance
1. Identifier le cas d'usage et la vue **Business** de l'architecture concernée.
2. Étudier objets, états et règles via la vue **Data**.
3. Établir contrats, responsabilités et cas d'erreur dans la vue **Application**.
4. Définir prérequis, isolation, versions et contrôles de la vue **Technology**.
5. Réaliser le TP proposé et commenter les résultats réels ou les blocages.
6. Réviser le schéma BDAT après la démonstration et publier les écarts.

### TP guidé
1. Rédiger quatre vues et contrats.
2. Assembler mocks API, participants et journal.
3. Exécuter tests et présenter écarts, incidents, limites.

**Préparation du TP :** lire [le catalogue des labs](../../../labs/README.md), choisir un exercice réalisable et consigner versions, licences et état réel des composants. **Un lab encore au stade d'issue n'est pas considéré exécutable.**

### Épreuve d'évaluation proposée
- **Concepts :** justifier les notions et les frontières de responsabilité du scénario.
- **Conception :** fournir schéma B/D/A/T, contrats d'interface et jeux de données inventées.
- **Pratique :** un succès et une erreur/reprise pertinente, avec résultat réellement observé ; sinon signaler « non exécuté ».
- **Revue :** rattacher les preuves à une exigence de l'architecture et à une issue/PR ; citer les limites.

**Critères spécifiques :**
- [ ] Architecture cohérente.
- [ ] Résultats réellement observés.
- [ ] Revue documentée.
- [ ] Le rapport distingue hypothèses, actions exécutées et éléments non vérifiés.
- [ ] Aucun système financier, client réel, secret ou rail de production n'est sollicité.

[Correspondance compétence ↔ cours](../CORRESPONDANCE-COMPETENCES-COURS.md) · [Atlas des vues BDAT](../../architecture/blueprints/BDAT-4-VUES-README.md) · [Modèle de preuve](../MODELE-PREUVE-COMPETENCE.md)

---

## Ressources OSEF
- [Atlas des architectures BDAT](../../architecture/blueprints/BDAT-README.md)
- [Catalogue des labs](../../../labs/README.md)
- [Évaluation du parcours](EVALUATION.md)
- [Politique sécurité](../../../SECURITY.md)

**English summary:** Proposed open-source digital payments and interoperability learning unit, Projet final : plateforme d'interopérabilité simulée. Synthetic transactions only; evidence-based review required.
