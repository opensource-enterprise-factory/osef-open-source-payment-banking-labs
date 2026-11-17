# Catalogue — 10 architectures cibles OSEF Payment & Banking

> **Visuels BDAT disponibles :** [Atlas des dix architectures Business / Data / Application / Technology](BDAT-README.md). Les schémas Mermaid sont éditables et documentent le statut proposé de chaque architecture.

> **Version 1.0 — 17 novembre 2026.** Toutes les architectures ci-dessous sont **proposées** et non validées en laboratoire. Aucun accès aux systèmes bancaires ou réseaux de paiement réels.

**Principe :** partir du cas d'usage, non d'une architecture monolithique qui forcerait tous les composants (Fineract, Mojaloop, jPOS, Kafka...) à coexister.

| ID | Architecture | Cas principal | Clients potentiels | Statut |
|---|---|---|---|---|
| [ARC-01](ARC-01.md) | Core Banking & Microfinance | Comptes, crédits, échéanciers et écritures fictives | Banques, SFD, microfinance | Proposée |
| [ARC-02](ARC-02.md) | Card Payment & ISO 8583 | Construire, décoder et tester les messages monétiques ISO 8583 | Banques, acquéreurs, ESN monétiques | Proposée |
| [ARC-03](ARC-03.md) | Payment Interoperability Hub | Transfert fictif entre deux participants distincts | Banques, EME, PSP, infrastructures interopérables | Proposée |
| [ARC-04](ARC-04.md) | Mobile Money & Wallet Platform | Créer des wallets et simuler soldes, transferts et paiement marchand | EME, fintechs, équipes wallet | Proposée |
| [ARC-05](ARC-05.md) | Open Banking API Platform | Exposer des données/services fictifs à un client autorisé | Banques, fintechs, intégrateurs API | Proposée |
| [ARC-06](ARC-06.md) | Financial Ledger & Reconciliation | Tenue d'écritures fictives et identification d'écarts de rapprochement | Fintechs, PSP, banques, microfinance | Proposée |
| [ARC-07](ARC-07.md) | Merchant Payment Gateway | Orchestrer des paiements marchands sur prestataires entièrement simulés | PSP, e-commerce, fintechs, ESN | Proposée |
| [ARC-08](ARC-08.md) | Payment Fraud & Security | Tester détection d'anomalies et politique d'accès sans données sensibles | Équipes sécurité, banques, fintechs | Proposée |
| [ARC-09](ARC-09.md) | Payment Observability & Resilience | Mesurer délais, erreurs, taux de succès et comportements sous panne | DSI, équipes SRE/production, intégrateurs | Proposée |
| [ARC-10](ARC-10.md) | Payment Integration & Testing Factory | Industrialiser des tests API et ISO 8583 avec preuves reproductibles | ESN, QA, banques, équipes de certification technique | Proposée |

## Quelle architecture pour quel acteur ?

| Acteur | Sélection initiale | Usage |
|---|---|---|
| SFD / microfinance | ARC-01 + ARC-06 | Comptes, crédits et rapprochement |
| Banque monétique | ARC-02 + ARC-09 | Messages cartes et fiabilité |
| Établissement de monnaie électronique | ARC-04 + ARC-06 | Wallet et cohérence des écritures |
| Fintech de paiement marchand | ARC-07 + ARC-05 | Prestataires, checkout et API |
| Opérateur de switch | ARC-03 + ARC-09 | Interopérabilité et résilience |
| ESN / intégrateur de paiement | ARC-10 + ARC-02 | Banc de simulation, tests et intégration |
| Banque exposant des API | ARC-05 + ARC-08 | Accès contrôlé et sécurité |

Ces associations ne sont **pas** des prescriptions techniques applicables sans étude du SI, des licences, des risques, des budgets et du cadre réglementaire.

## Priorisation initiale
1. **ARC-10 — Payment Integration & Testing Factory** : architecture transversale, produit potentiel OPP-01/OPP-02.
2. **ARC-02 — Card Payment & ISO 8583** : s'appuie sur le prototype OPB-D03-001, **non validé en exécution**.
3. **ARC-09 — Payment Observability & Resilience** : preuves de robustesse.
4. **ARC-01 — Core Banking & Microfinance** : labs Apache Fineract.
5. **ARC-03 — Payment Interoperability Hub** : labs Mojaloop avec participants simulés.

**Cette priorité est une décision de cadrage proposée, non une validation formelle de l'équipe OSEF.**

## Livrables communs
Utiliser le [template de blueprint](BLUEPRINT-TEMPLATE.md) : contexte, exigences, diagrammes, interfaces, technologies/licences, tests, données, sécurité, dimensionnement, exploitation, risques, décisions et preuves.

## Documents liés
- [Architecture générale OSEF](../README.md)
- [20 premiers labs](../../../labs/README.md)
- [Catalogue produits/services](../../strategy/OSEF-PAYMENT-ENGINEERING-PRODUCTS-SERVICES.md)
- [Feuille de route 2027–2029](../../strategy/OSEF-PAYMENT-ENGINEERING-ROADMAP-2027-2029.md)
