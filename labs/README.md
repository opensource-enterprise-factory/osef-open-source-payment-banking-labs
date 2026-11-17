# OSEF Payment & Banking Labs — Catalogue initial et parcours de réalisation

**20 premiers labs OPB + un lab spécialisé ISO 8583 OPB-D03-001**, pour construire des compétences vérifiables en banque, monétique, paiement, sécurité et exploitation Open Source.

> **Statut du catalogue — 17 novembre 2026 :** les 20 entrées OPB-001 à OPB-020 sont des sujets répertoriés dans GitHub, **pas vingt laboratoires exécutés**. Les seuls dossiers de lab repérés sous `labs/` lors de cette révision sont `01-foundations/OPB-001` et `03-card-payments/OPB-D03-001`. Le second contient un prototype Go **dont la compilation et les tests n'ont pas été confirmés**. Les autres liens ci-dessous mènent aux **issues de cadrage**, et non à des guides de déploiement existants.

**Navigation :** [Commencer](#commencer--première-contribution) · [Catalogue intégral](#catalogue-des-20-premiers-labs) · [ISO 8583](#premier-lab-spécialisé--opb-d03-001) · [Domaines](#naviguer-par-domaine-métier-et-technique) · [Parcours](#trois-parcours-conseillés) · [Validation](#critères-de-validation-dun-lab) · [English](#english-summary)

## Commencer — première contribution

1. Lire [JOIN-US](../JOIN-US.md), [CONTRIBUTING](../CONTRIBUTING.md), [SECURITY](../SECURITY.md) et [CODE_OF_CONDUCT](../CODE_OF_CONDUCT.md).
2. Choisir une issue dans le catalogue ci-dessous. **La présence d'une issue ne vaut pas affectation d'un ingénieur.**
3. Proposer en commentaire une contribution circonscrite avec son pseudo GitHub, sans coordonnées personnelles.
4. Construire **localement et en environnement isolé**, avec données entièrement synthétiques, et documenter ce qui est réellement testé.
5. Proposer une PR liée à l'issue, avec versions, scripts commentés, résultats et revue si disponible.

**Pour commencer sans monter d'infrastructure :** [OPB-001 — cartographie](01-foundations/OPB-001/README.md).  
**Pour pratiquer la monétique :** [OPB-D03-001 — ISO 8583](03-card-payments/OPB-D03-001/README.md) et son [guide de démarrage](03-card-payments/OPB-D03-001/START-HERE.md) ; **prototype non validé**.

## Mini-labs du tronc commun OSEF Academy

[TC-01 à TC-07 — sept exercices Python exécutables hors ligne](common-core/README.md). Ils s'ajoutent aux vingt sujets OPB initiaux et au prototype spécialisé OPB-D03-001 ; **aucun succès CI n'est déclaré sans vérification**.

## Catalogue des 20 premiers labs

Les **difficultés sont des estimations pédagogiques proposées** et ne représentent pas des niveaux officiellement validés. Les intitulés et IDs sont ceux du catalogue initial.

| ID / issue de suivi | Sujet | Difficulté proposée | Architecture(s) cible(s) | Preuve attendue (non réalisée par défaut) |
|---|---|---|---|---|
| [OPB-001](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/1) | Cartographier l'écosystème Open Source Banking & Payments | Démarrage | [ARC-01](../docs/architecture/blueprints/ARC-01.md) · [ARC-10](../docs/architecture/blueprints/ARC-10.md) | Fiche sourcée, licence, statut amont |
| [OPB-002](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/2) | Déployer Apache Fineract | Intermédiaire | [ARC-01](../docs/architecture/blueprints/ARC-01.md) | Configuration, API et preuves de déploiement |
| [OPB-003](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/3) | Créer des clients et comptes entièrement fictifs | Intermédiaire | [ARC-01](../docs/architecture/blueprints/ARC-01.md) | Scénarios API, erreurs, tests |
| [OPB-004](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/4) | Simuler un crédit et son remboursement | Intermédiaire | [ARC-01](../docs/architecture/blueprints/ARC-01.md) · [ARC-06](../docs/architecture/blueprints/ARC-06.md) | États métiers et écritures synthétiques |
| [OPB-005](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/5) | Étudier l'architecture Mojaloop | Démarrage | [ARC-03](../docs/architecture/blueprints/ARC-03.md) | Acteurs, interfaces et diagrammes |
| [OPB-006](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/6) | Déployer un environnement Mojaloop isolé | Avancé | [ARC-03](../docs/architecture/blueprints/ARC-03.md) | Environnement reproductible, traces |
| [OPB-007](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/7) | Simuler un transfert interopérable | Avancé | [ARC-03](../docs/architecture/blueprints/ARC-03.md) | États, doublons, timeouts et preuves |
| [OPB-008](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/8) | Étudier l'intégration Fineract–Mojaloop | Avancé | [ARC-01](../docs/architecture/blueprints/ARC-01.md) · [ARC-03](../docs/architecture/blueprints/ARC-03.md) | Contrats et preuve de compatibilité si testée |
| [OPB-009](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/9) | Construire une API de paiement fictive | Intermédiaire | [ARC-05](../docs/architecture/blueprints/ARC-05.md) · [ARC-07](../docs/architecture/blueprints/ARC-07.md) · [ARC-10](../docs/architecture/blueprints/ARC-10.md) | API documentée et tests négatifs |
| [OPB-010](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/10) | Sécuriser les API avec Keycloak | Intermédiaire | [ARC-05](../docs/architecture/blueprints/ARC-05.md) · [ARC-08](../docs/architecture/blueprints/ARC-08.md) | Autorisations, tests et expurgation |
| [OPB-011](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/11) | Gérer les secrets avec OpenBao | Intermédiaire | [ARC-08](../docs/architecture/blueprints/ARC-08.md) | Secrets locaux non publiés, contrôle d'accès |
| [OPB-012](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/12) | Simuler des contrôles antifraude | Intermédiaire | [ARC-08](../docs/architecture/blueprints/ARC-08.md) | Règles, faux positifs, audit |
| [OPB-013](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/13) | Publier des événements avec Kafka | Intermédiaire | [ARC-07](../docs/architecture/blueprints/ARC-07.md) · [ARC-10](../docs/architecture/blueprints/ARC-10.md) | Contrats événementiels et reprise |
| [OPB-014](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/14) | Créer un tableau de bord des paiements fictifs | Intermédiaire | [ARC-09](../docs/architecture/blueprints/ARC-09.md) | Métriques, tableaux et limites |
| [OPB-015](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/15) | Automatiser le rapprochement | Intermédiaire | [ARC-06](../docs/architecture/blueprints/ARC-06.md) | Écarts, doublons, rapport synthétique |
| [OPB-016](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/16) | Observer des transactions fictives de bout en bout | Intermédiaire | [ARC-09](../docs/architecture/blueprints/ARC-09.md) | Corrélation, traces, logs expurgés |
| [OPB-017](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/17) | Tester les pannes et la reprise | Avancé | [ARC-09](../docs/architecture/blueprints/ARC-09.md) | Pannes injectées et preuves de récupération |
| [OPB-018](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/18) | Construire une CI/CD sécurisée | Intermédiaire | [ARC-10](../docs/architecture/blueprints/ARC-10.md) | Tests, dépendances, contrôles CI |
| [OPB-019](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/19) | Évaluer les exigences techniques de sécurité/conformité | Avancé | [ARC-08](../docs/architecture/blueprints/ARC-08.md) · [ARC-10](../docs/architecture/blueprints/ARC-10.md) | Écarts documentés, aucune certification |
| [OPB-020](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/20) | Démontrer une plateforme intégrée fictive | Avancé | [ARC-10](../docs/architecture/blueprints/ARC-10.md) | Démo isolée, architecture, résultats et limites |

### État du contenu local vérifié

| Lab | Fichier présent | Ce que l'on peut confirmer | Ce qui reste à vérifier |
|---|---|---|---|
| [OPB-001](01-foundations/OPB-001/README.md) | Dossier de recherche et cartographie | Documentation présente dans le dépôt | Exhaustivité, sources, licences et revue de chaque fiche |
| [OPB-D03-001](03-card-payments/OPB-D03-001/README.md) | Dossier et prototype Go ISO 8583 | Fichiers de code, de tests et de démarrage présents | Compatibilité des API, compilation, versions figées, résultats et revue |

**Attention :** `OPB-D03-001` est un **lab spécialisé supplémentaire** (issue [#41](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/41)) ; il ne renumérote pas les vingt sujets initiaux.

## Premier lab spécialisé — OPB-D03-001

**Domaine :** D03 — monétique, cartes, ISO 8583.  
**Objectif :** construire un message de démonstration non sensible, le sérialiser, le décoder et analyser les erreurs de format.

- [Lire le lab](03-card-payments/OPB-D03-001/README.md).
- [Démarrer le prototype Go](03-card-payments/OPB-D03-001/START-HERE.md).
- [Fiches pédagogiques Ingénieur monétique / ISO 8583](../docs/academy/monetique-iso8583/README.md).
- [Architecture cible ARC-02](../docs/architecture/blueprints/ARC-02.md) et [vue BDAT](../docs/architecture/blueprints/ARC-02-BDAT.md).
- [Issue #41](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/41).

**Prochaine étape technique incontournable :** vérifier l'API de la version choisie de Moov ISO8583, figer `go.mod`/`go.sum`, exécuter les tests sur un environnement vierge et **publier l'échec comme le succès** sans inventer de résultats.

## Naviguer par domaine métier et technique

La [taxonomie OSEF de l'écosystème](01-foundations/OPB-001/ecosystem-taxonomy.md) couvre **14 domaines**. Ce regroupement constitue une **vue de navigation**, pas une affirmation de couverture exhaustive de chaque domaine.

| Domaine / ensemble | Labs disponibles en tant que sujets | Architectures correspondantes |
|---|---|---|
| D01 — Core Banking & Microfinance | [OPB-002](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/2), [OPB-003](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/3), [OPB-004](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/4) | [ARC-01](../docs/architecture/blueprints/ARC-01.md) |
| D03 — Cartes, monétique et ISO 8583 | [OPB-D03-001](03-card-payments/OPB-D03-001/README.md) | [ARC-02](../docs/architecture/blueprints/ARC-02.md) |
| D04 — Interopérabilité des paiements | [OPB-005](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/5), [OPB-006](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/6), [OPB-007](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/7), [OPB-008](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/8) | [ARC-03](../docs/architecture/blueprints/ARC-03.md) |
| D05 / D06 / D11 — Wallets, API et orchestration | [OPB-009](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/9) | [ARC-04](../docs/architecture/blueprints/ARC-04.md), [ARC-05](../docs/architecture/blueprints/ARC-05.md), [ARC-07](../docs/architecture/blueprints/ARC-07.md) |
| D07 — Ledger et rapprochement | [OPB-015](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/15) | [ARC-06](../docs/architecture/blueprints/ARC-06.md) |
| D10 — Fraude, sécurité et conformité | [OPB-010](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/10), [OPB-011](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/11), [OPB-012](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/12), [OPB-019](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/19) | [ARC-08](../docs/architecture/blueprints/ARC-08.md) |
| D14 — Exploitation et plateforme technique | [OPB-013](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/13), [OPB-014](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/14), [OPB-016](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/16), [OPB-017](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/17), [OPB-018](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/18) | [ARC-09](../docs/architecture/blueprints/ARC-09.md), [ARC-10](../docs/architecture/blueprints/ARC-10.md) |
| Transversal | [OPB-001](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/1), [OPB-020](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/20) | [ARC-10](../docs/architecture/blueprints/ARC-10.md) |

**Champs sans lab dédié documenté aujourd'hui :** par exemple wallet complet, gateway marchand avancée, ISO 20022 approfondi, transfrontalier et messagerie financière. Ces sujets peuvent faire l'objet de nouvelles issues après vérification des besoins et du périmètre.

## Trois parcours conseillés

### A. Découverte — pour une première contribution
```text
OPB-001 (recherche) → OPB-005 (architecture) → revue d'un BDAT → 1 PR documentaire
```
**Preuve attendue :** références officielles vérifiées, hypothèses explicites, sources datées et PR revue.

### B. Ingénieur monétique / ISO 8583
```text
Socle Git/Go → ARC-02 → OPB-D03-001 → tests négatifs → dossier de preuves → revue
```
Suivre les [six fiches de l'OSEF Academy](../docs/academy/monetique-iso8583/README.md). Le prototype est **à vérifier en exécution**, non « prêt ».

### C. Intégration et fiabilité des paiements
```text
OPB-009 (API) → OPB-010 (IAM) → OPB-013 (événements) → OPB-016 (traces)
         → OPB-017 (pannes) → OPB-018 (CI) → OPB-020 (synthèse)
```
**Attention :** ce chemin est une proposition ; les labs peuvent nécessiter des prérequis et composants qui ne sont pas encore fournis dans le dépôt. Aucune intégration n'est présumée fonctionnelle.

**Parcours complémentaire :** [Ingénierie des paiements numériques et de l'interopérabilité — huit fiches](../docs/academy/paiements-numeriques-interoperabilite/README.md). Les projets pratiques proposés ne signifient pas que les labs sont réalisés.

## Critères de validation d'un lab

Un lab ne passe à « **Validé en laboratoire** » que lorsque les critères établis pour **ce lab précis** ont été vérifiés et la revue documentée.

- [ ] Objectif métier, hypothèses et limites décrits.
- [ ] Prérequis, versions, dépendances et **licences** consignés.
- [ ] Architecture, interfaces, données et diagramme BDAT liés si pertinent.
- [ ] Procédure reproductible, **commandes et scripts commentés**.
- [ ] **Données synthétiques seulement** : aucun PAN, PIN, CVV, secret, compte ou réseau réel.
- [ ] Scénarios nominaux et dégradés exécutés, résultats réellement observés.
- [ ] Mesures, logs et captures expurgés ; nettoyage/rollback décrit.
- [ ] Exigences de sécurité et contraintes réglementaires clairement séparées des démonstrations.
- [ ] Une PR et une issue liées ; revue indépendante documentée si possible (ou absence signalée).
- [ ] Limites techniques et points non vérifiés conservés dans le compte rendu.

**Statuts recommandés :** `Proposé → Documenté → Construit → Testé → Revu → Validé en laboratoire`. Ces statuts ne sont pas un champ GitHub configuré automatiquement. **Validé en laboratoire ne signifie jamais conforme, homologué, certifié ou prêt pour la production.**

## Référentiels et participation

- [Catalogue des architectures de référence ARC-01 à ARC-10](../docs/architecture/blueprints/README.md) et [atlas BDAT](../docs/architecture/blueprints/BDAT-README.md).
- [Parcours communautaire Ingénieur monétique et paiement](../docs/academy/PARCOURS-INGENIEUR-MONETIQUE-PAIEMENT-OSEF.md).
- [Catalogue produits et services envisagés](../docs/strategy/OSEF-PAYMENT-ENGINEERING-PRODUCTS-SERVICES.md).
- [GitHub Project #7](https://github.com/orgs/opensource-enterprise-factory/projects/7/views/1), si accessible et correctement renseigné.
- [Toutes les issues](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues).
- [Proposer un lab](../.github/ISSUE_TEMPLATE/lab.md) · [Guide de contribution](../CONTRIBUTING.md).

### Sécurité et périmètre

OSEF expérimente avec des simulations **entièrement fictives**, en dehors de toute infrastructure de paiement réelle. Aucun lab n'autorise le traitement de fonds, la connexion à une banque ou un switch, ni l'utilisation de données financières ou personnelles réelles. La conformité BCEAO/UEMOA, PCI DSS ou à un scheme doit être examinée par des acteurs habilités et n'est pas certifiée par le dépôt.

### Propriété intellectuelle

Le catalogue présent est une documentation **OSEF** de ses travaux publics. Les curricula, méthodes, kits et documents OPPL marqués confidentiels ne sont pas redistribués ni incorporés dans ces labs sans autorisation écrite du titulaire des droits.

---

## English summary

Welcome to the **OSEF Payment & Banking Labs** catalog. It lists the **first 20 lab proposals** (OPB-001 through OPB-020) plus the specialized **OPB-D03-001 ISO 8583 Go prototype**. **Documented does not mean executed or validated.**

Start with [JOIN-US](../JOIN-US.md), select an [issue](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues), work on a fork/branch, use **synthetic data only**, record real test results and submit a focused PR.

Browse the [BDAT architecture atlas](../docs/architecture/blueprints/BDAT-README.md), the [Payment Engineering Academy](../docs/academy/PARCOURS-INGENIEUR-MONETIQUE-PAIEMENT-OSEF.md) and the [ISO 8583 practical track](../docs/academy/monetique-iso8583/README.md). No live payment rails, production systems, financial customer data or regulatory certification is involved.
