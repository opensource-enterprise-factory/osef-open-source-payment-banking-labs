# FRAUD-003 — Corrélation fédérée et investigation entre trois institutions fictives

> **Statut : cadrage Gates 0/1 et code Gate 2 proposés dans une PR en brouillon. Le code FRAUD-003 n'a pas encore été exécuté ni validé sur la VM.** Seules des données synthétiques sont autorisées ; il ne s'agit pas d'une implémentation OFTA officielle.

**Issue de référence :** [#63 — FRAUD-003](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63). **Meetup associé :** [#66](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/66).

## Journal d'exécution et preuves

Le [journal vivant du Gate 0 et des sessions suivantes](JOURNAL-EXECUTION-ET-PREUVES.md) conserve les sorties terminal réellement reçues, les statuts vérifiés, les limites et les incidents ouverts. **Tout résultat de test doit y être consigné au fur et à mesure, via une PR GitHub, jamais par édition manuelle sur la VM.**

## Formation et transmission — standard OSEF

**Chaque Gate couvre obligatoirement les dimensions technique, métier et meetup.** Le [parcours intégré des neuf Gates (0 à 8)](PARCOURS-TECHNIQUE-METIER-MEETUP.md) définit pour chaque jalon l'apprentissage, la preuve, la vulgarisation et la règle de clôture. Le kit de meetup est obligatoire avant la clôture du lab, mais la tenue de l'événement public peut être ultérieure.

## Commencer dans le bon ordre

1. [Gate 0 — dépendances, contrats et preuves FRAUD-001/FRAUD-002](GATE-0-DEPENDANCES-ET-PREUVES.md) : distingue les succès réellement observés, les limites et les interfaces restant à valider avant réutilisation.
2. [Gate 1 — gouvernance et contrats proposés](GATE-1-GOUVERNANCE-ET-CONTRATS.md) : rôles Banque A / PSP B / Mobile Money C, politique de minimisation, matrice d'accès, schémas JSON synthétiques, critères d'essai et arbitrages à approuver.
3. [Gate 2 — Simulateurs et protocole de recette](GATE-2-SIMULATEURS-ET-RECETTE.md) : API distincte pour trois identités fictives, clés propres, SQLite isolé, tests d'accès ; **code proposé non fusionné et non exécuté**.
4. **Gates suivants (non démarrés)** : proposer une corrélation explicable, ouvrir un dossier d'investigation, corriger un faux positif, démontrer audit et erreurs.

## Préconditions non négociables

- FRAUD-001 et FRAUD-002 sont des **dépendances de conception**, pas des preuves que FRAUD-003 est fonctionnel.
- La revue indépendante de FRAUD-002 [#50](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/50) reste ouverte.
- Le service FRAUD-001 existant a deux PSP simulés et **ne garantit pas** une isolation multi-institution FRAUD-003.
- Ne pas injecter de données réelles, exposer de secrets, faire de blocage automatique ni confondre alerte et fraude confirmée.
- Modifications du code/configuration exclusivement via **GitHub branch → PR → revue → merge**, puis synchronisation VM avec `git pull --ff-only`. Aucun fichier modifié à la main sur Ubuntu.

## Suivi des validations

- [x] Gates 0/1 : documents préparés en PR.
- [ ] Gate 0 : vérification indépendante du code et des contrats effectifs.
- [ ] Gate 1 : approbation des rôles, du partage et des exemples de schéma par les référents.
- [x] Gate 2 : première implémentation versionnée et tests écrits (PR, **non exécutés**).
- [ ] Gate 2 : tests exécutés, preuves sur VM et revue validée.
- [ ] Gates 3+ : corrélation, investigation, révocation, sécurité et démonstration.

Les cases cochées décrivent uniquement les **livrables de cadrage**, pas une recette technique.
