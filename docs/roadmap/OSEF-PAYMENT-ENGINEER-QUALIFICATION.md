# OSEF — Parcours interne de qualification Payment Engineering

> **Statut : programme proposé, non encore lancé.** Il ne s'agit ni d'une certification de la Linux Foundation, ni d'une certification PCI DSS/EMV/ISO, ni d'une homologation BCEAO. Les niveaux sont des badges **internes OSEF**, attribuables seulement après validation documentée et revue indépendante.

## Objectifs

Former des ingénieurs capables de **reproduire, expliquer, diagnostiquer et contribuer** à des systèmes de paiements open source, dans des environnements de laboratoire isolés et avec données exclusivement synthétiques.

**Catalogue de référence :** [75 labs possibles](./OSEF-PAYMENT-LABS-CATALOGUE-2026-11-21.md). Une ligne du catalogue est une proposition de lab, pas un lab réalisé.

## Niveaux, activités et preuves

| Niveau | Prérequis / contenus | Épreuve de qualification proposée | Preuves requises |
|---|---|---|---|
| L1 — Foundation | Git, Linux, Docker, protocoles ISO 8583/20022 (notions), BASE-001/003, MON-001, CORE-001, RAIL-001 | Installer un lab dans une VM neuve, produire et expliquer un échange fictif et ses erreurs | README de reproduction, hashes/digests des versions, traces nettoyées, résultat des tests |
| L2 — Payment Integrator | L1, MON-002/003, RAIL-002/003/010, CORE-004, SEC-002, SRE-001 | Démontrer un paiement fictif de bout en bout, un rejet et une répétition idempotente | Tests automatiques cas nominal/négatif, journaux corrélés, vérification absence de double imputation |
| L3 — Payment Reliability & Security | L2, RAIL-006/007, CORE-005/006, SEC-003/004, SRE-002/003 | Injecter une panne, restaurer le service, mesurer la cohérence et les pertes/duplicatas | Rapport d'incident, métriques, budget de risque et plan de correction ; aucun mouvement de fonds réel |
| L4 — Upstream Contributor | L3 ou expérience équivalente évaluée, contribution à un projet du radar | Publier une issue reproduisible ou PR et répondre à une revue technique externe | Liens upstream vérifiables, tests/doc/correctif, commentaires mainteneurs ; acceptation d'une PR valorisée mais non garantie |

## Filières de spécialisation (après L2)

- **Monétique & switching :** jPOS/Moov ISO8583, Mojaloop, simulations autorisation/reversal, timeouts.
- **Core & rails :** Fineract, Mifos Payment Hub EE, Mojaloop, réconciliation ISO 20022.
- **Fraude :** [OSFE #88](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/88), Tazama, Kafka/Flink, Jube/Ojuri sous réserve de licence.
- **Open banking & sécurité :** Open Bank Project, Keycloak, FAPI, secrets, consentement fictif.
- **FINOS & tokenisation :** FDC3, Fabric/Besu sur réseaux de test, sans monétisation ni actifs réels.

## Règle d'évaluation interne (proposition)

Grille sur 100 points :
- Reproductibilité (versions épinglées, README, automatisation) : **25**.
- Exactitude fonctionnelle, tests de succès et d'échec : **25**.
- Résilience, idempotence et qualité des diagnostics : **20**.
- Sécurité, absence de données réelles, dépendances/licences : **20**.
- Documentation et contribution à la communauté : **10**.

**Seuil de qualification proposé : 80/100**, sous réserve d'une revue indépendante et de zéro échec critique (double débit sur cas testé, fuite de secrets/PII, résultat inventé, absence de trace reproductible). Pour L4, la preuve d'une contribution upstream réelle est obligatoire, sans imposer son acceptation par le mainteneur.

Les évaluateurs consignent le résultat avec date, commit SHA, version de lab, preuves et commentaires ; un candidat peut refaire l'épreuve après correction. Ne publier aucun score nominatif sans accord.

## Cadence pilote proposée

1. Semaine 1 : identifier mentors/relecteurs, choisir trois labs existants opérationnels et documenter le matériel.
2. Semaines 2–3 : exécuter L1 et corriger la documentation.
3. Semaines 4–6 : épreuve L2 sur un environnement isolé.
4. Après revue : L3 par spécialisation ; L4 via une contribution upstream.

Ce calendrier est indicatif ; aucune équipe, disponibilité ou réussite n'est confirmée.

## Modèle de preuve par candidat

```yaml
qualification: OSEF-PAYMENT-L2
candidate_id: pseudonyme-local
assessment_date: null
repo_commit_sha: null
lab_ids: []
pinned_versions: []
test_report: null
evidence_links: []
score: null
critical_failures: []
reviewer: null
decision: pending
```

## Gouvernance

- La validation doit être faite par un relecteur différent du candidat.
- Séparer formation interne, badge interne et certification externe.
- Les exigences BCEAO/UEMOA et les certifications PCI/EMV nécessitent leurs propres processus et preuves : le lab ne les remplace pas.
- Les licences sont vérifiées dans les distributions réelles, pas déduites du nom des standards.
- Les contributeurs conservent les droits des projets upstream et respectent leurs guides de contribution.

**Sources internes GitHub :** [Catalogue des labs](./OSEF-PAYMENT-LABS-CATALOGUE-2026-11-21.md), [FRAUD-001 #43](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/43), [PAYMENT-001 #44](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/44), [MOJA-REGRESSION #62](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/62), [OSFE #88](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/88).
