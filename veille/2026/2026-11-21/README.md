# OSEF — Veille mondiale Open Source Finance & Paiements — 21 novembre 2026

**Fenêtre observée :** 20 novembre 08:08 → 21 novembre 08:08 GMT. **Élargissement explicite :** 14–21 novembre 2026, en l'absence de nombreuses annonces majeures sur 24 h. **Périmètre :** sources primaires et dépôts upstream ; vérification ciblée, non exhaustive.

## Synthèse et sources primaires

| Date | Projet/type | Fait vérifié | Source officielle | Implications Afrique francophone | Action OSEF |
|---|---|---|---|---|---|
| 20/11 | Mojaloop, commit/release composant | Central-ledger 20.5.1 ; correction des expirations et de l'idempotence du traitement timeout-reserved. Pas de validation d'une distribution complète. | [Release commit](https://github.com/mojaloop/central-ledger/commit/817844ff2863cc63ad67181551b9aa9e0976200f), [fix](https://github.com/mojaloop/central-ledger/commit/7e11fdaa11e58dc2902021c0e1df1a1e25b5e16e) | Fiabilité des rails instantanés et reprise après timeout | Étendre MOJA-REGRESSION-001 #62 |
| 19/11 | AfricaNenda, rapport SIIPS 2026 | 39 systèmes IPS couvrant fonctionnellement 43 pays (juillet 2026), 71,4 milliards de transactions (année 2025). Ces chiffres ne sont pas une mesure de disponibilité OSS. | [Rapport SIIPS](https://africanenda.org/siips/siips-report-2026) | PI-SPI/UEMOA, parcours de confirmation, recours et confiance | Scénarios SIIPS-TRUST-001, prolongements #62 et #63 |
| 18–19/11 | Linux Foundation / Tazama, annonce d'alliance | Lancement d'OFTA puis billet Tazama sur l'harmonisation des taxonomies antifraude. Aucun standard OFTA implémentable confirmé. | [Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-open-financial-trust-alliance-to-strengthen-coordinated-protection-against-fraud-scams-and-financial-crime), [Tazama](https://www.tazama.org/blog/2026/open-financial-trust-alliance/) | Partage interinstitutionnel de catégories de risques sans divulgation de données personnelles | Extension TAXONOMY-001 de FRAUD-003 #63 |
| 20/11 | FINOS, événement programmé | Journée de présentations et jury du Fall Hackathon ; gagnants non confirmés dans les sources consultées | [FINOS](https://www.finos.org/hosted-events/2026-11-13-finos-fall-2026-hackathon) | Contributions et compétences FDC3 | Enrichir FDC3-001 #61 |
| 20–21/11 | Fineract, Flink, Kafka, commits | Modifications de maintenance upstream, distinctes de releases majeures | [Fineract](https://github.com/apache/fineract/commit/de5c64036abedee1051fdd8c81f3e657f021a4f6), [Flink](https://github.com/apache/flink/commit/e7f1b590d0dbb3e82a84a7b6f2b801e00103d347), [Kafka](https://github.com/apache/kafka/commit/5fd98f7ec78be5dfbe85f45a09b23e6ff751ce1e) | Résilience des traitements et interopérabilité core banking / streaming | Réutiliser #27 et FRAUD-007 #82 |

## Couverture et limites

- **Switching, instant payments, clearing/settlement :** correctif Mojaloop et rapport SIIPS ; pas de nouvelle distribution intégrale confirmée.
- **ISO 8583/ISO 20022, EMV :** pas de nouvelle spécification datée et confirmée dans la fenêtre. Un correctif de compatibilité Gradle 9 pour jPOS du 19/11 est de l'outillage, non un changement de norme.
- **Mobile money, wallets, open banking, core banking, KYC/AML :** SIIPS et commits Fineract ; pas de nouvelle annonce générale établie pour Mifos.
- **Fraude, Jube, Ojuri, Tazama :** OFTA/Tazama vérifié ; aucune nouveauté 24 h Jube/Ojuri confirmée.
- **Kafka/Flink, cybersécurité, cloud-native :** commits upstream ; contrôle CVE non exhaustif et aucune CVE spécifique validée ici.
- **FINOS/FDC3, LF Decentralized Trust, identité, tokenisation :** événement FINOS ; aucune nouvelle release datée et confirmée à attribuer à ces autres thèmes.
- **Souveraineté, régulation francophone :** sujets importants, mais aucune nouvelle obligation réglementaire dans cette fenêtre confirmée.
- **Licences :** ne pas confondre Apache-2.0 (composants Mojaloop), AGPLv3 (Jube), MIT (Ojuri), Elastic License 2.0 (Marble : *source-available*, pas licence open source OSI), standards ouverts (FDC3) et solutions propriétaires. La présence de PI-SPI dans SIIPS ne prouve pas son ouverture logicielle.

## Fiches, labs et meetups

| Fiche | Extension reproductible | Meetup |
|---|---|---|
| [FIN-20261121-01](./FIN-20261121-01.md) | SIIPS-TRUST-001 → #62/#63 | Confiance, confirmation et recours (60 min) |
| [FIN-20261121-02](./FIN-20261121-02.md) | MOJA-TIMEOUT-001 → #62 | Mojaloop timeout/idempotence (75 min) |
| [FIN-20261121-03](./FIN-20261121-03.md) | TAXONOMY-001 → #63/#50 | OFTA/Tazama, taxonomies antifraude (60 min), extension #66 |
| [FIN-20261121-04](./FIN-20261121-04.md) | FDC3-001 → #61 | FINOS/FDC3 (60 min) |
| [FIN-20261121-05](./FIN-20261121-05.md) | Tests ciblés #27/#82 | Aucun nouveau meetup nécessaire |

**Références existantes :** [OSFE #88](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/88), [FRAUD-001 #43](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/43), [FRAUD-002 #50](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/50), [FRAUD-003 #63](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63), [FRAUD-005–008 #80–83](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/80).

## Trois priorités éditoriales
1. SIIPS : confiance, confirmation et recours dans les paiements instantanés.
2. Mojaloop : idempotence et tests reproductibles de timeout.
3. OFTA : taxonomies antifraude sans fuite de données.

Voir [brouillon LinkedIn](./BROUILLON_LINKEDIN.md), [index CSV](./INDEX_VEILLE_LAB_MEETUP.csv) et [export JSON](./VEILLE_2026-11-21.json). Aucune publication LinkedIn, aucun déploiement et aucune validation de conformité ne sont revendiqués.
