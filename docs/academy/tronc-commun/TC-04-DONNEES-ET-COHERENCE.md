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

## Séquence de cours détaillée — proposition pédagogique v0.2

**Nature :** syllabus à enseigner et exercices à réaliser. Les durées, présentations magistrales et résultats de l'apprenant ne sont pas confirmés. Cette section complète, sans remplacer, les objectifs et critères initiaux.

### Objectifs évaluables
1. Formaliser un invariant comptable de simulation.
2. Démontrer un rejeu sans double effet.
3. Expliquer une divergence de rapprochement.

### Chapitres / notions à expliquer
1. **Chapitre 1 — Modélisation et identifiants.** Définir les concepts, les illustrer avec un exemple OSEF fictif et expliciter les limites.
2. **Chapitre 2 — Ledger fictif à double écriture.** Définir les concepts, les illustrer avec un exemple OSEF fictif et expliciter les limites.
3. **Chapitre 3 — Idempotence/déduplication.** Définir les concepts, les illustrer avec un exemple OSEF fictif et expliciter les limites.
4. **Chapitre 4 — Écarts et rapprochement.** Définir les concepts, les illustrer avec un exemple OSEF fictif et expliciter les limites.

### Déroulement conseillé
1. **Découverte :** question de départ, prérequis et vocabulaire.
2. **Analyse :** lecture guidée des vues d'architecture liées à cette fiche.
3. **Démonstration :** parcourir le code ou le diagramme, identifier les hypothèses.
4. **TP guidé :** réaliser la démarche ci-dessous, sans connexion financière.
5. **Restitution :** relever résultats réels, écarts, risques et revue.

### Travaux pratiques guidés
1. Dessiner ARC-06-D.
2. Exécuter TC-04 deux fois avec la même clé.
3. Concevoir un cas d'écart sur jeu synthétique.

**Point de départ :** [mini-lab TC-04](../../../labs/common-core/TC-04.md), [code pédagogique](../../../labs/common-core/runner.py), [tests unitaires](../../../labs/common-core/test_runner.py).

**Commande de découverte (aucun paiement ni réseau) :**
```bash
# Depuis la racine du dépôt, exécuter uniquement le démonstrateur local.
python3 labs/common-core/runner.py TC-04

# Exécuter les tests unitaires du tronc commun et consigner le résultat réel.
python3 -m unittest discover -s labs/common-core -p 'test_*.py' -v
```

### Évaluation proposée
- **Compréhension :** expliquer les concepts avec ses propres mots et corriger une hypothèse fausse.
- **Pratique :** réaliser un cas nominal et au moins un cas d'erreur ou de limite.
- **Architecture :** identifier la vue BDAT mobilisée et relier au moins une exigence.
- **Preuve :** version, commande, date, sortie expurgée, lien vers contribution et revue si réalisée.

**Critères ciblés :**
- [ ] Somme des écritures égale zéro.
- [ ] Rejeu sans nouvelle écriture.
- [ ] Erreur de charge différente documentée.
- [ ] Distinguer les résultats attendus des résultats effectivement obtenus.
- [ ] Respecter la politique de sécurité et conserver une preuve de revue si possible.

**Ressources :** [matrice cours/compétences](../CORRESPONDANCE-COMPETENCES-COURS.md), [atlas BDAT](../../architecture/blueprints/BDAT-4-VUES-README.md), [fiche de preuve](../MODELE-PREUVE-COMPETENCE.md). Références technologiques amont à vérifier par le formateur avant séance.

---

## Raccordement aux spécialisations

- [Monétique & ISO 8583](../monetique-iso8583/README.md)
- [Paiements numériques & interopérabilité](../paiements-numeriques-interoperabilite/README.md)
- [Évaluation du tronc commun](EVALUATION.md)
- [Atlas BDAT](../../architecture/blueprints/BDAT-README.md)

**English summary:** Public OSEF core-engineering module, not an accredited qualification. Synthetic data and evidence-based review only; no production payment systems.
