# Grille de revue — Qualification interne OSEF L1/L2

> Modèle non rempli. Aucun score individuel ni validation n'est attribué.

## Fiche de preuve

- Identifiant pseudonyme du candidat : `A_COMPLETER`
- Niveau demandé : `L1 | L2`
- Date d'exécution : `A_COMPLETER`
- Références issues/labs : `A_COMPLETER`
- Commit(s), digest(s), versions : `A_COMPLETER`
- Matériel/VM/réseau : `A_COMPLETER`
- Relecteur indépendant : `A_COMPLETER`
- Lien vers rapport de tests : `A_COMPLETER`

## Grille sur 100

| Domaine | Max | Justificatifs attendus |
|---|---:|---|
| Reproductibilité | 25 | Installation depuis VM propre, commandes complètes, versions figées, nettoyage |
| Exactitude fonctionnelle | 25 | Tests positifs et négatifs ; états de transaction expliqués |
| Résilience/diagnostic | 20 | Reprise, timeouts, idempotence, logs de corrélation |
| Sécurité et licences | 20 | Aucune vraie donnée, aucun secret, SBOM/licences analysés |
| Documentation et contribution | 10 | README, limites, amélioration documentée ou signalement de bug |

**Seuil interne proposé :** 80/100 **et** aucun défaut critique, sous décision d'un relecteur indépendant.

## Bloquants critiques

- Écritures doublées dans un ledger de test après retry pour un scénario censé être idempotent.
- Exposition de clés/secrets ou de données personnelles réelles.
- Tests absents ou résultats déclarés sans exécution.
- Une dépendance utilisée en violation flagrante de sa licence.
- Impossible de rattacher preuves et code à une version.

## Procès-verbal de revue

```yaml
candidate_id: null
level: null
date: null
lab_ids: []
sha: []
environment: null
tests: null
score:
  reproducibility: null
  functional: null
  resilience: null
  security_licensing: null
  documentation: null
critical_findings: []
reviewer: null
decision: pending
notes: null
```

**Étiquettes de décision :** `pending`, `rework`, `qualified-internal`. La validation est interne, pas une certification tierce.
