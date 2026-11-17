# ARC-01 — Vue BDAT : Core Banking & Microfinance

> **Architecture cible proposée / non validée en laboratoire.** Diagramme conceptuel modifiable : aucun raccordement, support de production, conformité PCI DSS ou homologation BCEAO/PI-SPI n'est revendiqué.

## Diagramme BDAT

```mermaid
flowchart TB
    subgraph B["BUSINESS — Processus et acteurs"]
        direction LR
        B1["Client fictif"] --> B2["Agent / gestionnaire SFD"] --> B3["Gestion comptes et crédits"]
    end
    subgraph D["DATA — Données et flux informationnels"]
        direction LR
        D1["Clients et comptes synthétiques"] --> D2["Prêts et échéanciers"] --> D3["Écritures et audit"]
    end
    subgraph A["APPLICATION — Services et composants"]
        direction LR
        A1["Portail de lab"] --> A2["API métier / IAM"] --> A3["Apache Fineract candidat"]
    end
    subgraph T["TECHNOLOGY — Exécution et exploitation"]
        direction LR
        T1["Environnement isolé"] --> T2["Base de données de lab"] --> T3["Tests et sauvegardes"]
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
| **Business** | Client fictif · Agent / gestionnaire SFD · Gestion comptes et crédits | Quel processus et quels acteurs sont servis ? |
| **Data** | Clients et comptes synthétiques · Prêts et échéanciers · Écritures et audit | Quelles données fictives et quelles garanties de cohérence ? |
| **Application** | Portail de lab · API métier / IAM · Apache Fineract candidat | Quelles fonctions et interfaces sont nécessaires ? |
| **Technology** | Environnement isolé · Base de données de lab · Tests et sauvegardes | Où et comment exploiter/tester le service ? |

Les flèches entre couches indiquent la **traçabilité des préoccupations**, pas des appels techniques réellement implémentés. Les flèches internes sont des relations simplifiées pour le cadrage. Les composants candidats ne sont pas présumés intégrés.

## À vérifier avant validation
- [ ] Acteurs et processus Business revus par un praticien du domaine.
- [ ] Modèle Data et données de lab purement synthétiques définis.
- [ ] Contrats, versions et licences des composants Application vérifiés.
- [ ] Dimensionnement, sécurité, isolation, supervision Technology documentés.
- [ ] Scénarios nominal, rejet, timeout, reprise et doublon adaptés au cas d'usage.
- [ ] Revue indépendante avec preuves de tests anonymisées.

[Blueprint détaillé](./ARC-01.md) · [Catalogue BDAT](./BDAT-README.md) · [Architecture OSEF](../README.md)

## English summary
Four-layer Business/Data/Application/Technology conceptual view for Core Banking & Microfinance. All components and relationships require implementation, testing, licensing review and independent validation.
