# MOJA-TIMEOUT-001 — Expiration et idempotence du central-ledger

**Extension de :** [#62](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/62), sans nouvelle issue. **Source officielle :** https://github.com/mojaloop/central-ledger/commit/7e11fdaa11e58dc2902021c0e1df1a1e25b5e16e

**Objectif :** reproduire expiration avant réservation, timeout-reserved répété et redémarrage contrôlé du composant dans une instance test.

**Prérequis :** Docker/Compose, version épinglée et identifiée de Mojaloop central-ledger, TTK ou client de test compatible, participants fictifs, journaux.

**Étapes :**
1. Documenter la révision et les API réellement disponibles.
2. Configurer un scénario expiration avant réservation.
3. Émettre plusieurs fois le même timeout et injecter un redémarrage.
4. Comparer états, notifications, écritures et logs ; exécuter un baseline autorisé si disponible.

**Succès :** absence de double réservation/transition sur les cas testés ; état final vérifiable, logs et scripts de rejouabilité. Si l'environnement ne permet pas de tester le cas, rapporter « non testé », jamais « validé ».

**Meetup :** rattacher à [#65](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/65) ; 75 min, démonstration de non-régression et traitement d'échec.
