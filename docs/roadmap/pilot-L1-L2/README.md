# Pilote OSEF Payment Engineer — Niveaux L1 et L2

> **Statut : cadrage prêt pour revue, non lancé.** Aucune personne nommée, inscription, réservation de VM ni réussite n'est confirmée.

## Finalité

Tester la capacité de futurs ingénieurs OSEF à déployer, comprendre, diagnostiquer et documenter un environnement de paiement open source reproductible. Cette qualification est **interne OSEF** et ne vaut pas certification ISO, PCI DSS, EMV ou homologation BCEAO.

## Parcours et dépendances

| Étape | Exercices à utiliser | Compétence observable | Prérequis |
|---|---|---|---|
| L1.1 | [OPB-001 #12](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/12) | Cartographier OSS vs standards vs solutions propriétaires et licences | Git, Linux |
| L1.2 | [ISO 8583 Go #41](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/41) | Construire, parser et expliquer un message synthétique | Go, formats de messages |
| L1.3 | [Fineract #14](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/14) | Déployer et tester une API de core banking fictive | Docker, HTTP |
| L1.4 | [Mojaloop #21](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/21) | Expliquer les composants et déploiement en bac à sable | Linux, Docker/K8s selon la méthode retenue |
| L2.1 | [PAYMENT-001 #44](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/44) | Simuler un paiement interopérable entre DFSP fictifs | L1 validé ou expérience équivalente |
| L2.2 | [MOJA-REGRESSION #62](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/62) | Gérer expirations, répétitions et idempotence | TTK et logs |
| L2.3 | [Fineract–Mojaloop #27](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/27) | Vérifier l'intégration de deux systèmes et rapprochement | APIs et transaction state |
| L2.4 | [SIIPS-TRUST #92](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/92) | Expliquer confirmation et réclamations dans un parcours fictif | Tests négatifs et tracabilité |

Les issues constituent des références de travail ; elles ne démontrent pas que les implémentations sont prêtes. Un **gate technique** doit confirmer les labs exécutables avant de démarrer les évaluations.

## Gates du pilote

- **G0 — Disponibilité** : mainteneur/relecteur identifiés ; 2 participants pilotes volontaires minimum *proposés*, sans aucune personne présumée ; matériel et VM documentés ; droits GitHub limités.
- **G1 — Lab prêt** : installation depuis une VM propre ; digests/version épinglés ; données fictives ; README ; script de test ; licences connues ; nettoyage.
- **G2 — Épreuve L1** : comprendre message ISO 8583 synthétique, architecture de Mojaloop et Fineract ; déploiement/diagnostic consigné.
- **G3 — Épreuve L2** : scénario nominal + refus + timeout + reprise ; aucun double débit sur ledger fictif ; corrélation de bout en bout.
- **G4 — Revue** : double vérification des preuves ; décision interne documentée ; ouverture d'une issue/PR upstream si un bug reproductible est identifié.

## Évaluation

Utiliser [la grille](./RUBRIC.md) : 100 points, seuil **proposé** 80, zéro défaut critique ; révision indépendante obligatoire. Les niveaux ne sont pas attribués avant réalisation et preuve. Les épreuves devront être adaptées si les labs réels diffèrent du cahier des charges.

## Organisation et rôles (à attribuer)

| Rôle | Responsabilité | Affectation |
|---|---|---|
| Responsable de pilote | Priorisation, gates et journal de décision | À confirmer |
| Relecteur paiement/monétique | Contrats, états, erreurs et idempotence | À confirmer |
| Relecteur sécurité/SRE | Secrets, redaction, reproductibilité et pannes | À confirmer |
| Ingénieurs pilotes | Implémentation et collecte de preuves | À confirmer |

**Ne pas attribuer automatiquement une issue à une personne sans validation de sa disponibilité.**

## Livrables du pilote

- Un dossier de preuves **par lab** et par candidat (pseudonymisé).
- Une grille d'évaluation remplie, justifiée, avec relecteurs.
- Un registre des écarts/bugs et des contributions upstream potentielles.
- Un RETEX décrivant prérequis, durée *observée*, blocages, suites.

**Références :** [Programme de qualification](../OSEF-PAYMENT-ENGINEER-QUALIFICATION.md), [catalogue 75 labs](../OSEF-PAYMENT-LABS-CATALOGUE-2026-11-21.md), [registre upstream](../OSEF-UPSTREAM-CONTRIBUTIONS.md).
