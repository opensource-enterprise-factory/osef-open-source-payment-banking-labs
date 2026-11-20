# FRAUD-003 — Gate 1 : gouvernance fictive, partage et contrat de corrélation (proposition)

**Statut : spécification à relire, PAS une politique approuvée ni un système opérationnel.** Les termes, rôles et champs ci-dessous sont des **propositions OSEF pour FRAUD-003**, et ne sont ni un standard OFTA ni un contrat officiel Tazama.

## 1. Acteurs et frontières de confiance

| Institution fictive | Identifiant proposé | Droits initiaux | Interdictions |
|---|---|---|---|
| Banque A | `demo-bank-a` | Émettre, consulter et rectifier ses propres signalements et ses participations autorisées | Lire les données privées des autres institutions |
| PSP B | `demo-psp-b` | Même périmètre pour ses propres signalements | Accéder au journal complet du relais ou modifier le contenu de Banque A |
| Mobile Money C | `demo-mobile-c` | Même périmètre pour ses propres signalements | Voir un cas auquel C ne participe pas |
| Service de corrélation OSEF | `demo-correlation-service` | Lire uniquement les **projections minimales** autorisées ; proposer un lien avec justification | Accéder aux comptes et données brutes, déclarer une fraude établie, bloquer un paiement |
| Enquêteur fictif | `demo-investigator-*` | Consulter uniquement les dossiers où son institution est membre autorisé | Réutiliser les droits d'une autre institution |
| Auditeur de labo | `demo-auditor` | Consulter l'audit expurgé prévu pour l'exercice | Voir secrets ou données transactionnelles brutes |

**Principe :** aucune « super-clé » partagée entre Banque A, PSP B et Mobile Money C ; authentification d'acteur et autorisation *par institution, dossier et opération* dans FRAUD-003. Le relais FRAUD-001 ne fournit pas encore ces garanties et ne doit pas être supposé multi-tenant.

## 2. Vocabulaire proposé

- **Signal :** indication minimale de risque, ne prouvant pas une fraude.
- **Événement :** fait daté, par exemple signal créé, lu, révoqué ou rectifié.
- **Corrélation :** proposition explicable que plusieurs signaux synthétiques sont liés.
- **Référence de scénario :** identifiant fictif commun `demo-scenario-*` préparé uniquement pour les jeux de tests. Ne pas créer d'identifiant partagé à partir de données réelles.
- **Investigation :** dossier consultable par des rôles explicitement habilités, avec historique de décisions.
- **Faux positif :** signal reconnu comme non pertinent/incorrect après revue ; la correction ne doit pas effacer l'historique d'origine.
- **Retrait :** modification de statut empêchant une utilisation ultérieure du signal, sans supposer une suppression physique.
- **Provenance :** institution et source *fictives* du signal, avec date et preuve technique du labo.
- **Incertitude :** corrélation proposée et révocable ; aucune conclusion automatique « fraude avérée ».

## 3. Règles de partage — proposition « refus par défaut »

1. Les trois simulateurs utilisent uniquement des données fabriquées dans le laboratoire et des identifiants préfixés `demo-`.
2. Chaque institution possède ses signaux ; la lecture d'un dossier requiert une appartenance et un rôle explicites. L'identité d'une institution ne donne aucun droit sur les autres.
3. Le service de corrélation ne reçoit que les champs minimaux listés ci-dessous ; aucune référence bancaire réelle, aucun PAN, aucun MSISDN, aucun nom, montant, numéro de compte ou adresse.
4. La gravité `medium` / `high` est une valeur de politique testée, **pas** un calcul à partir du score Tazama.
5. Toute association de signaux exige une **raison explicable**, le nom de la règle de labo et des références vérifiées ; aucun rapprochement par similarité faible ou par identité client.
6. Les dossiers n'autorisent **aucun blocage automatique** ni action sur des paiements, comptes ou clients.
7. Correction et révocation : toute modification d'un signal conserve un événement d'audit immuable au niveau logique et n'est diffusée qu'aux participants autorisés.
8. TTL : le statut d'expiration empêche de nouvelles lectures et de nouvelles corrélations ; la rétention et la purge physique sont des tests distincts. Les durées précises seront approuvées avant la réalisation.
9. Les accès refusés sont testés (401 pour non authentifié, 403 pour authentifié sans autorisation selon l'API à concevoir). Ne pas utiliser le code HTTP comme seule preuve de séparation des données.
10. Secrets et clés restent hors Git ; toute modification passe par branche, PR et revue. Aucun fichier de code/configuration n'est modifié manuellement sur la VM.
11. Une approbation de laboratoire `approved_for_lab` ne vaut pas autorisation réglementaire ou institutionnelle pour de vraies données.
12. Aucune compatibilité avec Tazama Case Management, OFTA ou un protocole de partage réel n'est présumée sans test et documentation officiels.

## 4. Contrats JSON proposés (NON implémentés)

**Signal minimal en entrée du service de corrélation FRAUD-003 :**

```json
{
  "signal_id": "demo-signal-a-001",
  "origin_institution": "demo-bank-a",
  "category": "suspicious-transfer",
  "severity": "medium",
  "scenario_ref": "demo-scenario-001",
  "occurred_at": "2026-11-19T12:00:00Z",
  "expires_at": "2026-11-19T13:00:00Z",
  "source_type": "lab-synthetic"
}
```

**Proposition de corrélation, non publication automatique :**

```json
{
  "correlation_id": "demo-corr-001",
  "signal_ids": ["demo-signal-a-001", "demo-signal-b-001"],
  "rule_id": "demo-shared-scenario-v1",
  "explanation": "Deux signaux de test portent la même référence de scénario fictif",
  "status": "proposed",
  "created_at": "2026-11-19T12:05:00Z"
}
```

**Dossier d'investigation, création à autoriser explicitement :**

```json
{
  "case_id": "demo-case-001",
  "correlation_id": "demo-corr-001",
  "participants": ["demo-bank-a", "demo-psp-b"],
  "status": "open",
  "classification": "unconfirmed",
  "created_at": "2026-11-19T12:10:00Z"
}
```

Ces exemples sont **100 % fabriqués**. `scenario_ref` est une béquille pédagogique pour rendre les tests déterministes, non un mécanisme de rapprochement transfrontalier acceptable en production.

### États proposés

- Signal : `active → expired` ; `active → withdrawn` ; `active → corrected`.
- Corrélation : `proposed → accepted/rejected` ; une correction du signal lié doit déclencher une réévaluation.
- Dossier : `open → in_review → resolved_false_positive / resolved_unconfirmed` ; l'historique ne doit jamais être silencieusement réécrit.

## 5. Matrice d'autorisation à transformer en tests

| Action | Banque A | PSP B | Mobile C | Corrélation | Enquêteur habilité |
|---|---|---|---|---|---|
| Créer son signal | Oui pour A | Oui pour B | Oui pour C | Non | Non |
| Lire ses signaux | Oui pour A | Oui pour B | Oui pour C | Uniquement projection minimale approuvée | Selon dossier autorisé |
| Lire une alerte privée d'un autre | Non | Non | Non | Non | Non |
| Proposer une corrélation | Non | Non | Non | Oui, si politiques satisfaites | Non |
| Ouvrir / modifier un dossier | Sur rôle autorisé dans son périmètre | Idem | Idem | Non | Si habilité sur le dossier |
| Rectifier son signal | Oui | Oui | Oui | Non | Non |
| Lire les audits transverses | Non | Non | Non | Non | Non par défaut |

**Décision à approuver :** qui approuve une corrélation entre établissements ? Un modèle de consentement explicite des participants et une politique de visibilité par dossier sont proposés, mais non validés ici.

## 6. Scénarios de validation Gate 1 puis Gate 2+

| Référence | Scénario | Attendu |
|---|---|---|
| G1-01 | Banque A crée un signal fictif | Signal appartenant seulement à A |
| G1-02 | PSP B lit un signal privé de A | Refus sans fuite de données |
| G1-03 | Mobile Money C accède à un dossier A+B | Refus si C non participant |
| G1-04 | Deux signaux portent `demo-scenario-001` | Corrélation **proposée**, jamais fraude automatiquement confirmée |
| G1-05 | Signal expiré ou retiré | Exclu des nouvelles propositions |
| G1-06 | Retrait ou correction d'un faux positif | Dossier et historique réévalués, diffusion limitée |
| G1-07 | Rejeu d'un signal avec même ID | Idempotence vérifiée et pas de dossier dupliqué |
| G1-08 | Clé invalide, absence de clé, rôle non autorisé | Refus et événement d'audit expurgé |
| G1-09 | Indisponibilité du service de corrélation | Aucune création silencieuse de dossier, récupération explicite |
| G1-10 | Export des logs et pièces | Aucun secret ni données de compte/client |

## 7. Arbitrages restant avant tout développement

- [ ] Valider la matrice des rôles/permissions et l'autorité qui confirme une corrélation.
- [ ] Choisir le stockage des signaux/dossiers et les règles de rétention, sauvegarde et purge du labo.
- [ ] Décider si l'authentification est simulée avec clés distinctes ou testée avec Keycloak ; aucun déploiement Keycloak n'est acquis.
- [ ] Évaluer les interfaces et licences effectives de **Tazama Case Management**, avant toute promesse d'intégration.
- [ ] Décider la logique de corrélation (règles explicables et limites) et sa journalisation.
- [ ] Revue sécurité de l'isolation multi-institution et des politiques de diffusion.
- [ ] Approuver les contrats JSON ci-dessus avant d'implémenter les endpoints.

**Critère de fin du Gate 1 :** documents discutés et approuvés par le référent métier et le relecteur sécurité OSEF. La publication des présentes propositions ne vaut **pas** validation de Gate 1.
