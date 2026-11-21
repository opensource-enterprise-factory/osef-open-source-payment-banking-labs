# 01 — Définition du métier et responsabilités

## Mission

L'ingénieur paiement OSEF transforme des besoins fonctionnels de banques, PSP, établissements de monnaie électronique ou acteurs fintech en composants et intégrations **fiables, testables et explicables**, en privilégiant les standards appropriés et la contribution open source lorsque la licence et le contexte le permettent.

## Responsabilités essentielles

1. **Analyse des flux** : identifier acteurs, responsabilités, états, frais, reversals, autorisation, compensation, règlement et rapprochement.
2. **Architecture** : distinguer cœur bancaire, switch, canal, orchestrateur, wallet, ledger, anti-fraude et systèmes externes.
3. **Protocoles** : comprendre ISO 8583 et ISO 20022 dans leurs périmètres respectifs ; reconnaître le rôle d'EMV et des exigences propres aux réseaux.
4. **Intégration** : spécifier APIs, événements, sémantique de retry, clés d'idempotence, contrats et contrôles d'accès.
5. **Qualité** : établir des preuves sur cas nominaux, échecs, concurrence, duplication, délais et reprise.
6. **Fiabilité** : tracer une transaction bout en bout, diagnostiquer les états incohérents, documenter incidents et rollback.
7. **Sécurité** : minimiser les données, protéger les secrets, isoler les environnements et documenter les risques.
8. **Open source** : lire licences et politiques de contribution, produire des correctifs, tests et docs utiles aux mainteneurs.
9. **Éthique et exactitude** : ne jamais confondre un lab avec une infrastructure bancaire homologuée ; ne pas revendiquer des utilisateurs, performances, CVE ou validations non vérifiés.

## Ce que le rôle n'autorise pas automatiquement

- Se connecter à un switch, banque, réseau carte, mobile money ou rail de production sans mandat et autorisation.
- Utiliser de vrais PAN, PIN, CVV, données KYC, secrets, certificats ou comptes clients dans les labs.
- Déclarer une conformité PCI, EMV, ISO, BCEAO/UEMOA à partir de tests de laboratoire.
- Réutiliser du code *source-available* comme si une licence OSI l'autorisait.

## Interfaces de travail

Produit et opérations (parcours et litiges), architectes et dev (contrats), SRE (disponibilité), sécurité/RSSI et conformité (risques), OSPO/juristes (licences), QA (preuves), mainteneurs upstream (contribution).

## Définition de « prêt à être revu »

Toute demande d'intégration doit apporter : besoin et diagramme de séquence, contrats documentés, états terminaux, stratégie de retry et compensation, plan de tests, métriques, risques de sécurité, traçabilité des décisions, versions et licences des dépendances, limites connues.

## Filières possibles

Monétique & switching ; Core Banking & Rails ; Mobile Money ; Fraud Engineering ; API/Open Banking ; Payment Security & Reliability ; FINOS / Interopérabilité ; DLT/tokenisation en expérimentation.
