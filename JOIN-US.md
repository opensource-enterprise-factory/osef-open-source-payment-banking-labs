# Rejoindre OSEF Payment & Banking Labs
## JOIN US — Contribuer depuis l'Afrique francophone et au-delà

**Bienvenue dans Open Source Enterprise Factory (OSEF) — Payment & Banking Labs.**

Ce programme communautaire vise à **apprendre, expérimenter, documenter et contribuer** aux technologies Open Source de la banque, de la microfinance, de la monétique et des paiements. Nous voulons produire des laboratoires reproductibles, des architectures documentées et des contributions vérifiables aux projets internationaux.

> **Participation ouverte, sur la base des contributions.** Il n'est pas nécessaire d'être employé d'une banque, de détenir une certification ou de maîtriser parfaitement l'anglais. La participation à ce dépôt ne constitue ni un contrat de travail, ni une promesse de mission, de rémunération, de mentorat individualisé ou d'accès à des systèmes financiers.

**Nouveau :** [Parcours communautaire Ingénieur monétique & paiements — compétences et labs OSEF](docs/academy/PARCOURS-INGENIEUR-MONETIQUE-PAIEMENT-OSEF.md). Ce parcours est proposé, non diplômant et distinct des programmes confidentiels OPPL.

**Accès rapide :** [Trouver un lab](labs/README.md) · [Issues ouvertes](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues) · [Comment contribuer](CONTRIBUTING.md) · [Code de conduite](CODE_OF_CONDUCT.md) · [Sécurité](SECURITY.md) · [Atlas BDAT](docs/architecture/blueprints/BDAT-README.md)

---

## 1. À qui s'adresse le programme ?

| Profil | Contributions possibles |
|---|---|
| Développeuse / développeur (Go, Java, Python, autres) | Simulateurs, API, connecteurs de lab, tests, corrections |
| Ingénieur monétique ou paiement | Scénarios ISO 8583, modèles de messages fictifs, analyse des erreurs |
| Ingénieur Core Banking / microfinance | Architecture Fineract, modèles comptes/prêts fictifs, interfaces |
| DevOps / SRE / Cloud | Automatisation, observabilité, tests de reprise, fiabilité |
| Spécialiste sécurité / IAM | Analyse de menaces, contrôle d'accès, tests défensifs |
| Data / ledger / rapprochement | Jeux d'écritures synthétiques, cohérence, réconciliation |
| Architecte d'entreprise | Vues BDAT, contrats, ADR, revue des choix |
| Rédacteur, traducteur, étudiant, débutant | Documentation FR/EN, tutoriels, recherche et reproduction des labs |

**Aucune expérience bancaire préalable obligatoire pour les travaux de documentation et de découverte.** Certaines tâches exigent des compétences plus avancées, indiquées dans l'issue concernée.

## 2. Participer en cinq étapes

### Étape 1 — Se familiariser avec les règles

Lire :
- [README du programme](README.md) : ambition et limites.
- [CONTRIBUTING.md](CONTRIBUTING.md) : Git, issues, pull requests et critères de qualité.
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) : respect, attribution et collaboration.
- [SECURITY.md](SECURITY.md) : données synthétiques, signalement privé et sécurité.

**Obligatoire pour chaque lab :** aucune donnée de client, carte ou compte réel ; aucun secret ; aucune connexion à un système bancaire ou réseau de paiement de production.

### Étape 2 — Choisir sa première contribution

Trois parcours possibles :

**A. DISCOVER — Découvrir et documenter**
- Cartographier un logiciel, lire sa documentation officielle, relever la licence et les incertitudes.
- Améliorer une traduction, un glossaire, un README ou un diagramme.
- Point de départ : [OPB-001 — cartographie des projets](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/1).

**B. BUILD — Construire un lab**
- Développer, tester et documenter un simulateur, une API ou une architecture reproductible.
- Points de départ : [OPB-002 — Apache Fineract](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/2), [OPB-005 — Mojaloop](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/5), [OPB-D03-001 — Moov ISO8583](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/41).
- **Important :** le prototype ISO 8583 du dépôt n'est pas encore déclaré compilé et validé ; les contributeurs peuvent justement participer à cette vérification.

**C. CONTRIBUTE UPSTREAM — Contribuer aux communautés d'origine**
- Lire les règles du dépôt amont, identifier une tâche réellement ouverte, discuter avec les mainteneurs, préparer une contribution ciblée.
- Documenter les liens et le statut réel dans une issue OSEF ; **une PR envoyée n'est pas nécessairement une PR acceptée**.

Consulter le [catalogue initial des labs](labs/README.md), la [cartographie des quatorze domaines](labs/01-foundations/OPB-001/ecosystem-taxonomy.md) et les [architectures BDAT](docs/architecture/blueprints/BDAT-README.md).

### Étape 3 — Se manifester dans une issue existante

Vous pouvez laisser un commentaire public **minimal**, sans formulaire nominatif obligatoire :

```text
Bonjour, je souhaite contribuer à [ID de l'issue].

GitHub : @mon-pseudo
Parcours : DISCOVER / BUILD / UPSTREAM
Contribution proposée : [ex. relire la documentation, reproduire un test, écrire un test négatif]
Niveau sur ce sujet : découverte / intermédiaire / confirmé
Prochaine action : [une tâche concrète]
Besoin de clarification : [facultatif]
```

**Ne partagez pas :** téléphone, adresse privée, pièce d'identité, employeur non autorisé, données clients, coordonnées personnelles, justificatifs professionnels, secrets ou informations bancaires. Votre pseudo GitHub suffit pour commencer.

L'issue doit indiquer la disponibilité réelle de la tâche. **Un commentaire ne vaut pas attribution automatique** : la coordination et les droits de dépôt dépendent des mainteneurs et de leurs disponibilités.

### Étape 4 — Réaliser une contribution limitée et reproductible

Exemples de premières contributions :
- Corriger un lien de documentation avec une source officielle.
- Vérifier une licence et ajouter la date de vérification dans OPB-001.
- Ajouter un scénario de test négatif au lab ISO 8583.
- Clarifier une interface ou un flux sur un blueprint BDAT.
- Reproduire un lab sur un poste local, documenter un échec et proposer un correctif.

Pour le code, utilisez un **fork** si vous ne disposez pas des droits en écriture. Créez une branche dédiée, conservez des modifications limitées, exécutez les tests possibles et ouvrez une **pull request** liée à l'issue. Décrivez les commandes commentées, les résultats **observés**, les tests **non exécutés** et les limites.

Suivez la procédure détaillée dans [CONTRIBUTING.md](CONTRIBUTING.md).

### Étape 5 — Faire relire et transmettre

- Demander une revue technique adaptée au changement, sans supposer une disponibilité immédiate.
- Corriger les points soulevés, documenter les décisions et garder les preuves expurgées.
- Mettre à jour l'issue avec le statut véritable.
- Si la contribution est fusionnée, envisager de présenter le lab ou d'aider un autre contributeur, de manière volontaire.

**Une contribution est reconnue par ses preuves publiques, son attribution Git et sa qualité, pas par un titre auto-attribué.**

## 3. Progression proposée des contributeurs

| Étape | Ce que vous pouvez démontrer | Exemple |
|---|---|---|
| **Explorer** | Compréhension d'un projet et de sa documentation | Fiche de source relue |
| **Contributor** | Une contribution OSEF concrète, documentée et revue | PR dans un lab |
| **Lab Contributor** | Reproduction, tests et amélioration d'un lab | Tests et résultats expurgés |
| **Upstream Contributor** | Participation directe à un projet amont | Issue ou PR amont, avec statut précisé |
| **Reviewer / Mentor** | Relectures utiles et transmission des savoirs | Historique de revues et tutoriels |
| **Lab Lead / Maintainer** | Responsabilités explicitement confiées | Désignation confirmée et périmètre clair |

**Cette progression est pédagogique et indicative.** Elle ne constitue pas une certification, une politique de promotion automatique ou une nomination. Les rôles de revue et de maintenance exigent une décision de gouvernance et des permissions GitHub appropriées.

## 4. Les règles de collaboration OSEF

1. **Open Source :** respecter les licences, les projets amont, les auteurs et leurs consignes.
2. **Open Collaboration :** s'entraider, laisser des retours factuels, accueillir les débutants et les contributions FR/EN.
3. **Security by Design :** aucun système financier réel, secret, PAN, PIN, CVV ou donnée personnelle de client dans le dépôt.
4. **Evidence First :** distinguer une hypothèse, un prototype, un test réussi et une intégration validée.
5. **Documentation First :** les scripts doivent être commentés, les versions et dépendances précisées.
6. **Transparence :** pas de fausse affiliation, certification, approbation de régulateur ou partenariat.
7. **Participation volontaire :** aucune disponibilité imposée, pas de mission commerciale implicite.

Les contributions aux labs sont distinctes des **prestations commerciales OSEF** : toute mission pour une entreprise, toute rémunération et tout transfert de propriété intellectuelle nécessitent un accord spécifique. Voir le [catalogue de produits et services envisagés](docs/strategy/OSEF-PAYMENT-ENGINEERING-PRODUCTS-SERVICES.md).

## 5. Que faut-il installer ?

**Pour une contribution documentaire :**
- Un compte GitHub et un navigateur peuvent suffire.
- Git en ligne de commande est utile, mais pas obligatoire pour proposer une correction dans l'éditeur GitHub si les permissions le permettent.

**Pour une contribution technique :**
- Git et les outils du lab choisi (ex. Go, Java, Docker) selon sa documentation.
- Un environnement **local ou isolé**, avec uniquement des données synthétiques.
- Les versions, ressources CPU/RAM, ports et coûts varient selon le lab : **aucune machine universelle n'est imposée**.

La [sécurité](SECURITY.md) prime sur la simplicité du démarrage. Aucun accès à des environnements clients n'est nécessaire.

## 6. Suivre les travaux et les événements

- [Issues GitHub du programme](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues) : source de vérité sur les tâches.
- [GitHub Project #7](https://github.com/orgs/opensource-enterprise-factory/projects/7/views/1) : espace de pilotage, si accessible.
- [Catalogue des 20 premiers labs](labs/README.md) : parcours initial, non exhaustif.
- [Propositions de meetup](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues) : rechercher les issues concernées.

**Aucun événement, responsable, date de revue ou calendrier de mentorat n'est garanti par cette page.** Se fier uniquement aux annonces publiées et confirmées par les organisateurs.

## 7. Questions fréquentes

**Puis-je rejoindre OSEF si je débute en paiements ?**  
Oui. Commencez par une recherche sourcée, une documentation ou un test guidé.

**Faut-il résider dans l'UEMOA ?**  
Non. Le programme privilégie les besoins de l'Afrique francophone, tout en accueillant les contributions de toute provenance compatibles avec ses règles.

**Faut-il parler anglais ?**  
Vous pouvez commencer en français. Un niveau d'anglais technique aide pour contribuer à certains dépôts amont.

**Y a-t-il un coût d'inscription ou un formulaire à remplir ?**  
Cette page ne prévoit ni frais d'adhésion, ni formulaire nominatif obligatoire. Manifestez-vous sur une issue avec votre pseudo GitHub. Les autres conditions éventuelles d'une structure associative ou commerciale ne sont pas définies ici.

**Une PR me rend-elle ingénieur OSEF, mainteneur ou salarié ?**  
Non. Les droits de maintenance, rôles officiels et contrats sont distincts des contributions bénévoles.

**Mes contributions peuvent-elles être mises en valeur ?**  
Les commits, PR et issues publics constituent des éléments vérifiables de votre activité. Toute autre attestation ou certification nécessiterait un processus explicitement défini.

**Comment déclarer une vulnérabilité ou un comportement inapproprié ?**  
Consultez [SECURITY.md](SECURITY.md) pour les vulnérabilités et [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) pour les signalements de conduite. **Ne publiez pas de données sensibles dans une issue.**

---

## English — Join OSEF Payment & Banking Labs

**Welcome!** This community repository helps engineers explore open-source banking and payment technologies, build isolated labs with synthetic data, document reproducible results, and contribute to upstream projects.

### Five steps to join

1. Read [README](README.md), [CONTRIBUTING](CONTRIBUTING.md), [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md) and [SECURITY](SECURITY.md).
2. Choose a task in the [lab catalog](labs/README.md) or [open issues](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues).
3. Comment on the chosen issue with your **GitHub handle**, contribution track (**DISCOVER / BUILD / UPSTREAM**), concrete task and optional question. Do **not** post personal contact details, employer/client secrets, financial information or credentials.
4. Create a focused pull request with commented instructions, synthetic data and **real observed test results**. Use a fork unless you have repository write access.
5. Ask for review, address feedback and link the evidence back to the issue.

**Who can contribute?** Developers, payment and banking engineers, DevOps, SRE, architects, security and data specialists, students, technical writers, translators and reviewers. Beginners are welcome.

**Community contributions are voluntary.** Participation does not guarantee employment, payment, mentorship availability, repository permissions or a certification. Formal roles and paid customer work require separate agreements.

**Safety:** lab only — no live payment rails, real customer/card data, PIN/CVV/PAN, production secrets or unauthorized access to third-party systems.

**Get started:** [Browse issues](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues) · [Read the contributing guide](CONTRIBUTING.md) · [Explore BDAT architectures](docs/architecture/blueprints/BDAT-README.md).

**Learn · Build · Test · Document · Contribute.**
