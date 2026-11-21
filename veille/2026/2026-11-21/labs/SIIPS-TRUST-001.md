# SIIPS-TRUST-001 — Fiabilité du parcours de paiement instantané

**Issue :** [#92](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/92) ; **source :** https://africanenda.org/siips/siips-report-2026 ; **statut :** proposé, non testé.

**Objectif :** confirmer que statut, notification au bénéficiaire, timeout, répétition et réclamation restent cohérents sur une API de paiement fictive.

**Prérequis :** VM Ubuntu ou Docker ; API et ledger simulés ; données synthétiques ; pytest ou équivalent ; horloge programmable ; système de logs.

**Étapes :**
1. Installer le simulateur et épingler les versions.
2. Exécuter confirmation positive, bénéficiaire inconnu, timeout, réclamation.
3. Répéter l'identifiant d'une transaction ; redémarrer le simulateur pendant un état intermédiaire.
4. Comparer statuts visibles, écritures du ledger fictif, notifications, dossiers de recours.

**Succès :** zéro double imputation dans le simulateur, traces corrélées, scénarios négatifs reproductibles, PII absentes, documentation et résultats datés.

**Réutilisation :** PAYMENT-001 #44, MOJA-REGRESSION #62, OPB-015 #35, OPB-016 #36 ; aucun branchement PI-SPI réel.

**Meetup :** « Paiements instantanés : confiance et recours » ; ingénieurs PSP/banques, conformité, QA ; 60 min, démo des quatre scénarios. Aucun meetup programmé.
