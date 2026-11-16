# OPB-001 / D03 — Monétique et ISO 8583 : jPOS et Moov ISO8583

**Revue documentaire du 16 novembre 2026.** Ce document ne certifie ni interopérabilité avec un switch bancaire ni conformité réglementaire.

| Critère | jPOS | Moov ISO8583 |
|---|---|---|
| Dépôt amont | https://github.com/jpos/jPOS | https://github.com/moov-io/iso8583 |
| Technologie | Java / framework de messages financiers | Go / bibliothèque de sérialisation et désérialisation ISO 8583 |
| Licence déclarée par le dépôt | AGPL-3.0 (vérifier les fichiers de licence et conditions de l'édition retenue) | Apache-2.0 |
| Documentation | https://jpos.org/docs/ | https://github.com/moov-io/iso8583/blob/master/README.md |
| Contribution | https://github.com/jpos/jPOS/blob/main/CONTRIBUTING.md | https://github.com/moov-io/iso8583/blob/master/CONTRIBUTING.md |
| Premier usage OSEF | Étudier ultérieurement une architecture monétique | Créer un message fictif, l'encoder et le décoder |

## Limites importantes
- ISO 8583 est une famille de spécifications de messagerie, non un switch de paiement complet.
- Un MTI, un bitmap et des éléments de données ne suffisent pas à réaliser un paiement.
- Les variantes réseaux, spécifications d'hôtes, dispositifs cryptographiques et traitements de réconciliation ne sont pas couverts par un exercice de simple encodage.
- Ne pas supposer que le simple usage de jPOS ou de Moov ISO8583 rend une solution compatible avec un système national ou régional de paiement.
- **Aucune donnée de carte réelle, aucun PIN, cryptogramme, secret, connexion TPE, HSM ou switch de production.**

## Vérifications à poursuivre
- [x] Dépôts officiels et positionnement général identifiés.
- [x] Licences déclarées identifiées à partir des dépôts.
- [ ] Version exacte de chaque outil et dépendances figées.
- [ ] Lecture intégrale des règles de contribution et confirmation d'une issue disponible.
- [ ] Exécution pratique reproduite par deux ingénieurs.
- [ ] Revue juridique si une réutilisation hors lab est envisagée, notamment concernant jPOS.

## Suite proposée
Premier lab **OPB-D03-001 — Message ISO 8583 fictif avec Moov (Go)** : pack, unpack, assertions, erreurs et confidentialité des logs. Un lab jPOS suivra seulement après examen de ses prérequis et licences.
