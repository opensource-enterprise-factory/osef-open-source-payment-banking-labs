# OFTA — Interopérabilité de la lutte contre la fraude

- **Date de veille :** 2026-11-18
- **Date de l'annonce :** 2026-11-18 (à recontrôler sur la source primaire)
- **Statut :** fiche de veille, pas une preuve de déploiement en Afrique
- **Tags :** open-source, fraud, payments, interoperability, africa-francophone
- **Source primaire :** https://www.linuxfoundation.org/press/linux-foundation-announces-the-open-financial-trust-alliance-to-strengthen-coordinated-protection-against-fraud-scams-and-financial-crime

## Faits à vérifier / faits rapportés
La Linux Foundation annonce l'Open Financial Trust Alliance (OFTA), destinée à renforcer la coordination entre dispositifs de prévention de la fraude et des escroqueries. Vérifier le périmètre technique, la gouvernance, les licences et la disponibilité d'artefacts avant de qualifier un produit de logiciel open source.

## Ce qui change
Une initiative d'interopérabilité entre réseaux et acteurs de lutte antifraude est annoncée ; aucun déploiement OSEF ni adoption régionale n'est confirmé.

## Intérêt pour l'Afrique francophone
Piste de coopération entre banques, fintechs, opérateurs mobile money et PSP ; examiner protection des données, qualité des signalements, faux positifs et transferts transfrontaliers.

## Action OSEF
Étudier les standards publiés et rédiger une architecture de référence avec données exclusivement synthétiques.

## Lab à construire — FRAUD-001 (proposé)
- **Objectif :** échanger un signal antifraude entre deux PSP simulés.
- **Prérequis :** API REST, authentification, Docker, données de test.
- **Étapes :** définir un schéma de signalement ; déployer deux simulateurs ; contrôler l'accès ; tracer les échanges ; simuler erreur et révocation.
- **Critères d'acceptation :** scénario reproductible, logs d'audit, tests de rejet et faux positifs documentés.
- **Preuves :** code, tests, captures de logs, README.

## Meetup afférent (proposé)
**Open Source Fraud Intelligence in Francophone Africa** — DSI, PSP, ingénieurs sécurité ; présentation, démo sur données fictives et débat gouvernance.

## Suivi
- [ ] Vérifier l'annonce et les artefacts techniques OFTA
- [ ] Vérifier les licences et conditions de participation
- [ ] Désigner un référent volontaire
- [ ] Créer séparément l'issue de lab après validation
