# 03 — Parcours d'apprentissage et de progression

## L0 — Orientation (facultatif, pré-L1)

**But :** savoir ce qu'est un paiement et préparer son environnement.

- Comprendre banque/PSP/EME, payeur/bénéficiaire, différence autorisation/clearing/settlement.
- Installer Git, Docker ou outil de conteneur retenu, Go ou Java selon filière et client HTTP.
- Créer un dépôt de travail, exécuter un test simple, rédiger un README.
- Distinguer open source, source-available, standards et produits propriétaires.
- **Gate :** VM propre, procédure de démarrage reproduite, premiers messages fictifs.

## L1 — Foundation

- **Étudier :** ISO 8583, ISO 20022 (notions), architecture Mojaloop, fonctions Fineract, API/JSON, Linux et journaux.
- **Labs recommandés :** OPB-001 #12 ; ISO8583 #41 ; Fineract #14 ; Mojaloop #21.
- **Preuve :** message ISO 8583 synthétique analysé, erreurs expliquées, déploiement vérifié depuis une VM propre et journal de preuves.
- **Gate :** conformité au référentiel de qualité et revue indépendante.

## L2 — Payment Integrator

- **Étudier :** routage, ledger, quotes, statut transaction, reversal, réconciliation, sécurité API, idempotence.
- **Labs :** PAYMENT-001 #44, MOJA-REGRESSION #62, Fineract–Mojaloop #27, SIIPS-TRUST #92.
- **Preuve :** parcours nominal, rejet, expiration et reprise démontrés sur environnement fictif, sans double débit selon le scénario.
- **Gate :** tests automatiques exécutés, traces corrélées et rapport d'écart.

## L3 — Payment Reliability & Security

- **Étudier :** ISO 20022 approfondi, clearing/settlement, CI/CD, vulnérabilités, observabilité, tests de charge et chaos, sécurisation des dépendances.
- **Labs candidats :** CORE-005/006, RAIL-006/007, SEC-003/004, SRE-002/003 dans le [catalogue](../../roadmap/OSEF-PAYMENT-LABS-CATALOGUE-2026-11-21.md).
- **Preuve :** reprise après incident, mesure des écarts et démonstration de remédiation.

## L4 — Upstream Contributor / mentor

- **But :** produire des améliorations utiles aux projets : tests, correctifs ou documentation ; assurer une revue de qualité.
- **Preuve :** lien vers issue/PR **réellement** publié chez le mainteneur et échanges suivis ; l'acceptation n'est jamais supposée.

## Séquence type pour chaque lab

1. **Lire** : problème métier et documentation officielle.
2. **Modéliser** : séquence, états, risques et hypothèses.
3. **Installer** : versions figées, données synthétiques.
4. **Tester** : succès, refus, timeout, doublon et reprise selon le périmètre.
5. **Mesurer** : logs, métriques, traces, écarts.
6. **Documenter** : environnement, résultats réels et limites.
7. **Faire relire** : second ingénieur, demandes de correction, validation datée.
8. **Contribuer** : tests/docs upstream si le besoin est avéré.

## Quand je suis bloqué

- **Installation :** vérifier digest, OS, dépendances, variables et ports ; copier erreur sans secrets dans l'issue.
- **Tests :** distinguer erreur de configuration, écart de contrat et bug ; produire une reproduction minimale.
- **Protocole :** consulter la référence normative accessible/licite et les docs officielles avant d'inférer un comportement.
- **Conception :** écrire la décision d'architecture (ADR) et soumettre une alternative en revue.
- **Disponibilité d'un mentor :** demander une revue asynchrone sur issue ; ne jamais présumer l'affectation d'une personne.
- **Réglementation :** consigner « à vérifier » auprès de l'autorité compétente ; ne pas transformer une hypothèse en exigence validée.

**Travaux suivis par :** [pilote #94](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/94).
