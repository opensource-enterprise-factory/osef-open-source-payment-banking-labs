# OPB-D03-001 — Premier prototype Go / ISO 8583

**Prototype pédagogique non exécuté et non validé.** Ce dossier contient le premier code proposé; les versions et les résultats restent à certifier par une exécution sur une machine de laboratoire.

## Prérequis
- Go pris en charge par la version Moov sélectionnée (voir politique officielle : https://github.com/moov-io/iso8583#go-version-support-policy).
- Accès à l'écosystème Go Modules uniquement pour récupérer le module public.
- Aucun réseau bancaire ou service monétique externe n'est sollicité par le programme.

## Exécution (dans ce dossier)
```bash
# Initialiser un module pédagogique local; aucune ressource financière réelle n'est créée.
go mod init github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/labs/03-card-payments/OPB-D03-001

# Télécharger une version publiée du composant open source.
# Pour un résultat reproductible, noter la version résolue et committer go.mod + go.sum après vérification.
go get github.com/moov-io/iso8583@latest

# Exécuter les trois tests prévus (bon parcours et deux erreurs).
go test -v ./...

# Démonstration en boucle locale : pas de connexion à un switch.
go run .
```

**Attention :** `@latest` n'est utilisé que pour l'amorçage. Figer une version et enregistrer le `go.sum` avant de déclarer le lab reproductible. Ne pas lancer `go mod init` si le module existe déjà.

## Résultats attendus (NON vérifiés en exécution)
- Retour du MTI 0100 et de la valeur fictive du champ 4 : 000000001000.
- `Unpack` rejette un message tronqué.
- Un champ non pris en charge doit déclencher une erreur.
- `go test` devra être exécuté et les éventuels écarts corrigés.

## Limites
L'opération `Pack/Unpack` porte uniquement sur les formats. Ce lab **ne simule pas** l'autorisation financière de bout en bout, l'EMV, la cryptographie, la compensation ou le règlement.

Aucun PAN, Track, PIN, CVV, HSM, TPE ou réseau de production. Ne jamais afficher un message brut contenant des données sensibles.

Sources : https://github.com/moov-io/iso8583 et https://github.com/moov-io/iso8583/blob/master/README.md
