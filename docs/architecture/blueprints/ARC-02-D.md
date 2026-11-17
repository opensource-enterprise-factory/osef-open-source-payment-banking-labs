# ARC-02-D — Vue Data · Card Payment & ISO 8583

**Version 0.1 · 17 novembre 2026 · Statut : proposé, non validé en laboratoire**  
**Objectif de cette couche :** rendre visibles les objets d'information et règles de cohérence.

> **Diagramme pédagogique et conceptuel** fondé sur le [blueprint ARC-02](ARC-02.md). Les flèches décrivent des relations **proposées**, pas une preuve d'intégration. Tous les acteurs, données, environnements et transferts sont fictifs. La conformité, les performances et la production ne sont pas démontrées.

## 1. Visuel Data — Mermaid modifiable

```mermaid
flowchart LR
    subgraph S["DATA — Card Payment & ISO 8583"]
        direction LR
        N1["IsoMessageFake"]
        N2["MessageSpec"]
        N3["HostResponseFake"]
        N4["TestEvidence"]
    end
    N1 -->|"référence"| N2
    N2 -->|"produit / décrit"| N3
    N3 -->|"contribue à"| N4
    classDef layer fill:#e6f5eb,stroke:#328054,color:#183040,stroke-width:1.5px;
    class N1,N2,N3,N4 layer;
```

## 2. Descriptif de la vue

Cette vue est un modèle de données **conceptuel**. Les liens n'impliquent ni schéma SQL ni données persistées ; les clés et règles doivent être complétées dans un dictionnaire de données.

**Éléments de la couche :**
- **IsoMessageFake** — élément 1 à préciser dans une revue Data.
- **MessageSpec** — élément 2 à préciser dans une revue Data.
- **HostResponseFake** — élément 3 à préciser dans une revue Data.
- **TestEvidence** — élément 4 à préciser dans une revue Data.

**Cas / informations à documenter pour ARC-02 :**
- mti
- bitmap
- stan_fictif
- montant_fictif

## 3. Prérequis
- Connaître les notions de schéma de données, identifiant et référentiel.
- Savoir distinguer état métier, écriture, événement, trace et donnée d'audit.
- Maîtriser les jeux de données entièrement synthétiques.

## 4. Exigences détaillées
- [ ] **ARC-02-D-01 :** Définir un dictionnaire de données avec types, identifiants et règles d'unicité.
- [ ] **ARC-02-D-02 :** Décrire les relations et le cycle de vie des objets fictifs.
- [ ] **ARC-02-D-03 :** Spécifier les règles d'intégrité, idempotence, conservation et suppression.
- [ ] **ARC-02-D-04 :** Prévoir la traçabilité des changements d'état et le traitement des doublons.
- [ ] **ARC-02-D-05 :** Documenter la classification, l'expurgation et les jeux de tests synthétiques.

## 5. Livrables de validation
- [ ] Diagramme source révisé, périmètre, hypothèses et exclusions datés.
- [ ] Liste des acteurs/objets/composants/outils confrontée au besoin.
- [ ] Contrats, dictionnaires, tests ou mesures propres à cette couche annexés.
- [ ] Revue indépendante et statut réel consignés, avec liens vers les preuves.
- [ ] Aucun secret ou donnée bancaire réelle dans les fichiers.

## 6. Risques et limites

- **Spécification** : le diagramme simplifie le domaine ; les règles et interfaces exactes restent à établir.
- **Sécurité** : pas de PAN, PIN, CVV, compte client, clé HSM, identifiant ou infrastructure financière réels.
- **Maturité** : « proposé » n'est ni « testé », ni « validé en laboratoire », ni « homologué ».
- **Licences / réglementation** : chaque composant et activité doit être évalué pour sa version, sa licence et ses obligations applicables.

## 7. Articulation des vues et labs

**Navigation :** [Business](ARC-02-B.md) · [Data](ARC-02-D.md) · [Application](ARC-02-A.md) · [Technology](ARC-02-T.md) · [BDAT synthèse](ARC-02-BDAT.md) · [Blueprint](ARC-02.md)

**Labs / issues de rattachement envisagés :** OPB-D03-001. Aucun test n'est présumé réussi.

[Catalogue des 40 vues](BDAT-4-VUES-README.md) · [SECURITY.md](../../../SECURITY.md)

**EN:** Proposed Data layer view for Card Payment & ISO 8583. Synthetic data, non-production scope, no assumed integration or certification.
