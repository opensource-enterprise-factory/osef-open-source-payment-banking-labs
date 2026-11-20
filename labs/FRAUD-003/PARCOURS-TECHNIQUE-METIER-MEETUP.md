# FRAUD-003 — Parcours intégré Technique · Métier · Meetup

**Statut : référentiel pédagogique proposé pour revue dans la PR #79.** Ce document ne prouve ni fonctionnement d'un composant FRAUD-003 ni conformité bancaire.

## Règle OSEF

Chaque étape du lab produit **trois éléments indissociables** :
1. **Technique** : une réalisation vérifiable, un protocole de test, des journaux expurgés et un résultat observé.
2. **Métier** : le problème antifraude traité, les rôles, les décisions, les faux positifs, les risques et les limites.
3. **Meetup** : une explication vulgarisée, une démonstration reproductible et au moins une question pour les praticiens.

Une **preuve technique obtenue** ne vaut pas **validation métier** ; une **présentation préparée** ne vaut pas **meetup tenu**. Le kit de meetup est un critère de clôture du lab ; la tenue publique de l'événement peut être ultérieure.

## Étapes et livrables

| Gate | Technique (à démontrer) | Métier (à expliquer) | Meetup (à préparer) | Clôture du Gate |
|---|---|---|---|---|
| 0 — Fondations | Contrats et preuves FRAUD-001/002 vérifiés ; écarts recensés | Différence détection, signalement, corrélation et investigation | Schéma simple FRAUD-001 → 002 → 003 | Revue des dépendances et des limites |
| 1 — Gouvernance | Matrice d'identités, permissions, API JSON et tests attendus | Banque, PSP, mobile money : propriété des signaux, habilitations et partage | Exemple : « pourquoi ne pas partager les données clients ? » | Approbation métier et sécurité des politiques |
| 2 — Trois simulateurs | Banque A, PSP B et Mobile C ; isolation démontrée par tests d'accès autorisés et interdits | Frontière entre établissements, responsabilités et confidentialité | Trois consoles, démonstration « B ne lit pas A » | Tests d'isolation réussis, preuves et revue |
| 3 — Corrélation | Règle explicable, idempotence, expiration et signal absent | Différence entre suspicion, alerte et fraude établie ; limites des rapprochements | Deux signaux synthétiques → une **proposition** motivée | Scénarios positifs et négatifs démontrés |
| 4 — Dossier | Ouvrir, modifier et consulter un dossier avec historique ; accès par participant | Cycle d'investigation, décisions et audit ; étude préalable de Tazama CMS | Démo « de l'alerte au dossier » | Dossier et journal vérifiables |
| 5 — Faux positif | Rétractation/correction, réévaluation et notifications autorisées | Coûts et effets des faux positifs, mécanisme de contestation | Démo d'une erreur corrigée sans effacement de l'histoire | Historique intact et diffusion contrôlée |
| 6 — Sécurité et fiabilité | Refus 401/403 selon contrat, rejeu 409, panne/reprise, TTL, tests fuite de données | Risque opérationnel, exigences de conservation, traçabilité | Discussion « ce qui échoue encore en production » | Rapport des tests, écarts et limites |
| 7 — Recette | Rejeu complet depuis un clone propre, logs expurgés, versions et limites | Valeur pour un établissement financier, conditions d'un pilote distinct | Répétition de démonstration et support | Revue indépendante et PV approuvé |
| 8 — Transmission | Script de démo reproductible avec commandes et résultats attendus | Explication non experte des étapes et identification des questions réservées aux spécialistes | Kit final : titre, déroulé, slides, démo, FAQ, appel aux contributeurs | Kit relu et répétition validée ; meetup public facultatif |

## Objectifs d'apprentissage métier (à documenter, non à présumer acquis)

- Distinguer fraude au virement, fraude par ingénierie sociale, prise de contrôle de compte et comptes mules ; consulter des références documentaires fiables et distinguer exemples synthétiques / incidents avérés.
- Expliquer l'utilisation des **règles**, **typologies**, **scores** et **seuils** dans le seul profil Tazama testé, sans généraliser ces configurations à toutes les institutions.
- Expliquer le parcours : événement → alerte → qualification → partage autorisé → corrélation → investigation → rectification/clôture.
- Reconnaître l'incertitude d'une alerte, les faux positifs et le coût d'un accès non autorisé ; aucune décision automatique de blocage.
- Expliquer les limites : pas de données réelles, pas de performance validée, pas de preuve de conformité, pas d'intégration OFTA officielle.

## Sujet meetup proposé

**« De l'alerte à l'investigation : comment l'Open Source peut renforcer la lutte contre la fraude dans les paiements en Afrique francophone ? »**

**75 minutes proposées :** 0–10 min typologies et enjeux métier ; 10–25 min Tazama et cheminement d'une alerte ; 25–45 min démonstration *réellement validée* de FRAUD-001/002/003 ou architecture explicitement théorique si le troisième lab n'est pas prêt ; 45–60 min discussion avec un praticien de la fraude invité **si confirmé** ; 60–75 min questions, limites, contribution.

### Kit meetup — critères de préparation

- [ ] Support de vulgarisation et glossaire
- [ ] Démo rejouée avec données synthétiques et plan de secours
- [ ] Chronogramme et questions d'animation
- [ ] Explication des limites de Tazama, des faux positifs et du partage
- [ ] Sources et liens GitHub, sans secrets ni données personnelles
- [ ] Répétition évaluée par un autre ingénieur OSEF
- [ ] Invitation d'un expert métier (option recommandée, sa participation n'est pas présumée)

## Règles de clôture du laboratoire entier

- [ ] Gates techniques 0–7 validés et preuves reproductibles
- [ ] Apprentissage métier démontré (fiche métier + explications, non simple liste de définitions)
- [ ] Gate 8 kit meetup prêt et répétition effectuée
- [ ] Revue indépendante sécurité/technique et réserves traitées ou acceptées explicitement
- [ ] Procès-verbal final approuvé, liens vers résultats, versions et limites
- [ ] Issue #63 fermée **seulement après** satisfaction de ces conditions

## Gouvernance GitHub/VM

Les changements de scripts, code, documentation et configuration passent par **branche → PR → revue → fusion** puis mise à jour `git pull --ff-only` dans la VM. Les diagnostics exécutés sur VM sont en lecture seule. Les données sont intégralement fictives.
