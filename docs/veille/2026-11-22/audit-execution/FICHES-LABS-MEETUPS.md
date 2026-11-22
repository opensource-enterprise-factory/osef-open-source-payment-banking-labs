# Fiches opérationnelles issues du test — extensions sans doublons

## Fiche T1 — Fraude temps réel : sécurité des runtimes Flink
- **Fait :** avis de sécurité Apache daté du 18 novembre 2026 (à lire avant tout diagnostic local).
- **Source primaire :** https://flink.apache.org/2026/11/18/mitigating-cve-2026-114938-java4shell-in-apache-flink-deployments/
- **Catégorie :** alerte sécurité ; ne prouve pas l'exposition des systèmes OSEF.
- **Lab existant :** [FRAUD-007 #82](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/82).
- **Objectif :** identifier les versions JDK, fournisseurs, architectures et versions d'images du laboratoire ; comparer strictement à l'avis et tester le correctif.
- **Prérequis :** Flink isolé, image digest, inventaire SBOM, flux de transactions synthétiques et version JDK connue.
- **Étapes :** relever inventaire → comparer à l'avis → mettre à jour dans une branche de test → lancer tests de non-régression et reprise → conserver logs.
- **Critères :** exposé/non exposé justifié par preuve technique ; aucune interruption de pipeline test ; aucune exploitation de la faille.
- **Meetup proposé :** « Sécuriser les pipelines antifraude Kafka/Flink », public DevSecOps/SRE/banque, 60 min, démo de contrôle d'images fictives.

## Fiche T2 — Taxonomies de risque : OFTA + Tazama
- **Fait :** annonce d'OFTA par Linux Foundation le 18 novembre 2026 ; cela ne prouve pas qu'une API finale est disponible.
- **Sources :** https://www.linuxfoundation.org/press/linux-foundation-announces-the-open-financial-trust-alliance-to-strengthen-coordinated-protection-against-fraud-scams-and-financial-crime ; https://www.tazama.org/blog/2026/open-financial-trust-alliance/
- **Lab existant :** [FRAUD-003 #63](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63).
- **Objectif :** comparer les catégories de trois établissements fictifs, avec contrôle des règles de partage.
- **Prérequis :** données et taxonomies inventées, matrice d'accès, audit trail, contrats de messages synthétiques.
- **Étapes :** concevoir dictionnaires → mapper classes → simuler échange → injecter classes inconnues/contradictoires → vérifier refus et traçabilité.
- **Critères :** conformité aux droits déclarés, aucune donnée personnelle, classes ambiguës détectées et journalisées.
- **Meetup :** « OFTA et interopérabilité des alertes en Afrique », public PSP et conformité, 60 min avec démonstration sur alertes fictives.

## Fiche T3 — Paiements instantanés : confirmations et litiges
- **Fait de contexte :** étude AfricaNenda SIIPS 2026, source https://africanenda.org/siips/siips-report-2026 ; ne constitue pas une release logicielle.
- **Lab existant :** [MOJA-REGRESSION #62](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/62).
- **Objectif :** maintenir un état cohérent de transaction malgré timeouts, doublons, reversals et réclamations.
- **Prérequis :** switch/PSP fictifs, simulateur d'API et références corrélées.
- **Étapes :** exécuter nominal → injecter timeout → rejouer paiement → comparer soldes → simuler une réclamation → réconcilier résultat.
- **Critères :** absence de double débit dans les scénarios, état final documenté, historique exploitable pour réclamation.
- **Meetup :** « Résilience et recours dans le paiement instantané », banques/fintechs/ingénieurs, atelier 75 min.

## Fiche T4 — Reporting financier et IA : concept commercial
- **Fait :** avis officiel de présélection de cabinets BAD, à qualifier selon les pièces et dates du dossier : https://www.afdb.org/en/consultants/eoi-pre-qualification-consulting-firms-support-98728
- **Lab :** DATA-FIN-POC **concept à dédupliquer** avant création ; aucune issue ou recette revendiquée.
- **Objectif :** construire un entrepôt fictif de données financières réconciliées.
- **Prérequis :** PostgreSQL, ETL sous licence vérifiée, Docker, données synthétiques, contrôles de qualité.
- **Étapes :** générer données → charger → dédupliquer → appliquer contrôles → produire indicateurs → redémarrer ingestion → vérifier écarts.
- **Critères :** reproductibilité, idempotence, explicabilité des transformations, zéro donnée confidentielle.
- **Meetup :** « Construire un Data Warehouse financier auditable », équipes IT, finance et data, 75 min avec démonstration.

Aucune nouvelle issue ni meetup n'est créé par ces fiches ; voir également [PR #104](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/pull/104), [PR #105](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/pull/105) et [OSFE #88](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/88).
