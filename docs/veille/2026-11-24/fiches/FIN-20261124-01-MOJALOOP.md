# FIN-20261124-01 — Mojaloop : qualification des évolutions upstream

**Édition :** 24 novembre 2026. **Nature :** signal technique **non encore vérifié à la précision du commit**.

## Faits et limites
La veille initiale a mentionné des modifications de plusieurs composants Mojaloop entre les 20 et 22 novembre (SDK Scheme Adapter, ML API Adapter, TTK, etc.). Lors du contrôle de publication, la [page officielle de l'organisation Mojaloop](https://github.com/mojaloop) était accessible mais renvoyait un contenu indexé ancien : **elle ne prouve pas les dates, l'existence de commits précis, ni la publication de nouvelles releases les 20–24 novembre**. Ne pas reprendre la liste des dépôts mis à jour comme fait confirmé sans examiner leurs historiques directs.

- Source upstream : https://github.com/mojaloop
- Catégorie : **à vérifier**, pas « nouvelle release », pas déploiement.
- Domaine A : switching, API, clearing/settlement, idempotence.
- Limite : aucune adoption régionale ou homologation BCEAO déduite.

## Action OSEF — extension du lab existant
[MOJA-REGRESSION-001 #62](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/62), sans nouvelle issue en doublon.

**Objectif :** qualifier chaque changement upstream réellement identifié avant de modifier le laboratoire.

**Prérequis :** Git, Docker, Mojaloop TTK, environnement isolé de PSP fictifs, références des commits et versions figées.

**Étapes**
1. Inspecter les dépôts composants et relever SHA, date réelle du commit, PR de fusion et tag/release éventuel.
2. Comparer le comportement avant/après sur tests TTK synthétiques.
3. Tester nominal, timeout, rejeu, annulation, rapprochement, reprise.
4. Archiver journaux, écarts, limites et conditions de reproductibilité.

**Validation :** SHA et versions traçables ; zéro doublon sur scénarios sélectionnés ; régressions documentées ; pas d'accès à la production.

## Meetup
[MOJA-REGRESSION #65](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/65) — « Tester une évolution de switch avant déploiement » ; 75 min, PSP/ingénieurs paiement ; démo sous réserve de lab validé.

**Business :** audit de fiabilité et recette d'intégration, **offre exploratoire sans client confirmé**.
