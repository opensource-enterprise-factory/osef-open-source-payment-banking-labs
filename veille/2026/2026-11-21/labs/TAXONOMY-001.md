# TAXONOMY-001 — Taxonomies antifraude fédérées

**Extension de :** [FRAUD-003 #63](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63), en synergie avec [FRAUD-002 #50](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/50) et [OSFE #88](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/88).

**Sources :** https://www.tazama.org/blog/2026/open-financial-trust-alliance/ ; annonce Linux Foundation du 18 novembre 2026. **La taxonomie de ce lab est fictive et non un standard OFTA.**

**Objectif :** démontrer la traduction contrôlée d'événements de fraude synthétiques venant de trois institutions fictives, avec traçabilité des ambiguïtés.

**Prérequis :** trois catalogues CSV fictifs (banque, PSP, mobile money), scripts Python, tests unitaires, schémas JSON, aucune donnée personnelle.

**Étapes :**
1. Définir des catégories communes **pédagogiques**, versionnées et sourcées.
2. Construire les mappings de chaque catalogue et documenter « sans équivalent ».
3. Vérifier transformation aller-retour sur des événements synthétiques et rejets explicites.
4. Tester le contrôle d'accès, les logs redigés et la provenance des mappings.

**Succès :** 100 % des catégories d'entrée mappées ou marquées non mappées, aucun champ PII transmis, version des mappings conservée, rapports reproductibles.

**Meetup :** réutiliser [#66](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/66) ; démo mapping inter-PSP fictif, 60 min.
