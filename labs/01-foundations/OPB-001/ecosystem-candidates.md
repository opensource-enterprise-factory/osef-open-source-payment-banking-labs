# OPB-001 — Catalogue initial de projets candidats

**Statut : repérage, pas validation technique.** Vérifier la licence du **composant précis** et les conditions des éventuelles éditions commerciales. Projets, fondations, standards et outils transversaux ne sont pas interchangeables.

| Domaine | Candidat | Source initiale / dépôt à examiner | Statut | Points à vérifier |
|---|---|---|---|---|
| D01 | Apache Fineract | https://github.com/apache/fineract | Partiellement vérifié | Versions et processus amont actuels (voir project-matrix.md) |
| D01–D02 | Mifos | https://mifos.org/ | Candidat | Dépôt exact, fonctionnalités, licences |
| D02 | Apache Fineract (produits de crédit/épargne) | https://fineract.apache.org/ | Candidat par domaine | Fonctions précises selon version |
| D03 | jPOS | https://github.com/jpos/jPOS | Candidat | Licence par module, options commerciales, contribution |
| D03 | Moov ISO8583 | https://github.com/moov-io/iso8583 | Candidat | Licence et prise en charge des variantes ISO 8583 |
| D04 | Mojaloop | https://mojaloop.io/ | Candidat | Dépôts modules, licences, versions et guide contributeurs |
| D05 | Mojaloop (cas d'usage wallet/participants) | https://docs.mojaloop.io/ | Candidat par domaine | Couverture fonctionnelle réelle |
| D06 | Open Bank Project | https://www.openbankproject.com/ | Candidat | Licence des dépôts, offre open core, périmètre gratuit |
| D06 | FINOS | https://www.finos.org/projects | Écosystème / fondation | Sélectionner des projets précis, licences projet par projet |
| D07 | TigerBeetle | https://github.com/tigerbeetle/tigerbeetle | Candidat | Modèle de comptes et journal; licences, intégrations |
| D07 | Formance Ledger | https://github.com/formancehq/ledger | Candidat | Licence par version, fonctions ouvertes et commerciales |
| D08 | Mojaloop (scénarios de transfert) | https://mojaloop.io/ | Candidat par domaine | Applicabilité réelle aux remittances |
| D09 | Moov ACH | https://github.com/moov-io/ach | Candidat | Format ACH américain; **ne pas supposer** compatibilité UEMOA |
| D09 | Projets ISO 20022 à rechercher | https://www.iso20022.org/ | Standard / recherche | Le standard ISO 20022 n'est pas en soi un projet Open Source |
| D10 | Keycloak / Open Policy Agent | https://www.keycloak.org/ ; https://www.openpolicyagent.org/ | Briques transversales | Cas d'usage conformité, aucune homologation implicite |
| D11 | Hyperswitch | https://github.com/juspay/hyperswitch | Candidat | Licence et fonctionnalités de chaque édition |
| D12 | Kill Bill | https://github.com/killbill/killbill | Candidat | Licence, plugins paiement et périmètre de facturation |
| D13 | Apache Kafka / Flink / Superset | https://projects.apache.org/ | Briques transversales | Sélectionner dépôts et versions exactes |
| D14 | Kubernetes / OpenTelemetry / Prometheus | https://landscape.cncf.io/ | Briques transversales | Pertinence par architecture et exploitation bancaire |

## Ce qui n'est pas encore démontré

- L'exhaustivité des solutions par domaine et l'absence de doublons.
- La compatibilité d'un projet avec les schémas interbancaires UEMOA.
- La conformité réglementaire, PCI DSS ou la sécurité opérationnelle.
- La disponibilité actuelle d'issues débutants et l'accueil des contributions.
- Les performances et la pertinence pour la production.

## Prochaine recherche

Prioriser une fiche vérifiable pour **jPOS**, **Moov ISO8583**, **Mojaloop**, **Mifos** et **Hyperswitch** puis augmenter progressivement la couverture des 14 domaines. Documenter chaque vérification dans evidence.md.
