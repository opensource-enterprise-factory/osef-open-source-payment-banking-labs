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
