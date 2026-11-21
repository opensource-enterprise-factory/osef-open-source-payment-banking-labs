# FDC3-CONTEXT-001 — Tests de contrat d'interopérabilité

**Extension de :** [FDC3-001 #61](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/61), sans issue supplémentaire.
**Source d'origine :** https://www.finos.org/hosted-events/2026-11-13-finos-fall-2026-hackathon

**Objectif :** mesurer la réception et le traitement de contextes financiers fictifs entre deux applications compatibles FDC3.

**Prérequis :** Node.js, agent desktop FDC3 compatible choisi et épinglé, deux applications de démonstration, fixtures anonymes.

**Étapes :**
1. Vérifier les versions, licences et schémas de l'agent et des applications utilisés.
2. Envoyer un contexte d'instrument synthétique entre deux applications.
3. Injecter schéma invalide, destinataire indisponible et événement répété.
4. Capturer reçus, erreurs, traces et la matrice de compatibilité.

**Succès :** réception des contextes valides, erreurs explicites sur invalides, absence de données financières réelles, reproduction automatisable.

**Meetup :** réutiliser [#64](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/64) ; 60 min, démonstration double application.
