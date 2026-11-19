# OSFE — Protocole de benchmark antifraude reproductible (v0.1)

> Protocole prospectif, **aucune mesure réelle consignée**. Ne pas publier de classement sans tests répétés et équivalents.

## Question d'évaluation

Pour un **même scénario métier fictif**, quelles sont les performances et limites mesurables des moteurs Tazama et Jube, des expérimentations ML Ojuri et d'un moteur de règles maison Flink/Kafka, en tenant compte de leurs fonctions différentes ?

## 1. Préconditions et traçabilité obligatoires

Pour chaque exécution, conserver :
- Identifiant de test, UTC, commit SHA/version image/digest, licence vérifiée à la révision utilisée.
- Matériel hôte et invité (CPU, RAM, stockage, hyperviseur), versions OS, Docker, dépendances.
- Configuration : nombre de partitions, consommateurs, fenêtres, règles/seuils, concurrence, tailles du corpus.
- Commandes et scripts de lancement, générateur de données, schéma et seed aléatoire.
- Pipeline d'entrée/sortie réellement documenté, adaptateur/version et normalisation des champs.
- Temps de préchauffage, durée de test, nombre de répétitions et incidents.
- Logs filtrés (aucune clé, donnée réelle, URL privée) et lien vers PR de revue.

## 2. Corpus synthétique commun — version à concevoir

Catégories proposées :
- **NORMAL** : usage habituel fictif, paiements espacés.
- **VELOCITY** : volume inhabituel de paiements dans une fenêtre courte.
- **MULTI-PSP** : transaction liée à un scénario commun sur plusieurs acteurs fictifs.
- **DUPLICATE** : réémission de la même transaction fictive.
- **LATE** : événement arrivé en retard, hors ordre.
- **FALSE_POSITIVE** : transaction atypique mais légitime dans l'oracle synthétique.
- **FAILOVER** : interruption/reprise du traitement, sans supposer d'exactly-once.

Chaque événement contient uniquement `demo_event_id`, `demo_actor_id`, `timestamp_utc`, `synthetic_amount`, `scenario` et `oracle_label`. **Ce schéma est un contrat de test OSEF, pas un format officiel Tazama/Jube.** Les adaptateurs réalisent des conversions explicites, vérifiées et versionnées.

## 3. Mesures et calculs

- **TP, FP, TN, FN** selon l'oracle : une alerte ne prouve jamais une fraude réelle.
- **Precision = TP/(TP+FP)**, **Recall = TP/(TP+FN)**, **FPR = FP/(FP+TN)** ; dénominateur nul => non calculable.
- **PR-AUC** si un score continu est disponible et un protocole de calibration a été défini.
- **Débit** : événements traités/s mesurés après échauffement.
- **Latence p50/p95/p99** : préciser horloge/point de mesure (entrée → résultat) ; comparer seulement si les points sont équivalents.
- **Ressources** : CPU/RAM/pic, consommation disque, croissance des logs, ressources des dépendances incluses.
- **Résilience** : backlog, doublons, pertes, timeouts, reprise, état final et durée de rétablissement selon procédure documentée.
- **Investigation** : création/assignation d'un cas, statut, justification et correction de faux positif — présence/absence vérifiée pour version retenue.
- **Interopérabilité** : schéma, authentification, séparation de rôles, minimisation et rétention des signaux.

## 4. Exécutions de référence

1. Vérifier la santé du moteur et son état initial ; enregistrer le résultat.
2. Exécuter le corpus fonctionnel (chaque catégorie) ; ne pas mélanger création de données et mesure de latence sans le documenter.
3. Rejouer une deuxième fois, vérifier doublons/idempotence et absence de perte silencieuse.
4. Monter progressivement la charge : noter débit effectif, erreurs et saturation, sans fixer arbitrairement un seuil SLA.
5. Introduire une panne contrôlée (processus/transport), mesurer récupération et exhaustivité.
6. Exporter la matrice d'erreurs, tracer les faux positifs, comparer qualitativement les cas d'investigation.
7. Répéter à configuration constante ; mentionner dispersion et toute incertitude.
8. Revue d'un autre ingénieur sur la reproductibilité et l'interprétation.

## 5. Format minimal du rapport

| Champ | Valeur à renseigner |
|---|---|
| Lab / moteur / SHA / licence | NON TESTÉ |
| CPU / RAM / OS / Docker | NON RENSEIGNÉ |
| Jeu de données / seed / période | NON RENSEIGNÉ |
| TP / FP / TN / FN | NON MESURÉ |
| Precision / Recall / FPR | NON CALCULÉ |
| p50 / p95 / p99 | NON MESURÉ |
| Débit / erreurs / ressources | NON MESURÉ |
| Résilience / audit / cas | NON TESTÉ |
| Rapports et PR | À FOURNIR |

Ne jamais remplir les valeurs par intuition. Les résultats sont des **benchmarks de lab**, pas une certification ni une preuve d'aptitude à la production.

## 6. Sécurité, licences et contrôles

Valider les textes de licence et leurs obligations selon les usages (on-premises, self-hosted, service managé). Marble/ELv2 fait uniquement l'objet d'un comparatif documentaire sauf revue juridique et autorisation explicite. Interdire les données clients et les secrets de production. Isoler les réseaux, documenter la destruction des données de test, et ne pas interpréter les événements fictifs comme des renseignements réels.

## 7. Gates de validation

- [ ] Contrat de données synthétiques relu
- [ ] Matrice de versions et licences signée par relecteur
- [ ] Mapping d'entrée/sortie sourcé pour chaque moteur
- [ ] Scripts et rapports de tests reproductibles
- [ ] Métriques calculées et résultats non mesurés explicitement identifiés
- [ ] Résilience/faux positifs/audit documentés
- [ ] Revues sécurité et métier réalisées
- [ ] Publication d'un rapport avec limites
