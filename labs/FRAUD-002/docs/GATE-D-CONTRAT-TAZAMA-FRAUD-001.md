# FRAUD-002 — Gate D : contrat de traduction Tazama vers FRAUD-001

**Statut : spécification de conception, pas une intégration déployée.** Environnement pédagogique avec transactions synthétiques uniquement. Aucune connexion à une IMF, banque, EME ou PSP réel.

## 1. Sources vérifiées

- [Code de l'API FRAUD-001](../../FRAUD-001/app.py) : `POST /submit` côté PSP A ; `POST /signals` et `GET /signals` côté relais ; authentification, schéma, idempotence.
- [README FRAUD-002](../README.md) : objectifs des Gates D/E, limites de diffusion des données.
- [Collection de test Tazama Public DockerHub](https://github.com/tazama-lf/postman/blob/main/Newman/Newman%20-%202.1.%20(NO-AUTH)%20Public%20DockerHub%20End-to-End%20Test.postman_collection.json) : API de rapport `GET /v1/admin/reports/getreportbymsgid?msgid=...`.

**Preuve rapport Tazama 19/11/2026, identifiant de laboratoire expurgé :** transaction Web simulée de 370 USD, `data.report.status=NALT`, `tadpResult.typologyResult[0].result=200`, `workflow.alertThreshold=300`, `interdictionThreshold=500`, `review=false`. Rapport retourné en HTTP 200. Le moteur a traité la transaction, mais l'interface Demo affichait encore `null` : anomalie d'affichage séparée, non bloquante.

## 2. Principes de sécurité et métier

1. **Fail-closed** : aucun rapport absent, invalide, ambigu ou `NALT` ne doit être transformé en signal frauduleux.
2. **Validation explicite** : uniquement les statuts Tazama et les seuils dont la sémantique est confirmée par documentation et par un test positif de démonstration.
3. **Jamais de données de transaction** dans FRAUD-001 : pas de montant, devise, compte, nom, coordonnées GPS, `dbtrId`, `cdtrId`, MSISDN ou référence d'opération réelle.
4. **Jeton opaque propre au laboratoire** : un identifiant aléatoire `demo-` produit par l'adaptateur, avec table de correspondance locale protégée et durée de conservation limitée. Ne pas hacher un identifiant réel sans analyse de réidentification.
5. **Aucune décision automatisée de blocage** dans FRAUD-001 : les signaux ne constituent pas une preuve de fraude.
6. **Source autorisée seulement** : accès contrôlé à l'API Admin, absence d'identifiants de production et pas d'accès direct aux bases Tazama.
7. **Réémission sûre** : une même évaluation ne peut conduire qu'à un seul signal transmis ; prévoir reprise après erreur et gestion HTTP 409 sans journaliser de secrets.

## 3. Interfaces établies et à qualifier

| Étape | Contrat | Statut |
|---|---|---|
| Résultat Tazama | `GET http://127.0.0.1:5100/v1/admin/reports/getreportbymsgid?msgid=...`, exemple confirmé HTTP 200 avec `data.report` | Observé dans FRAUD-002 **en mode sans authentification** |
| Résultat sans rapport | `HTTP 204 No Content` possible quand le rapport n'est pas encore disponible | Observé ; prévoir polling borné avec timeout |
| Soumission PSP A | `POST /submit` + en-tête `X-Lab-Key` et corps `Signal` de FRAUD-001 | Vérifié dans `app.py` |
| Relais via PSP A | `POST /signals` avec `X-API-Key`, 201 accepté, 409 doublon | Vérifié dans `app.py` |
| Consultation PSP B | `GET /inbox` avec `X-Lab-Key` ; relay `GET /signals` restreint à PSP B | Vérifié dans `app.py` |
| État d'alerte Tazama positif | Règles, statuts et sortie représentatifs d'une alerte authentique du profil | **Non encore validés** |

## 4. Politique de décision proposée pour l'adaptateur (non implémentée)

| Entrée | Décision | Motif |
|---|---|---|
| `HTTP 204`, timeout, erreur HTTP, JSON invalide | **Ne pas publier** ; diagnostic explicite | Absence de preuve de détection |
| `data.report.status == NALT` | **Ne pas publier** | Rapport sans alerte dans le scénario validé |
| Typologie présente mais `result < alertThreshold` | **Ne pas publier** | Résultat sous seuil |
| Statut d'alerte / interdiction inconnu | **Ne pas publier** | Sémantique non qualifiée |
| Alerte positive confirmée selon un jeu synthétique, version et règles approuvées | **Candidat à publication sous contrôle** | Exige l'approbation d'un mapping explicite, pas un automatisme sur le seul score |

Pour un premier pilote, le signal `suspicious-transfer` peut être proposé **uniquement après** un résultat Tazama positif validé et une approbation de la catégorie par les responsables métier/sécurité. La sévérité `low/medium/high` ne doit pas être devinée à partir du score ; établir une politique versionnée et testée.

### Schéma de sortie FRAUD-001 (contrat réel)

```json
{
  "transaction_token": "demo-opaque-generated-token",
  "category": "suspicious-transfer",
  "severity": "high",
  "recipient": "psp-b",
  "expires_in_hours": 1
}
```

La valeur de sévérité `high` ci-dessus **illustre la syntaxe autorisée par l'API**, elle **n'est pas déduite** du rapport NALT de 370 USD et ne doit pas être publiée pour celui-ci.

## 5. Scénarios de Gate D et Gate E

- [ ] D01 — Charger un rapport `NALT` confirmé → aucun appel PSP A, aucune publication, journal de décision local sans données sensibles.
- [ ] D02 — Réponse `204` puis `200` → attente bornée, pas de signal prématuré.
- [ ] D03 — Entrée invalide/absente ou erreur d'authentification → arrêt sans publication.
- [ ] D04 — Produire et vérifier un scénario **d'alerte positive authentique** dans Tazama, avec une configuration de test versionnée.
- [ ] D05 — Valider les statuts, champs et seuils du résultat positif puis approuver catégorie et sévérité.
- [ ] D06 — Soumettre via PSP A et vérifier réception uniquement par PSP B, sans données sensibles.
- [ ] E01 — Doublon/idempotence, HTTP 409, vérification de la corrélation et de l'audit.
- [ ] E02 — Échec du relais (503), récupération et absence de double livraison.
- [ ] E03 — Expiration TTL, autorisations 401, et refus de lecture non autorisée.
- [ ] E04 — Tests de non-régression FRAUD-001 T01–T10 et Newman Tazama 39/39.
- [ ] E05 — Revue sécurité, compatibilité des versions et validation d'un deuxième ingénieur.

## 6. Séquence d'implémentation PR-first

**PR suivante** : prototype Python **sans émission réseau** (mode dry-run), analyse de fixtures JSON synthétiques et tests unitaires NALT/204/erreur. Ensuite seulement, tests positifs Tazama, autorisation du mapping, puis émission réelle vers PSP A sur le réseau de laboratoire. Toute modification de code ou de config doit être revue et fusionnée dans GitHub avant déploiement Ubuntu.

## 7. Réserves pour un usage IMF en production

Ce laboratoire ne valide pas Tazama pour production. La stack Docker Compose officielle utilisée ici est réservée aux démonstrations ; pour une IMF, il faut un projet distinct de qualification réglementaire, architecture sécurisée/résiliente, protection des données, règles de surveillance validées, exploitation et gouvernance des alertes.
