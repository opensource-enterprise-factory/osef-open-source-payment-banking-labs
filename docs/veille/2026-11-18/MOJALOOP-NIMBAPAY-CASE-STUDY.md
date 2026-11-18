# Mojaloop et NimbaPay — Retour d'expérience guinéen

- **Date de veille :** 2026-11-18
- **Annonce rapportée :** 9–10 novembre 2026 ; hors fenêtre principale de 7 jours
- **Statut :** étude de cas à approfondir ; ne pas inférer les résultats opérationnels
- **Tags :** mojaloop, instant-payments, interoperability, guinea, africa-francophone
- **Source officielle à consulter :** https://mojaloop.io/blog/

## Faits rapportés et vérification
Une annonce de la Mojaloop Foundation indique l'utilisation de la technologie Mojaloop dans le système de paiement instantané NimbaPay en Guinée. Le lien direct vers le billet et les détails techniques doivent être confirmés avant diffusion externe.

## Ce qui change
Un cas d'utilisation africain de Mojaloop est signalé ; cette fiche ne confirme ni volumes, ni disponibilité, ni performance.

## Intérêt pour l'Afrique francophone
Étudier l'interopérabilité, les compétences d'exploitation, les interfaces des participants et les contributions possibles aux infrastructures de paiement open source.

## Action OSEF
Documenter architecture, participants, flux de transaction, règlement, sécurité, observabilité et limites de transposition.

## Lab à construire — PAYMENT-001 (proposé)
- **Objectif :** simuler un paiement instantané entre deux participants.
- **Prérequis :** Docker/Kubernetes, API, notions de compensation et règlement, ressources compatibles avec la documentation upstream.
- **Étapes :** installer une distribution de lab Mojaloop ; créer deux participants fictifs ; exécuter un paiement ; injecter un échec ; observer les traces.
- **Critères d'acceptation :** scénario nominal et erreur documentés avec traces reproductibles.
- **Preuves :** README, configuration, tests, captures de traces.

## Meetup afférent (proposé)
**Inside an Open Source Instant Payment System** — ingénieurs monétiques et fintech ; architecture, démo, discussion sur compétences.

## Suivi
- [ ] Identifier et vérifier le billet primaire précis
- [ ] Examiner la documentation et les licences Mojaloop
- [ ] Vérifier les prérequis matériels du lab
- [ ] Désigner un référent volontaire
