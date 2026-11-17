# OSEF Academy — Catalogue des 21 fiches de cours détaillées

**Version pédagogique proposée v0.2 — 17 novembre 2026**  
Ce document organise la correspondance **compétence → cours → chapitres → architecture BDAT → TP → preuve d'évaluation**.

> **État :** 21 fiches de syllabus approfondi sont présentes dans le dépôt, avec objectifs, chapitres, travaux dirigés et critères. Elles **ne signifient pas** que 21 cours ont été dispensés, que des vidéos et supports complets existent, que les labs passent, ou que les compétences sont certifiées. Les documents OPPL confidentiels ne sont pas réutilisés.

## Tronc commun — 7 cours

| Code | Cours | Point d'entrée pratique |
|---|---|---|
| TC-01 | [Environnement, Git et reproductibilité](tronc-commun/TC-01-SYSTEMES-ET-GIT.md) | [TC-01](../../labs/common-core/TC-01.md) |
| TC-02 | [Réseaux, API et contrats](tronc-commun/TC-02-RESEAUX-API-ET-CONTRATS.md) | [TC-02](../../labs/common-core/TC-02.md) |
| TC-03 | [Acteurs et cycle du paiement](tronc-commun/TC-03-METIERS-ET-CYCLE-PAIEMENT.md) | [TC-03](../../labs/common-core/TC-03.md) |
| TC-04 | [Données, ledger et cohérence](tronc-commun/TC-04-DONNEES-ET-COHERENCE.md) | [TC-04](../../labs/common-core/TC-04.md) |
| TC-05 | [IAM, sécurité et confidentialité](tronc-commun/TC-05-SECURITE-ET-CONFIANCE.md) | [TC-05](../../labs/common-core/TC-05.md) |
| TC-06 | [Tests et résilience](tronc-commun/TC-06-QUALITE-ET-RESILIENCE.md) | [TC-06](../../labs/common-core/TC-06.md) |
| TC-07 | [Architecture BDAT et Open Source](tronc-commun/TC-07-ARCHITECTURE-ET-OPEN-SOURCE.md) | [TC-07](../../labs/common-core/TC-07.md) |

## Spécialisation A — Ingénieur monétique (6 cours)

| Code | Cours | Lab et architecture |
|---|---|---|
| MON-01 | [Acteurs et flux monétiques](monetique-iso8583/01-ECOSYSTEME-ET-FLUX.md) | ARC-02 B ; OPB-D03-001 |
| MON-02 | [Structure ISO 8583](monetique-iso8583/02-STRUCTURE-MESSAGE-ISO8583.md) | ARC-02 D ; OPB-D03-001 |
| MON-03 | [Programmation Go ISO8583](monetique-iso8583/03-PACK-UNPACK-GO.md) | ARC-02 A/T ; OPB-D03-001 |
| MON-04 | [Erreurs et états incertains](monetique-iso8583/04-CAS-NEGATIFS-ET-ETATS.md) | ARC-02 D/A ; OPB-D03-001 |
| MON-05 | [Sécurité et observabilité](monetique-iso8583/05-SECURITE-ET-OBSERVABILITE.md) | ARC-08 ; OPB-D03-001 |
| MON-06 | [Intégration et revue](monetique-iso8583/06-INTEGRATION-ET-REVUE.md) | ARC-10 ; OPB-D03-001 |

**Attention :** l'exécution et les tests du prototype Go OPB-D03-001 ne sont pas confirmés par des preuves consultées.

## Spécialisation B — Paiements numériques et interopérabilité (8 cours)

| Code | Cours | Architecture cible |
|---|---|---|
| PNI-01 | [Acteurs et cycles](paiements-numeriques-interoperabilite/01-ACTEURS-ET-CYCLE.md) | ARC-03 |
| PNI-02 | [API de paiement fictive](paiements-numeriques-interoperabilite/02-API-PAIEMENT.md) | ARC-05 |
| PNI-03 | [Wallet et ledger](paiements-numeriques-interoperabilite/03-WALLET-ET-LEDGER.md) | ARC-04 / ARC-06 |
| PNI-04 | [Interopérabilité](paiements-numeriques-interoperabilite/04-INTEROPERABILITE.md) | ARC-03 |
| PNI-05 | [Événements et orchestration](paiements-numeriques-interoperabilite/05-EVENEMENTS-ET-ORCHESTRATION.md) | ARC-07 / ARC-10 |
| PNI-06 | [Sécurité des API](paiements-numeriques-interoperabilite/06-SECURITE.md) | ARC-05 / ARC-08 |
| PNI-07 | [Observabilité et résilience](paiements-numeriques-interoperabilite/07-RESILIENCE.md) | ARC-09 |
| PNI-08 | [Projet final simulé](paiements-numeriques-interoperabilite/08-CAPSTONE.md) | ARC-03 / ARC-05 / ARC-06 / ARC-09 / ARC-10 |

## Standard minimum du cours OSEF

Chaque fiche doit désormais documenter :
1. la compétence attendue et les prérequis ;
2. les objectifs mesurables et les chapitres à enseigner ;
3. la lecture guidée des vues Business, Data, Application et Technology ;
4. les travaux pratiques et leur environnement fictif ;
5. une épreuve avec critères vérifiables, scénarios positifs et négatifs ;
6. les sources, versions et limites, ainsi que les preuves observées.

**Trois niveaux de maturité à distinguer :**
- **Cours documenté :** objectifs, syllabus et exercices rédigés.
- **Cours enseignable :** exemples contrôlés, supports prêts et labs vérifiés.
- **Compétence évaluée :** exécution, relecture et décision tracées pour un apprenant.

À ce stade, nous sommes au niveau **cours documenté** ; le passage à « cours enseignable » nécessite d'exécuter les labs et de contrôler les supports.

## Travaux complémentaires à faire avant pilote
- S'assurer que chaque environnement et dépendance est reproductible.
- Mettre à disposition les supports d'explication détaillés et corrigés d'exercices.
- Vérifier les tests réels et corriger les échecs.
- Définir les responsables pédagogiques, les reviewers, les règles de notation et la confidentialité.
- Mesurer effectivement les durées lors d'une cohorte pilote.

[Parcours général](PARCOURS-INGENIEUR-MONETIQUE-PAIEMENT-OSEF.md) · [Matrice compétence ↔ cours](CORRESPONDANCE-COMPETENCES-COURS.md) · [Matrice compétence × BDAT × lab](MATRICE-COMPETENCES-BDAT-LABS.md) · [Preuves](MODELE-PREUVE-COMPETENCE.md)

**EN:** Twenty-one detailed proposed course syllabi across a shared foundation and two specializations. Outlines are documented; delivery and skills validation have not yet occurred.
