# OSEF-ENG-012 — Matrice Twelve-Factor : osef-open-source-payment-banking-labs

> **Évaluation initiale : non réalisée (NE)**. Cette matrice documente le plan de vérification ; aucun test n'est réputé réussi par sa création. C = Conforme ; NC = Non conforme ; NA = Non applicable motivé ; NE = Non évalué.

**Cible :** laboratoire/prototype uniquement à ce stade.  
**Référence :** [OSEF-ENG-012](https://github.com/opensource-enterprise-factory/.github/blob/main/docs/engineering/OSEF-ENG-012.md)  
**Responsable de revue :** à désigner  
**Commit et date d'évaluation :** à renseigner

| Facteur | Statut (C/NC/NA/NE) | Preuve observée | Action / limites |
|---|---|---|---|
| 01 Codebase | NE | À joindre | Vérifier dépôt, IaC et reproductibilité |
| 02 Dependencies | NE | À joindre | Vérifier pinning, digests, licences |
| 03 Config | NE | À joindre | Vérifier configuration externe et secrets |
| 04 Backing services | NE | À joindre | Vérifier interfaces, dépendances, persistance |
| 05 Build, release, run | NE | À joindre | Vérifier build / promotion / déploiement |
| 06 Processes | NE | À joindre | Distinguer processus et services persistants |
| 07 Port binding | NE | À joindre | Ports et exposition vérifiés |
| 08 Concurrency | NE | À joindre | Limites et tests de charge |
| 09 Disposability | NE | À joindre | Démarrage, arrêt, reprise |
| 10 Dev/prod parity | NE | À joindre | Écarts lab/prod documentés |
| 11 Logs | NE | À joindre | Logs, collecte, protection données |
| 12 Admin processes | NE | À joindre | Administration traçable et reproductible |

## Adaptation au projet

**Payment & Banking Labs / FRAUD (PSP, relay, Tazama) :** séparer l'état des moteurs/bases, isoler les ports du laboratoire, vérifier clés/API, logs d'audit, transactions simulées, tests 401/409/422, idempotence, arrêt/reprise et rollback. Aucune transaction ou donnée bancaire réelle par défaut. Volet métier + meetup obligatoire au parcours du lab.

## Exceptions et remédiations

Aucune exception approuvée recensée dans cette matrice. Ouvrir une issue pour tout NC/NA et suivre la [procédure d'exception](https://github.com/opensource-enterprise-factory/.github/blob/main/docs/engineering/EXCEPTIONS.md).

## Trace de revue

- [ ] Évaluation technique effective avec commandes, preuves et résultat
- [ ] Revue indépendante
- [ ] Risques métier documentés
- [ ] Mini-présentation / meetup : enseignements, limites et contribution upstream possibles

**Ce document ne constitue pas une attestation de conformité ni de préparation à la production.**
