# OSEF Academy — Évaluation : paiements numériques et interopérabilité

**Statut : barème proposé v0.1.** Non approuvé comme dispositif officiel de certification ou d'attestation.

## Critères proposés — 100 points

| Domaine | Points max | Preuve attendue |
|---|---:|---|
| Analyse métier et diagrammes BDAT | 10 | Acteurs, rôles, frontières, états |
| API, contrats et modèles de données | 20 | OpenAPI ou équivalent versionné, erreurs et schémas |
| Ledger et cohérence | 15 | Écritures fictives, non-duplication et écarts |
| Interopérabilité et orchestration | 20 | Deux participants mockés, statuts, rejets, timeouts, retries |
| Sécurité / IAM / confidentialité | 15 | Threat model, contrôles d'accès, aucun secret ni donnée réelle |
| SRE / observabilité | 10 | Traces, métriques, alertes et runbook |
| Documentation, reproductibilité, revue | 10 | Commandes commentées, résultats observés, PR et revue |
| **Total** | **100** | |

**Seuil de pilote à discuter :** 70/100 **et** aucune violation des règles de sécurité. Ne pas utiliser ce seuil avant décision collective d'OSEF.

## Scénarios obligatoires proposés pour le projet final
- [ ] Paiement fictif nominal entre participants mockés.
- [ ] Rejet motivé et traçable.
- [ ] Requête identique rejouée sans double effet.
- [ ] Timeout conservé comme **état indéterminé** jusqu'à vérification de statut.
- [ ] Panne de dépendance et mécanisme de reprise documentés.
- [ ] Écritures/états cohérents dans la simulation.
- [ ] API non autorisée rejetée, preuves sans secrets.
- [ ] Logs et traces corrélés mais expurgés.
- [ ] Versions, licences et limites référencées.

## Modèle de dossier de preuve

```text
ID module : PNI-XX
Auteur / pseudo GitHub :
Issue / PR :
Date et environnement :
Composants / versions / licences :
Contrats et schémas :
Cas nominaux exécutés + résultats :
Cas d'erreur exécutés + résultats :
Cas non exécutés / limites :
Métriques et logs expurgés :
Analyse des risques :
Relecteur (si disponible) :
Statut : proposé / construit / testé / revu / validé en lab
```

Un composant démontré localement n'est pas un réseau de paiement autorisé. **Ne jamais publier de données clients, cartes, comptes ou secrets réels.**

[Retour au parcours](README.md) · [Politique sécurité](../../../SECURITY.md)
