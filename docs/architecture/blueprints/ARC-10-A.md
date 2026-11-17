# ARC-10-A — Application · Payment Integration & Testing Factory

**Version 0.1 — 17 novembre 2026 · Vue proposée, non validée en laboratoire.**

> La vue est conceptuelle et se fonde sur le [blueprint ARC-10](ARC-10.md). Aucun paiement, banque, compte, secret ou réseau réel. Aucune homologation ni compatibilité intégrée démontrée.

## 1. Diagramme Mermaid modifiable
```mermaid
flowchart LR
  subgraph V["Application — Payment Integration & Testing Factory"]
    direction LR
    X1["Simulateur API/ISO8583"]
    X2["Runner de tests"]
    X3["Collecteur rapports"]
    X4["Revue de résultats"]
  end
  X1 -->|"sollicite"| X2
  X2 -->|"appelle"| X3
  X3 -->|"expose"| X4
  classDef layer fill:#f0e8fc,stroke:#4a637e,color:#183040;
  class X1,X2,X3,X4 layer;
```

## 2. Descriptif
La vue applicative décrit des responsabilités et des contrats envisagés, sans présumer de la compatibilité ou de la mise en œuvre réelle des composants.

**Éléments de la couche :**
- **Simulateur API/ISO8583** : rôle et comportement exacts à confirmer.
- **Runner de tests** : rôle et comportement exacts à confirmer.
- **Collecteur rapports** : rôle et comportement exacts à confirmer.
- **Revue de résultats** : rôle et comportement exacts à confirmer.

**Aspects spécifiques à cette architecture :**
- Simulateur ↔ runner : contrat
- Runner ↔ rapport : résultat
- Rapport ↔ reviewer : preuve

## 3. Prérequis
- Lecture des schémas d'architecture applicative.
- API, contrats, messages, idempotence et erreurs.
- Principes d'authentification et d'intégration.

## 4. Exigences détaillées
- [ ] **ARC-10-A-01 :** Définir les responsabilités de chaque application et son API.
- [ ] **ARC-10-A-02 :** Versionner les contrats d'interface et formats d'erreur.
- [ ] **ARC-10-A-03 :** Documenter succès, échec, timeout, retry et réexécution.
- [ ] **ARC-10-A-04 :** Préciser IAM, secrets de lab et frontière de confiance.
- [ ] **ARC-10-A-05 :** Distinguer les mocks, composants candidats et composants testés.

## 5. Preuves attendues
- [ ] Acteurs, objets, interfaces ou composants explicités dans un registre.
- [ ] Diagramme relu par un praticien concerné ; décisions et hypothèses tracées.
- [ ] Contrat, dictionnaire, cas de test ou mesures adaptés à la couche.
- [ ] Versions et licences vérifiées lorsqu'un composant externe est cité.
- [ ] Résultat observé distinct du résultat attendu ; absence de test signalée.
- [ ] Aucune donnée sensible réelle, fichiers et logs expurgés.

## 6. Risques, statut, traçabilité
- Les liens du diagramme sont des **relations proposées** et ne démontrent pas l'existence de connecteurs.
- Un timeout ne signifie pas systématiquement une opération rejetée.
- Aucun contrôle de sécurité, métrique de production ou conformité réglementaire ne peut être déduit de cette fiche.
- **Labs/études liés :** OPB-D03-001, OPB-009, OPB-018, OPB-020 ; état de validation à vérifier dans les issues.

## 7. Navigation
[Business](ARC-10-B.md) · [Data](ARC-10-D.md) · [Application](ARC-10-A.md) · [Technology](ARC-10-T.md) · [Synthèse BDAT](ARC-10-BDAT.md) · [Blueprint complet](ARC-10.md) · [Atlas](BDAT-4-VUES-README.md)

**English summary:** Proposed standalone Application view of Payment Integration & Testing Factory, documented for offline, synthetic labs only; independent review and tests are pending.
