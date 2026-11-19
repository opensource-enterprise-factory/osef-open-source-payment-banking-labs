# FRAUD-002 — Gate D06-1 : préparer un signal minimal sans transmission

**Statut : prototype en PR, non exécuté en VM. Aucune publication à FRAUD-001.**

## Objectif

Relier conceptuellement un rapport Tazama `ALRT` **authentique** (Gate D05) au contrat JSON réel de `POST /submit` côté PSP A (FRAUD-001), tout en maintenant la séparation entre **qualification technique**, **approbation métier** et **transmission réseau**.

Le nouveau script `scripts/tazama-signal-preview.py` :
- Reprend la qualification stricte `REVIEW_ONLY / ALRT_CANDIDATE` du Gate D05.
- Vérifie que `data.transactionID` et `transaction.FIToFIPmtSts.GrpHdr.MsgId` correspondent à l'identifiant synthétique `pacs.002` présenté. Si un champ manque : **NO_PUBLISH**.
- Exige une **politique explicite de laboratoire** contenant `approved_for_lab=true`, une référence de validation non vide, et les valeurs définies par les responsables autorisés : `category`, `severity`, `recipient=psp-b`, TTL 1 à 24 heures. **Aucune gravité n'est déduite du score 600.**
- Requiert une clé dédiée d'au moins 32 octets lue à l'exécution depuis `OSEF_FRAUD002_LAB_TOKEN_KEY` (jamais enregistrée dans Git).
- Produit en mémoire un jeton `demo-` à partir d'un **HMAC-SHA256 avec clé dédiée et séparation de domaine** sur l'identifiant de transaction *synthétique*. Il est stable pour les reprises avec la même clé ; la clé et la table de correspondance ne doivent jamais être publiées.
- Ne construit que les cinq champs autorisés par `FRAUD-001/app.py` : `transaction_token`, `category`, `severity`, `recipient`, `expires_in_hours`.
- Ne stocke ni ne transmet de message ; la CLI affiche uniquement `decision` et `reason`, **jamais le token ni le JSON du rapport**.

**Important :** la présence de `approved_for_lab=true` dans un fichier n'est pas, à elle seule, une approbation institutionnelle. La référence d'approbation doit correspondre à une décision revue hors de ce script. Le mode dry-run ne valide aucun partage réel.

## Référence de contrat

[Code FRAUD-001](../../FRAUD-001/app.py) : sur PSP A, `POST /submit` exige `X-Lab-Key`; le relais accepte la soumission avec `X-API-Key` et le modèle `Signal` ci-dessus. La lecture via PSP B passe par `GET /inbox` avec sa clé de laboratoire.

Une fois le mode d'émission autorisé dans **une PR distincte**, il faudra tester 201/409/401/503, l'audit, l'isolation entre PSP et le TTL. **Ce prototype ne contient aucun POST.**

## Test après revue et fusion dans main

```bash
cd /home/lionel/osef-open-source-payment-banking-labs
git status -sb
git checkout main
git pull --ff-only origin main

# Tous les tests sont déterministes et n'ouvrent aucune connexion réseau.
python3 -m unittest discover -s labs/FRAUD-002/tests -p 'test_*.py' -v

# Revalider l'alerte réelle via la lecture seule D05.
python3 labs/FRAUD-002/scripts/tazama-read-only-dry-run.py \
  --msgid a8a4d16c08dc481ba85092c9abf895a4
```

Lancer un test CLI de preview exige d'abord un rapport **entièrement synthétique et expurgé** et une **politique déjà revue**, fournis par GitHub/PR, plus une clé de laboratoire gérée hors Git. Il ne faut **pas** copier le rapport brut de la VM ni créer manuellement une configuration non revue sur cette VM.

## Tests ajoutés

`tests/test_signal_preview.py` vérifie :
- Le contrat minimal et le préfixe `demo-`.
- Le refus d'un statut NALT, d'une politique absente/non approuvée, d'un manque de sévérité ou d'un destinataire inattendu.
- Les identifiants de rapport et de message cohérents (pas de mapping sur un autre rapport).
- La stabilité du jeton pour une reprise avec la même clé, et sa variation pour une clé différente.
- L'absence de compte, montant, identifiant et données transactionnelles dans le signal préparé.
- L'absence de régression sur la qualification des règles.

**Environnements exclus :** données client, production IMF/SFD, intégration bancaire, règle de blocage des paiements ou diffusion OFTA officielle.

## Restant avant clôture

- [ ] Gate D06-1 : revue de cette PR et tests unitaires sur VM.
- [ ] Politique de partage approuvée : catégorie, gravité, TTL, destinataire, conservation et traçabilité d'approbation.
- [ ] Gate D06-2 : PR d'émission contrôlée et test positif PSP A → relais → PSP B, uniquement synthétique.
- [ ] Gate E : doublon 409, refus 401, panne 503, TTL, audit, absence de fuite, non-régression et revue indépendante.
