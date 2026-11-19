# FIN-20261119-04 — Mojaloop : activité des dépôts et qualification des changements

- **Veille :** 19 novembre 2026
- **Date de l'activité observée dans la veille :** 18 novembre 2026
- **Acteur :** Mojaloop / GitHub
- **Statut :** activité de dépôts signalée, portée des commits et éventuelle release non confirmées
- **Tags :** `veille`, `Mojaloop`, `payment-switch`, `regression`, `instant-payments`, `afrique-francophone`
- **Source primaire à examiner :** https://github.com/mojaloop

## Faits et réserves
La veille du 19 novembre a relevé des mises à jour de projets tels que `central-ledger`, `documentation` et `iac-modules` le 18 novembre. Cette fiche **ne qualifie pas les changements comme nouvelles fonctionnalités, corrections de sécurité ou nouvelle release**, faute de comparaison des commits/version tags.

## Ce qui change
Signal d'activité d'ingénierie à suivre. La portée opérationnelle ne doit pas être déduite d'une simple date de mise à jour du dépôt.

## Intérêt pour l'Afrique francophone
Pour les switches, banques et PSP évaluant des composants open source de paiements interopérables : besoin de qualification des versions, de régression, de fiabilité et d'observabilité.

## Action OSEF
Comparer les SHAs, les notes de release, le changelog et les tests avant d'annoncer une amélioration.

## Lab proposé (non créé) — LAB-MOJA-REGRESSION
- **Objectif :** mettre en œuvre un cycle de tests de non-régression sur un sandbox Mojaloop.
- **Prérequis :** Docker/Kubernetes selon upstream, Git, connaissances switching/clearing, environnement isolé, Mojaloop Testing Toolkit (TTK).
- **Étapes :** figer commit/versions ; déployer stack de test officielle ; exécuter un transfert nominal, un refus et un timeout ; recueillir preuves ; comparer deux versions lorsque documentées.
- **Critère de succès :** rapport comparatif reproductible avec SHAs, logs expurgés et limites identifiées.

## Meetup proposé (non créé) — MEETUP-MOJA-OPS
**« Qualifier une évolution de switch open source »** ; public PSP, switches, SRE et architectes paiement ; format 60 minutes, démonstration de tests TTK sur transactions fictives.

## Suivi
- [ ] Relever la liste exacte des commits et tags (dates et SHAs)
- [ ] Vérifier la présence d'une release de sécurité ou fonctionnelle
- [ ] Sélectionner la version de test et les ressources du lab
- [ ] Vérifier licences et dépendances
- [ ] Faire relire le scénario métier avant ouverture d'un lab
