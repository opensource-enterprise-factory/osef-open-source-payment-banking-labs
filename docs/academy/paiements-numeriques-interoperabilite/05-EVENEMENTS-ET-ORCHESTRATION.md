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

## Ressources OSEF
- [Atlas des architectures BDAT](../../architecture/blueprints/BDAT-README.md)
- [Catalogue des labs](../../../labs/README.md)
- [Évaluation du parcours](EVALUATION.md)
- [Politique sécurité](../../../SECURITY.md)

**English summary:** Proposed open-source digital payments and interoperability learning unit, Orchestration et événements de paiement. Synthetic transactions only; evidence-based review required.
