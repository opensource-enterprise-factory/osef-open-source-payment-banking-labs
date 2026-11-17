# TC-04 — Données transactionnelles, ledger et idempotence

**OSEF Academy · Tronc commun · Proposition v0.1 du 17 novembre 2026**  
**Statut : support pédagogique écrit, non exécuté ni évalué.**  
**Architectures associées :** ARC-06 · **Issues ou labs de départ :** OPB-015

## Compétence visée

Modèle de données, identifiants, corrélation, partie double fictive, doublons, rapprochement et invariant de cohérence.

## Pré-requis
- Avoir lu [JOIN-US](../../../JOIN-US.md), [SECURITY.md](../../../SECURITY.md) et [CONTRIBUTING.md](../../../CONTRIBUTING.md).
- Disposer d'un poste personnel ou d'un environnement isolé.
- Être à l'aise avec la lecture de documentation ; les bases nécessaires peuvent être acquises progressivement.

## Activité proposée

Construire un jeu synthétique d'écritures équilibrées ; simuler un ordre rejoué et un écart ; proposer une règle de réconciliation.

**Attention :** l'activité concerne une démonstration strictement fictive et locale. Aucune connexion à une institution, passerelle, carte ou réseau financier ; aucun secret ni donnée de client réel.

## Livrables et preuves

Modèle de données, tests d'invariants et tableau des écarts.

Le dossier doit distinguer **résultats attendus**, **résultats réellement observés** et **tests non exécutés** ; inclure versions, commandes commentées, limites et liens vers des sources officielles utilisées.

## Checklist de revue
- [ ] Cas et objectif pédagogique compréhensibles.
- [ ] Hypothèses, terminologie et architecture justifiées.
- [ ] Données purement synthétiques, pas de secret ni accès tiers.
- [ ] Instructions et éventuels scripts commentés.
- [ ] Scénario nominal et scénario négatif pertinents exécutés, ou absence explicitement signalée.
- [ ] Preuves vérifiables et limites connues conservées.
- [ ] Revue indépendante documentée si réalisée.

## Raccordement aux spécialisations

- [Monétique & ISO 8583](../monetique-iso8583/README.md)
- [Paiements numériques & interopérabilité](../paiements-numeriques-interoperabilite/README.md)
- [Évaluation du tronc commun](EVALUATION.md)
- [Atlas BDAT](../../architecture/blueprints/BDAT-README.md)

**English summary:** Public OSEF core-engineering module, not an accredited qualification. Synthetic data and evidence-based review only; no production payment systems.
