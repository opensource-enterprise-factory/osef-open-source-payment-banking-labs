# Veille Fintech & Business OSEF — 22 novembre 2026

**Périmètre :** faits des dernières 24 heures, élargissement explicite au 15–22 novembre 2026. La fiche BCEAO du 9 novembre est uniquement du contexte. **Audit partiel, sans prétention d'exhaustivité.**

Cette édition complète les [six fiches techniques de la PR #104](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/pull/104), sans les recopier. Il s'agit de pistes et d'extensions : aucun lab exécuté, meetup tenu, client acquis ni contrat signé.

## Index veille → lab → meetup → business

| Fiche | Source primaire | Lab | Meetup | Nature commerciale |
|---|---|---|---|---|
| [B01 — BAD Data Warehouse / reporting IA](FIN-20261122-B01.md) | [BAD](https://www.afdb.org/en/consultants/eoi-pre-qualification-consulting-firms-support-98728) | DATA-FIN-POC (concept à dédupliquer) | Reporting financier avec IA | Appel à manifestation d'intérêt à qualifier |
| [B02 — OFTA et Tazama](FIN-20261122-B02.md) | [Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-open-financial-trust-alliance-to-strengthen-coordinated-protection-against-fraud-scams-and-financial-crime) | [FRAUD-003 #63](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63) | Taxonomies antifraude | Hypothèse d'offre, pas de client identifié |
| [B03 — sécurité Flink/JVM](FIN-20261122-B03.md) | [Apache Flink](https://flink.apache.org/2026/11/18/mitigating-cve-2026-114938-java4shell-in-apache-flink-deployments/) | [FRAUD-007 #82](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/82) | Sécurité des JVM en streaming | Hypothèse d'audit |
| [B04 — SIIPS 2026](FIN-20261122-B04.md) | [AfricaNenda](https://africanenda.org/siips/siips-report-2026) | [MOJA-REGRESSION #62](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/62) | Confiance et réclamations | Hypothèse de tests parcours et résilience |
| [B05 — PI-SPI](FIN-20261122-B05.md) | [BCEAO](https://downloads.bceao.int/sites/default/files/2026-11/liste_des_api-business_pi-spi_homologuees_Nov_2026-11-09.pdf) | PI-SPI-CONTRACT (concept à dédupliquer) | Contrats d'API fictives | Hypothèse exploratoire, hors fenêtre |

## Couverture et limites
- Rails et instant payments, fraud/KYC, data/sécurité, institutions régionales, fintech et intelligence commerciale : **partiellement examinés**.
- EMV/PCI et monétique : **non vérifiés systématiquement**.
- Core banking, FINOS/FDC3/DLT et écosystèmes : **partiellement examinés**, sans inventaire complet des releases.
- **0/10 domaines** ont fait l'objet d'un audit complet de couverture pendant cette édition. Ne jamais convertir cette absence d'audit complet en absence d'activité.
- Les dates limites d'appels et critères d'éligibilité nécessitent une ultime revue de l'avis officiel avant candidature.
- L'opportunité BAD ne démontre pas qu'OSEF est éligible. Les autres pistes ne sont pas des leads qualifiés.

## Gouvernance et suite
- Programme de référence : [Open Source Fraud Engineering #88](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/88).
- Aucun nouveau ticket de lab n'est ouvert ici. Les extensions ciblent d'abord les tickets existants.
- Lancer un lab ou une démarche commerciale seulement après revue des sources, licences, habilitations et conditions de consultation.
- Trois priorités : qualification de l'avis BAD ; extension OFTA/Tazama dans FRAUD-003 ; audit JVM/Flink dans FRAUD-007.
