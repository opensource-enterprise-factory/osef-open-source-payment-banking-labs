# PNI-04 — Simuler un transfert entre deux institutions

**OSEF Academy · Proposition pédagogique originale v0.1 (17 novembre 2026)**  
**Niveau visé :** P3 Integrator · **Architectures :** ARC-03 · **Issues/labs de départ :** OPB-005, OPB-006, OPB-007, OPB-008.

> Formation communautaire non certifiante. Activités uniquement sur machines isolées et acteurs/données fictifs ; aucun accès à un système bancaire, PSP, switch, wallet, HSM ou rail réel. La présente fiche n'est pas un support OPPL et ne reprend pas ses méthodes confidentielles.

## Objectifs et acquis observables
- Définir les participants, contrats, identifiants et états d'un transfert simulé sans confondre transfert, compensation et règlement.

## Prérequis
- Lire [le parcours](README.md), [SECURITY.md](../../../SECURITY.md) et [CONTRIBUTING.md](../../../CONTRIBUTING.md).
- Git et bases de programmation ou de modélisation ; pour le code, un outil/langage choisi par le contributeur, avec version fixée.
- Délimiter un laboratoire totalement fictif avant toute exécution.

## Travail à réaliser
1. Créer deux participants mockés.
2. définir requêtes/réponses et statuts.
3. tester rejet, duplication, indisponibilité et réponse tardive.

## Livrables et preuve
Diagramme de séquence, contrats versionnés, traces expurgées et tests de scénarios.

Pour chaque test : préciser **entrée synthétique, résultat attendu, commande exécutée, résultat observé, date, versions et éventuel échec**. Les composants de référence décrits par les blueprints sont des **candidats**, non des intégrations OSEF validées.

## Critères de revue
- [ ] Objectif métier, périmètre, acteurs et limites décrits.
- [ ] Contrats, schémas et hypothèses versionnés et sourcés.
- [ ] Aucune donnée personnelle ou financière réelle, aucun secret ni connexion à des tiers.
- [ ] Au moins un scénario positif et un scénario négatif pertinents ont été **effectivement testés**, ou leur absence est explicitement déclarée.
- [ ] Problèmes, décisions d'architecture, licences et risques documentés.
- [ ] Instructions et scripts commentés ; logs/artefacts expurgés.
- [ ] PR ou issue liée avec statut honnête, revue indépendante si disponible.

## Ressources OSEF
- [Atlas des architectures BDAT](../../architecture/blueprints/BDAT-README.md)
- [Catalogue des labs](../../../labs/README.md)
- [Évaluation du parcours](EVALUATION.md)
- [Politique sécurité](../../../SECURITY.md)

**English summary:** Proposed open-source digital payments and interoperability learning unit, Simuler un transfert entre deux institutions. Synthetic transactions only; evidence-based review required.
