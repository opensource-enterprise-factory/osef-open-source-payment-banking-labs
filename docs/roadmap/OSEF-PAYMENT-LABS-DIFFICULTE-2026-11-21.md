# OSEF — Classification des labs par difficulté

> Proposition pédagogique datée du 21 novembre 2026. **La difficulté n'est pas le statut d'exécution**, ni la priorité métier P0/P1/P2, ni un niveau automatiquement attribué à un ingénieur. Les 75 premiers labs proviennent du catalogue JSON sur `main`; 3 labs complémentaires ont leurs propres issues.

## Répartition

| Difficulté | Dans les 75 labs | Avec 3 compléments | Compétence visée |
|---|---:|---:|---|
| Débutant | 8 | 8 | Comprendre et reproduire un exercice isolé |
| Intermédiaire | 30 | 31 | Installer, tester et diagnostiquer un composant |
| Avancé | 27 | 28 | Intégrer des systèmes et traiter incidents et sécurité |
| Expert | 10 | 11 | Concevoir et valider des architectures transactionnelles complexes |

## Classification complète (78 propositions)


### Débutant — 8 labs

| Code | Domaine | Lab | Priorité métier | Issue liée |
|---|---|---|---|---|
| `CORE-001` | Core banking | Installer Apache Fineract | P0 | [#14](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/14) |
| `CORE-002` | Core banking | Clients et comptes fictifs | P0 | [#16](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/16) |
| `DATA-004` | Data | Dashboard indicateurs de paiement | P1 | [#34](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/34) |
| `BASE-001` | Fondations | Cartographie technologies, licences et standards | P0 | [#12](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/12) |
| `BASE-003` | Fondations | Environnement reproductible Ubuntu / Docker / 12-Factor | P0 | [#90](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/90) |
| `FRAUD-008` | Fraude | Licences open source vs source-available | P0 | [#83](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/83) |
| `BIZ-001` | Gouvernance | Catalogue de maturité et licences open source | P0 | À cadrer |
| `MON-001` | Monétique | Construire/parser un ISO 8583 fictif | P0 | [#41](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/41) |

### Intermédiaire — 31 labs

| Code | Domaine | Lab | Priorité métier | Issue liée |
|---|---|---|---|---|
| `CORE-003` | Core banking | Crédit, échéancier et remboursement | P1 | [#17](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/17) |
| `DATA-001` | Data | Kafka events et contrats Avro/JSON | P0 | [#33](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/33) |
| `DATA-003` | Data | Qualité de données et rapprochement | P1 | [#35](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/35) |
| `FINOS-001` | FINOS | Governance-as-Code et contribution | P1 | [#45](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/45) |
| `FINOS-002` | FINOS | Interopérabilité FDC3 entre deux apps | P1 | [#61](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/61) |
| `FINOS-WORKSPACE-001` | FINOS | Évaluer un poste de travail financier et les agents FDC3 | P1 | [#97](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/97) |
| `BASE-002` | Fondations | SBOM, provenance et licences des dépendances | P1 | [#83](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/83) |
| `FRAUD-001` | Fraude | Échange de signaux entre 2 PSP fictifs | P0 | [#43](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/43) |
| `FRAUD-002` | Fraude | Surveillance Tazama et adaptateur | P0 | [#50](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/50) |
| `FRAUD-004` | Fraude | Déploiement Kubernetes/Helm Tazama | P1 | [#68](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/68) |
| `FRAUD-009` | Fraude | Taxonomie fictive interinstitutionnelle | P1 | [#63](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63) |
| `BIZ-002` | Gouvernance | Contribution upstream (issue → PR → revue) | P0 | À cadrer |
| `MM-001` | Mobile money | Wallet synthétique et ledger double entrée | P0 | À cadrer |
| `MM-002` | Mobile money | Cash-in/cash-out et agents fictifs | P1 | À cadrer |
| `MON-002` | Monétique | Simulateur émetteur / acquéreur ISO 8583 | P0 | [#41](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/41) |
| `MON-004` | Monétique | Field 55 TLV EMV sur données synthétiques | P1 | À cadrer |
| `OPEN-001` | Open banking | API bancaire et consentement simulé | P0 | À cadrer |
| `OPEN-002` | Open banking | OAuth2/OIDC, PKCE et consentement | P0 | [#30](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/30) |
| `OPEN-005` | Open banking | Identité et vérification KYC simulée | P1 | À cadrer |
| `RAIL-001` | Rails | Architecture et déploiement Mojaloop | P0 | [#21](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/21) |
| `RAIL-002` | Rails | Transfert entre DFSP fictifs | P0 | [#44](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/44) |
| `RAIL-004` | Rails | Quotes, fees et chemin d'échec | P0 | [#44](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/44) |
| `RAIL-007` | Rails | Validation ISO 20022 schemas et règles métier | P0 | À cadrer |
| `RAIL-010` | Rails | Confirmation, statut, recours et litiges | P0 | [#92](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/92) |
| `SRE-001` | Reliabilité | Observabilité transactionnelle end-to-end | P0 | [#36](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/36) |
| `SRE-005` | Reliabilité | Runbooks et reprise après incident | P1 | À cadrer |
| `SRE-006` | Reliabilité | Chaîne CI/CD sécurisée et tests de contrats | P0 | [#38](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/38) |
| `SEC-001` | Sécurité | Gestion de secrets et rotation | P0 | [#31](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/31) |
| `SEC-002` | Sécurité | API authentifiées et autorisations | P0 | [#30](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/30) |
| `SEC-004` | Sécurité | Scanning SBOM, CVE et correctifs | P0 | [#38](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/38) |
| `SEC-005` | Sécurité | Threat modeling STRIDE paiement | P1 | [#39](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/39) |

### Avancé — 28 labs

| Code | Domaine | Lab | Priorité métier | Issue liée |
|---|---|---|---|---|
| `CORE-004` | Core banking | Connecteur Fineract ↔ Mojaloop | P0 | [#27](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/27) |
| `CORE-005` | Core banking | Mifos Payment Hub EE : installation et adaptateur | P0 | À cadrer |
| `DATA-002` | Data | Paiement streaming et Flink CEP | P1 | [#82](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/82) |
| `FINOS-003` | FINOS | Tests de compatibilité FDC3 et invalid contexts | P1 | [#61](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/61) |
| `FRAUD-005` | Fraude | Benchmark Tazama vs Jube | P1 | [#80](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/80) |
| `FRAUD-006` | Fraude | ML et explicabilité des alertes | P1 | [#81](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/81) |
| `FRAUD-007` | Fraude | Fraude streaming vélocité | P0 | [#82](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/82) |
| `FRAUD-010` | Fraude | Graphes de comptes et réseaux suspects synthétiques | P1 | À cadrer |
| `FRAUD-011` | Fraude | AML : surveillance typologies et fausses alertes | P1 | À cadrer |
| `FRAUD-012` | Fraude | Gestion des cas, audit trail et droits d'accès | P1 | [#63](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63) |
| `BIZ-003` | Gouvernance | Matrice conformité technique UEMOA contextualisée | P1 | [#39](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/39) |
| `MM-003` | Mobile money | Interopérabilité wallet-banque-PSP | P1 | À cadrer |
| `MM-004` | Mobile money | Réconciliation et commissions d'agents | P1 | À cadrer |
| `MON-003` | Monétique | Autorisation, reversal, advice et duplicate MTI | P0 | [#41](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/41) |
| `MON-006` | Monétique | Routage multi-acquéreur fictif et timeouts | P1 | À cadrer |
| `MON-007` | Monétique | Réconciliation monétique et chargeback simulé | P1 | [#35](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/35) |
| `OPEN-003` | Open banking | Profils FAPI et tests de conformité locaux | P1 | À cadrer |
| `OPEN-004` | Open banking | Webhook signé, mTLS et anti-rejeu | P1 | À cadrer |
| `PISPI-API-001` | Rails | Simuler une API Business de paiement instantané en UEMOA | P0 | [#96](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/96) |
| `RAIL-003` | Rails | Non-régression timeout et idempotence | P0 | [#62](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/62) |
| `RAIL-006` | Rails | Passerelle ISO 20022 pacs.* synthétique | P0 | À cadrer |
| `RAIL-008` | Rails | Simulation multirail wallet / banque / PSP | P1 | À cadrer |
| `SRE-002` | Reliabilité | Chaos testing timeout, panne, reprise | P0 | [#37](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/37) |
| `SRE-004` | Reliabilité | Capacity test 1x/10x/100x sur données fictives | P1 | À cadrer |
| `SEC-003` | Sécurité | TLS/mTLS, certificats et révocation | P0 | À cadrer |
| `SEC-006` | Sécurité | Signature événements, audit et non-répudiation | P1 | À cadrer |
| `DLT-001` | Tokenisation | Ledger permissionné d'actifs fictifs | P2 | À cadrer |
| `DLT-002` | Tokenisation | Tokenisation et transfert sur réseau de test | P2 | À cadrer |

### Expert — 11 labs

| Code | Domaine | Lab | Priorité métier | Issue liée |
|---|---|---|---|---|
| `CORE-006` | Core banking | Réconciliation Fineract–Hub–Switch | P0 | [#35](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/35) |
| `CORE-007` | Core banking | Écritures comptables et soldes après retry | P1 | À cadrer |
| `CORE-008` | Core banking | Traitement batch, EOD et cut-off | P2 | À cadrer |
| `FRAUD-003` | Fraude | Corrélation fédérée et investigation | P0 | [#63](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63) |
| `BIZ-004` | Gouvernance | Capstone banque → hub → switch → fraude → ledger | P2 | [#40](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/40) |
| `MON-005` | Monétique | Simuler clés, rotation et PIN sans PIN réel | P1 | [#31](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/31) |
| `MOJA-MIGRATION-001` | Rails | Auditer la migration Central Settlement vers Central Ledger | P0 | [#95](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/95) |
| `RAIL-005` | Rails | Liquidity positions, net settlement et reconciliation | P1 | [#35](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/35) |
| `RAIL-009` | Rails | Paiement transfrontalier simulé et FX/fees | P2 | À cadrer |
| `SRE-003` | Reliabilité | Idempotence, outbox/inbox et exactly-once applicatif | P0 | À cadrer |
| `DLT-003` | Tokenisation | Atomicity d'un règlement simulé, sans fonds réels | P2 | À cadrer |

## Comment employer le classement

- **Débutant → L1** : initier Git/Linux/Docker, formats de message et premières installations ; certains labs intermédiaires font partie des épreuves L1.
- **Intermédiaire → L1/L2** : reproduire les scénarios, fournir logs et tests ; L2 requiert une intégration et des cas négatifs.
- **Avancé → L2/L3** : relier plusieurs composants, vérifier les effets des retries, documenter la sécurité et les incidents.
- **Expert → L3/L4** : systèmes multi-acteurs, conformité de flux, settlement, cohérence du ledger et preuves reproductibles ; **L4 implique aussi une contribution upstream vérifiée**, pas seulement un lab Expert.

La difficulté reflète la complexité envisagée avec une installation contrôlée et des **données synthétiques**. Elle peut être réévaluée après une recette pratique. Ne pas confondre une simulation avec une conformité PCI/EMV/ISO ou une homologation BCEAO.

## Critères d'évaluation de difficulté

1. Prérequis systèmes, protocoles et programmation.
2. Nombre de composants, interfaces et contrats à gérer.
3. Complexité transactionnelle : états, compensation, retry, ledger et rapprochement.
4. Risque de sécurité, cryptographie et exploitation.
5. Effort de test/reproductibilité et diagnostic des erreurs.

## Références internes

- [Catalogue source — 75 labs](./OSEF-PAYMENT-LABS-CATALOGUE-2026-11-21.md)
- [Qualification des ingénieurs L1–L4](./OSEF-PAYMENT-ENGINEER-QUALIFICATION.md)
- [Manuel de l'ingénieur paiement](../academy/payment-engineer/README.md)
- [Nouveaux labs de la veille](../../veille/2026/2026-11-21/LABS-DEDUITS-VEILLE-EXHAUSTIVE.md)
