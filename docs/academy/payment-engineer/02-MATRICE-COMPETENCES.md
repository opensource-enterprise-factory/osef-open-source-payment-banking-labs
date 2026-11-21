# 02 — Matrice de compétences OSEF Payment Engineer

## Échelle commune

- **0 — À découvrir** : ne sait pas expliquer ou exécuter.
- **1 — Comprend** : décrit le concept et ses limites avec sources.
- **2 — Applique** : reproduit un lab, suit une procédure et explique ses résultats.
- **3 — Autonome** : diagnostique un échec, écrit tests et documentation, fait une revue.
- **4 — Transmet/contribue** : conçoit une amélioration et accompagne les pairs, avec traces de contribution.

Cette échelle **n'est pas** une certification de compétence professionnelle par une autorité externe.

| Domaine | Notions et acquis à démontrer | Preuve minimale |
|---|---|---|
| Linux, Git, conteneurs, CI | branches, commits, Compose/K8s selon périmètre, logs, tests | bootstrap VM et CI reproductibles |
| Paiement métier | payeur/bénéficiaire, autorisation, capture, annulation, reversal, remboursement, litige, frais | diagramme des états et cas négatifs |
| ISO 8583 | MTI, bitmap, DE, pack/unpack, codes réponse | messages fictifs via #41 |
| ISO 20022 | structure XML, familles pacs/pain/camt, validation de schéma et sémantique | XML synthétique et tests négatifs |
| EMV / monétique | TLV, rôles émetteur/acquéreur, cryptographie, terminaux, conformité à distinguer | décodage fictif sans données carte |
| Switching | routage, quotes, retries, timeouts, idempotence | #44 / #62 |
| Clearing, settlement, ledger | positions, rapprochement, écritures équilibrées, liquidité | exercice de règlement fictif et rapprochement |
| Core banking | clients/comptes fictifs, opérations et écritures | Fineract #14/#16 et #27 |
| Mobile money | wallet, agents, cash-in/out et interopérabilité | API/ledger simulés |
| APIs & identité | OAuth/OIDC, consentement, mTLS, anti-replay | Keycloak #30 + tests |
| Fraude & AML | alertes, règles, faux positifs, investigation et minimisation | OSFE #88 et FRAUD-001/002/003 |
| SRE | traces distribuées, SLO, charge, chaos, reprise | #36/#37 |
| Security & supply chain | secrets, SBOM, dépendances, provenance, vulnérabilités | #31/#38 et rapport d'analyse |
| Licences & gouvernance | OSI vs source-available, droits d'usage, attribution | FRAUD-008 #83 |
| Contribution upstream | reproduction, issue, PR, code review | lien upstream et statut réel |

## Objectifs indicatifs par niveau

| Niveau | Socle | Paiement/interop | Sécurité/fiabilité | Contribution |
|---|---:|---:|---:|---:|
| L0 | 1 | 0–1 | 0–1 | 0 |
| L1 | 2 | 1–2 | 1 | 0–1 |
| L2 | 3 | 2–3 | 2 | 1–2 |
| L3 | 3–4 | 3 | 3 | 2 |
| L4 | 3–4 | 3–4 | 3 | 3–4 |

**Important :** les valeurs sont des cibles pédagogiques, pas un barème automatique de qualification. L'épreuve pratique et la revue indépendante priment.

## Auto-évaluation

Copier cette matrice dans sa propre issue ; inscrire le niveau estimé, la preuve/lien et la prochaine action pour chaque domaine. Ne pas publier d'informations RH sensibles ni de notes nominatives sans consentement.
