# ARC-08-A — Application · Payment Fraud & Security

**Version 0.1 — 17 novembre 2026 · Vue proposée, non validée en laboratoire.**

> La vue est conceptuelle et se fonde sur le [blueprint ARC-08](ARC-08.md). Aucun paiement, banque, compte, secret ou réseau réel. Aucune homologation ni compatibilité intégrée démontrée.

## 1. Diagramme Mermaid modifiable
```mermaid
flowchart LR
  subgraph V["Application — Payment Fraud & Security"]
    direction LR
    X1["Collecteur d'événements"]
    X2["Moteur de règles candidat"]
    X3["Gestionnaire d'alertes"]
    X4["Vue de revue"]
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
- **Collecteur d'événements** : rôle et comportement exacts à confirmer.
- **Moteur de règles candidat** : rôle et comportement exacts à confirmer.
- **Gestionnaire d'alertes** : rôle et comportement exacts à confirmer.
- **Vue de revue** : rôle et comportement exacts à confirmer.

**Aspects spécifiques à cette architecture :**
- Collecteur ↔ règles : schéma d'événement
- Règles ↔ alerte : critère
- Alerte ↔ revue : accusé

## 3. Prérequis
- Lecture des schémas d'architecture applicative.
- API, contrats, messages, idempotence et erreurs.
- Principes d'authentification et d'intégration.

## 4. Exigences détaillées
- [ ] **ARC-08-A-01 :** Définir les responsabilités de chaque application et son API.
- [ ] **ARC-08-A-02 :** Versionner les contrats d'interface et formats d'erreur.
- [ ] **ARC-08-A-03 :** Documenter succès, échec, timeout, retry et réexécution.
- [ ] **ARC-08-A-04 :** Préciser IAM, secrets de lab et frontière de confiance.
- [ ] **ARC-08-A-05 :** Distinguer les mocks, composants candidats et composants testés.

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
- **Labs/études liés :** OPB-010, OPB-011, OPB-012 ; état de validation à vérifier dans les issues.

## 7. Navigation
[Business](ARC-08-B.md) · [Data](ARC-08-D.md) · [Application](ARC-08-A.md) · [Technology](ARC-08-T.md) · [Synthèse BDAT](ARC-08-BDAT.md) · [Blueprint complet](ARC-08.md) · [Atlas](BDAT-4-VUES-README.md)

**English summary:** Proposed standalone Application view of Payment Fraud & Security, documented for offline, synthetic labs only; independent review and tests are pending.
