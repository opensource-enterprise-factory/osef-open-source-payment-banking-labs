# 06 — Contribution open source, mentorat et collaboration OSEF

## Manière de travailler

1. **Observer** : lire README, CONTRIBUTING, SECURITY, licence et issues mainteneurs.
2. **Reproduire** : écrire un test minimal avec données fictives et versions figées.
3. **Discuter** : ne pas créer de PR de grande taille sans comprendre les attentes du projet.
4. **Proposer** : issue upstream claire ou patch/test/doc avec justification et preuves.
5. **Faire relire** : corrections, CI, respect de la licence et des conventions.
6. **Suivre** : l'acceptation, le refus ou l'attente ne doivent jamais être inventés.

## Modes de contribution autorisés

Documentation, traduction si acceptée upstream, tests, exemples de contrats, reproduction d'anomalie, benchmarks reproductibles, outils de déploiement et code correctif.

## Revue entre ingénieurs

- Le mentor aide à isoler le problème ; **il ne signe pas à la place du candidat**.
- Le relecteur vérifie : exactitude, sécurité, idempotence, reproductibilité, licence et clarté.
- Les demandes de changements sont explicites, limitées et vérifiables ; l'ingénieur documente la résolution.
- Favoriser une réunion courte pour les blocages, puis capitaliser la solution dans une issue/ADR.
- Les responsables et mentors restent **à désigner** ; ne pas présumer la disponibilité de personnes.

## Étiquette des contributions

Éviter les issues vagues, les benchmarks biaisés, les annonces prématurées et la copie de codes ou spécifications non redistribuables. Ne pas pousser de secrets, données clients ou résultats fabriqués.

## Fiche de contribution

```yaml
osef_lab: null
upstream_project: null
upstream_repository: null
problem: null
reproduction_commit: null
issue_url: null
pr_url: null
status_verified: proposed
review_date: null
source_link: null
```

**Registre :** [OSEF Upstream Contributions](../../roadmap/OSEF-UPSTREAM-CONTRIBUTIONS.md). L4 exige une interaction upstream vérifiable mais pas obligatoirement une PR fusionnée.
