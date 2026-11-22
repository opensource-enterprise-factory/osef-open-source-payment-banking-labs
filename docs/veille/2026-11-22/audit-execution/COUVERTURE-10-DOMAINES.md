# Audit du test et protocole de contrôle des dix domaines

**Date :** 22 novembre 2026. **But :** vérifier la présence des rubriques obligatoires, identifier les preuves manquantes et ne pas confondre surveillance thématique et vérification exhaustive.

## Bilan
| Contrôle | Résultat documenté |
|---|---|
| Déclenchement manuel | Succès signalé par la tâche planifiée |
| Rubriques thématiques produites | 10 sur 10 |
| Domaines audités intégralement | 0 sur 10 |
| Domaines avec examen partiel | 9 sur 10 |
| Domaine de vérification insuffisante | 1 sur 10 (régulation francophone) |
| Matrice des sources prioritaires interrogées | Non entièrement renseignée |
| Inventaire des releases/commits prioritaires | Incomplet |
| Inventaire de toutes les opportunités fintech ouvertes | Incomplet |

## Procédure à appliquer à la prochaine édition
1. Fixer heure de départ/fin UTC. Couvrir les dernières 24 h, puis élargir explicitement à 7 jours si faible volume.
2. Pour A–J, interroger **au moins une source primaire dédiée**, si accessible, en notant titre, URL directe, publication et consultation.
3. Distinguer événement, publication, commit, release, consultation, mise en production et entrée en vigueur.
4. Étiqueter chaque résultat : confirmé primaire / non confirmé / source inaccessible / absence de nouveau fait **après vérification**.
5. Pour projets techniques : vérifier releases, changelogs et avis de sécurité, et pas uniquement les blogs.
6. Pour B : contrôler séparément EMVCo, PCI SSC, ISO 8583, ISO 20022 et tokenisation ; une page de standards ne prouve pas l'absence d'actualités.
7. Pour G : couvrir BCEAO, BEAC, COBAC, GIM-UEMOA/GIMAC et limiter toute conclusion aux textes effectivement accessibles.
8. Pour I/J : distinguer financement fintech, appel d'offres, signal de besoin, piste hypothétique, lead qualifié et contrat. Vérifier dates de clôture et admissibilité.
9. Établir un inventaire des sources effectivement consultées, les erreurs d'accès et les recherches à relancer ; annoncer le score `domaines réellement vérifiés / 10`, pas seulement `rubriques rédigées / 10`.
10. Ne proposer que des labs reproductibles, avec données fictives, critères mesurables et liens vers travaux existants ; jamais de doublons automatiques.

## Registre de sources à suivre
- Rails/paiements : Mojaloop, AfricaNenda, BCEAO PI-SPI, opérateurs publics de paiement instantané.
- Monétique : EMVCo, PCI SSC, fournisseurs/mainteneurs open source de switching ; ISO 8583/ISO 20022 en qualité de standards.
- Banking : Apache Fineract, Mifos, Open Banking, Open Bank Project.
- Fraude : Tazama, Jube, Ojuri, Marble ELv2 (source-available), OFTA.
- Infrastructure : Kafka, Flink, OpenSSF, CNCF, avis sécurité des fournisseurs.
- Finance/DLT : FINOS FDC3, LF Decentralized Trust et dépôts concernés.
- Régulation : BCEAO, BEAC, COBAC, GIM-UEMOA, GIMAC, régulateurs locaux.
- Fintech/business : appels d'offres BAD, plateformes officielles d'achats publics, annonces d'acteurs, appels à projets, communiqués investisseurs.

**Limite :** le test du 22 novembre n'a pas établi la consultation exhaustive de ce registre. Il sert de checklist, pas de preuve d'audit réalisé.
