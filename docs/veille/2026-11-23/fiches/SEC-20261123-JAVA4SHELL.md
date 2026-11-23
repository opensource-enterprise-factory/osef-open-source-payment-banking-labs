# Sécurité Kafka/Flink et JDK

- **Période de veille :** 16–23 novembre 2026 ; 18–19 novembre 2026.
- **Classification :** avis de sécurité (ne pas assimiler à un déploiement ni à une release).
- **Source primaire :** https://flink.apache.org/2026/11/18/mitigating-cve-2026-114938-java4shell-in-apache-flink-deployments/
- **Implication Afrique francophone :** opportunité d'étudier la fiabilité, la sécurité ou l'interopérabilité de systèmes financiers locaux ; **aucun client ni déploiement régional n'est inféré**.
- **Action OSEF :** rattacher à FRAUD-007 #82, voir https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/82 ; vérifier les doublons avant ouverture de lab.

## Lab reproductible proposé
**Objectif :** Identifier les environnements Java potentiellement exposés, sans affirmer que l'infrastructure OSEF est vulnérable.

**Prérequis :** Flink/Kafka local, inventaire JDK et images, flux de tests synthétiques.

**Étapes :** Figer images et versions ; inventorier vendor/JDK/architecture ; comparer aux conditions exactes de l'avis ; appliquer les correctifs dans un lab ; rejouer les tests et conserver les logs.

**Critères de réussite :** Exposition documentée avec preuves, correctif validé sans régression et aucun usage de données réelles.

## Meetup proposé
Sécuriser les pipelines antifraude Kafka/Flink — SRE, DevSecOps et ingénieurs paiement ; atelier de 60 minutes avec audit d'images.

## Limites
Piste pédagogique non exécutée ; dates, disponibilité upstream et licences à revérifier avant publication externe. Aucun benchmark ni résultat d'essai affirmé.
