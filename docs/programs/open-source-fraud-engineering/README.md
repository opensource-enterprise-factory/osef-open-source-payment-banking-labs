# OSEF — Open Source Fraud Engineering (OSFE)

**Statut : programme proposé et documenté, lancement opérationnel à valider.**
**Périmètre : Afrique francophone, avec veille et contributions upstream internationales.**
**Date de cadrage : 19 novembre 2026.**

## 1. Vision et finalité

Former et mobiliser un collectif d'ingénieurs capables **d'évaluer, déployer en laboratoire, intégrer, tester, sécuriser, exploiter et contribuer** à plusieurs solutions open source de lutte contre la fraude financière. Construire des éléments de preuve reproductibles plutôt que promouvoir un seul moteur.

L'OSFE n'est **pas** un système antifraude de production, une certification de conformité ni une offre commerciale validée.

## 2. Objectifs mesurables — objectifs cibles, non résultats acquis

| Objectif cible | Mesure de succès | Échéance proposée |
|---|---|---|
| Référencer 5 approches principales | Fiches sourcées Tazama, Jube, Ojuri, Flink/Kafka, Fraud Detection Handbook et étude spécifique de Marble source-available | Sprint 1 |
| Obtenir au moins 2 moteurs installés | Logs de déploiement, commits, versions, essais sur transactions fictives | Sprint 2–3 |
| Construire 1 corpus transversal | Jeu de transactions entièrement synthétiques, dictionnaire, oracle de tests et conditions de réutilisation | Sprint 2 |
| Produire 1 comparaison documentée | Métriques précises, ressources, licences, limites, cas d'échec et scripts reproductibles | Sprint 4–6 |
| Démontrer 1 chaîne de partage d'alerte | FRAUD-001/002 validés, adaptation contrôlée et journal d'audit | Sous condition des gates |
| Tenir 2 meetups démonstratifs | Enregistrement/compte rendu autorisé, démos réellement testées et retours | Après validation technique |
| Soumettre au moins 1 contribution upstream | Lien vers issue/PR acceptée ou ouverte, sans présumer du merge | Après revue du mainteneur |

Ces échéances sont un **cadencement suggéré** dépendant de volontaires ; aucune date d'exécution ou affectation n'a été confirmée.

## 3. Six workstreams

| Workstream | Responsabilité | Livrable principal | Référence |
|---|---|---|---|
| **WS1 — Technology Intelligence & Licensing** | Inventaire, licences, dépendances, CVE, maintenance, frontières OSS / source-available | Matrice de licences et fiches d'évaluation | [FRAUD-008 #83](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/83) |
| **WS2 — Detection Engines & ML** | Déployer Tazama/Jube/Ojuri, comparer règles, scoring, dérive, faux positifs | Configurations, résultats, hypothèses et limites | [#50](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/50), [#80](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/80), [#81](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/81) |
| **WS3 — Performance, Reliability & SRE** | Charge reproductible, p50/p95/p99, mémoire, disponibilité, panne et replay | Rapport comparatif sans extrapolation production | [#80](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/80), [#82](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/82) |
| **WS4 — Interoperability & Fraud Intelligence** | Contrats de signaux minimisés, mapping, politiques de partage, dédoublonnage | Schémas, adaptateurs, traces et tests d'isolement | [#43](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/43), [#63](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63) |
| **WS5 — Investigation & Case Management** | Cas d'investigation, traçabilité, corrections de faux positifs, revue humaine | Scénarios et matrice d'accès, sans sanction automatique | [#63](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63) |
| **WS6 — Community, Learning & Upstream** | Meetups, onboarding, guides lab, contribution upstream | Supports, enregistrements autorisés, PR et rétrospectives | [Catalogue](../../strategy/OPEN-SOURCE-FRAUD-ENGINEERING-CATALOGUE.md) |

## 4. Programme technique et technologies

| Produit / approche | Rôle | Modalités de qualification |
|---|---|---|
| **Tazama** | Pipeline de surveillance, règles, résultats, modules d'investigation | Installer Core puis caractériser précisément API, licences par composant, ressources et résultats |
| **Jube** | Plateforme de surveillance et workflow AML/fraude | Vérifier licence **AGPLv3**, interfaces et possibilité de reproduire le même corpus |
| **Ojuri** | Piste ML, scoring et investigation annoncés par son dépôt | Vérifier licence **MIT**, maturité, interfaces, dépendances, dérive et transparence du scoring |
| **Apache Kafka + Flink** | Construire un pipeline de règles événementielles | Évaluer exploitation, latence, idempotence, fenêtres et reprise ; **pas un moteur antifraude clé en main** |
| **Fraud Detection Handbook** | Matériel pédagogique et protocole ML | Vérifier licences du code et des jeux de données séparément |
| **Marble** | Comparaison fonctionnelle et étude de licence uniquement | **Elastic License 2.0, source-available, non open source OSI** ; ne pas assimiler à une solution libre exploitable en SaaS |

L'architecture de référence **n'impose pas** l'intégration directe de ces moteurs entre eux : privilégier des **adaptateurs testés** et des schémas OSEF explicitement non officiels.

## 5. Gouvernance proposée pour 20 ingénieurs en soirée/week-end

**Rôles à pourvoir volontairement**, sans désignation automatique : un coordinateur OSFE, un référent par workstream (cumul possible), un relecteur indépendant des résultats, et un point de contact sécurité/licences.

Rythme conseillé : un planning asynchrone hebdomadaire, un créneau de revue technique, un sprint de contribution en week-end, et une démonstration mensuelle uniquement si preuves suffisantes.

**Definition of Ready (DoR)** : source/version/licence renseignées, objectif métier testable, environnement et données fictives définis, budget matériel et risques identifiés.

**Definition of Done (DoD)** : PR relue, README de reproduction, versions figées, tests positifs/négatifs, journaux expurgés, limites consignées, nettoyage, absence de secrets et validation métier/sécurité. Une issue simplement ouverte ne vaut pas un lab validé.

## 6. Séquencement et gates

1. **Gate G0 — Inventaire fiable.** Valider licences, version des sources et contrats de données. Propriétaire : WS1.
2. **Gate G1 — Labs élémentaires reproductibles.** Valider les scénarios FRAUD-001 et le déploiement Tazama FRAUD-002 avec résultats mesurés. Propriétaires : WS2/WS4.
3. **Gate G2 — Corpus commun & mesure.** Corpus synthétique et protocole de benchmark validés ; exécuter Jube/Tazama séparément. Propriétaires : WS2/WS3.
4. **Gate G3 — Interopérabilité.** Confirmer le contrat réel des sorties Tazama/Jube avant mapping ; tests d'isolement, faux positifs et erreurs. Propriétaires : WS4/WS5.
5. **Gate G4 — Contributions et démonstrations.** Revue indépendante, publication de résultats documentés, meetup et remontée upstream éventuelle. Propriétaire : WS6.

**FRAUD-004** garde son périmètre de contribution Tazama existant ; ne pas le remplacer par un nouveau lab.

## 7. Roadmap de référence — 12 semaines relatives

| Semaines | Focus | Gate et livrables attendus |
|---|---|---|
| 1–2 | WS1 : sources, licences, environnement ; générateur et corpus synthétiques | G0 + matrice sourcée |
| 3–4 | FRAUD-001/002 : exécution indépendante, tests, versions et outils | G1 + rapports d'exécution |
| 5–6 | FRAUD-005 : Jube vs Tazama, seuils, métriques et mesures | G2 + benchmark initial |
| 7–8 | FRAUD-006/007 : ML, dérive, Kafka/Flink et fiabilité | Benchmarks complémentaires |
| 9–10 | FRAUD-003 et investigations : corrélation, permissions et dédoublonnage | G3 + scénario de bout en bout |
| 11–12 | Relecture, documentation, rapports et meetups | G4 + bilan et backlog upstream |

Il s'agit d'un **modèle de calendrier**, pas d'une tâche planifiée ni d'un engagement de ressources.

## 8. Risques et garde-fous

- **Données** : seulement des identités `demo-` et opérations synthétiques ; jamais PAN, MSISDN, données KYC ou comptes réels.
- **Fraude suspectée ≠ fraude avérée** : toute investigation et décision reste revue par un humain ; aucune sanction automatisée.
- **Conformité** : cadre local pays par pays, protection des données et secret bancaire à faire analyser avant projet réel.
- **Licences** : les obligations d'AGPLv3, MIT, ELv2 et dépendances sont examinées au regard de l'usage précis, sans avis juridique implicite.
- **Sécurité / fiabilité** : réseau local isolé, aucun service exposé au public, secrets hors GitHub, suppression contrôlée des environnements.
- **Performance** : charges et caractéristiques matérielles publiées ; aucun résultat de VM labo ne justifie une promesse SLA de production.
- **Propriété / gouvernance** : attribution claire des contributions, revues et droits de réutilisation.

## 9. Mesures de pilotage

Données hebdomadaires à **renseigner à partir de preuves**, non inventées : nombre de labs reproductibles, jeux de données validés, % tests réussis, résultats benchmark sourcés, PR relues, issues upstream effectivement ouvertes, contributeurs actifs volontaires, meetups tenus et feedback documenté.

## 10. Références et traçabilité

- [Étude comparative officielle OSEF](../../strategy/OPEN-SOURCE-FRAUD-ENGINEERING-COMPARATIF-2026-11.md)
- [Catalogue existant des labs et meetups](../../strategy/OPEN-SOURCE-FRAUD-ENGINEERING-CATALOGUE.md)
- [Méthodologie de benchmark et schéma de preuve](BENCHMARK-PROTOCOL.md)
- [Backlog et contributions](BACKLOG.md)
- Tazama : https://github.com/tazama-lf/tazama-stack
- Jube : https://github.com/jube-home/aml-fraud-transaction-monitoring
- Ojuri : https://github.com/ojuri-io/ojuri
- Marble : https://github.com/checkmarble/marble
- Apache Flink / Kafka : https://github.com/apache/flink et https://github.com/apache/kafka

**Statut : programme documenté, équipe à mobiliser et jalons à valider.**
