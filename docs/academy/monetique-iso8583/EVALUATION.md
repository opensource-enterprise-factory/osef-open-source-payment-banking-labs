# OSEF Academy — Grille d'évaluation du parcours ISO 8583

**Statut : proposition v0.1 — 17 novembre 2026.** À faire approuver avant utilisation comme validation communautaire. Ce document ne délivre pas une certification.

## Dossier de preuves à produire
- Lien GitHub vers le travail et vers l'issue ou la PR.
- Version de l'outil, spécification ISO 8583 retenue, licence et source consultée.
- Commandes exécutées, résultats réels, environnement, date.
- Jeu de données 100 % fictives et captures/logs expurgés.
- Schémas et contrats, cas nominaux, négatifs et limites.
- Rapport de revue indépendante si disponible.

## Barème proposé — 100 points

| Critère | Maximum | Comment attribuer |
|---|---:|---|
| Fondamentaux métiers et acteurs | 15 | Flux précis, distinctions des rôles et limites |
| Compréhension ISO 8583 / spécification | 20 | MTI/bitmap/champs et encodage justifiés |
| Code et reproductibilité | 20 | Version figée, installation claire, tests réellement exécutés |
| Cas d'erreur et comportement | 20 | Rejet, troncature, doublons/timeout selon l'exercice, états cohérents |
| Sécurité et observabilité | 15 | Données synthétiques, logs expurgés, threat model |
| Documentation et revue | 10 | README, PR, commentaires et restitution honnête |
| **Total** | **100** | |

**Seuil expérimental proposé :** 70/100 et **aucune violation de sécurité** ; non applicable tant que la gouvernance pédagogique n'a pas validé le barème. Une erreur grave de sécurité doit suspendre l'évaluation indépendamment du score.

## Échelle de preuves
- **Non commencé** : pas de livrable.
- **Soumis** : artefact accessible, mais non vérifié.
- **Reproductible** : exécution testée avec résultats consignés.
- **Revu** : contrôle indépendant documenté.
- **Validé en lab** : critères acceptés par un référent explicitement désigné, sans portée de production.

## Modèle de restitution

```text
Fiche : OSEF-MON-XX
Contributeur (pseudo) :
Issue / PR :
Date / environnement :
Version Go / bibliothèque / spec :
Commandes réellement exécutées :
Tests réussis / tests échoués / tests non exécutés :
Constats et mesures :
Risques de sécurité / licence :
Relecteur et lien de revue (si confirmé) :
Statut : non commencé / soumis / reproductible / revu / validé en lab
Prochaine correction :
```

## Cas d'échec qui doivent être documentés
- Une dépendance ou un import ne compile pas.
- Une spécification ne reconnaît pas un champ attendu.
- Un message tronqué est accepté alors qu'une erreur était attendue.
- Un message fictif est journalisé sans précaution.
- Un délai dépassé est assimilé à un refus définitif sans justification.
- Un statut « validé » est revendiqué sans preuve.

Le devoir d'un ingénieur est aussi de **démontrer ce qu'il ne peut pas encore confirmer**.

[Retour au parcours](README.md) · [Politique de sécurité](../../../SECURITY.md) · [Guide de contribution](../../../CONTRIBUTING.md)
