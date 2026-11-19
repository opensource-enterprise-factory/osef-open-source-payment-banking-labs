# OSEF Open Source Fraud Engineering — Catalogue opérationnel

> **Programme de référence :** [Charte OSFE et roadmap](../programs/open-source-fraud-engineering/README.md) · [Benchmark](../programs/open-source-fraud-engineering/BENCHMARK-PROTOCOL.md) · [Backlog](../programs/open-source-fraud-engineering/BACKLOG.md) · [Pilotage GitHub #88](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/88)

**Mise à jour : 19 novembre 2026** · Travail de formation et contribution open source pour les ingénieurs de paiement en Afrique francophone.

## Étude
[Étude comparative Tazama, Jube, Ojuri, Marble, Flink/Kafka et Fraud Detection Handbook](OPEN-SOURCE-FRAUD-ENGINEERING-COMPARATIF-2026-11.md).

**Marble est sous Elastic License 2.0, source-available ; ne pas le présenter comme open source OSI.** Les capacités décrites sont celles annoncées par les projets, pas des performances mesurées par OSEF.

## Parcours des labs

| Lab | Sujet | Issue | Condition |
|---|---|---|---|
| FRAUD-001 | Échange de signaux fictifs entre deux PSP | [#43](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/43) | Base API / autorisation / audit |
| FRAUD-002 | Surveillance Tazama et adaptateur | [#50](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/50) | Tazama Core à vérifier |
| FRAUD-003 | Coopération et investigations fédérées | [#63](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63) | Après validation #43 et #50 |
| FRAUD-004 | Travaux Tazama distincts | — | Conserver les travaux existants ; ne pas réaffecter le numéro |
| FRAUD-005 | Comparatif Tazama/Jube | [#80](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/80) | Versions, licences, règles comparables |
| FRAUD-006 | Ojuri / ML et faux positifs | [#81](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/81) | Données synthétiques, métriques |
| FRAUD-007 | Kafka/Flink et streaming antifraude | [#82](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/82) | Streaming, règles, reprise |
| FRAUD-008 | Revue licences et gouvernance | [#83](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/83) | Validation juridique avant offre |

## Catalogue de meetups

| Rencontre | Issue | Lab |
|---|---|---|
| Coopération antifraude / échanges de signaux | [#46](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/46) | FRAUD-001 |
| Fraude fédérée et investigation | [#66](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/66) | FRAUD-003 |
| Comparer Tazama et Jube | [#84](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/84) | FRAUD-005 |
| ML, fraude et faux positifs | [#85](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/85) | FRAUD-006 |
| Kafka/Flink : détection en temps réel | [#86](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/86) | FRAUD-007 |
| Licences et souveraineté antifraude | [#87](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/87) | FRAUD-008 |

## Premier programme de contribution proposé (4 week-ends, non planifié)

- **Week-end A :** vérifier les sources/licences, préparer corpus et jeux de tests communs.
- **Week-end B :** tester Jube et Tazama séparément (selon ressources disponibles), comparer les résultats sans notes fictives.
- **Week-end C :** notebooks d'évaluation ML puis détection de vélocité Flink/Kafka.
- **Week-end D :** revue croisée des PR, fiches de sécurité et répétition des démonstrations.

**Critères communs :** aucune donnée réelle ; environnement isolé ; PR et README commentés ; preuve horodatée de test ; revue par un second ingénieur ; statut « à faire / en cours / testé / revu » fondé sur preuves. Les issues ci-dessus sont **créées, pas exécutées**.

## Prochaine action pour les volontaires
Choisir une issue lab, se manifester en commentaire avec son GitHub, proposer une PR contenant la procédure reproduite et les résultats (sans publier de secrets). Les mainteneurs valident les contributions selon les règles du dépôt.
