# Labs déduits de la reprise de veille exhaustive — 21 novembre 2026

> **État : propositions et extensions, pas de tests exécutés.** S'appuie sur les sources primaires et le [catalogue existant de 75 labs](../../../docs/roadmap/OSEF-PAYMENT-LABS-CATALOGUE-2026-11-21.md). Aucun lien à un participant réel PI-SPI et aucune certification ou homologation n'est revendiqué.

## Nouveaux chantiers (issues créées)

| Priorité | Lab | Issue | Fait/source | Critère décisif |
|---|---|---|---|---|
| P0 | MOJA-MIGRATION-001 | [#95](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/95) | [Mojaloop central-settlement README](https://github.com/mojaloop/central-settlement/blob/main/README.md), [changelog](https://github.com/mojaloop/central-settlement/blob/main/CHANGELOG.md), dépréciation explicitée en version 17.5.4 du 17/11/2026 | Matrice de tests d'états/settlement avant-après, écarts documentés |
| P0 | PISPI-API-001 | [#96](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/96) | [Communiqué BCEAO sur liste au 9/11/2026](https://www.bceao.int/fr/communique-presse/liste-actualisee-des-api-business-pi-spi-homologuees-par-la-bceao-au-9-11-2026) | API **entièrement fictive**, idempotence, refus, webhook, statut et non-double-débit |
| P1 | FINOS-WORKSPACE-001 | [#97](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/97) | [Portail officiel FINOS](https://www.finos.org/), projet/artefact précis à confirmer avant mise en œuvre | Audit dépôt/licence préalable, puis tests d'interopérabilité FDC3 si réalisable |

Chaque issue détaille objectifs, prérequis, étapes, tests, limites et meetup envisagé.

## Extensions sans nouvelles issues

| Priorité | Lab / issue existante | Complément à écrire et tester |
|---|---|---|
| P0 | [MOJA-REGRESSION #62](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/62) | TTK : timeout réservé, notification, idempotence et reprise |
| P0 | [OPB-015 rapprochement #35](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/35) | Réconciliation comptable avant/après consolidation des services Mojaloop |
| P0 | RAIL-006/007 du [catalogue](../../../docs/roadmap/OSEF-PAYMENT-LABS-CATALOGUE-2026-11-21.md) | Messages ISO 20022 synthétiques et validation de schémas ; ne pas revendiquer une conformité intégrale |
| P1 | CORE-005/006 du catalogue, [Fineract-Mojaloop #27](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/27) | Mifos Payment Hub EE, flux adaptateur et réconciliation |
| P1 | [CI/CD sécurité #38](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/38) | SBOM, dépendances, vulnérabilités vérifiées par version et gestion de remédiation |
| P1 | [FRAUD-003 #63](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63) | TAXONOMY-001 : dictionnaires fictifs, traçabilité et confidentialité |
| P1 | [FDC3-001 #61](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/61) | Tests de contrats FDC3 entre applications financières synthétiques |

## Schéma de fiche technique à suivre

- **Objective / portée** : problème métier et valeur Afrique francophone.
- **Source** : annonce, norme, commit ou documentation officielle datée et lien direct.
- **Environnement** : versions vérifiées et épinglées, VM ou conteneurs isolés, licences et SBOM.
- **Étapes** : installer, injecter fixtures synthétiques, cas nominal, échec, duplication, reprise et nettoyage.
- **Succès** : critères mesurables, logs sans données réelles, rapport d'essai avec SHA et date.
- **Contribution** : reproduire bug, produire test/documentation, proposer upstream après validation ; aucune acceptation présumée.

## Meetups possibles (non programmés)

1. Migration d'architecture Mojaloop — 75 min, ingénieurs switch/SRE/QA, comparaison des scénarios de settlement (issue #95).
2. API Business de paiement instantané en UEMOA — 60 min, PSP/fintechs, démonstration fictive et limites de l'homologation (issue #96).
3. FINOS Workspace et FDC3 — 60 min, architectes et développeurs, démonstration uniquement après vérification du composant et du lab (issue #97).

## Limites

La liste BCEAO des API homologuées ne constitue ni une licence open source ni une publication de contrat d'API utilisable librement. Pour FINOS Workspace, confirmer dépôt, code, licence, statut et documentation avant toute installation ; ne pas inférer la compatibilité à partir d'une annonce générale. Des labs déjà présents dans les 75 thèmes n'ont pas été recréés.
