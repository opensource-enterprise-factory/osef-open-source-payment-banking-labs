# OPB-D03-001 — Construire et décoder un message ISO 8583 fictif avec Moov

**État : spécification du laboratoire ; code et tests non exécutés.** Domaine D03 — Monétique, niveau débutant/intermédiaire.

## But pédagogique
Comprendre comment une bibliothèque Go représente et sérialise un message ISO 8583 : **MTI**, **bitmap**, **champs**, encodage et décodage. Les scénarios ne simulent pas une autorisation bancaire authentique.

## Pré-requis
- Go et Git ; figer les versions après vérification des exigences officielles.
- Lire https://github.com/moov-io/iso8583 et ses exemples.
- Maîtriser les commandes élémentaires Go (`go mod init`, `go test`).
- Utiliser uniquement des données entièrement inventées et non réutilisables dans des paiements réels.

## Activités
1. Créer un module Go indépendant et déclarer la dépendance Moov ISO8583 avec une version fixée.
2. Choisir une spécification éducative issue des exemples du projet ou documenter la spécification de lab.
3. Construire un message **MTI 0100 fictif**, avec plusieurs champs non sensibles (par exemple montant de démonstration, identifiant local et terminal inventés). Aucun PAN, track, PIN ou CVV, même de test, n'est nécessaire.
4. Sérialiser avec `Pack()`, puis décoder avec `Unpack()`.
5. Comparer le MTI et les champs retenus après l'aller-retour.
6. Tester deux échecs : troncature et champs/specification incohérents.
7. Documenter les formats, le bitmap, les erreurs attendues, les limites et les précautions de logging.
8. Faire relire code, tests et documentation avant fusion dans OSEF.

## Critères d'acceptation
- [ ] Versions de Go et de la bibliothèque consignées, build reproductible
- [ ] Message fictif construit avec une spec documentée
- [ ] Pack / Unpack fonctionnels et égalité des champs utiles démontrée
- [ ] Deux tests négatifs reproductibles et expliqués
- [ ] Aucun numéro de carte, secret ou système réel
- [ ] Scripts commentés, README FR/EN au moins pour l'installation
- [ ] Revue d'un second contributeur et PR associée

## Livrables attendus
- `go.mod`, `main.go`, `main_test.go` (à développer)
- `results.md` (preuves expurgées)
- `README.md` (procédure et risques)

## Sources officielles
- https://github.com/moov-io/iso8583
- https://github.com/moov-io/iso8583/blob/master/README.md
- https://github.com/moov-io/iso8583/blob/master/CONTRIBUTING.md

**Sécurité :** fonctionnement en boucle locale, aucune connexion à une banque, à un acquéreur, à un switch ou à un réseau de paiement.
