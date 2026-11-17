# ARC-01-A — Vue Application · Core Banking & Microfinance

**Version 0.1 · 17 novembre 2026 · Statut : proposé, non validé en laboratoire**  
**Objectif de cette couche :** décrire les services applicatifs et leurs frontières contractuelles.

> **Diagramme pédagogique et conceptuel** fondé sur le [blueprint ARC-01](ARC-01.md). Les flèches décrivent des relations **proposées**, pas une preuve d'intégration. Tous les acteurs, données, environnements et transferts sont fictifs. La conformité, les performances et la production ne sont pas démontrées.

## 1. Visuel Application — Mermaid modifiable

```mermaid
flowchart LR
    subgraph S["APPLICATION — Core Banking & Microfinance"]
        direction LR
        N1["Portail SFD fictif"]
        N2["API métier"]
        N3["Moteur de comptes/prêts candidat"]
        N4["Audit applicatif"]
    end
    N1 -->|"interface envisagée"| N2
    N2 -->|"contrat à définir"| N3
    N3 -->|"résultats / traces"| N4
    classDef layer fill:#f0e8fc,stroke:#7953aa,color:#183040,stroke-width:1.5px;
    class N1,N2,N3,N4 layer;
```

## 2. Descriptif de la vue

Cette vue distingue les services de laboratoire des produits candidats. Les appels doivent encore être spécifiés dans des contrats et démontrés dans des tests reproductibles.

**Éléments de la couche :**
- **Portail SFD fictif** — élément 1 à préciser dans une revue Application.
- **API métier** — élément 2 à préciser dans une revue Application.
- **Moteur de comptes/prêts candidat** — élément 3 à préciser dans une revue Application.
- **Audit applicatif** — élément 4 à préciser dans une revue Application.

**Cas / informations à documenter pour ARC-01 :**
- Application ↔ API : requête identifiée
- API ↔ moteur bancaire : contrat à valider
- Moteur ↔ journal : écritures simulées

## 3. Prérequis
- Comprendre les API, adaptateurs, mocks et contrats d'interface.
- Connaître les erreurs, rejets, timeouts, réessais et idempotence.
- Lire un diagramme de composants et de séquence.

## 4. Exigences détaillées
- [ ] **ARC-01-A-01 :** Décrire les responsabilités, interfaces, entrées et sorties de chaque composant.
- [ ] **ARC-01-A-02 :** Définir et versionner API, schémas, messages et erreurs.
- [ ] **ARC-01-A-03 :** Tracer les séquences nominales, refus, timeout, reprise et double requête.
- [ ] **ARC-01-A-04 :** Documenter authentification, autorisation et appels entre domaines de confiance.
- [ ] **ARC-01-A-05 :** Préciser quels composants sont mockés, candidats ou réellement construits.

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

**Navigation :** [Business](ARC-01-B.md) · [Data](ARC-01-D.md) · [Application](ARC-01-A.md) · [Technology](ARC-01-T.md) · [BDAT synthèse](ARC-01-BDAT.md) · [Blueprint](ARC-01.md)

**Labs / issues de rattachement envisagés :** OPB-002, OPB-003, OPB-004. Aucun test n'est présumé réussi.

[Catalogue des 40 vues](BDAT-4-VUES-README.md) · [SECURITY.md](../../../SECURITY.md)

**EN:** Proposed Application layer view for Core Banking & Microfinance. Synthetic data, non-production scope, no assumed integration or certification.
