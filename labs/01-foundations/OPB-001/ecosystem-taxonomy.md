# OPB-001 — Cartographie élargie de l'Open Source bancaire, monétique et paiements

**Version de cadrage : 2026-11-16.** Taxonomie **proposée par OSEF**, non classification officielle. Cette liste n'est ni exhaustive ni un catalogue de solutions homologuées.

## Les 14 domaines

| Code | Domaine | Priorité de recherche |
|---|---|---|
| D01 | Core Banking et systèmes de comptes | P0 |
| D02 | Microfinance, SFD et crédit | P0 |
| D03 | Monétique, cartes, TPE et ISO 8583 | P0 |
| D04 | Switches et interopérabilité des paiements | P0 |
| D05 | Mobile Money, wallets et paiements marchands | P0 |
| D06 | Open Banking et Open Finance | P0 |
| D07 | Ledgers, comptabilité et rapprochement | P0 |
| D08 | Paiements transfrontaliers et remittances | P1 |
| D09 | Messaging financier, ISO 20022 et SWIFT | P1 |
| D10 | Fraude, KYC, AML et conformité | P1 |
| D11 | Passerelles et orchestration des paiements | P1 |
| D12 | Facturation, recouvrement et trésorerie | P1 |
| D13 | Financial Data, Analytics et IA | P1 |
| D14 | Infrastructure, sécurité, DevSecOps et SRE | P1 |

P0 et P1 indiquent la priorité **d'exploration par OSEF**, pas la maturité, sécurité ou valeur du logiciel.

## Critères d'admission d'un projet dans le catalogue « vérifié »

- Identifier l'entité, le produit et le dépôt officiel exact.
- Vérifier la licence du composant concerné : correspond-elle aux critères [OSI](https://opensource.org/osd) ? Documenter les différences entre open source, open core, source-available, service commercial et standard ouvert.
- Vérifier les fonctions revendiquées dans documentation/source primaire; ne pas extrapoler depuis des présentations marketing.
- Identifier gouvernance, guides de contribution, communauté, version, maintenance, sécurité, dépendances et limites de production.
- Ajouter les liens, date de vérification et statut de preuve.
- Décrire l'intérêt technique spécifique des ingénieurs d'Afrique francophone sans supposer une conformité BCEAO/UEMOA, PCI DSS ou une certification.
- Distinguer explicitement **outil dédié à la finance**, **brique transversale réutilisable**, **standard/spécification** et **fondation hébergeant des projets**.

## Statuts de vérification

- **Candidat :** identifié, vérification détaillée non réalisée.
- **Partiellement vérifié :** source primaire consultée, éléments restants à contrôler.
- **Vérifié :** licence, dépôt, fonctionnalité décrite et contribution établis avec sources datées.
- **À exclure / autre catégorie :** non Open Source, licence restrictive, standard uniquement, projet abandonné ou sans source suffisante, avec justification.

La présence d'un projet dans le [catalogue de candidats](ecosystem-candidates.md) n'implique pas sa validation.

## Livrables associés

- [Catalogue des candidats](ecosystem-candidates.md)
- [Matrice de vérification](project-matrix.md)
- [Guide de première contribution](first-contribution.md)
- [Journal des preuves](evidence.md)
- [Définition OSEF](open-source-banking-payments-definition.md)

## English summary
OSEF proposes a 14-domain research taxonomy covering banking, microfinance, card payments, interoperability, wallets, open banking, financial ledgers, international payments, messaging, compliance, payment orchestration, billing, data and infrastructure. All candidate projects require independent verification of license, repository, features, governance and contribution process before being listed as verified.
