# OSEF Payment Engineering — Vision et feuille de route 2027–2029

**Statut : proposition stratégique pour discussion et validation au sein d'OSEF**  
**Version : 1.0 — 16 novembre 2026**  
**Périmètre : Afrique francophone, avec ouverture aux contributions mondiales**

## Vision

> Faire émerger en Afrique francophone une capacité collective d'ingénierie Open Source bancaire et de paiement, reconnue pour ses contributions internationales, ses réalisations techniques reproductibles et la qualité des services apportés aux entreprises financières africaines.

## Positionnement

OSEF ne cherche pas à devenir une banque, un établissement de paiement ou un opérateur de switch interbancaire. Son positionnement **proposé** est celui d'une fabrique de compétences, de biens communs techniques et de prestations d'ingénierie Open Source dans la banque, la monétique et les paiements.

**Promesse proposée :** aider les banques, EME, SFD, fintechs, prestataires technologiques et ESN à comprendre, intégrer, tester, sécuriser et exploiter des composants Open Source, tout en contribuant à leurs communautés amont.

**Chaîne de valeur :** CONTRIBUTION UPSTREAM → LABS REPRODUCTIBLES → COMPÉTENCES DÉMONTRÉES → SERVICES AUX ENTREPRISES → RETOURS ET CONTRIBUTIONS UPSTREAM.

## Cinq capacités structurantes

| Capacité | Production attendue | Preuve |
|---|---|---|
| Recherche et cartographie | Catalogue sourcé de logiciels, standards, licences et communautés | Fiches datées, relues et versionnées |
| Labs & ingénierie | Simulateurs, API, tests de protocoles, blueprints et tests de résilience | Démonstrations et CI vertes |
| Contribution upstream | Documentation, bugs, tests, patches, échanges communautaires | Issues/PR amont consultables; acceptation mesurée séparément |
| Services aux entreprises | Diagnostics, intégration, tests, support, observabilité | Contrats, livrables acceptés et références autorisées |
| Academy et mentorat | Parcours de compétences et ateliers pratiques | Réalisations individuelles et évaluations reproductibles |

## Modèle organisationnel — séparation des responsabilités

### Volet A : OSEF Payment & Banking Labs (bien commun)
- Dépôts publics, données entièrement synthétiques, documentation FR/EN, tests reproductibles.
- Accès et contribution ouverts selon les règles du projet; aucune obligation d'être client OSEF.
- Contributions upstream respectueuses des licences et processus de chaque projet.
- Gestion des vulnérabilités par signalement responsable, sans publier des détails exploitables.

### Volet B : OSEF Payment Engineering Services (activité commerciale envisagée)
- Prestations contractualisées de conseil, intégration, simulation, exploitation et formation.
- Responsabilités, périmètre, qualité de service, confidentialité et propriété intellectuelle définis par contrat.
- Aucun accès ni opération sur systèmes financiers réels sans autorisation et encadrement.
- Tarification fondée sur les coûts réels, les risques, la capacité de livraison et la validation commerciale.
- Partenariats non exclusifs avec ESN et intégrateurs; pas d'allégation de partenariat institutionnel non confirmé.

### Gouvernance commune proposée
- Comité technique pour architecture, qualité, sécurité et contributions.
- Responsable commercial/contractuel pour les engagements clients.
- Politique conflits d'intérêts, publication des travaux et licences, rémunération des contributeurs engagés sur prestations.
- Séparation des informations clients confidentielles et des référentiels publics.
- Suivi distinct des indicateurs « contribution communautaire » et « prestation commerciale ».

## Offres commerciales à expérimenter, sans prétendre qu'elles sont déjà lancées

| Offre | Cible | Livrable | Mode de revenus envisagé |
|---|---|---|---|
| Payment OSS Discovery | DSI, ESN, fintechs et SFD | Cartographie de dépendances, licences, architecture, risques, recommandations | Forfait de diagnostic |
| Payment Integration & Simulation Lab | ESN, monétique et équipes d'intégration | Simulateurs ISO 8583/API, jeux de tests et rapports d'écarts | Mission à jalons |
| Payment Platform Reliability | Équipes production et SRE | Instrumentation, SLO, runbooks et tests de reprise | Projet + support récurrent après qualification |
| Payment OSS Enablement | Ingénieurs, ESN et institutions | Formation appliquée et mentorat contributions | Cohortes ou contrats entreprise |

**Privilégier au démarrage les ESN et intégrateurs** comme partenaires B2B2B : OSEF apporte une expertise complémentaire de déploiement, de test, d'observabilité et de maintenance au bénéfice de leurs clients finaux.

## Feuille de route indicative et jalons de validation

### Horizon 1 — novembre 2026 à février 2027 : crédibilité technique
- [ ] 3 labs reproductibles et évalués par deux ingénieurs, incluant OPB-D03-001 (Moov ISO8583).
- [ ] 1 simulateur ISO 8583 documenté, sans données sensibles ni liaison bancaire.
- [ ] 5 ingénieurs actifs documentés par leurs contributions, sans attribution fictive de rôle.
- [ ] 2 contributions amont proposées et tracées (acceptation non garantie).
- [ ] 5 entretiens qualifiés avec acheteurs/professionnels (besoins et budgets explicités).

**Gate H1 :** au moins un démonstrateur reproductible + revue sécurité/licences + problème client réel validé. Si non atteint, ne pas promettre de services opérationnels.

### Horizon 2 — mars à décembre 2027 : crédibilité commerciale
- [ ] 10 labs/blueprints techniques validés.
- [ ] Offre pilote d'intégration ou diagnostic structurée, avec coûts et limites de responsabilité.
- [ ] Un ou plusieurs pilotes contractuels **si** clients et capacités identifiés.
- [ ] Processus de support, traçabilité, escalade et sécurité éprouvé.
- [ ] Participation récurrente à des communautés amont; RETEX publiés uniquement avec autorisation.

**Gate H2 :** livrables acceptés, responsabilité contractuelle maîtrisée, coût de service connu et expérience réutilisable.

### Horizon 3 — 2028–2029 : reconnaissance durable
- [ ] Équipe spécialisée avec gouvernance, relais et financement soutenable.
- [ ] Prestations récurrentes et qualité mesurée.
- [ ] Contributions upstream significatives et vérifiables.
- [ ] Références publiques autorisées et interventions dans événements techniques internationaux.
- [ ] Documentation et programmes accessibles aux ingénieurs de plusieurs pays d'Afrique francophone.

**Ces cibles sont des propositions de pilotage et non des faits réalisés ni des prévisions garanties.**

## Première séquence d'exécution

1. **OPB-001** — maintenir la cartographie vivante des 14 domaines; recenser licences et contributions amont vérifiées.
2. **OPB-D03-001** — corriger, figer les dépendances, exécuter et faire relire le prototype Go/Moov ISO8583; ne pas annoncer de succès sans journaux de tests.
3. **OPB-002** — environnement Fineract de laboratoire, API fictive et preuves.
4. **OPB-005** — architecture Mojaloop et scénarios d'échanges documentés.
5. Mettre en place la fiche d'offre pilote Payment Integration & Simulation Lab, **après** validation du premier démonstrateur.
6. Organiser un meetup « Peut-on construire et exploiter des infrastructures de paiement avec l'Open Source en Afrique francophone ? », sans prétendre qu'une date ou des invités sont confirmés.

## Risques et conditions

- Une licence Open Source ne garantit pas l'exploitabilité ou la conformité réglementaire.
- Respecter les obligations des licences amont, dont les éventuelles obligations copyleft, et obtenir une revue juridique sur les contrats et la propriété intellectuelle.
- Distinguer une activité de services informatiques d'une activité financière réglementée; ne pas revendiquer d'agrément BCEAO, PCI DSS ni une compatibilité PI-SPI sans justificatif.
- Aucun secret, compte bancaire réel, PAN, PIN ou rail de paiement de production dans les laboratoires.
- Ne pas revendiquer de partenariats institutionnels ou de contributions upstream acceptées sans preuve.

## Indicateurs de pilotage

- **Communauté** : contributeurs réellement actifs, PR et contributions amont, relectures et mentorat.
- **Technique** : labs testés, pourcentage de tests verts, reproduction par un second ingénieur, vulnérabilités ouvertes/résolues.
- **Commercial** : entretiens acheteurs, pilotes signés, marge réelle, renouvellements, satisfaction documentée.
- **Soutenabilité** : coût de support, temps d'ingénierie, rémunération, nombre de personnes capables d'opérer la solution.

## Sources de référence

- [Open Source Initiative — Open Source Definition](https://opensource.org/osd)
- [Apache Fineract](https://fineract.apache.org/)
- [Mojaloop — contributions](https://docs.mojaloop.io/community/contributing/contributors-guide.html)
- [FINOS — Open Source Readiness](https://www.finos.org/open-source-readiness)
- [Moov ISO8583](https://github.com/moov-io/iso8583)
- [BCEAO — site officiel](https://www.bceao.int/)

## Statut de validation

- Proposition rédigée : oui.
- Adoption formelle par l'équipe OSEF : **non confirmée**.
- Clients, partenariats et pilotes : **non confirmés**.
- Revenus, tarification et agréments : **non établis**.
