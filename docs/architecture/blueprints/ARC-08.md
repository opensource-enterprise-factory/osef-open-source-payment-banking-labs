# ARC-08 — Payment Fraud & Security

**Statut : proposée · Version : cadrage v1.0 (17 novembre 2026) · Responsable : à attribuer**  
**Cas d'usage :** Tester détection d'anomalies et politique d'accès sans données sensibles  
**Acteurs cibles :** Équipes sécurité, banques, fintechs

> Architecture **pédagogique et hypothétique**. Les interfaces, composants, performances et licences restent à valider dans les labs. Aucune homologation bancaire ou connexion à un réseau de paiement n'est revendiquée.

## 1. Architecture cible simplifiée
```text
Événements synthétiques → Moteur de règles → Alertes → Tableau de revue
```

## 2. Composants candidats et responsabilités
Open Policy Agent ou règles développées pour le lab ; Keycloak comme candidat IAM

Ces produits ne constituent pas automatiquement une solution intégrée, cohérente ou prête pour production. Pour chaque composant : sélectionner la version, relever la licence et documenter la compatibilité.

## 3. Interfaces et données à spécifier
Données minimales, seuils, règles, versionnement, alertes, accusés de traitement

**Documentation obligatoire :** schéma des acteurs, contrat API/protocole versionné, schéma de données synthétiques, diagramme de séquence (succès/erreur), gestion des doublons, timeouts, journalisation expurgée et mécanismes de reprise appropriés.

## 4. Scénarios de tests et démonstrations
Burst de transactions, anomalie de montant, faux positifs, permissions, traçabilité

Les tests doivent être transformés en cas reproductibles : entrée, résultat attendu, résultat observé, version, date, logs expurgés, nettoyage et limites connues.

## 5. Sécurité et limites
- Pas d'identités financières réelles, PAN, PIN, CVV, cryptogrammes, HSM, clés de production ou réseau bancaire.
- Uniquement données synthétiques, accès minimaux et isolation réseau.
- Aucun SLA, débit, capacité ou conformité n'est attesté sans mesures et audit approprié.
- Vérifier licences et conditions d'usage de chaque composant/édition, ainsi que les obligations réglementaires applicables **avant toute mission client**.

## 6. Labs et produits/services OSEF associés
- **Labs :** OPB-010, OPB-011, OPB-012.
- **Produits / services envisagés :** Lab sécurité / OPS-03.
- **Livrable de blueprint :** architecture documentée, scripts commentés, contrats, tests, rapport et limites.

## 7. Critères de validation
- [ ] Composants, versions et licences vérifiés dans les sources officielles.
- [ ] Diagrammes de contexte, de composants et de séquence revus.
- [ ] Contrats d'interface et données synthétiques définis.
- [ ] Scénarios nominals, négatifs et de reprise exécutés.
- [ ] Preuves reproductibles, logs expurgés et mesures disponibles.
- [ ] Revue indépendante par un autre ingénieur.
- [ ] Décisions, risques et limites consignés.

## 8. Source amont de départ
- https://www.openpolicyagent.org/

> Source de référence initiale : elle ne vaut pas confirmation de compatibilité ou de validation de cette architecture OSEF.
