# ARC-07 — Vue BDAT : Merchant Payment Gateway

> **Architecture cible proposée / non validée en laboratoire.** Diagramme conceptuel modifiable : aucun raccordement, support de production, conformité PCI DSS ou homologation BCEAO/PI-SPI n'est revendiqué.

## Diagramme BDAT

```mermaid
flowchart TB
    subgraph B["BUSINESS — Processus et acteurs"]
        direction LR
        B1["Marchand fictif"] --> B2["Client fictif"] --> B3["Paiement marchand simulé"]
    end
    subgraph D["DATA — Données et flux informationnels"]
        direction LR
        D1["Intent de paiement"] --> D2["Statut et idempotence"] --> D3["Notifications webhook"]
    end
    subgraph A["APPLICATION — Services et composants"]
        direction LR
        A1["Checkout de lab"] --> A2["Orchestrateur candidat"] --> A3["Connecteurs PSP fictifs"]
    end
    subgraph T["TECHNOLOGY — Exécution et exploitation"]
        direction LR
        T1["Services et mocks isolés"] --> T2["Tests de callback"] --> T3["Observabilité API"]
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
| **Business** | Marchand fictif · Client fictif · Paiement marchand simulé | Quel processus et quels acteurs sont servis ? |
| **Data** | Intent de paiement · Statut et idempotence · Notifications webhook | Quelles données fictives et quelles garanties de cohérence ? |
| **Application** | Checkout de lab · Orchestrateur candidat · Connecteurs PSP fictifs | Quelles fonctions et interfaces sont nécessaires ? |
| **Technology** | Services et mocks isolés · Tests de callback · Observabilité API | Où et comment exploiter/tester le service ? |

Les flèches entre couches indiquent la **traçabilité des préoccupations**, pas des appels techniques réellement implémentés. Les flèches internes sont des relations simplifiées pour le cadrage. Les composants candidats ne sont pas présumés intégrés.

## À vérifier avant validation
- [ ] Acteurs et processus Business revus par un praticien du domaine.
- [ ] Modèle Data et données de lab purement synthétiques définis.
- [ ] Contrats, versions et licences des composants Application vérifiés.
- [ ] Dimensionnement, sécurité, isolation, supervision Technology documentés.
- [ ] Scénarios nominal, rejet, timeout, reprise et doublon adaptés au cas d'usage.
- [ ] Revue indépendante avec preuves de tests anonymisées.

[Blueprint détaillé](./ARC-07.md) · [Catalogue BDAT](./BDAT-README.md) · [Architecture OSEF](../README.md)

## English summary
Four-layer Business/Data/Application/Technology conceptual view for Merchant Payment Gateway. All components and relationships require implementation, testing, licensing review and independent validation.
