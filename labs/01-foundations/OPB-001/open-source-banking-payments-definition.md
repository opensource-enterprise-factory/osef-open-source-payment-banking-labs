# Définir l'Open Source bancaire et des paiements

**OSEF — OPB-001 | Proposition de définition et de classification, version 1.0 | 16 novembre 2026**

## Définition de travail

> L'Open Source bancaire et des paiements désigne l'écosystème de logiciels dont les licences permettent l'utilisation, l'étude, la modification et la redistribution, et qui servent à concevoir, intégrer, sécuriser, exploiter ou faire évoluer des services bancaires et des infrastructures de paiement.

Il s'agit d'une **définition de travail OSEF**, non d'une norme sectorielle reconnue. « Open Source » renvoie aux critères de l'Open Source Definition de l'OSI et ne signifie pas simplement « code source consultable ».

## Six domaines proposés

| Domaine OSEF | Périmètre étudié | Exemples de technologies à examiner |
|---|---|---|
| 1. Core Banking | Comptes, crédits, opérations et tenue des écritures | Apache Fineract, écosystème Mifos |
| 2. Payment Infrastructure | Initiation, routage, interopérabilité et orchestration des paiements | Mojaloop, GNU Taler (modèles différents) |
| 3. Open Banking & Open Finance | Interfaces d'accès contrôlé aux données et services financiers | Apache APISIX, Keycloak (briques transversales, pas solutions complètes d'Open Banking) |
| 4. Security & Compliance Engineering | Identité, secrets, contrôle d'accès et audit | Keycloak, OpenBao, Open Policy Agent |
| 5. Financial Data & Analytics | Collecte d'événements, traitement et analyse | Apache Kafka, Apache Flink, Apache Superset |
| 6. Banking Infrastructure & Reliability | Déploiement, observabilité, disponibilité et résilience | Kubernetes, OpenTelemetry, Prometheus |

Les produits mentionnés sont des **exemples d'étude**, pas des outils officiellement homologués pour les banques ni des solutions substituables entre elles. Cette classification est proposée par OSEF.

## Trois distinctions fondamentales

1. **Logiciel Open Source ≠ standard ouvert.** Un standard peut être publiquement accessible sans implémentation Open Source; un logiciel Open Source peut ne respecter aucun standard d'interopérabilité particulier.
2. **Licence Open Source ≠ conformité bancaire.** La licence ne garantit ni la cybersécurité, ni l'aptitude à la production, ni la conformité réglementaire, ni la certification PCI DSS.
3. **Fondation ≠ produit.** FINOS est un écosystème de projets, pas un logiciel de traitement des paiements ; examiner chaque projet et ses licences individuellement.

## Pourquoi ce périmètre pour l'Afrique francophone ?

Créer un cadre de recherche, de tests reproductibles et de contributions upstream (documentation, tests, code, traductions lorsque permises), fondé sur des besoins techniques documentés plutôt que sur des promesses de souveraineté ou de conformité non démontrées.

## Sources primaires

- Open Source Initiative — Open Source Definition : https://opensource.org/osd/
- OSI — FAQ : https://opensource.org/faq
- Apache Fineract — présentation officielle : https://fineract.apache.org/
- Apache Fineract — documentation : https://fineract.apache.org/docs/stable/
- Mojaloop — site officiel : https://mojaloop.io/
- FINOS — catalogue : https://www.finos.org/projects

**À vérifier dans les fiches techniques :** version actuelle de chaque composant, dépôt d'origine, licence par dépôt, support des fonctions décrites, état de maintenance et exigences applicables selon le pays / régulateur.

## English summary

Open Source banking and payments refers to the ecosystem of software distributed under licenses permitting use, study, modification and redistribution, used to build, integrate, secure and operate banking services and payment infrastructure. This is an OSEF working definition, not a regulatory standard. Open Source software, open standards and regulatory compliance must be evaluated separately.
