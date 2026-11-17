# Atlas OSEF — 40 vues BDAT séparées (B / D / A / T)

**Version 1.0 — 17 novembre 2026 · Statut : vues conceptuelles proposées.**  
Ce catalogue décompose les **10 architectures cibles** en **4 visuels Mermaid indépendants** chacun, soit **40 fiches**. Elles sont modifiables directement dans GitHub.

## Accès direct aux vues

| Architecture | Business (B) | Data (D) | Application (A) | Technology (T) | Synthèse |
|---|---|---|---|---|---|
| **[ARC-01 — Core Banking & Microfinance](ARC-01.md)** | [B](ARC-01-B.md) | [D](ARC-01-D.md) | [A](ARC-01-A.md) | [T](ARC-01-T.md) | [BDAT](ARC-01-BDAT.md) |
| **[ARC-02 — Card Payment & ISO 8583](ARC-02.md)** | [B](ARC-02-B.md) | [D](ARC-02-D.md) | [A](ARC-02-A.md) | [T](ARC-02-T.md) | [BDAT](ARC-02-BDAT.md) |
| **[ARC-03 — Payment Interoperability Hub](ARC-03.md)** | [B](ARC-03-B.md) | [D](ARC-03-D.md) | [A](ARC-03-A.md) | [T](ARC-03-T.md) | [BDAT](ARC-03-BDAT.md) |
| **[ARC-04 — Mobile Money & Wallet Platform](ARC-04.md)** | [B](ARC-04-B.md) | [D](ARC-04-D.md) | [A](ARC-04-A.md) | [T](ARC-04-T.md) | [BDAT](ARC-04-BDAT.md) |
| **[ARC-05 — Open Banking API Platform](ARC-05.md)** | [B](ARC-05-B.md) | [D](ARC-05-D.md) | [A](ARC-05-A.md) | [T](ARC-05-T.md) | [BDAT](ARC-05-BDAT.md) |
| **[ARC-06 — Financial Ledger & Reconciliation](ARC-06.md)** | [B](ARC-06-B.md) | [D](ARC-06-D.md) | [A](ARC-06-A.md) | [T](ARC-06-T.md) | [BDAT](ARC-06-BDAT.md) |
| **[ARC-07 — Merchant Payment Gateway](ARC-07.md)** | [B](ARC-07-B.md) | [D](ARC-07-D.md) | [A](ARC-07-A.md) | [T](ARC-07-T.md) | [BDAT](ARC-07-BDAT.md) |
| **[ARC-08 — Payment Fraud & Security](ARC-08.md)** | [B](ARC-08-B.md) | [D](ARC-08-D.md) | [A](ARC-08-A.md) | [T](ARC-08-T.md) | [BDAT](ARC-08-BDAT.md) |
| **[ARC-09 — Payment Observability & Resilience](ARC-09.md)** | [B](ARC-09-B.md) | [D](ARC-09-D.md) | [A](ARC-09-A.md) | [T](ARC-09-T.md) | [BDAT](ARC-09-BDAT.md) |
| **[ARC-10 — Payment Integration & Testing Factory](ARC-10.md)** | [B](ARC-10-B.md) | [D](ARC-10-D.md) | [A](ARC-10-A.md) | [T](ARC-10-T.md) | [BDAT](ARC-10-BDAT.md) |

**Utilisation dans OSEF Academy :** [matrice des 21 modules, compétences, vues BDAT et preuves](../../academy/MATRICE-COMPETENCES-BDAT-LABS.md).

## Comment étudier une architecture ?

1. **B — Business (bleu) :** acteurs et processus, objectifs métiers, événements, exceptions et responsabilités.
2. **D — Data (vert) :** objets, identifiants, états, cohérence, déduplication, journalisation et confidentialité.
3. **A — Application (violet) :** services, API, adaptateurs, contrats, dépendances, erreurs et limites des mocks.
4. **T — Technology (orange) :** runtime, stockage, réseau, déploiement, sécurité, observabilité, licences et exploitation.
5. **Synthèse BDAT :** lecture transverse et vérification des dépendances entre les quatre couches.

**Chaque fiche contient :** visuel Mermaid, descriptif, prérequis, exigences détaillées numérotées, livrables, critères de revue, limites, labs liés et navigation inter-vues.

## Règles de qualité
- **Source d'architecture :** la fiche `ARC-XX.md` et les labs publics, pas des documents confidentiels.
- **Statut :** une vue documentée **n'est pas** un composant déployé, testé ni homologué.
- **Contrats :** un schéma de blocs ne suffit pas ; définir ensuite interface, données, états, SLA de laboratoire, erreurs et preuves.
- **Sécurité :** aucune donnée financière personnelle, carte, PAN, PIN, CVV, secret ni réseau de paiement réel.
- **Liberté logicielle :** vérifier licence, version et obligations des dépendances avant déploiement.
- **Revue :** faire vérifier la cohérence B–D–A–T et relier les décisions aux issues des labs.
- **Confidentialité :** les supports privés OPPL ne sont pas reproduits dans ces fiches.

## Prochaine étape de modélisation

Pour transformer ces vues conceptuelles en blueprints d'architecture de plus haute précision : ajouter dictionnaires de données, diagrammes d'états et de séquence, catalogue de contrats API/protocoles, scénarios de sécurité et preuves de test. Une modélisation ArchiMate formelle requiert un travail supplémentaire et ne peut être déduite automatiquement des seules figures Mermaid.

[Atlas BDAT historique](BDAT-README.md) · [Catalogue ARC-01 à ARC-10](README.md) · [Règles de sécurité](../../../SECURITY.md)

**EN:** 40 separate editable Mermaid diagrams (Business, Data, Application, Technology) for 10 proposed OSEF architectures. They are planning artifacts, not validated production integrations.
