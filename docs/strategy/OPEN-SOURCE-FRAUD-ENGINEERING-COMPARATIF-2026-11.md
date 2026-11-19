# OSEF — Open Source Fraud Engineering : étude comparative et programme de labs

**Édition :** 19 novembre 2026 · **Périmètre :** fraude aux paiements, surveillance transactionnelle et AML, avec priorité aux compétences applicables en Afrique francophone.

> **Qualification des preuves :** étude documentaire fondée sur des dépôts et documentations des éditeurs/communautés, **pas sur un benchmark exécuté par OSEF**. Les capacités ci-dessous sont **annoncées par les projets**, non indépendamment certifiées. Aucune donnée bancaire réelle, aucun accès de production, aucune promesse de conformité réglementaire.

## 1. Décision de cadrage

Ne pas réduire OSEF à une technologie. Organiser l'apprentissage autour de cinq compétences : **détection par règles**, **ML/anomalies**, **streaming**, **investigation/gestion de cas**, **interopérabilité et gouvernance du partage**. Évaluer d'abord les licences et les interfaces réelles, puis la reproductibilité des tests, avant toute question de commercialisation.

## 2. Comparatif vérifiable

| Projet | Catégorie | Code / licence vérifiée | Fonctions annoncées | Maturité / limite de la présente étude | Intérêt OSEF |
| --- | --- | --- | --- | --- | --- |
| **Tazama** | Plateforme de surveillance transactionnelle | Dépôts ouverts Tazama LF ; vérifier la licence **composant par composant** | Core TMS, règles/typologies, adjudication, extensions et case management | Le dépôt `tazama-stack` est expressément réservé à la démo/test ; pas de déploiement de production démontré par OSEF | Référence des labs FRAUD-002/003 |
| **Jube** | Plateforme AML/fraude | **AGPL-3.0** dans le dépôt principal | Surveillance temps réel, règles, ML, workflow/case management | Fonctions déclarées ; installation Compose à éprouver ; AGPL et implications d'une offre managée à étudier juridiquement | Comparaison Tazama/Jube |
| **Ojuri** | Moteur antifraude auto-hébergé | **MIT** dans le dépôt `ojuri-io/ojuri` | Scoring XGBoost, détection de dérive, investigation assistée par LLM et dashboard, selon le README | Capacités et niveau de sûreté non validés indépendamment ; vérifier version, dépendances et conditions d'usage des modèles | Expérimenter scoring, précision/rappel, dérive, explicabilité |
| **Marble** | Moteur de décision fraude/AML source-available | **Elastic License 2.0 (ELv2)** dans `checkmarble/marble` | Règles, décisions et investigation, selon documentation | **Pas open source au sens OSI** ; restriction de fourniture comme service hébergé/managé ; aucune offre SaaS OSEF à en déduire | Étude comparative fonctionnelle et juridique seulement, sans lab de service managé |
| **Apache Flink + Kafka** | Briques techniques open source | Licences Apache-2.0 des projets à revérifier par version/distribution | Streaming, fenêtres de temps, états, agrégations, détection de vélocité à développer | **Ce n'est pas une solution antifraude prête à l'emploi** ; le moteur métier, les règles et les contrôles d'accès restent à construire | Maîtriser les architectures antifraude événementielles |
| **Fraud Detection Handbook** | Ressource pédagogique de ML | **GPL-3.0 pour le code des notebooks** selon README ; vérifier séparément les jeux de données | Simulation de transactions, modèles, jeux d'évaluation et métriques | **Pas une plateforme de production**, contraintes sur licences des données à vérifier | Évaluer la qualité des décisions et l'impact des faux positifs |

### Sources primaires

- Tazama stack / avertissement de sandbox : https://github.com/tazama-lf/tazama-stack
- Jube source et licence : https://github.com/jube-home/aml-fraud-transaction-monitoring ; https://github.com/jube-home/aml-fraud-transaction-monitoring/blob/master/LICENSE
- Jube installation Compose : https://github.com/jube-home/aml-fraud-transaction-monitoring/blob/master/docker-compose.yml
- Ojuri source et licence : https://github.com/ojuri-io/ojuri ; https://github.com/ojuri-io/ojuri/blob/main/LICENSE
- Marble source et licence : https://github.com/checkmarble/marble ; https://github.com/checkmarble/marble/blob/main/LICENSE
- Apache Flink — démo pédagogique : https://github.com/afedulov/fraud-detection-demo
- Apache Kafka : https://github.com/apache/kafka ; Apache Flink : https://github.com/apache/flink
- Fraud Detection Handbook : https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook ; https://fraud-detection-handbook.github.io/fraud-detection-handbook/

**À vérifier avant choix d'une stack :** commit SHA et tag, licence du fichier correspondant au commit, dépendances, versions d'images, vulnérabilités publiées, interfaces réelles, ressources nécessaires, tests upstream, maintenance et présence de composants propriétaires facultatifs. Les interfaces des plateformes ne sont pas supposées interchangeables.

## 3. Grille de benchmark OSEF

**Ne pas attribuer de notes sans mesures.** Benchmark par jeu **synthétique partagé** : mêmes scénarios métier, mais adaptateurs d'entrée individuels et règles comparables, en explicitant que les résultats ne sont pas nécessairement équivalents par défaut.

| Axe | Méthode et preuve attendue |
| --- | --- |
| Qualité | Précision, rappel, faux positifs par scénario, confusion matrix, seuils documentés |
| Performance | Débit soutenu, p50/p95/p99, CPU/RAM, version machine, échauffement, volumes de données |
| Robustesse | Doublons, réordonnancement, expiration, redémarrage, panne réseau, reprise après incident |
| Investigation | Rôles, justification d'alerte, ouverture/révision de cas, piste d'audit, gestion des faux positifs |
| Sécurité | Contrôles d'accès et de secrets, logs minimisés, exposition réseau, CVE et SBOM selon outils disponibles |
| Souveraineté | Déploiement local, sauvegarde, export des données, licences, dépendances externes, support possible |
| Contribution | Issue/PR reproductible en amont, engagement des mainteneurs, calendrier de releases, docs et tests |

**Aucune affirmation de supériorité de Jube, Tazama ou Ojuri n'est possible avant mesures.**

## 4. Implications pour l'Afrique francophone

Applications à explorer pour banques, PSP, switchs, fintechs et mobile money : supervision des transactions, lutte contre fraudes de transfert, détection de vélocité et de comptes de passage, investigation humaine, échange contrôlé de renseignements antifraude, résilience et exploitation sur infrastructures maîtrisées localement.

**Points non vérifiés :** références clients dans les pays, conformité à chaque réglementation, modalités autorisées de transfert des données et licence des éventuels modèles ou datasets. Un signal suspect n'est jamais une preuve de fraude et ne justifie pas à lui seul un blocage automatique.

## 5. Catalogue de labs proposés

### FRAUD-005 — Comparatif Tazama versus Jube (avancé)
- **Objectif :** reproduire des scénarios synthétiques comparables sur deux moteurs de surveillance.
- **Prérequis :** Tazama FRAUD-002, Docker/Compose, Linux/VM, SQL, API, règles métier.
- **Étapes :** figer les commits/licences → préparer corpus commun → configurer deux moteurs → exécuter nominal/doublon/faux positif/panne → mesurer qualité, ressources et erreurs → produire benchmark sans notes inventées.
- **Succès :** deux configurations reproductibles, traces expurgées, rapport d'écarts et limites.

### FRAUD-006 — Ojuri et Fraud Detection Handbook : ML et faux positifs (intermédiaire/avancé)
- **Objectif :** tester un détecteur ML sur données synthétiques, séparer entraînement/test et évaluer dérive et explicabilité.
- **Prérequis :** Python, notebooks, Docker, bases de ML et de paiement.
- **Étapes :** licences/datasets → pipeline reproductible → baseline simple → évaluer Ojuri uniquement sur interface vérifiée → faux positifs et dérive → rapport.
- **Succès :** précision/rappel et matrices de confusion calculées, modèle/version/données consignés ; pas de données personnelles.

### FRAUD-007 — Apache Kafka + Flink : détection de vélocité en streaming (avancé)
- **Objectif :** simuler des paiements et détecter des scénarios de vélocité, doublons et anomalies temporelles.
- **Prérequis :** Docker, Kafka, Flink SQL/DataStream, Python/Java, observabilité.
- **Étapes :** générer transactions fictives → topics → fenêtres et règles → sorties d'alertes → tests de latence et de redémarrage → logs et protocole de mesure.
- **Succès :** règles vérifiables, aucun doublon non maîtrisé, résultats reproductibles avec mesures machine.

### FRAUD-008 — Revue licences, gouvernance et investigations (atelier d'ingénierie)
- **Objectif :** établir une matrice d'éligibilité OSEF pour Tazama, Jube, Ojuri, Marble et les dépendances.
- **Prérequis :** bases de licences OSS, AGPLv3, MIT, ELv2, architecture bancaire et sécurité.
- **Étapes :** vérifier licences à SHA → usages on-prem/self-hosted/SaaS → dépendances et composants non-libres → accès données et audit → recommandations à revue juridique.
- **Succès :** matrice de preuves avec citations des clauses, hypothèses de déploiement, recommandations **non assimilables à un avis juridique**.
- **Marble :** étude de licence et architecture uniquement, pas de recommandation de service managé.

## 6. Meetups proposés (à planifier, aucune date ni intervenant confirmé)

1. **Panorama antifraude open source : Tazama, Jube, Ojuri, Marble** — 75 min ; DSI/CTO, payment engineers, antifraude ; démonstration comparée sur données fictives, transparence sur les licences.
2. **Détection de fraude par ML : comment mesurer les faux positifs ?** — 60 min ; data engineers, fraude, fintechs ; notebook reproductible et matrice de confusion.
3. **Construire un moteur de vélocité de paiements avec Kafka et Flink** — 75 min ; SRE, DevOps, architectes paiement ; démo streaming et reprise.
4. **Open source ou source-available : peut-on opérer un service antifraude en Afrique francophone ?** — 60 min ; OSPO, juristes, DSI et ESN ; étude de cas de licences et gouvernance.

**Ne pas dupliquer** les meetups antifraude déjà ouverts : [#46](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/46) sur partage de signaux et [#66](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/66) sur coopération fédérée.

## 7. Lien avec les labs existants

- [FRAUD-001 #43 — échange sécurisé de signalements](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/43).
- [FRAUD-002 #50 — Tazama Core et adaptateur](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/50).
- [FRAUD-003 #63 — corrélation fédérée et investigations](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63).
- **FRAUD-004 :** réservé à des travaux préexistants ; ne pas réaffecter ce numéro.
- Études postérieures proposées : FRAUD-005 à FRAUD-008.

## 8. Gouvernance de la validation

- [ ] Revue de licences et des sources par deux ingénieurs
- [ ] Validation du jeu de données fictif et des politiques de partage
- [ ] Dimensionnement VM mesuré et versions figées
- [ ] Résultats reproductibles signés dans les issues et PR
- [ ] Revue sécurité et analyse juridique avant tout scénario d'entreprise
- [ ] Contributions upstream soumises seulement avec preuve de PR
- [ ] Meetups programmés uniquement lorsque démonstration/test réels et intervenants sont confirmés

**Statut : documentation de référence créée ; aucun benchmark, lab ni meetup n'est déclaré exécuté.**
