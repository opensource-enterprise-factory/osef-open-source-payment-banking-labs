# OSEF — Audit initial de préparation à l'exécution des labs

> **Date : 21 novembre 2026.** Audit **documentaire et du contenu GitHub**, pas exécution en VM. Les résultats de tests ci-dessous sont **rapportés par les issues et preuves historiques du dépôt**, sans nouvelle reproduction indépendante. Ne pas assimiler code présent, CI documentaire réussie et lab certifié opérationnel.

## Périmètre et échelle de preuve

| Code | Définition |
|---|---|
| **R0 — Idée / issue** | Exigences ou scénario, sans démonstration de code exécutable vérifiée |
| **R1 — Prototype présent** | Code/scripts présents, compilation ou recette non confirmée dans l'audit |
| **R2 — Exécution rapportée** | Des tests et résultats d'exécution sont consignés avec liens/commits ; reproduction indépendante encore à faire |
| **R3 — Revue indépendante** | Autre ingénieur a reproduit à partir d'une VM propre, documenté version, logs, incidents et verdict |
| **R4 — Parcours pédagogique validé** | Tests R3, sécurité/licences et dossier d'évaluation approuvés pour les candidats |

R2 n'est pas équivalent à R3. Une issue fermée n'est pas nécessairement un signe de recette ; une issue ouverte peut posséder des preuves d'essais.

## Échantillon prioritaire — résultats constatés dans GitHub

| Lab et issue | Pièces observées dans GitHub | Classement documentaire | Action de passage au gate suivant |
|---|---|---|---|
| **FRAUD-001 [#43](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/43)** | Dossier `labs/FRAUD-001`, app, Docker/Compose, scripts, preuves ; issue fermée : T01–T11 rapportés sur une VM Ubuntu le 18–19 novembre | **R2 — exécution rapportée**, pas de reproduction indépendante réalisée par cet audit | Deuxième ingénieur : checkout d'un SHA figé, installation VM vierge, tests normaux, dégradés et audit des secrets |
| **FRAUD-002 [#50](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/50)** | Dossier `labs/FRAUD-002`, scripts/tests/docs ; issue ouverte, indique 83 tests Python et 39 assertions Newman, intégration Tazama→FRAUD-001 sur transactions synthétiques | **R2 — exécution rapportée**, revue indépendante explicitement en attente dans l'issue | Reproduire les tests, figer versions/images/licences, vérifier traces et capacités de reprise |
| **ISO 8583 [#41](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/41)** | Répertoire `labs/03-card-payments/OPB-D03-001` ; issue indique « prototype Go soumis », compilation et tests non confirmés | **R1 — prototype** | Exécuter `go test ./...` sur l'outil/le module approprié, documenter dépendances et cas négatifs |
| **Apache Fineract [#14](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/14)** | Issue ouverte, libellé « à concevoir / non validé » ; aucune recette consultée prouvant le déploiement | **R0 — non validé dans cet audit** | Identifier stack/version officielle et prérequis VM, installer, tester API fictive, conserver preuves |
| **Mojaloop [#21](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/21)** | Issue ouverte, libellé « à concevoir / non validé » ; aucune recette consultée prouvant le déploiement | **R0 — non validé dans cet audit** | Qualifier le profil de déploiement, ressources, distribution, services et test entre participants fictifs |

**Portée limitée** : ce tableau ne classe que cinq scénarios consultés. Les **73 autres propositions du catalogue élargi de 78** restent **non auditées** ici ; elles ne doivent pas recevoir automatiquement un état R0, R1, R2, R3 ou R4.

## Revue à faire avant une session de qualification L1–L2

1. **Choisir la référence exacte** : issue, branche, SHA, versions et fichiers de configuration sans secrets.
2. **Sécuriser un environnement neuf** : VM isolée, accès limité, aucune donnée réelle, aucun rail externe.
3. **Rejouer le build** : installer à partir du README et noter toute commande manquante.
4. **Rejouer les tests** : tests nominal, entrée invalide, rejet de sécurité, délai, reprise et duplication lorsque pertinents.
5. **Vérifier les invariants** : absence de double effet métier, cohérence d'état, écritures équilibrées si ledger.
6. **Conserver la preuve** : terminal/codes de sortie, date, versions, SHA, logs nettoyés et résultats observés.
7. **Auditer la supply chain** : licences réelles des dépendances, inventaire et vulnérabilités versionnées sans extrapoler.
8. **Faire relire** : un pair indépendant enregistre un verdict R3 avec réserves.
9. **Autoriser l'usage pédagogique** : R4 uniquement avec dossier complet et accord de l'équipe.

## Actions priorisées

| Ordre | Scénario | Motif |
|---|---|---|
| 1 | FRAUD-001 → revue R3 | Preuves déjà documentées : meilleur candidat au premier exercice de reproduction indépendante |
| 2 | ISO 8583 → construire R2 | Socle monétique de niveau initial ; compilation à confirmer |
| 3 | FRAUD-002 → revue R3 | Écosystème plus complexe, intégration et revue externe en attente |
| 4 | Fineract → R1/R2 | Préparer le core banking dans le parcours L1 |
| 5 | Mojaloop → R1/R2 | Prérequis d'infrastructure et intégration L2 à qualifier |

## Ce que cet audit ne démontre pas

- Aucune VM n'a été démarrée par cet audit ; aucun test de code exécuté en environnement réel.
- Aucune installation Fineract/Mojaloop nouvelle n'est confirmée.
- Aucun lab n'a été déclaré R3/R4 et aucune qualification de personne n'a été attribuée.
- L'utilisation de données synthétiques dans un lab ne prouve aucune homologation BCEAO, conformité PCI DSS ou certification EMV.

## Sources internes

[PR #102 parcours guidés](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/pull/102) · [issue pilote #94](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/94) · [FRAUD-001 #43](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/43) · [FRAUD-002 #50](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/50) · [ISO8583 #41](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/41) · [Fineract #14](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/14) · [Mojaloop #21](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/21).
