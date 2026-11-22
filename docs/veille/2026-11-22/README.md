# Veille Finance & Paiements OSEF — 22 novembre 2026

**Périmètre :** 21–22 novembre 2026 UTC, élargi au 15–22 novembre faute de nombreuses annonces majeures. Cette édition distingue commits, avis de sécurité et orientations de projet ; elle ne revendique aucun déploiement client ni aucune exécution des labs.

## Fiches et index veille → lab → meetup

| Fiche | Signal | Lab existant à compléter | Meetup proposé |
|---|---|---|---|
| [FIN-20261122-01](fiches/FIN-20261122-01.md) | Apache Fineract : hiérarchie d'agences | CORE-002 / SEC-002 | Core banking multi-agences |
| [FIN-20261122-02](fiches/FIN-20261122-02.md) | Apache Flink : TO_APPEND | FRAUD-007 #82 | Flink append-only et ledger |
| [FIN-20261122-03](fiches/FIN-20261122-03.md) | Hyperledger Fabric : erreurs CouchDB | DLT-001 / SRE-002 | Résilience Fabric |
| [FIN-20261122-04](fiches/FIN-20261122-04.md) | Avis sécurité Apache Flink / Java | SEC-004 / FRAUD-007 #82 | Auditer les JVM Flink |
| [FIN-20261122-05](fiches/FIN-20261122-05.md) | Mojaloop : Central Settlement | #95 / #62 | Migration du settlement |
| [FIN-20261122-06](fiches/FIN-20261122-06.md) | jPOS : Control Plane | MON-002 / CORE-007 | Contrat switching–ledger |

## Priorités éditoriales (trois maximum)
1. Audit des JVM et des images de pipelines antifraude.
2. Intégrité des permissions d'agences en core banking.
3. Résilience des migrations de settlement Mojaloop.

## Gouvernance et anti-doublons
- Programme de référence : [Open Source Fraud Engineering #88](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/88).
- Vérifier FRAUD-001/002/003/005–008 et les tickets cités avant de lancer toute nouvelle issue ou implémentation.
- Ces six fiches sont des **propositions documentaires** : aucun lab exécuté, meetup organisé ou compatibilité de version vérifiée.
- Les mentions de licences nécessitent examen composant par composant : standard ouvert ≠ logiciel sous licence OSI ; Marble ELv2 est source-available et non assimilable à une licence OSI.
- Absence de nouveautés confirmées dans cette édition pour plusieurs axes (mobile money, wallets, KYC/AML, identité, FINOS/FDC3, OFTA, etc.) ; une absence de signal vérifié ne signifie pas absence d'activité.
