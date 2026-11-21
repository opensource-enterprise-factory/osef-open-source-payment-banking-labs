# 09 — Glossaire métier Payment Engineering (introduction)

| Terme | Sens opérationnel simplifié |
|---|---|
| Acquéreur | Entité qui fournit des services d'acceptation à un commerçant dans le modèle considéré |
| Émetteur | Institution associée à l'instrument ou au compte du payeur |
| PSP | Prestataire de services de paiement ; périmètre juridique selon la juridiction |
| DFSP | Digital Financial Services Provider, terme fréquent dans Mojaloop |
| Switch | Composant qui route/orchestre des messages ou transactions entre participants |
| Autorisation | Décision sur la possibilité d'effectuer une opération, distincte du règlement final |
| Clearing / compensation | Échange et calcul d'obligations entre participants |
| Settlement / règlement | Extinction des obligations financières selon les règles du système |
| Ledger | Journal comptable des écritures et soldes selon un modèle défini |
| Rapprochement | Comparaison de références, montants et états entre systèmes |
| Reversal | Message ou opération visant à inverser/annuler l'effet selon le protocole concerné |
| Refund / remboursement | Nouveau mouvement compensant un paiement, selon les règles applicables |
| Idempotence | Répéter une même commande ne doit pas multiplier son effet métier |
| Timeout | Délai expiré ; n'implique pas automatiquement que la transaction ait échoué |
| Retry | Nouvelle tentative ; requiert des règles de sécurité et de déduplication |
| ISO 8583 | Norme relative aux messages d'échange de transactions cartes, avec variantes/profils |
| MTI / DE | Message Type Indicator / Data Element en ISO 8583 |
| EMV | Ensemble de spécifications relatives notamment aux paiements cartes et acceptation |
| TLV | Encodage Tag-Length-Value, utilisé dans divers systèmes dont EMV |
| ISO 20022 | Modèle et catalogue de messages financiers, pas logiciel exécutable |
| pacs / pain / camt | Familles de messages ISO 20022, selon leurs usages |
| HSM | Module matériel de sécurité utilisé pour certaines opérations de clés/cryptographie |
| KYC / AML | Connaissance du client / lutte contre le blanchiment, exigences contextuelles |
| OFTA | Open Financial Trust Alliance, initiative de coordination et d'interopérabilité antifraude |
| FDC3 | Standard FINOS d'interopérabilité contextuelle entre applications financières |
| Source-available | Code consultable sous conditions ne répondant pas nécessairement à la définition OSI |
| Upstream | Projet d'origine auquel OSEF peut soumettre des contributions |
| SLO | Objectif de niveau de service défini et mesuré |
| ADR | Architecture Decision Record, trace écrite d'une décision technique |

**Attention :** ce glossaire n'est pas un substitut aux textes normatifs et réglementaires, qui peuvent avoir des définitions juridiquement précises.
