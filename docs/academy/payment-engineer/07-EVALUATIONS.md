# 07 — Évaluation et qualification interne OSEF

> **Proposition de gouvernance pédagogique**, pas de dispositif RH ou certification officielle actuellement en vigueur.

## Étapes

1. **Pré-évaluation** : candidat documente ses prérequis et ses lacunes ; une expérience antérieure peut être reconnue après vérification.
2. **Choix des labs** : les évaluateurs sélectionnent des labs réellement exécutables et adaptent l'épreuve au niveau.
3. **Exécution** : environnement vierge, code/version épinglés, données synthétiques, tests consignés.
4. **Revue** : évaluateur indépendant reproduit les scénarios et vérifie les preuves.
5. **Décision** : `pending`, `rework`, `qualified-internal`. Les écarts sont commentés, sans jugement personnel.
6. **Réévaluation** : possibilité de corriger et resoumettre.

## Barème de référence

| Critère | Points |
|---|---:|
| Reproductibilité | 25 |
| Exactitude et tests fonctionnels | 25 |
| Résilience et diagnostic | 20 |
| Sécurité / licences / confidentialité | 20 |
| Documentation et contribution | 10 |
| **Total** | **100** |

**Seuil indicatif :** 80/100 et zéro défaut critique ; validation indépendante obligatoire. Ce seuil est une proposition documentée, pas un niveau déjà attribué.

## Défauts critiques

Double imputation non maîtrisée dans l'exercice d'idempotence ; fuite de secrets ou données réelles ; preuve inventée ; dépendance illégitime ; incapacité à reproduire un résultat revendiqué.

## Artefacts

Issue et PR, rapport de tests daté, digests et SHA, captures sans PII, grille notée, commentaires de revue, décision et limites. Ne pas publier de dossiers personnels de candidats dans un dépôt public.

**Références :** [grille officielle du pilote interne (proposée)](../../roadmap/pilot-L1-L2/RUBRIC.md), [programme L1-L4](../../roadmap/OSEF-PAYMENT-ENGINEER-QUALIFICATION.md), [pilote #94](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/94).
