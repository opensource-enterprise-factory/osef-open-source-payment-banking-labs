# Tazama pour les institutions de microfinance (IMF) d'Afrique francophone

**Note d'opportunité et de préqualification production — 19 novembre 2026**  
**Destinataires :** directions générales d'IMF/SFD, DSI, conformité LBC/FT/FP, risques, audit interne et ingénieurs OSEF.  
**Nature :** analyse de cas d'usage et grille d'ingénierie ; **ni avis juridique, ni certification réglementaire, ni offre de production déjà validée**.

## 1. Pourquoi Tazama ?

Tazama est une plateforme open source de surveillance des transactions, destinée à aider des prestataires de services financiers à évaluer les opérations susceptibles de présenter des indicateurs de fraude ou de blanchiment. Elle accepte des événements transactionnels, exécute des processeurs de règles/typologies et génère des résultats de surveillance. Une **alerte est un indicateur à investiguer**, et non une preuve de fraude ni une décision automatique de déclaration aux autorités.

**Valeur possible pour les IMF/SFD :**
- Adapter des contrôles aux activités réelles (dépôts, retraits, transferts, agents, mobile money, comptes liés) si les données et connecteurs existent.
- Disposer de résultats de règles exploitables et de journaux permettant la revue par les métiers, la conformité et le contrôle interne.
- Éviter le verrouillage complet par une solution de détection propriétaire : inspecter les composants ouverts, versionner les règles, former les équipes et organiser des contributions.
- Articuler des systèmes de microfinance hétérogènes à une couche de surveillance, sous réserve de développer des adaptateurs et de maîtriser la qualité des données.
- Construire une compétence locale en ingénierie antifraude, SRE, sécurité et conformité. **Le gain financier, la baisse de fraude et les performances en production restent à mesurer**.

**Cas d'usage proposés, non présents automatiquement dans notre démo :**

| Cas | Exemple de scénario de surveillance | Validation indispensable |
|---|---|---|
| Vélocité | Volume/frequence inhabituel(le) de transferts ou retraits par compte ou agent | Fenêtres temporelles, saisonnalité, faux positifs |
| Fractionnement | Opérations répétées proches d'un seuil métier | Historique, contexte, réglementation |
| Comptes de passage | Entrées de fonds suivies de sorties rapides | Liens entre comptes, règles et droits d'accès |
| Comportement atypique | Écart significatif de l'activité habituelle | Segmentation clients, historique fiable |
| Risques liés aux canaux digitaux | Corrélation d'événements agent, mobile money et compte | Interfaces, qualité des événements et gestion des identifiants |

**Attention :** pas de garantie que ces cinq scénarios soient disponibles « prêts à l'emploi » avec les seules images et règles 901/902 du lab.

## 2. Ce que FRAUD-002 a réellement démontré

Sur la VM Ubuntu isolée `osef-fraud-01` (VirtualBox, profil DockerHub Public Tazama) :
- 13 services Tazama démarrés, correction contrôlée du healthcheck Batch PPA et persistance de l'état `healthy` après redémarrage.
- Tests officiels Newman Public DockerHub 2.1 : **4 requêtes, 39 assertions, aucune erreur** lors d'une exécution confirmée le 19/11/2026.
- Transaction Web **fictive de 370 USD** ; TMS a transmis `pacs.008` et `pacs.002` ; Admin Service a renvoyé un rapport `NALT` avec score de typologie **200**, seuil d'alerte **300**, seuil d'interdiction **500** ; règles 901/902 pondérées à 100 chacune et EFRuP à 0.
- Une anomalie de visualisation persistante (`null`) dans Tazama Demo est **non résolue** : le rapport backend existe malgré cet affichage.
- **Non démontré** : réduction de fraude, scénario d'alerte positive maîtrisé, performance à charge réelle, intégration à un cœur de microfinance, usage de données réelles, conformité ou sécurité de production.

Voir le [contrat de mapping Gate D](GATE-D-CONTRAT-TAZAMA-FRAUD-001.md) : `NALT` implique **aucun signal** transmis au relais FRAUD-001.

## 3. Production IMF : distinguer faisabilité technique et conformité

L'utilisation de Tazama par une IMF/SFD en production est **un projet de transformation et de maîtrise des risques**, pas une conversion du laboratoire en service exposé.

### 3.1 Gouvernance et obligations de l'institution

Avant tout déploiement, l'IMF et ses conseils doivent établir une matrice de textes **par pays, activité, statut d'agrément et autorité compétente**, puis en vérifier les versions applicables :
- Cadre applicable aux **systèmes financiers décentralisés (SFD)** de l'UMOA et ses déclinaisons/actes nationaux, selon la situation de l'IMF.
- Cadre **LBC/FT/FP**, obligations de vigilance, organisation, contrôle interne, surveillance, traitement des alertes et, le cas échéant, signalement à l'autorité compétente.
- Dispositions relatives aux **services de paiement** si l'IMF offre les services concernés : ne pas présumer qu'elles s'appliquent à toutes les IMF de façon identique.
- **Données personnelles** : droit national applicable, finalités, base légale, accès, sous-traitance, hébergement/transferts transfrontaliers, conservation et droits des personnes.
- **Externalisation, résilience et sécurité** : exigences réglementaires ou contractuelles applicables à l'hébergement et aux prestataires.

**Important :** les textes BCEAO constituent les références de vérification, mais l'application d'une obligation à une institution particulière doit être confirmée avec son responsable conformité/conseil juridique et les autorités compétentes. Nous **ne pouvons pas confirmer** une autorisation automatique, une certification Tazama BCEAO ou des obligations uniformément applicables à toutes les IMF des huit pays.

**Sources BCEAO :**
- [Réglementation des systèmes financiers décentralisés](https://www.bceao.int/fr/reglementations/reglementation-des-systemes-financiers-decentralises).
- [LBC/FT/FP — instruction n°001-03-2025 du 18 mars 2025](https://www.bceao.int/fr/reglementations/instruction-ndeg001-03-2025-du-18-mars-2025-portant-modalites-de-mise-en-oeuvre-par).
- [LBC/FT/FP — textes et loi uniforme](https://ns2.bceao.int/index.php/fr/reglementations/lutte-contre-le-blanchiment-de-capitaux-et-le-financement-du-terrorisme).
- [Fintech et digitalisation des services financiers : réglementation et guide de digitalisation des SFD](https://www.bceao.int/fr/content/fintech-et-digitalisation-des-services-financiers-dans-luemoa).

### 3.2 Architecture et sécurité

**Ne pas mettre en production notre `tazama-stack` Docker Compose de démonstration.** Son README avertit explicitement de la limitation à la démonstration/exploration/tests. Étudier les guides Helm/distribués officiels et une architecture adaptée à la charge et au niveau de criticité.

Minimum de qualification technique :
- Segmentation réseau et absence d'API métier sans authentification ; SSO/IAM, RBAC, moindre privilège et authentification interservices.
- TLS/chiffrement en transit et au repos, gestion et rotation des secrets, traçabilité/horodatage, logs sans données sensibles.
- Inventaire des images/versions/licences, analyse vulnérabilités et dépendances, chaîne CI/CD contrôlée, SBOM et politiques de correctifs.
- Haute disponibilité, supervision, alertes d'exploitation, gestion de capacité, sauvegarde/restauration testée, objectifs RPO/RTO approuvés.
- Contrôles de confidentialité sur les événements transactionnels, minimisation et conservation légale des données.
- Tests de charge, perturbation de NATS/PostgreSQL/Valkey, pannes réseau, rejeux et reprise contrôlée.
- Intégration documentée avec le core banking/SIG de l'IMF et ses partenaires, et validation des schémas/qualité/idempotence.

**Sources Tazama :**
- [README Tazama Core — avertissement de démonstration](https://github.com/tazama-lf/tazama-stack/blob/main/core/README.md).
- [Architecture de déploiement via Kubernetes/Terraform/Helm/ArgoCD (production-like)](https://github.com/tazama-lf/cloud-infrastructure-deploy).
- [Principes d'architecture Tazama](https://github.com/tazama-lf/docs/blob/dev/Guides/tazama-design-principles.md).

### 3.3 Règles métier et exploitation

- Formaliser le catalogue de risques de l'IMF, la segmentation des clients/agents et la gouvernance des règles.
- Rejouer des données fictives, puis utiliser des données réelles **uniquement après** la validation des autorisations et contrôles de confidentialité.
- Mesurer latence de surveillance, qualité des données, taux d'alertes, faux positifs et cas non détectés avec des jeux d'essai documentés.
- Prévoir une file d'investigation, la séparation des tâches, les délais de traitement, les escalades et les règles de clôture d'alerte.
- Tester les règles après chaque modification avec non-régression, revue et approbation par les responsables habilités.
- Éviter de confondre scoring, alerte, interdiction et décision réglementaire. Toute automatisation de blocage nécessite un cadrage juridique et opérationnel séparé.

## 4. Parcours d'adoption proposé pour une IMF

| Phase | Objectif | Preuves de sortie |
|---|---|---|
| **P1 — Diagnostic** | Identifier activités, risques, architecture, SI, flux, données et textes applicables | Cartographie et registre des écarts, risques prioritaires, sponsor conformité |
| **P2 — Pilote isolé** | Intégrer un canal fictif puis des cas approuvés, créer 2–3 règles adaptées et des jeux de tests synthétiques | Démonstrations, catalogue de règles, mesures de précision et de latence |
| **P3 — Qualification** | Audit sécurité, revue juridique, charge, reprise, exploitation et autorisations nécessaires | Décision go/no-go formelle ; architecture et procédures approuvées |
| **P4 — Production maîtrisée** | Déployer progressivement avec surveillance, revue des alertes, support, gestion des incidents/changements | PV de mise en service, suivi KPI, preuves d'exploitation |

**Aucun calendrier ou budget n'est garanti.** La durée et le coût dépendent des flux, du SI, des règles, de l'hébergement, des intégrations et du périmètre réglementaire.

## 5. Opportunité de service OSEF (hypothèse commerciale à tester)

Proposition de valeur possible :
1. **Diagnostic antifraude & readiness Open Source** : analyse des flux, dispositifs actuels, risques, gouvernance des règles, sécurité et prérequis réglementaires.
2. **Pilote Tazama** : laboratoire reproductible, adaptateur vers système de microfinance, règles documentées et tests.
3. **Ingénierie de production** : infrastructure, sécurité, résilience, CI/CD, observabilité, contrôle de conformité avec l'institution et ses conseils.
4. **Support / formation / contribution** : montée en compétence des ingénieurs et des équipes conformité, support récurrent, contribution aux composants upstream.

La licence Apache 2.0 des projets Tazama concernés permet des usages et redistributions soumis à ses conditions ; **vérifier le dépôt et la licence de chaque composant/image**, notamment les règles et extensions. Les coûts d'intégration, support, sécurité, exploitation et audit restent à évaluer.

**Ce document n'affirme aucun partenariat commercial, aucune homologation BCEAO et aucune capacité de production déjà obtenue par OSEF.**

## 6. Critères de clôture de cette analyse

- [x] Cas d'usage IMF, bénéfices potentiels et limites du lab explicités.
- [x] Principaux thèmes réglementaires UMOA et sources officielles référencés.
- [x] Conditions techniques, sécuritaires et organisationnelles de production décrites.
- [x] Parcours pilote → qualification → production proposé.
- [ ] Vérification juridique **par pays et par IMF cible**, avec l'établissement concerné.
- [ ] Qualification terrain du besoin, des données, de la performance et des coûts.
- [ ] Revue par un responsable conformité IMF et un architecte sécurité indépendant.

**Prochaine étape FRAUD-002 :** terminer Gate D/E de l'adaptateur fictif vers FRAUD-001. La préparation production IMF constitue un chantier ultérieur distinct du lab pédagogique.
