# Évaluation proposée du tronc commun OSEF

**Version 0.1 — proposition de barème, non certifiant et non approuvé par une instance pédagogique.**

## Grille sur 100 points

| Domaine | Points | Preuve demandée |
|---|---:|---|
| Outillage, Git et reproductibilité | 10 | Versions, commandes, PR et README |
| Réseaux, contrats d'API et erreurs | 20 | Contrat versionné, tests valides/invalides |
| Fondamentaux du paiement | 15 | Acteurs, flux, états et limites du lab |
| Données, cohérence et idempotence | 15 | Invariants et cas de doublon, données fictives |
| Sécurité, IAM et confidentialité | 15 | Modèle de menace, accès refusé, logs expurgés |
| Tests, incidents et reprise | 15 | Cas réellement exécutés et runbook |
| Architecture, licences et revue | 10 | BDAT, ADR, sources et feedback |
| **Total** | **100** | |

**Seuil expérimental suggéré :** 70/100, **zéro violation de sécurité** et publication de résultats vérifiables. Il ne doit pas être utilisé comme certification avant approbation de la gouvernance OSEF.

## Livrable de synthèse

Dossier :
- issue/PR et pseudo GitHub du contributeur ;
- choix du langage/outillage et versions exactes ;
- architecture, contrat API et données fictives ;
- scripts commentés et instructions d'exécution ;
- scénarios : succès, refus, doublon, timeout et résolution ;
- captures/logs expurgés, erreurs rencontrées et correctifs ;
- décision ADR, licence et revue indépendante si possible.

## Statuts de progression
`Proposé → Soumis → Testé → Revu → Validé en laboratoire`.

**Une fiche publiée ne vaut pas évaluation accomplie.** « Validé en laboratoire » ne signifie ni homologué, ni apte à la production.

[Tronc commun](README.md) · [Sécurité](../../../SECURITY.md) · [Contributing](../../../CONTRIBUTING.md)
