# 11 — Parcours guidés des labs OSEF Payment Engineering

> Version proposée le 21 novembre 2026. **Ce sont des parcours pédagogiques, non la preuve que les labs sont exécutables.** Toutes les données sont synthétiques. La difficulté se réfère au [classement des 78 labs](../../roadmap/OSEF-PAYMENT-LABS-DIFFICULTE-2026-11-21.md). L'évaluation interne L1–L4 n'est ni une certification PCI/EMV/ISO ni une homologation BCEAO.

## Démarrage : avant tout lab

1. Créer une issue de progression ou un journal privé avec un identifiant non sensible.
2. Configurer une VM Linux propre et Git ; réserver des ressources suffisantes selon le lab effectivement choisi.
3. Documenter OS, versions, digests d'images, dépendances, licence et ports utilisés.
4. Préparer **uniquement** des jeux synthétiques et une commande de nettoyage.
5. Vérifier que le lab est **exécutable** ; les issues OSEF peuvent être de simples propositions.

## Parcours A — Découverte et bases (L0 → L1)

| Séquence | Lab | Compétence observable | Gate |
|---|---|---|---|
| A1 | BASE-001 | Différencier logiciel, standard, licence et statut open source | Comparatif sourcé |
| A2 | BASE-003 | Installer VM Ubuntu, Git, Docker et expliquer les variables d'environnement | README de reproduction sur VM neuve |
| A3 | MON-001 | Construire et analyser un ISO 8583 fictif (Moov) | Tests de parsing + cas invalides |
| A4 | CORE-001 puis CORE-002 | Déployer Fineract et manipuler des comptes fictifs | API testée, traces expurgées |
| A5 | FRAUD-008 | Distinguer licences OSI et source-available | Tableau argumenté |

**Évaluation A :** un autre ingénieur doit pouvoir exécuter A2–A4 avec les instructions, sans accès à des systèmes bancaires réels. Si Fineract exige des ressources indisponibles, garder le lab « bloqué » plutôt que déclarer une réussite.

## Parcours B — Intégration (L1 → L2)

| Séquence | Lab | Compétence observable | Gate |
|---|---|---|---|
| B1 | MON-002 | Simuler émetteur/acquéreur fictifs | Messages d'autorisation cohérents |
| B2 | SEC-002 et OPEN-002 | Sécuriser une API fictive | Tests d'accès autorisé et refusé |
| B3 | RAIL-001 puis RAIL-002 | Expliquer, installer et simuler des transferts Mojaloop | Statuts et traces documentés |
| B4 | RAIL-003 | Tester timeout et retry idempotent | Pas de double effet métier dans le scénario |
| B5 | RAIL-010 | Expliquer confirmation, statut et recours | Cas nominaux et d'échec |
| B6 | CORE-004 | Relier Fineract et Mojaloop dans le lab | Rapport des rapprochements et limites |

**Évaluation B :** rendre le trajet d'un paiement fictif observable de bout en bout, avec erreur et reprise. **Ne pas déduire de la réussite d'un lab la disponibilité ou la robustesse d'une plateforme de production.**

## Parcours C — Fiabilité, fraude et sécurité (L2 → L3)

| Séquence | Lab | Compétence observable | Gate |
|---|---|---|---|
| C1 | SRE-001 puis SRE-002 | Corrélation, incidents et reprise | Rapport de panne daté |
| C2 | SEC-003 puis SEC-004 | mTLS, certificats, SBOM et vulnérabilités | Scénarios négatifs et versions vérifiées |
| C3 | DATA-001 puis FRAUD-007 | Événements Kafka, vélocité et Flink | Tests de retard et duplicatas |
| C4 | FRAUD-002 puis FRAUD-003 | Surveillance, corrélation et investigation | Cas fictifs, protection des données |
| C5 | RAIL-006 puis RAIL-007 | ISO 20022 synthétique, validation XML et règles | Cas valides/invalides |
| C6 | CORE-005 puis CORE-006 | Hub d'intégration et réconciliation | Ledger fictif équilibré et écarts expliqués |

**Évaluation C :** échec injecté, mesure, remédiation, revue indépendante ; aucune donnée financière personnelle ou clé réelle.

## Parcours D — Architecture et contribution (L3 → L4)

| Séquence | Lab | Compétence observable | Gate |
|---|---|---|---|
| D1 | RAIL-005, CORE-007 | Settlement, positions et intégrité comptable | Invariants documentés sous retry |
| D2 | MON-005 | Cryptographie et rotation de clés **strictement de test** | Preuves d'absence de vrais PIN / secrets |
| D3 | SRE-003 | Outbox/inbox et limites des garanties de traitement | Tests de cohérence après panne |
| D4 | BIZ-004 | Capstone banque → hub → switch → fraude → ledger | Dossier architecture + tests + limites |
| D5 | BIZ-002 | Contribution upstream | Issue, test, documentation ou PR réelle et vérifiable |

**Évaluation D :** L4 ne résulte jamais d'un score technique seul. Il faut une contribution upstream identifiable et un examen indépendant.

## Spécialisations facultatives

- **Monétique et cartes :** MON-003, MON-004, MON-006, MON-007.
- **Mobile money et wallets :** MM-001 → MM-004.
- **Open banking :** OPEN-001 → OPEN-005, avec tests et profils FAPI au périmètre exact.
- **Fraude et AML :** FRAUD-001 → FRAUD-012 selon les dépendances et licences vérifiées.
- **FINOS/FDC3 :** FINOS-001 → FINOS-003 ; FINOS-WORKSPACE-001 après vérification du projet.
- **DLT :** DLT-001 → DLT-003 sur réseaux et actifs fictifs.
- **UEMOA :** BIZ-003, PISPI-API-001, exclusivement simulation documentée.
- **Migration Mojaloop :** MOJA-MIGRATION-001 (#95), réservé après validation des bases de settlement.

## Contrat de preuve identique pour tous les parcours

- Issue liée, objectif, prérequis, environnement/version/commit SHA.
- Script d'installation et de nettoyage, fixtures synthétiques.
- Résultats de tests réellement exécutés (succès, erreur, timeout/retry si pertinents).
- Observabilité, sécurité, licences et limitations.
- Revue indépendante et décision datée.
- Éventuelle contribution upstream : URL et statut réellement vérifié.

**Références :** [classification 78 labs](../../roadmap/OSEF-PAYMENT-LABS-DIFFICULTE-2026-11-21.md), [catalogue original](../../roadmap/OSEF-PAYMENT-LABS-CATALOGUE-2026-11-21.md), [programme de qualification](../../roadmap/OSEF-PAYMENT-ENGINEER-QUALIFICATION.md), [pilote #94](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/94).
