# Contribuer à OSEF Payment & Banking Labs
**Contribution Guide — Français / English**

Bienvenue dans **Open Source Enterprise Factory (OSEF) — Payment & Banking Labs**.

Notre objectif : apprendre collectivement, produire des expérimentations **reproductibles et sécurisées** sur les systèmes bancaires et de paiement, et contribuer aux projets Open Source internationaux. Nous accueillons les développeurs, ingénieurs monétiques, architectes, DevOps, SRE, spécialistes sécurité, data engineers, rédacteurs techniques, traducteurs et praticiens des services financiers.

> **Environnement de laboratoire uniquement.** OSEF ne fournit pas ici de services financiers, ne traite aucun paiement réel et ne revendique ni homologation BCEAO/PI-SPI, ni certification PCI DSS, ni approbation des fondations ou mainteneurs amont.

**Navigation :** [Démarrer](#1--démarrer-en-5-étapes) · [Types de contributions](#2--que-pouvez-vous-apporter-) · [Cycle de vie](#3--cycle-de-vie-dune-contribution) · [Exigences de qualité](#4--définition-de-terminé--definition-of-done) · [Sécurité](#5--sécurité-et-données-financières) · [Upstream](#7--contribuer-aux-projets-amont) · [English](#english--contributing-guide)

## 1 — Démarrer en 5 étapes

1. **Lire les règles** : [README](README.md), [Sécurité](SECURITY.md) [JOIN-US](JOIN-US.md) et [Code de conduite](CODE_OF_CONDUCT.md).
2. **Choisir un sujet** : [catalogue des 20 premiers labs](labs/README.md), [issues ouvertes](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues), ou [architectures BDAT](docs/architecture/blueprints/BDAT-README.md).
3. **Signaler son intention** : commenter l'issue : `Je souhaite contribuer à OPB-XXX — domaine : … — contribution envisagée : …`. N'annoncer de disponibilité ou de responsabilité que si elle est confirmée.
4. **Proposer une modification** dans une branche personnelle ou un fork, sans pousser directement sur `main` pour les contributions ordinaires.
5. **Ouvrir une Pull Request (PR)** reliant l'issue, décrivant les tests exécutés et demandant une revue.

**Premières portes d'entrée :**
- [OPB-001 — cartographie Open Source bancaire](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/1) : recherche, sources, licences, documentation.
- [OPB-002 — Apache Fineract](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/2) : déploiement et tests de Core Banking fictif.
- [OPB-005 — Mojaloop](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/5) : architecture et flux de paiements simulés.
- [OPB-D03-001 — Moov ISO8583](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/41) : code de laboratoire Go, compilation et tests **à confirmer**.

Les sujets portant la mention « proposé » ou « prototype non validé » ne doivent jamais être présentés comme réalisés.

## 2 — Que pouvez-vous apporter ?

| Type | Exemples | Preuve attendue |
|---|---|---|
| **Documentation** | README, tutoriels FR/EN, glossaires, corrections de liens | PR documentaire et sources |
| **Recherche / écosystème** | Licence, gouvernance, état de maintenance, catalogue OPB-001 | Fiche datée et liens officiels |
| **Architecture** | Cas d'usage, BDAT, diagrammes, interfaces, ADR | Diagramme source + décisions et limites |
| **Développement** | Simulateurs, mocks API, adaptateurs de lab, scripts | Code testé et explicité |
| **QA / tests** | Scénarios nominaux, négatifs, idempotence, non-régression | Commandes + résultats réellement observés |
| **Sécurité et SRE** | Threat modeling, secrets de test, observabilité, reprise | Contrôles documentés et preuves expurgées |
| **Contribution upstream** | Rapport de bug, test, documentation ou correctif vers le projet d'origine | Lien vers l'échange/issue/PR amont et son **statut réel** |
| **Relecture / transmission** | Vérification des tests, traduction, démonstration technique | Commentaires de revue et recommandations |

Les propositions de meetups sont bienvenues mais **un meetup non confirmé ne doit pas être annoncé comme programmé**.

## 3 — Cycle de vie d'une contribution

### A. Préparer l'issue

Chercher si le sujet existe déjà. S'il manque, utiliser les modèles GitHub : [LAB](.github/ISSUE_TEMPLATE/lab.md), [MEETUP](.github/ISSUE_TEMPLATE/meetup.md) ou [UPSTREAM](.github/ISSUE_TEMPLATE/upstream.md).

L'issue doit contenir : **contexte, objectif, périmètre/exclusions, architecture ou sources, prérequis, livrable, critères d'acceptation, risques, dépendances, personne responsable si confirmée et statut**.

Pour les nouveaux labs, utiliser un identifiant unique cohérent (`OPB-XXX` ou `OPB-Dxx-XXX`). **Ne pas réutiliser** un identifiant existant. Les étiquettes et les statuts du GitHub Project doivent refléter l'avancement réel, et non une progression supposée.

### B. Développer dans une branche

Exemple local **sans effet sur la production** :

```bash
# Récupère le dépôt public; ne copie aucune donnée bancaire réelle dedans.
git clone https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs.git
cd osef-open-source-payment-banking-labs

# Part de la version courante de main.
git switch main
git pull --ff-only

# Crée une branche personnelle pour éviter de modifier directement main.
git switch -c docs/opb-001-matrix-update

# Après modification, contrôler ce qui sera publié et éviter les secrets.
git status
git diff --check
git diff

# Indexe uniquement les fichiers voulus : éviter git add . sans inspection.
git add labs/01-foundations/OPB-001/project-matrix.md

# Message de commit clair, lié au périmètre.
git commit -m "docs(OPB-001): verify ecosystem sources"

# Publier la branche sur un dépôt où vous avez droit d'écriture,
# ou pousser vers votre fork si vous contribuez depuis l'extérieur.
git push -u origin docs/opb-001-matrix-update
```

Si vous travaillez depuis un **fork**, adaptez les remotes `origin` et `upstream` : ne supposez pas disposer des droits d'écriture sur le dépôt OSEF. Ces commandes nécessitent Git installé; aucune commande de déploiement bancaire n'est incluse.

### C. Ouvrir la PR

Titre recommandé : `docs(OPB-001): update verified project matrix` ou `test(OPB-D03-001): add ISO8583 negative cases`.

Dans la description, préciser :
- **Issue liée** (`Relates to #…`, ou `Closes #…` uniquement si la PR la termine réellement).
- Objectif, périmètre, changements et éléments volontairement exclus.
- **Versions** des outils et dépendances et instructions pour reproduire.
- Tests **effectivement exécutés** (commandes, résultats, environnement) et tests **non exécutés** avec justification.
- Risques : licences, exposition des données, sécurité, compatibilité.
- Preuves expurgées : logs, captures, références et diagrammes.
- Demande de revue et décisions en suspens.

Ne cochez jamais un test que vous n'avez pas exécuté. Une CI configurée n'est pas une CI passée.

### D. Revue et fusion

Les changements ordinaires devraient recevoir **au moins une revue humaine indépendante** avant fusion. Pour l'authentification, les données, les protocoles de paiement, les secrets et les interfaces sensibles, rechercher aussi une revue de sécurité et/ou métier adaptée. La disponibilité des réviseurs n'est pas présumée.

Un mainteneur peut demander des corrections ou refuser une PR insuffisamment fondée. La fusion ne constitue **ni une homologation de production ni un accord de sécurité**. Après fusion, l'issue est mise à jour avec les preuves et limites.

## 4 — Définition de terminé / Definition of Done

### Checklist commune aux labs
- [ ] Objectif métier et périmètre de simulation compréhensibles.
- [ ] Versions, dépendances, licences et sources officielles identifiées.
- [ ] Architecture / flux / contrats documentés lorsque pertinents.
- [ ] Installation et scripts **commentés** : raison des choix, risques, nettoyage, différence lab/production.
- [ ] Données **entièrement synthétiques** sans information financière personnelle ni secrets.
- [ ] Scénario nominal et au moins un scénario négatif testés si applicable.
- [ ] Résultats observés et commandes réellement exécutées consignés.
- [ ] Logs et captures expurgés, date/environnement et limites visibles.
- [ ] Reproductibilité contrôlée par une seconde personne si possible; toute absence indiquée.
- [ ] Documentation et PR relues, issue liée et statut actualisé.

### Exigences propres aux BDAT et architectures
Une vue **Business / Data / Application / Technology** doit distinguer acteurs, données, applications et technologies, puis indiquer les **hypothèses et interfaces non validées**. Un diagramme Mermaid rendu dans GitHub ne prouve pas que les composants sont intégrés.

Références : [catalogue de blueprints](docs/architecture/blueprints/README.md) · [template](docs/architecture/blueprints/BLUEPRINT-TEMPLATE.md).

### Niveaux de maturité
`Proposé → Construit → Testé → Revu → Validé en laboratoire`.

« Validé en laboratoire » signifie seulement que les critères de test du lab sont satisfaits avec preuve. Il ne signifie jamais « prêt pour production », « certifié » ou « agréé ».

## 5 — Sécurité et données financières

**Règle non négociable : aucun accès bancaire réel ni aucune transaction réelle.** Lire [SECURITY.md](SECURITY.md).

**Interdits dans GitHub (issues, commits, logs, captures et PR) :**
- Numéros de carte réels ou complets (PAN), pistes magnétiques, PIN, CVV/CVC, cryptogrammes ou identifiants de paiement réels.
- Secrets, tokens, clés privées, certificats de production, accès HSM, mots de passe et fichiers `.env` remplis.
- Données bancaires, relevés, fichiers clients ou informations personnelles réelles, même « anonymisées » sans contrôle.
- Adresses ou configurations confidentielles d'infrastructures réelles, tests non autorisés et scans de tiers.

**À faire :** utiliser des identités synthétiques, numéros fictifs qui ne représentent aucun compte ou instrument financier actif, services mockés, isolation réseau, privilèges minimaux, logs expurgés et scans de secrets adaptés. Si vous suspectez une fuite, **arrêtez la publication**, ne la recopiez pas dans une issue publique et utilisez un canal privé de signalement / les responsables du dépôt; révoquez les secrets via leur propriétaire si nécessaire.

Les tests de sécurité ou de performance sur des systèmes tiers exigent une autorisation explicite écrite. Ne pas prétendre à une conformité BCEAO/PI-SPI ou PCI DSS sur la base d'un lab.

## 6 — Qualité, licences et intégrité technique

- Documenter les licences des **dépendances et des fichiers copiés**, conserver leurs avis de copyright. **Ne pas supposer** que la licence du dépôt couvre automatiquement toute dépendance.
- Ne pas importer de code propriétaire, de schémas confidentiels, de spécifications sous restriction ou de données de clients.
- Vérifier chaque affirmation de fonctionnalité, version, certification, conformité ou maintenance à partir d'une source officielle; ajouter une date de vérification.
- Pour toute modification technique, fournir des tests et ne pas affirmer qu'ils ont réussi sans preuve.
- Éviter l'introduction de dépendances inutiles; figer versions et empreintes de dépendances pour les labs reproductibles.
- Documenter le statut des contributions et **déclarer l'utilisation significative d'outils d'IA** lorsque le projet amont ou les règles applicables l'exigent; toujours relire, tester et assumer les changements soumis.
- Les contributions restent attribuées à leurs auteurs selon les licences et conventions applicables. Aucune rémunération ou prestation contractuelle n'est implicite dans une contribution communautaire.

## 7 — Contribuer aux projets amont

OSEF **n'est pas** Apache Fineract, Mojaloop, Moov, jPOS, Mifos ou FINOS et ne promet ni approbation ni soutien officiel de ces projets.

1. Sélectionner le **dépôt amont précis**, depuis [OPB-001](labs/01-foundations/OPB-001/README.md).
2. Lire les règles `CONTRIBUTING`, licence, code de conduite et consignes de sécurité **du projet amont**.
3. Vérifier qu'une issue est encore ouverte et libre, ou discuter d'abord une proposition avec les mainteneurs.
4. Reproduire le problème, préparer un correctif limité et exécuter les tests exigés.
5. Soumettre la contribution selon les règles upstream (CLA, DCO, signature, politique d'IA, etc. **seulement si requises**).
6. Documenter dans une issue OSEF de type `UPSTREAM` les liens, échanges et le **statut réel** : proposé, soumis, en revue, accepté ou refusé.

**Une PR upstream soumise n'est pas une contribution acceptée.** Éviter les contributions de masse sans qualité ou non sollicitées.

## 8 — Communication, respect et gouvernance

- Bienvenue aux contributions en **français et en anglais**. Pour les guides essentiels, privilégier un résumé bilingue; les échanges techniques avec un projet upstream suivent la langue et les règles de celui-ci.
- Être précis, respectueux et constructif : critiquer le code et les idées, pas les personnes. Respecter le [Code de conduite OSEF](CODE_OF_CONDUCT.md) : échanges courtois, absence de harcèlement, discrimination, attaques personnelles et représailles. Les incidents de conduite doivent être signalés avec discrétion selon sa procédure ; ne pas publier de données privées.
- Les issues et PR du dépôt public sont visibles mondialement. Ne publiez ni numéros de téléphone, ni coordonnées personnelles, ni documents de clients, ni informations sur vos employeurs sans permission.
- Les labels, rôles, dates et responsabilités doivent être **confirmés**. Ne pas s'auto-attribuer des privilèges de mainteneur, une affiliation institutionnelle ou une certification.
- Les prestations commerciales éventuelles d'OSEF sont distinctes des contributions bénévoles : voir [catalogue produits/services](docs/strategy/OSEF-PAYMENT-ENGINEERING-PRODUCTS-SERVICES.md). Les droits, la rémunération et la confidentialité sur une mission client doivent être contractualisés séparément.

## 9 — Liens utiles

- [Issues à rejoindre](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues)
- [GitHub Project OSEF Payment & Banking](https://github.com/orgs/opensource-enterprise-factory/projects/7)
- [Catalogue des labs](labs/README.md)
- [Atlas BDAT](docs/architecture/blueprints/BDAT-README.md)
- [Politique de sécurité](SECURITY.md)
- [Code de conduite](CODE_OF_CONDUCT.md)
- [Guide de participation](JOIN-US.md)

---

## English — Contributing guide

**OSEF Payment & Banking Labs** welcomes developers, financial engineers, DevOps, SRE, security specialists, researchers, documentation writers and translators.

### Quick start
1. Read [README](README.md), [SECURITY.md](SECURITY.md), [JOIN-US](JOIN-US.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).
2. Pick a [lab](labs/README.md) or [open issue](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues); comment to express interest.
3. Fork or create a feature branch (if you have write access), then make a focused change.
4. Run and document the actual tests, sanitize evidence, and submit a pull request linked to an issue.
5. Address independent review feedback before merging.

### Contribution types
Documentation/translation, ecosystem mapping, BDAT architecture, code, synthetic-data simulators, automated tests, security/SRE, upstream contributions, and technical review are all welcome.

### Pull request essentials
Describe the problem, changes, known limitations, dependencies and licenses, exact commands and **observed** test results, security implications, sanitized logs, and linked issue. Never claim a test or certification that has not happened.

### Strict financial safety
**Synthetic data only. No live bank or payment connection.** Never upload real account/card data, PAN, PIN, CVV, secrets, production certificates, customer logs, or confidential host specifications. Do not scan or test third-party financial systems without written authorization. Use private security reporting channels for suspected leaks.

### Upstream and community rules
Follow each upstream project's contribution policies, licensing, CLA/DCO/signing and AI disclosure requirements where applicable. A submitted PR is not necessarily an accepted contribution. Communicate respectfully and distinguish community volunteering from separately contracted client work.

### Done means evidenced
A lab is finished only when its documented criteria have been met, tested and reviewed, with honest reporting of unexecuted tests. **Lab validation is not production certification.**

Welcome to OSEF — **learn, build, test, document, contribute.**
