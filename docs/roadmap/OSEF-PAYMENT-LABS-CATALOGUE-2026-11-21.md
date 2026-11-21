# OSEF — Catalogue élargi de laboratoires Finance & Payment Engineering

> **Catalogue de possibilités, non liste de labs déployés.** Établi le 21 novembre 2026 à partir des issues existantes et de l'audit stratégique. Les technologies candidates doivent être vérifiées (licence, versions, APIs et environnement) avant implémentation. Un lien vers une issue signifie un rattachement, pas une preuve d'exécution.

## Règles communes

1. Prérequis : VM Ubuntu ou Docker/Kubernetes selon lab ; versions/digests figés ; fixtures synthétiques, aucun identifiant réel ; README, architecture et licence.
2. Étapes : installer → charger fixtures → exécuter cas nominal → injecter panne/cas négatif → relever traces/métriques → nettoyage.
3. Critères de succès : commandes reproductibles, tests positifs/négatifs, pas de mouvement de fonds réel, preuves de non-double-débit quand pertinent, logs sans PII, résultats datés et limites explicites.
4. Contribution : privilégier tests et documentation upstream ; aucune certification PCI-DSS/EMV/BCEAO n'est inférée.
5. Éviter les doublons : `existant` désigne une issue déjà créée (pas forcément un lab exécuté), `extension` un ajout au lab/issue existant, `nouveau` un thème sans issue identifiée dans la recherche effectuée.

**Priorités de planification :** P0 = fondation ; P1 = spécialisation ; P2 = avancé/recherche. Ces priorités sont des recommandations OSEF et non des jugements de maturité officiels.

## Inventaire

### Fondations (3)

| Identifiant | Lab / objectif | Technologies candidates | Statut GitHub | Priorité |
|---|---|---|---|---|
| BASE-001 | Cartographie technologies, licences et standards | inventaire OSI, SPDX, normes | [#12](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/12) — existant | P0 |
| BASE-002 | SBOM, provenance et licences des dépendances | Syft, CycloneDX, OSV | [#83](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/83) — extension | P1 |
| BASE-003 | Environnement reproductible Ubuntu / Docker / 12-Factor | Docker, Compose, CI | [#90](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/90) — extension | P0 |

### Monétique (7)

| Identifiant | Lab / objectif | Technologies candidates | Statut GitHub | Priorité |
|---|---|---|---|---|
| MON-001 | Construire/parser un ISO 8583 fictif | Moov ISO8583 (Go) | [#41](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/41) — existant | P0 |
| MON-002 | Simulateur émetteur / acquéreur ISO 8583 | jPOS, Moov | [#41](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/41) — extension | P0 |
| MON-003 | Autorisation, reversal, advice et duplicate MTI | jPOS | [#41](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/41) — extension | P0 |
| MON-004 | Field 55 TLV EMV sur données synthétiques | TLV, outils de parsing | nouveau — à cadrer | P1 |
| MON-005 | Simuler clés, rotation et PIN sans PIN réel | SoftHSM2, OpenBao | [#31](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/31) — extension | P1 |
| MON-006 | Routage multi-acquéreur fictif et timeouts | jPOS, simulateurs | nouveau — à cadrer | P1 |
| MON-007 | Réconciliation monétique et chargeback simulé | PostgreSQL, règles | [#35](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/35) — extension | P1 |

### Rails (10)

| Identifiant | Lab / objectif | Technologies candidates | Statut GitHub | Priorité |
|---|---|---|---|---|
| RAIL-001 | Architecture et déploiement Mojaloop | Mojaloop Helm | [#21](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/21) — existant | P0 |
| RAIL-002 | Transfert entre DFSP fictifs | Mojaloop | [#44](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/44) — existant | P0 |
| RAIL-003 | Non-régression timeout et idempotence | Mojaloop TTK | [#62](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/62) — extension | P0 |
| RAIL-004 | Quotes, fees et chemin d'échec | Mojaloop | [#44](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/44) — extension | P0 |
| RAIL-005 | Liquidity positions, net settlement et reconciliation | Mojaloop | [#35](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/35) — extension | P1 |
| RAIL-006 | Passerelle ISO 20022 pacs.* synthétique | ISO 20022 schémas, XML | nouveau — à cadrer | P0 |
| RAIL-007 | Validation ISO 20022 schemas et règles métier | XML Schema, Schematron | nouveau — à cadrer | P0 |
| RAIL-008 | Simulation multirail wallet / banque / PSP | Mojaloop, adaptateurs | nouveau — à cadrer | P1 |
| RAIL-009 | Paiement transfrontalier simulé et FX/fees | ISO 20022, règles | nouveau — à cadrer | P2 |
| RAIL-010 | Confirmation, statut, recours et litiges | API fictive | [#92](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/92) — existant | P0 |

### Core banking (8)

| Identifiant | Lab / objectif | Technologies candidates | Statut GitHub | Priorité |
|---|---|---|---|---|
| CORE-001 | Installer Apache Fineract | Apache Fineract | [#14](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/14) — existant | P0 |
| CORE-002 | Clients et comptes fictifs | Fineract | [#16](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/16) — existant | P0 |
| CORE-003 | Crédit, échéancier et remboursement | Fineract | [#17](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/17) — existant | P1 |
| CORE-004 | Connecteur Fineract ↔ Mojaloop | Fineract, Mojaloop | [#27](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/27) — existant | P0 |
| CORE-005 | Mifos Payment Hub EE : installation et adaptateur | Mifos PHEE | nouveau — à cadrer | P0 |
| CORE-006 | Réconciliation Fineract–Hub–Switch | Fineract, Mifos, Mojaloop | [#35](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/35) — extension | P0 |
| CORE-007 | Écritures comptables et soldes après retry | Fineract, ledger de test | nouveau — à cadrer | P1 |
| CORE-008 | Traitement batch, EOD et cut-off | Fineract | nouveau — à cadrer | P2 |

### Mobile money (4)

| Identifiant | Lab / objectif | Technologies candidates | Statut GitHub | Priorité |
|---|---|---|---|---|
| MM-001 | Wallet synthétique et ledger double entrée | PostgreSQL, API | nouveau — à cadrer | P0 |
| MM-002 | Cash-in/cash-out et agents fictifs | wallet simulé | nouveau — à cadrer | P1 |
| MM-003 | Interopérabilité wallet-banque-PSP | Mojaloop, adaptateurs | nouveau — à cadrer | P1 |
| MM-004 | Réconciliation et commissions d'agents | SQL, ledger | nouveau — à cadrer | P1 |

### Open banking (5)

| Identifiant | Lab / objectif | Technologies candidates | Statut GitHub | Priorité |
|---|---|---|---|---|
| OPEN-001 | API bancaire et consentement simulé | Open Bank Project | nouveau — à cadrer | P0 |
| OPEN-002 | OAuth2/OIDC, PKCE et consentement | Keycloak | [#30](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/30) — extension | P0 |
| OPEN-003 | Profils FAPI et tests de conformité locaux | OpenID FAPI | nouveau — à cadrer | P1 |
| OPEN-004 | Webhook signé, mTLS et anti-rejeu | Keycloak, OpenSSL | nouveau — à cadrer | P1 |
| OPEN-005 | Identité et vérification KYC simulée | Keycloak, données fictives | nouveau — à cadrer | P1 |

### Fraude (12)

| Identifiant | Lab / objectif | Technologies candidates | Statut GitHub | Priorité |
|---|---|---|---|---|
| FRAUD-001 | Échange de signaux entre 2 PSP fictifs | OSEF FRAUD | [#43](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/43) — existant | P0 |
| FRAUD-002 | Surveillance Tazama et adaptateur | Tazama | [#50](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/50) — existant | P0 |
| FRAUD-003 | Corrélation fédérée et investigation | Tazama, API | [#63](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63) — existant | P0 |
| FRAUD-004 | Déploiement Kubernetes/Helm Tazama | Helm, Kubernetes | [#68](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/68) — existant | P1 |
| FRAUD-005 | Benchmark Tazama vs Jube | Tazama, Jube | [#80](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/80) — existant | P1 |
| FRAUD-006 | ML et explicabilité des alertes | Ojuri, notebooks | [#81](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/81) — existant | P1 |
| FRAUD-007 | Fraude streaming vélocité | Kafka, Flink | [#82](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/82) — existant | P0 |
| FRAUD-008 | Licences open source vs source-available | SPDX, Marble ELv2 | [#83](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/83) — existant | P0 |
| FRAUD-009 | Taxonomie fictive interinstitutionnelle | mappings CSV/JSON | [#63](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63) — extension | P1 |
| FRAUD-010 | Graphes de comptes et réseaux suspects synthétiques | NetworkX, Neo4j community | nouveau — à cadrer | P1 |
| FRAUD-011 | AML : surveillance typologies et fausses alertes | règles fictives | nouveau — à cadrer | P1 |
| FRAUD-012 | Gestion des cas, audit trail et droits d'accès | workflow, PostgreSQL | [#63](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63) — extension | P1 |

### Sécurité (6)

| Identifiant | Lab / objectif | Technologies candidates | Statut GitHub | Priorité |
|---|---|---|---|---|
| SEC-001 | Gestion de secrets et rotation | OpenBao | [#31](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/31) — existant | P0 |
| SEC-002 | API authentifiées et autorisations | Keycloak | [#30](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/30) — existant | P0 |
| SEC-003 | TLS/mTLS, certificats et révocation | OpenSSL, step-ca | nouveau — à cadrer | P0 |
| SEC-004 | Scanning SBOM, CVE et correctifs | Trivy, OSV | [#38](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/38) — extension | P0 |
| SEC-005 | Threat modeling STRIDE paiement | OWASP, diagrams | [#39](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/39) — extension | P1 |
| SEC-006 | Signature événements, audit et non-répudiation | OpenSSL, logs | nouveau — à cadrer | P1 |

### Reliabilité (6)

| Identifiant | Lab / objectif | Technologies candidates | Statut GitHub | Priorité |
|---|---|---|---|---|
| SRE-001 | Observabilité transactionnelle end-to-end | OpenTelemetry | [#36](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/36) — existant | P0 |
| SRE-002 | Chaos testing timeout, panne, reprise | Docker, Kubernetes | [#37](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/37) — existant | P0 |
| SRE-003 | Idempotence, outbox/inbox et exactly-once applicatif | Kafka, PostgreSQL | nouveau — à cadrer | P0 |
| SRE-004 | Capacity test 1x/10x/100x sur données fictives | k6, Prometheus | nouveau — à cadrer | P1 |
| SRE-005 | Runbooks et reprise après incident | Grafana, scripts | nouveau — à cadrer | P1 |
| SRE-006 | Chaîne CI/CD sécurisée et tests de contrats | GitHub Actions | [#38](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/38) — existant | P0 |

### Data (4)

| Identifiant | Lab / objectif | Technologies candidates | Statut GitHub | Priorité |
|---|---|---|---|---|
| DATA-001 | Kafka events et contrats Avro/JSON | Kafka | [#33](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/33) — existant | P0 |
| DATA-002 | Paiement streaming et Flink CEP | Flink | [#82](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/82) — extension | P1 |
| DATA-003 | Qualité de données et rapprochement | Great Expectations, SQL | [#35](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/35) — extension | P1 |
| DATA-004 | Dashboard indicateurs de paiement | Grafana | [#34](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/34) — existant | P1 |

### FINOS (3)

| Identifiant | Lab / objectif | Technologies candidates | Statut GitHub | Priorité |
|---|---|---|---|---|
| FINOS-001 | Governance-as-Code et contribution | FINOS, CI | [#45](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/45) — existant | P1 |
| FINOS-002 | Interopérabilité FDC3 entre deux apps | FDC3 | [#61](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/61) — existant | P1 |
| FINOS-003 | Tests de compatibilité FDC3 et invalid contexts | FDC3 | [#61](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/61) — extension | P1 |

### Tokenisation (3)

| Identifiant | Lab / objectif | Technologies candidates | Statut GitHub | Priorité |
|---|---|---|---|---|
| DLT-001 | Ledger permissionné d'actifs fictifs | Hyperledger Fabric | nouveau — à cadrer | P2 |
| DLT-002 | Tokenisation et transfert sur réseau de test | Hyperledger Besu | nouveau — à cadrer | P2 |
| DLT-003 | Atomicity d'un règlement simulé, sans fonds réels | Fabric/Besu simulateur | nouveau — à cadrer | P2 |

### Gouvernance (4)

| Identifiant | Lab / objectif | Technologies candidates | Statut GitHub | Priorité |
|---|---|---|---|---|
| BIZ-001 | Catalogue de maturité et licences open source | SPDX, OSI, CHAOSS | nouveau — à cadrer | P0 |
| BIZ-002 | Contribution upstream (issue → PR → revue) | GitHub, guides | nouveau — à cadrer | P0 |
| BIZ-003 | Matrice conformité technique UEMOA contextualisée | sources BCEAO | [#39](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/39) — extension | P1 |
| BIZ-004 | Capstone banque → hub → switch → fraude → ledger | Fineract, Mifos, Mojaloop, Tazama | [#40](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/40) — extension | P2 |

## Parcours recommandé

- **Débutant** : BASE-001/003, MON-001, CORE-001/002, RAIL-001, DATA-001.
- **Intermédiaire** : MON-002/003, RAIL-002/003/006/007/010, CORE-004/005/006, FRAUD-001/002/007, SRE-001/002/003, SEC-001/002/003.
- **Avancé** : RAIL-005/008/009, FRAUD-003/005/010/011, FINOS-003, DLT-001/002/003 et BIZ-004.

## Source GitHub et état des lieux

[Issues du dépôt](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues) · [OSFE #88](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/88) · [Veille du 21 novembre / PR #91](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/pull/91)

**Attention :** les issues OPB-001..020 sont parfois présentes en double dans ce dépôt ; le catalogue référence une issue représentative par objectif. Avant de créer une nouvelle issue, vérifier aussi les autres branches et les fichiers du dépôt. Pas de validation de compatibilité de toutes les combinaisons technologiques proposées.
