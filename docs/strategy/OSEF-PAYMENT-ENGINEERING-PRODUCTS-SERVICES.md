# OSEF Payment Engineering — Catalogue des produits et services

**Version : 1.0 — 16 novembre 2026**  
**Statut : proposition de portefeuille à valider ; aucune offre ci-dessous n'est présumée commercialisée.**  
**Périmètre : ingénierie Open Source bancaire, monétique, paiement et microfinance.**

## Positionnement

OSEF propose d'agir comme **fabrique de biens communs et partenaire d'ingénierie Open Source** pour les ESN, intégrateurs, banques, fintechs, EME, PSP et SFD. Notre rôle cible consiste à documenter, développer, intégrer, tester et fiabiliser des composants techniques, **sans** nous substituer à un prestataire de paiement agréé.

Deux familles complémentaires :

- **Produits (OPP)** : kits logiciels, simulateurs, bibliothèques, configurations et référentiels réutilisables. Publication Open Source envisagée selon les licences, droits et validations.
- **Services (OPS)** : expertise humaine et engagements contractuels payants (diagnostics, intégration, tests, exploitation, formation).

**Ne pas confondre** prototype GitHub, produit exploitable et offre commercialement disponible.

## A — Produits technologiques proposés

| ID | Nom | Description / composants envisageables | Clients utilisateurs | Statut au 16-11-2026 | Critère minimal de sortie |
|---|---|---|---|---|---|
| OPP-01 | **OSEF Payment Simulation Kit** | Messages ISO 8583 fictifs, simulateurs d'hôte, jeux de tests nominal/dégradé, traçabilité; d'abord Moov ISO8583 | ESN monétiques, fintechs, équipes QA | **Prototype commencé**, code OPB-D03-001 non validé | Dépendances figées, tests verts, revue et démonstration reproductible |
| OPP-02 | **OSEF Payment API Testing Kit** | Tests de contrats REST, idempotence, auth, délais, scénarios d'échec, rapports | PSP, fintechs, banques, ESN | **Concept** | Kit CI reproductible et jeux de données synthétiques |
| OPP-03 | **OSEF Payment Observability Pack** | Tableaux de bord, instrumentation OpenTelemetry, métriques et SLO, alertes et runbooks | Équipes SRE, production et DSI | **Concept** | Lab instrumenté avec panne/reprise et indicateurs mesurés |
| OPP-04 | **OSEF Payment Reconciliation Lab** | Moteur de rapprochement pédagogique, cas d'écarts et rapports d'anomalies | Banques, PSP, fintechs | **Concept** | Rapprochement déterministe sur données fictives, tests de non-régression |
| OPP-05 | **OSEF Open Banking Sandbox** | API de comptes fictifs, wallets simulés, consentement de lab, mocks et docs développeur | Fintechs, écoles, intégrateurs | **Concept** | API sécurisée de démonstration et scénarios d'intégration sans données réelles |
| OPP-06 | **OSEF Financial OSS Knowledge Hub** | Cartographie sourcée, comparaison de licences, contributions upstream et guides FR/EN | Communautés, écoles et entreprises | **En construction : OPB-001** | Fiches revues, sources datées et processus de mise à jour |

### Limites produit
Un message ISO 8583 parsé n'est **pas** un switch monétique. Une sandbox API n'est **pas** un PSP. Un package d'observabilité n'est **pas** une garantie de disponibilité. Aucun produit ne revendique compatibilité PI-SPI, homologation BCEAO ni certification PCI DSS sans preuve indépendante.

## B — Services professionnels proposés

| ID | Service | Acheteur cible | Livrables précis | Modèle contractuel envisageable | Statut |
|---|---|---|---|---|---|
| OPS-01 | **Payment OSS Assessment** | DSI, architectes, ESN, SFD | Inventaire, dépendances, licences, risques, scénarios et feuille de route | Diagnostic au forfait et périmètre fermé | **Offre à formaliser** |
| OPS-02 | **Payment Integration Engineering** | Intégrateurs, équipes paiement | Interfaces et adaptateurs autorisés, tests contractuels, documentation, passation | Mission par jalons et critères d'acceptation | **Offre à formaliser** |
| OPS-03 | **Payment Testing & Certification Readiness** | QA, monétique, fintechs | Bancs de tests, couverture de scénarios, analyse d'écarts, préparation de dossier | Mission d'essais; **aucune certification délivrée** | **Offre à formaliser** |
| OPS-04 | **Payment Reliability & Managed Support** | Production, SRE, DSI | SLO, monitoring, alertes, runbooks, support, tests de reprise | Forfait de mise en place puis contrat récurrent seulement après qualification | **Capacité non démontrée** |
| OPS-05 | **Payment Modernization Advisory** | Banques, fintechs, ESN | Diagnostic de dette technique, architecture cible, trajectoire de migration/rollback | Conseil au forfait et assistance projet | **Offre à formaliser** |
| OPS-06 | **Payment Engineering Academy** | ESN, équipes internes, écoles | Formations pratiques, évaluation sur labs, mentorat upstream, documentation | Par cohorte ou convention entreprise | **Programme proposé** |

### Exclusions et conditions
- Aucun mouvement de fonds, tenue de comptes clients, conservation de données de paiement réelles ou accès au réseau d'un tiers sans mandat et conformité.
- Ne pas utiliser les termes **certification**, **homologation**, **auditeur agréé** ou **support officiel du projet** sans autorisation/preuve.
- Les responsabilités de sécurité, confidentialité, disponibilité, SLA, propriété intellectuelle, licences et sous-traitance doivent être contractualisées.
- Le « support managé » n'est commercialisable qu'après démonstration de la capacité d'astreinte, d'escalade, de maintenance et de couverture contractuelle.

## C — Produits ↔ services : comment vendre sans fermer l'Open Source

| Actif public | Prestation payante | Ce que conserve le client |
|---|---|---|
| OPP-01 ISO 8583 Simulation Kit | OPS-02 et OPS-03 : intégration et tests adaptés au contexte client | Livrables, rapports, documentation et droits définis au contrat |
| OPP-02 API Testing Kit | OPS-02 et OPS-03 | Tests et rapport d'écarts contractuels |
| OPP-03 Observability Pack | OPS-04 : instrumentation et assistance | Dashboards et runbooks livrés selon contrat |
| OPP-04 Reconciliation Lab | OPS-01/OPS-02 : diagnostic et adaptation | Spécifications et tests métiers contractuels |
| OPP-05 Open Banking Sandbox | OPS-02/OPS-06 : intégration et formation | Exercices, schémas et transferts de compétences |
| OPP-06 Knowledge Hub | OPS-01/OPS-05/OPS-06 : conseil et formation | Rapport contextualisé et recommandations |

**Principe :** facturer le travail, les compétences et la responsabilité réellement assumée, pas inventer une exclusivité sur du code libre.

## D — Ordre de lancement recommandé

**P0 — Preuves techniques et premiers entretiens**
1. OPP-06 — cartographie et référentiel OPB-001.
2. OPP-01 — stabiliser et tester OPB-D03-001, puis proposer un simulateur minimal publiquement démontrable.
3. OPS-01 — fiche commerciale de diagnostic (périmètre, exclusions, durée, coûts, livrables).
4. OPS-03 — offre de banc de tests limitée à un environnement fictif ou explicitement autorisé.

**P1 — Après démonstration et demande client vérifiée**
- OPP-02, OPP-03, OPS-02 et OPS-06.

**P2 — Après compétences, capacité opérationnelle et contrats**
- OPP-04, OPP-05, OPS-04 et OPS-05.

Ces priorités sont des **propositions de séquencement**, pas une évaluation commerciale confirmée.

## E — Qualification commerciale des offres

Avant toute première proposition client, vérifier :
- [ ] Problème explicite, décideur et budget du client documentés.
- [ ] Périmètre, livrables, hypothèses, exclusions et critères d'acceptation établis.
- [ ] Licences des dépendances et droits sur les développements analysés.
- [ ] Contrats et clauses de confidentialité, assurance/responsabilité, protection des données.
- [ ] Conditions de sécurité, accès, stockage et gestion des secrets.
- [ ] Compétences des ingénieurs et capacité de support réellement démontrées.
- [ ] Prix calculé sur coûts, charge, risques et marge cible; non inventé.
- [ ] Vérification des obligations réglementaires applicables à la mission exacte.

## F — KPIs de pilotage (ne pas confondre objectifs et réalisations)

**Produits :** prototypes revus, couverture de tests, reproducibilité, issues résolues, licences vérifiées, contributions upstream.  
**Services :** prospects qualifiés, diagnostic vendu, pilote accepté, marge nette, incidents, satisfaction, renouvellement.  
**Communauté :** contributeurs actifs, relectures, formations, liens upstream acceptés et transparence sur les limites.

## G — Sources primaires

- Open Source Definition — https://opensource.org/osd
- Moov ISO8583 — https://github.com/moov-io/iso8583
- Apache Fineract — https://fineract.apache.org/
- Mojaloop — https://mojaloop.io/
- Instruction BCEAO n°001-01-2024 — https://www.bceao.int/index.php/fr/reglementations/instruction-ndeg001-01-2024-du-23-janvier-2024-relative-aux-services-de-paiement

## Statut de gouvernance
**Catalogue proposé pour validation par OSEF.** Pas de produit déclaré prêt pour la production; pas de chiffre d'affaires, client, partenariat, agrément ou certification revendiqués.
