# Atlas BDAT — OSEF Payment & Banking Labs

**Version 1.0 — 17 novembre 2026.** Dix vues conceptuelles en quatre couches : **Business, Data, Application, Technology**. Diagrammes Mermaid rendus directement par GitHub et modifiables dans les fichiers Markdown.

> **Statut : proposées.** Aucune intégration, performance, conformité ou habilitation d'exploitation de systèmes financiers réels ne découle de ces diagrammes.


**Décomposition en quatre visuels :** [Atlas des 40 vues Business, Data, Application et Technology](BDAT-4-VUES-README.md). Les présentes fiches restent des vues de synthèse.
## Galerie des diagrammes

| ID | Cas d'usage | Diagramme BDAT | Blueprint métier détaillé |
|---|---|---|---|
| ARC-01 | Core Banking & Microfinance | [Voir BDAT](ARC-01-BDAT.md) | [Lire architecture](ARC-01.md) |
| ARC-02 | Card Payment & ISO 8583 | [Voir BDAT](ARC-02-BDAT.md) | [Lire architecture](ARC-02.md) |
| ARC-03 | Payment Interoperability Hub | [Voir BDAT](ARC-03-BDAT.md) | [Lire architecture](ARC-03.md) |
| ARC-04 | Mobile Money & Wallet | [Voir BDAT](ARC-04-BDAT.md) | [Lire architecture](ARC-04.md) |
| ARC-05 | Open Banking API Platform | [Voir BDAT](ARC-05-BDAT.md) | [Lire architecture](ARC-05.md) |
| ARC-06 | Financial Ledger & Reconciliation | [Voir BDAT](ARC-06-BDAT.md) | [Lire architecture](ARC-06.md) |
| ARC-07 | Merchant Payment Gateway | [Voir BDAT](ARC-07-BDAT.md) | [Lire architecture](ARC-07.md) |
| ARC-08 | Payment Fraud & Security | [Voir BDAT](ARC-08-BDAT.md) | [Lire architecture](ARC-08.md) |
| ARC-09 | Payment Observability & Resilience | [Voir BDAT](ARC-09-BDAT.md) | [Lire architecture](ARC-09.md) |
| ARC-10 | Payment Integration & Testing Factory | [Voir BDAT](ARC-10-BDAT.md) | [Lire architecture](ARC-10.md) |

## Convention de lecture

- **Business** (bleu) : acteurs, objectifs et processus métier fictifs.
- **Data** (vert) : informations, états, écritures ou résultats de test, uniquement synthétiques.
- **Application** (violet) : services, API, simulateurs et composants candidats à valider.
- **Technology** (orange) : environnements, exécution, stockage, tests et observabilité.

Les liens pointillés entre couches sont des **liens de traçabilité conceptuelle** et non des appels réseau ou contrats d'interface démontrés. Les flux techniques restent à préciser dans des diagrammes de séquence, schémas de données et tests pour chaque lab.

## Validations attendues
1. Revue métier par des spécialistes du processus ciblé.
2. Schéma de données fictives et règles de cohérence.
3. Contrats d'interface, versions, licences et alternatives des composants.
4. Conditions de déploiement, sécurité, observabilité et reprise.
5. Scénarios de tests vérifiés, journal des preuves et revue indépendante.

[Catalogue général](README.md) · [Template blueprint](BLUEPRINT-TEMPLATE.md) · [Architecture globale](../README.md)
