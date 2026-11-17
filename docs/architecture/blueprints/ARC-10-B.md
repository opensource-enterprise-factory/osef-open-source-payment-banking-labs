# ARC-10-B — Business · Payment Integration & Testing Factory

**Version 0.1 — 17 novembre 2026 · Vue proposée, non validée en laboratoire.**

> La vue est conceptuelle et se fonde sur le [blueprint ARC-10](ARC-10.md). Aucun paiement, banque, compte, secret ou réseau réel. Aucune homologation ni compatibilité intégrée démontrée.

## 1. Diagramme Mermaid modifiable
```mermaid
flowchart LR
  subgraph V["Business — Payment Integration & Testing Factory"]
    direction LR
    X1["Ingénieur QA"]
    X2["Intégrateur ESN"]
    X3["Relecteur indépendant"]
    X4["Responsable lab"]
  end
  X1 -->|"initie"| X2
  X2 -->|"collabore"| X3
  X3 -->|"contrôle"| X4
  classDef layer fill:#e4f0ff,stroke:#4a637e,color:#183040;
  class X1,X2,X3,X4 layer;
```

## 2. Descriptif
La vue métier montre qui réalise les activités du cas fictif, ce qui est attendu et comment les exceptions sont traitées. Les flèches sont indicatives, pas des workflows approuvés.

**Éléments de la couche :**
- **Ingénieur QA** : rôle et comportement exacts à confirmer.
- **Intégrateur ESN** : rôle et comportement exacts à confirmer.
- **Relecteur indépendant** : rôle et comportement exacts à confirmer.
- **Responsable lab** : rôle et comportement exacts à confirmer.

**Aspects spécifiques à cette architecture :**
- Définir scénario
- Exécuter tests
- Comparer résultats
- Revoir preuve

## 3. Prérequis
- Notions des rôles bancaires ou de paiement concernés.
- Compréhension d'un processus, ses acteurs et exceptions.
- Lecture de la description du cas d'usage.

## 4. Exigences détaillées
- [ ] **ARC-10-B-01 :** Attribuer explicitement les rôles et droits des acteurs fictifs.
- [ ] **ARC-10-B-02 :** Décrire le scénario métier nominal et les exceptions.
- [ ] **ARC-10-B-03 :** Distinguer acceptation, rejet et statut indéterminé.
- [ ] **ARC-10-B-04 :** Documenter règles métier et exclusions (pas de paiement réel).
- [ ] **ARC-10-B-05 :** Associer processus à événements et indicateurs observables.

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

**English summary:** Proposed standalone Business view of Payment Integration & Testing Factory, documented for offline, synthetic labs only; independent review and tests are pending.
