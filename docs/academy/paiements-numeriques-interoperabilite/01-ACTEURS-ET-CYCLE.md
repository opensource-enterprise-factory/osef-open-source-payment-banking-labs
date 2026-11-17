# PNI-01 — Acteurs et cycle de vie d'un paiement numérique

**OSEF Academy · Proposition pédagogique originale v0.1 (17 novembre 2026)**  
**Niveau visé :** P1 Explorer · **Architectures :** ARC-03 · **Issues/labs de départ :** OPB-001, OPB-005.

> Formation communautaire non certifiante. Activités uniquement sur machines isolées et acteurs/données fictifs ; aucun accès à un système bancaire, PSP, switch, wallet, HSM ou rail réel. La présente fiche n'est pas un support OPPL et ne reprend pas ses méthodes confidentielles.

## Objectifs et acquis observables
- Distinguer client, PSP, institution teneuse de compte, hub et rail simulé.
- dessiner un cycle de paiement et ses états.

## Prérequis
- Lire [le parcours](README.md), [SECURITY.md](../../../SECURITY.md) et [CONTRIBUTING.md](../../../CONTRIBUTING.md).
- Git et bases de programmation ou de modélisation ; pour le code, un outil/langage choisi par le contributeur, avec version fixée.
- Délimiter un laboratoire totalement fictif avant toute exécution.

## Travail à réaliser
1. Cartographier deux institutions fictives.
2. produire un diagramme de séquence succès/refus.
3. décrire ce qu'un timeout ne permet pas de conclure.

## Livrables et preuve
Diagramme Mermaid, glossaire et machine à états avec hypothèses.

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
1. Identifier les participants et responsabilités.
2. Tracer succès/refus/état inconnu.
3. Distinguer transfert simulé et règlement réel.

### Chapitres et notions
1. **Chapitre 1 — Écosystème PSP/banques/EME.** Définir la notion, illustrer avec une situation fictive et examiner son impact sur les interfaces et données.
2. **Chapitre 2 — Participants et frontières.** Définir la notion, illustrer avec une situation fictive et examiner son impact sur les interfaces et données.
3. **Chapitre 3 — États et événements d'un paiement.** Définir la notion, illustrer avec une situation fictive et examiner son impact sur les interfaces et données.
4. **Chapitre 4 — Interopérabilité métier fictive.** Définir la notion, illustrer avec une situation fictive et examiner son impact sur les interfaces et données.

### Parcours d'une séance
1. Identifier le cas d'usage et la vue **Business** de l'architecture concernée.
2. Étudier objets, états et règles via la vue **Data**.
3. Établir contrats, responsabilités et cas d'erreur dans la vue **Application**.
4. Définir prérequis, isolation, versions et contrôles de la vue **Technology**.
5. Réaliser le TP proposé et commenter les résultats réels ou les blocages.
6. Réviser le schéma BDAT après la démonstration et publier les écarts.

### TP guidé
1. Dessiner un parcours A-vers-B à partir d'ARC-03-B.
2. Établir une table d'états fictifs.
3. Analyser une réponse absente sans conclure à un rejet.

**Préparation du TP :** lire [le catalogue des labs](../../../labs/README.md), choisir un exercice réalisable et consigner versions, licences et état réel des composants. **Un lab encore au stade d'issue n'est pas considéré exécutable.**

### Épreuve d'évaluation proposée
- **Concepts :** justifier les notions et les frontières de responsabilité du scénario.
- **Conception :** fournir schéma B/D/A/T, contrats d'interface et jeux de données inventées.
- **Pratique :** un succès et une erreur/reprise pertinente, avec résultat réellement observé ; sinon signaler « non exécuté ».
- **Revue :** rattacher les preuves à une exigence de l'architecture et à une issue/PR ; citer les limites.

**Critères spécifiques :**
- [ ] Acteurs clairement définis.
- [ ] Machine à états cohérente.
- [ ] Exclusions financières explicites.
- [ ] Le rapport distingue hypothèses, actions exécutées et éléments non vérifiés.
- [ ] Aucun système financier, client réel, secret ou rail de production n'est sollicité.

[Correspondance compétence ↔ cours](../CORRESPONDANCE-COMPETENCES-COURS.md) · [Atlas des vues BDAT](../../architecture/blueprints/BDAT-4-VUES-README.md) · [Modèle de preuve](../MODELE-PREUVE-COMPETENCE.md)

---

## Ressources OSEF
- [Atlas des architectures BDAT](../../architecture/blueprints/BDAT-README.md)
- [Catalogue des labs](../../../labs/README.md)
- [Évaluation du parcours](EVALUATION.md)
- [Politique sécurité](../../../SECURITY.md)

**English summary:** Proposed open-source digital payments and interoperability learning unit, Acteurs et cycle de vie d'un paiement numérique. Synthetic transactions only; evidence-based review required.
