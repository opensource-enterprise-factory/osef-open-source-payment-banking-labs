# ARC-08 — Vue BDAT : Payment Fraud & Security

> **Architecture cible proposée / non validée en laboratoire.** Diagramme conceptuel modifiable : aucun raccordement, support de production, conformité PCI DSS ou homologation BCEAO/PI-SPI n'est revendiqué.

## Diagramme BDAT

```mermaid
flowchart TB
    subgraph B["BUSINESS — Processus et acteurs"]
        direction LR
        B1["Analyste fraude fictif"] --> B2["Responsable sécurité"] --> B3["Revue des alertes simulées"]
    end
    subgraph D["DATA — Données et flux informationnels"]
        direction LR
        D1["Événements synthétiques"] --> D2["Règles et seuils"] --> D3["Alertes et audit"]
    end
    subgraph A["APPLICATION — Services et composants"]
        direction LR
        A1["Collecteur d'événements"] --> A2["Moteur de règles candidat"] --> A3["Tableau de revue"]
    end
    subgraph T["TECHNOLOGY — Exécution et exploitation"]
        direction LR
        T1["Politique accès de lab"] --> T2["Journal sécurisé fictif"] --> T3["Tests faux positifs"]
    end
    B3 -. "besoin métier" .-> D1
    D3 -. "données à traiter" .-> A1
    A3 -. "s'appuie sur" .-> T1
    classDef business fill:#e3efff,stroke:#447db6,color:#18344f;
    classDef data fill:#e7f4e7,stroke:#56865d,color:#204b2a;
    classDef app fill:#f2e9ff,stroke:#8763ab,color:#402358;
    classDef tech fill:#fff0df,stroke:#b5874b,color:#553915;
    class B1,B2,B3 business;
    class D1,D2,D3 data;
    class A1,A2,A3 app;
    class T1,T2,T3 tech;
```

## Lecture par couche

| Couche | Éléments principaux | Question d'architecture |
|---|---|---|
| **Business** | Analyste fraude fictif · Responsable sécurité · Revue des alertes simulées | Quel processus et quels acteurs sont servis ? |
| **Data** | Événements synthétiques · Règles et seuils · Alertes et audit | Quelles données fictives et quelles garanties de cohérence ? |
| **Application** | Collecteur d'événements · Moteur de règles candidat · Tableau de revue | Quelles fonctions et interfaces sont nécessaires ? |
| **Technology** | Politique accès de lab · Journal sécurisé fictif · Tests faux positifs | Où et comment exploiter/tester le service ? |

Les flèches entre couches indiquent la **traçabilité des préoccupations**, pas des appels techniques réellement implémentés. Les flèches internes sont des relations simplifiées pour le cadrage. Les composants candidats ne sont pas présumés intégrés.

## À vérifier avant validation
- [ ] Acteurs et processus Business revus par un praticien du domaine.
- [ ] Modèle Data et données de lab purement synthétiques définis.
- [ ] Contrats, versions et licences des composants Application vérifiés.
- [ ] Dimensionnement, sécurité, isolation, supervision Technology documentés.
- [ ] Scénarios nominal, rejet, timeout, reprise et doublon adaptés au cas d'usage.
- [ ] Revue indépendante avec preuves de tests anonymisées.

[Blueprint détaillé](./ARC-08.md) · [Catalogue BDAT](./BDAT-README.md) · [Architecture OSEF](../README.md)

## English summary
Four-layer Business/Data/Application/Technology conceptual view for Payment Fraud & Security. All components and relationships require implementation, testing, licensing review and independent validation.
