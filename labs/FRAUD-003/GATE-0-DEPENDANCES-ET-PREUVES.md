# FRAUD-003 — Gate 0 : reprise des preuves FRAUD-001 et FRAUD-002

**Statut : cadrage documenté, revue de conformité des interfaces par un ingénieur encore à faire.** Projet exclusivement pédagogique, trois établissements fictifs, aucune connexion aux institutions financières réelles. Ce document n'est pas le procès-verbal de validation indépendante de FRAUD-002.

## 1. Pourquoi commencer malgré la revue FRAUD-002 en attente ?

Le code et les essais du laboratoire FRAUD-002 sont utilisables comme *base expérimentale*, sans considérer le lab formellement clôturé. FRAUD-003 doit maintenir ses propres tests, données, approbations et décisions de sécurité. Toute découverte qui remet en cause la sécurité de FRAUD-002 doit bloquer son réemploi tant que l'écart n'est pas corrigé via une PR.

## 2. Dépendances et preuves observées

| Composant | Ce qui est étayé | Limite ou tâche ouverte | Référence |
|---|---|---|---|
| FRAUD-001 | PSP A envoie un signal minimal au relais, PSP B lit les signaux autorisés ; T01–T10 réussis, HTTP 201/409/401/422, 503 puis retour 200, contrôle TTL à la lecture | Le relais n'implémente **pas** l'isolation native de trois institutions ni la corrélation fédérée ; audit simplifié, pas de disponibilité HA prouvée | [Issue #43](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/43), [README](../FRAUD-001/README.md), [PR #76](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/pull/76) |
| Tazama Core | Profil Public DockerHub déployé dans la VM isolée, 13 services ; API TMS et Admin disponibles | La topologie laboratoire et le mode NO-AUTH ne sont pas un profil de production ; le Case Management de Tazama n'est **pas** qualifié | [Issue #50](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/50), [Architecture](../FRAUD-002/docs/ARCHITECTURE-13-SERVICES-TAZAMA.md) |
| Détection Tazama | Rapport authentique `ALRT` (score 600) et rapport `NALT` (score 200), tous deux produits à partir de transactions synthétiques | `ALRT` n'est pas une preuve de fraude ; les règles et pondérations sont propres au profil de test | [Gate E05](../FRAUD-002/docs/GATE-E05-Tazama-DIRECT.md) |
| Adaptateur OSEF D06/E05 | Prévisualisation sans publication ; `ALRT` qualifié et approuvé → signal minimal ; livraison `SENT_AND_RECEIVED / PSP_B_CONFIRMED` | Émet vers le **PSP A** fictif existant, pas vers les trois nouveaux établissements ; revue indépendante FRAUD-002 à obtenir | [Issue #50](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/50), [PR #76](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/pull/76) |
| Filtre négatif | `NALT → NO_PUBLISH`, observé via la lecture réelle de rapport | Ne démontre pas de correction des faux positifs dans le nouveau workflow d'investigation | [PR #76](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/pull/76) |
| Régression | 83/83 tests Python, Newman officiel 39/39 assertions, deux phases avec attente bornée du rapport | Résultats pour la VM testée ; ni dimensionnement sous charge ni qualification bancaire | [PR #77](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/pull/77) |

## 3. Contrats observés, non assimilables à un protocole fédéré

**FRAUD-001** : API PSP A `POST /submit` avec clé `X-Lab-Key`, schéma :

```json
{
  "transaction_token": "demo-example-transaction-0001",
  "category": "suspicious-transfer",
  "severity": "medium",
  "recipient": "psp-b",
  "expires_in_hours": 1
}
```

Le relais utilise `POST /signals`, `GET /signals` et l'en-tête `X-API-Key` avec des clés séparées. PSP B consulte `GET /inbox`. Le relais journalise les créations et lectures de façon simplifiée. `409` indique un doublon, `401` un accès refusé et `503` un relais indisponible dans les scénarios testés. Une suppression TTL physique en SQLite n'est **pas** déduite du filtre à la lecture.

**FRAUD-002** : `GET http://127.0.0.1:5100/v1/admin/reports/getreportbymsgid?msgid=...` lit un rapport Tazama. Le passage `204 → 200` peut nécessiter une attente bornée ; deux liaisons d'identifiant `data.transactionID` et `data.transaction.FIToFIPmtSts.GrpHdr.MsgId` doivent correspondre au msgid synthétique. Une politique de lab autorisée contrôle catégorie, niveau, destinataire, durée ; l'HMAC-SHA256 produit un jeton opaque. Le script de liaison directe ne publie rien sans opt-in.

**Décision Gate 0 :** ces contrats **ne suffisent pas** pour trois institutions. FRAUD-003 ne doit pas contourner l'isolation par des clés communes, ni accorder un accès global au journal ou à la base de FRAUD-001. Une nouvelle couche de contrôle d'accès et de corrélation spécifique au laboratoire est nécessaire.

## 4. Réutilisable / à créer

| Réutiliser avec restrictions | Construire et tester pour FRAUD-003 |
|---|---|
| Jeux d'événements synthétiques, schéma minimal, refus NALT, sécurité fail-closed | Identité des trois organisations, rôles et périmètres d'accès propres |
| Tests 401/409/503, contrôles TTL, patterns GitHub PR | Contrat de corrélation distinct des signaux transportés |
| Lecture Tazama Admin / qualification stricte (sans nouveau POST par défaut) | Dossier d'investigation, audit chronologique, correction de faux positif |
| Rapports expurgés et commandes de recette existantes | Tests inter-établissements, révocation, erreur/réessai, rétention et effacement |

## 5. Critères de sortie Gate 0

- [x] Les preuves déjà rapportées par FRAUD-001/002 sont inventoriées et sourcées.
- [x] Les API réutilisables et leurs limites sont identifiées dans le présent document.
- [x] La dépendance à la revue indépendante de FRAUD-002 est explicite, sans blocage de la conception FRAUD-003.
- [ ] Un ingénieur vérifie les contrats contre le code effectivement fusionné dans `main`.
- [ ] Les décisions d'isolation, de stockage et de propriété du nouveau service sont approuvées avant toute mise en service.
- [ ] Les prérequis de calcul, réseau, sauvegarde et secret pour un troisième établissement sont vérifiés avant déploiement.

**Interdit :** données réelles (PAN, MSISDN, numéros de comptes, noms de clients), connexion à un PSP/banque/EME réel, conclusion de fraude sur un `ALRT` isolé, blocage automatique et communication de conformité/OFTA officielle.
