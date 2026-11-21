# OSEF — Modèle de procès-verbal de reproduction d'un lab

> À remplir avec **observations réellement exécutées** ; ce fichier est un modèle vierge. Ne pas publier d'informations privées ou secrets dans un dépôt public.

## Identification

- Lab / issue :
- Date et fuseau :
- Réviseur indépendant (identifiant GitHub professionnel ou pseudonyme autorisé) :
- Commit Git SHA :
- Versions des images/dépendances :
- OS/CPU/RAM/disque et ressources réellement observées :
- Profil réseau et restrictions :

## Commandes et cas de tests

| Étape | Commande exacte (sans secret) | Attendu | Observé / code retour | Preuve expurgée |
|---|---|---|---|---|
| Installation | | | | |
| Service sain | | | | |
| Nominal | | | | |
| Entrée invalide / rejet | | | | |
| Timeout / retry | | | | |
| Sécurité / accès | | | | |
| Restauration / nettoyage | | | | |

## Invariants pertinents

- [ ] Aucune double imputation suite à répétition de commande, **si applicable**
- [ ] Écritures fictives équilibrées, **si ledger**
- [ ] Statuts terminaux et erreurs expliqués
- [ ] Secrets absents des logs et fichiers livrés
- [ ] Dépendances et licences vérifiées
- [ ] Nettoyage et réexécution documentés

## Décision

- Niveau : R0 / R1 / R2 / R3 / R4
- **R3** requiert reproduction effective et revue indépendante.
- **R4** requiert en outre acceptation pédagogique documentée.
- Décision : pending / rework / approved
- Réserves :
- Liens vers logs/tests/PR :
- Signature ou approbation GitHub du relecteur :
