# 04 — Standards d'ingénierie applicables aux labs OSEF

## Definition of Ready (avant de coder)

- [ ] Issue GitHub unique, objectif, utilisateur et scénario métier définis.
- [ ] Référence projet/licence/version identifiée ; pas de duplication d'un lab existant.
- [ ] Architecture minimale, périmètre, hypothèses, dépendances et risques documentés.
- [ ] Données synthétiques, environnement isolé et commande de nettoyage définis.
- [ ] Tests attendus et critères mesurables identifiés.

## Architecture et Twelve-Factor (application pertinente)

- Configuration externalisée, pas de secrets committés ; builds reproductibles ; séparation du code, de la configuration et des données.
- Les services stateless peuvent être remplacés ; les **datastores** et systèmes de ledger sont explicitement persistants et sauvegardés.
- Logs structurés, corrélation, métriques ; ports explicites et contrôles de santé.
- Les applications ne doivent pas être artificiellement rendues sans état quand le métier impose un état transactionnel durable.
- Décrire timeouts, retries avec backoff, idempotence, outbox/inbox quand utile, compensations, dead-letter et états inconnus.
- Définir les invariants du ledger fictif : conservation du montant, absence de double écriture pour une commande idempotente et rapprochement des états.

## Structure conseillée d'un lab

```text
labs/<LAB-ID>/
  README.md           # objectif, prérequis, versions, commandes
  compose.yaml        # ou manifeste Kubernetes, si nécessaire
  .env.example        # variables sans secrets
  docs/architecture.md
  docs/adr-0001.md
  fixtures/synthetic/
  tests/
  scripts/setup.sh
  scripts/test.sh
  scripts/cleanup.sh
  evidence/README.md  # règles de collecte, pas de données sensibles
  LICENSES.md
```

## Definition of Done (documenté, distinct d'un déploiement)

- [ ] Script d'installation testé dans une VM ou runner propre.
- [ ] Cas nominal et au moins un cas négatif automatisés ; timeout/duplicate/retry si applicable.
- [ ] Versions/digests, hardware et variables documentés.
- [ ] Rapport daté : commande, résultat observé, commit SHA, journaux nettoyés.
- [ ] Tests sécurité, licences, dépendances et secrets contrôlés.
- [ ] Nettoyage et rollback documentés ; aucune connexion au réel.
- [ ] Relecteur indépendant a examiné code, limites et preuves.
- [ ] Statut GitHub cohérent : `proposé` / `en cours` / `testé` / `revue validée`.

## Revue de code

PR petites, message explicite, lien issue, tests reproductibles, analyse des risques et capture d'impact ; pas de fusion uniquement sur l'affirmation « marche chez moi ». CI bloquante lorsque les contrôles sont réellement installés. Documentation et code sont soumis aux mêmes exigences de preuve.

## Références

[The Twelve-Factor App](https://12factor.net/) · [OpenSSF](https://openssf.org/) · [GitHub documentation](https://docs.github.com/) · [Pilote de revue OSEF](../../roadmap/pilot-L1-L2/CONTRIBUTION-CHECKLIST.md).
