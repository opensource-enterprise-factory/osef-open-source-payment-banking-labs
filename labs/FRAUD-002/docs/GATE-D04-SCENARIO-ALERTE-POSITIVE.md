# FRAUD-002 — Gate D04 : obtenir une alerte positive authentique

**Statut au 19/11/2026 : ALRT non encore reproduit. Plan d'investigation uniquement. Pas de changement de VM.**

## Éléments prouvés

- Les 13 services Tazama Core du profil Public DockerHub sont déployés dans le lab isolé.
- La suite officielle Newman 2.1 a réussi (39 assertions), mais elle ne démontre pas une alerte positive.
- Une transaction synthétique de 370 USD a produit un rapport NALT, score 200, seuil d'alerte 300.
- Gate D01/D02 : 19 tests unitaires réussis et API locale lue ; résultat NO_PUBLISH / NALT.
- Le frontend Demo affiche parfois null malgré un rapport backend existant : suivi séparé, non bloquant.

## Sources officielles et limites

- [Guide Tazama Demo UI](https://github.com/tazama-lf/docs/blob/dev/Guides/demo-ui-guide.md) : ALRT signifie alerte ; NALT signifie absence d'alerte ; les seuils de typologie déterminent les indications visuelles.
- [Event Adjudicator](https://github.com/tazama-lf/event-adjudicator) : décrit la génération de rapports d'alerte et le paramètre ALERTS_ONLY ; la valeur active sur notre VM n'est pas établie ici.
- [Collection officielle Newman 3.1 Full-Service](https://github.com/tazama-lf/postman/blob/main/Newman/Newman%20-%203.1.%20(NO-AUTH)%20Public%20DockerHub%20Full-Service%20Test.postman_collection.json) : résultat attendu NALT dans l'assertion de rapport inspectée.
- [Collection de tests des règles 901/902 — profil Public DockerHub](https://github.com/tazama-lf/postman/blob/main/2.3.%20Rule%20Functionality%20Testing%20-%20Public%20DockerHub.postman_collection.json) : scénarios de répétition, fenêtres temporelles et multitenancy ; pas une garantie d'ALRT end-to-end.

## Configuration officielle retrouvée au commit épinglé

Le fichier officiel [00-public-base.sql](https://github.com/tazama-lf/tazama-stack/blob/83e4b12c16986aedfff843ed84b7045ac912ec0a/core/postgres/migration/config/00-public-base.sql), et non une hypothèse, définit :

- Règle **901** : nombre de transactions sortantes du débiteur dans les dernières **86 400 000 ms** (24 h). Bandes `.01` : moins de 2 ; `.02` : de 2 à moins de 3 ; `.03` : 3 ou plus.
- Règle **902** : nombre de transactions entrantes du créancier, même fenêtre de 24 h et bandes analogues.
- Typologie `999-901-902@4.0.0` : addition des poids des règles 901 et 902. Bandes `.01` = 100, `.02` = 200, `.03` = 400 pour chacune.
- Seuil d'alerte **300** ; seuil d'interdiction **500** ; EFRuP contribue un poids **0** dans cette configuration.
- [02-public-dockerhub.sql](https://github.com/tazama-lf/tazama-stack/blob/83e4b12c16986aedfff843ed84b7045ac912ec0a/core/postgres/migration/config/02-public-dockerhub.sql) relie la typologie 999-901-902 au message `pacs.002.001.12`.

**Conséquence testable, pas résultat déjà observé :** une séquence de transactions synthétiques *réussies* entre les mêmes comptes peut conduire à la bande `.02` ou `.03` et à un total atteignant ou dépassant 300. Le statut exact doit être contrôlé dans le rapport émis par la VM ; les résultats peuvent dépendre de l'historique enregistré et des états métier.

## Scénario positif proposé — pas encore exécuté

1. Conserver la configuration de la VM et les mêmes débiteur et créancier fictifs dans Tazama Demo.
2. Envoyer une **nouvelle transaction fictive** via l'interface Demo ; noter l'heure, le montant fictif et les réactions visibles. L'interface peut afficher `null` sans que le backend soit en échec.
3. Identifier dans les logs TMS le nouvel identifiant `pacs.002`, et récupérer son rapport via Admin Service ; **ne pas associer automatiquement un identifiant ancien à un nouvel envoi**.
4. Contrôler `data.report.status`, les règles `subRuleRef`, les poids et le score. Si toujours `NALT`, inspecter si les messages réutilisent les mêmes IDs ou si les règles conservent le bon historique ; éviter des clics en rafale.
5. Quand une alerte `ALRT` apparaît réellement, consigner les champs expurgés du rapport, la configuration/version et la preuve ; cela validera D04.
6. Ne pas publier de signal FRAUD-001 tant que D05 (politique de mapping et sévérité) n'est pas approuvé.

**Interdictions :** ne pas éditer la configuration SQL/Compose sur la VM, ne pas forcer un score dans une réponse JSON, ne pas utiliser de vrais comptes, ne pas effacer les volumes de données pour forcer le scénario.

## Plan d'exécution

1. Inspecter dans GitHub les configurations exactes des règles 901 et 902 et de la typologie 999-901-902@4.0.0, pour le profil épinglé et les images utilisées.
2. Définir une séquence de transactions strictement synthétiques censée provoquer une alerte via le pipeline complet. Ne pas falsifier le JSON ou les scores.
3. Si du code ou de la configuration doit changer, créer et revoir une PR GitHub, la fusionner puis appliquer uniquement par git pull --ff-only. Aucune édition manuelle sur la VM.
4. Lancer le scénario dans le réseau de laboratoire, récupérer le rapport par Admin Service et conserver une preuve expurgée.
5. D04 est validé uniquement si data.report.status == ALRT est observé avec scores, typologie, règles et version identifiables.
6. D05 : approuver le mapping métier (catégorie, gravité, destinataire, TTL et jeton opaque) avant toute publication vers FRAUD-001.

## Contrôle immédiat non destructif

```bash
cd /home/lionel/osef-open-source-payment-banking-labs
git status -sb
python3 labs/FRAUD-002/scripts/tazama-safe.py ps
```

## Reste pour clôturer FRAUD-002

- [ ] D04 : rapport ALRT réel sur données fictives.
- [ ] D05 : mapping métier approuvé ; aucun secret ni donnée client partagée.
- [ ] D06 : transmission autorisée PSP A → relais FRAUD-001 → PSP B.
- [ ] Gate E : accès 401, doublon 409, panne 503, TTL, journal d'audit, non-régression, revue par un second ingénieur.

**Ne représente ni une implémentation OFTA officielle ni une validation de production pour une IMF.**
