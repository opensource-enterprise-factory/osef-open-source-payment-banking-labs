# Glossaire complet — OSEF FRAUD-001 & FRAUD-002 / Tazama

**Édition de référence : 19 novembre 2026.** Glossaire destiné aux ingénieurs paiement, développeurs, DevOps, SRE et relecteurs du laboratoire OSEF. Ce document définit les termes employés dans les guides, les tests et les discussions. Il ne remplace pas la documentation officielle d'un produit ou une norme et **ne constitue pas une validation de production**.

**Convention :** « dans le laboratoire » décrit le comportement effectivement implémenté ou vérifié dans OSEF ; « en général » décrit une notion technique. Les données et PSP sont **fictifs**. Les statuts et seuils Tazama mentionnés sont spécifiques au profil de démonstration testé.

## 1. Paiement, monétique et acteurs

| Terme | Définition et rôle dans le laboratoire |
|---|---|
| **Paiement électronique** | Transfert de valeur ou instruction de paiement traité par des systèmes numériques. FRAUD-002 simule des messages de paiement, sans transférer de fonds réels. |
| **Monétique** | Domaine technique et opérationnel des paiements électroniques, notamment cartes, terminaux, acceptation et traitements associés. FRAUD-002 relève plus largement des infrastructures de paiement. |
| **PSP — Payment Service Provider** | Prestataire de services de paiement. **PSP A** et **PSP B** sont des services fictifs qui émettent et consultent des signaux antifraude. |
| **PSP A / origin** | PSP émetteur du signal dans FRAUD-001 ; soumet une alerte minimale à travers le relais. N'est pas la banque émettrice d'un paiement réel. |
| **PSP B / recipient** | PSP destinataire autorisé du signal ; consulte son `inbox`. |
| **Banque** | Établissement bancaire ; aucun établissement réel n'est raccordé au lab. |
| **Fintech** | Entreprise proposant des services financiers par la technologie. Le lab s'adresse notamment à ses ingénieurs sans brancher de données clients. |
| **Mobile money** | Services de monnaie électronique accessibles notamment sur mobile ; aucun portefeuille réel n'est utilisé. |
| **EME** | Émetteur de monnaie électronique ; catégorie d'acteurs régionaux, distincte des PSP fictifs du lab. |
| **SFD / IMF** | Système financier décentralisé / institution de microfinance ; publics potentiels d'un pilote futur, non participants au lab. |
| **BCEAO / UMOA / UEMOA** | Banque Centrale des États de l'Afrique de l'Ouest / Union monétaire ouest-africaine / Union économique et monétaire ouest-africaine ; contexte institutionnel à considérer lors d'une étude réelle, pas une certification du lab. |
| **OFTA** | Open Financial Trust Alliance, initiative d'écosystème citée comme contexte de coopération antifraude. Le relais OSEF n'est **pas** une intégration OFTA officielle. |
| **Interopérabilité** | Capacité de systèmes distincts à échanger et exploiter des informations selon un contrat défini. FRAUD-002 prouve un échange contrôlé entre services simulés. |
| **Transfert inter-PSP** | Transmission d'un signal de risque entre deux prestataires simulés via un relais, sans transfert d'argent. |
| **Transaction synthétique / fictive** | Message de paiement fabriqué pour un test, sans personne ni compte réel. |
| **Signal antifraude** | Information minimale signalant un risque potentiel ; **ce n'est pas une preuve de fraude ni un ordre de bloquer le paiement**. |
| **Suspicious transfer** | Valeur de catégorie `suspicious-transfer` utilisée par FRAUD-001 ; classification explicitement approuvée pour le lab. |
| **Account takeover** | Prise de contrôle d'un compte ; catégorie de risque acceptée par le schéma FRAUD-001. |
| **Social engineering** | Manipulation d'une personne pour provoquer une action ou révéler des informations ; catégorie de risque acceptée par FRAUD-001. |
| **AML / LBC-FT** | Anti-Money Laundering / lutte contre le blanchiment de capitaux et le financement du terrorisme ; domaine voisin, **non validé réglementairement** par le lab. |
| **Scam** | Escroquerie, souvent obtenue par manipulation de la victime. À distinguer d'une simple alerte technique. |
| **Fraud detection** | Détection ou signalement de comportements potentiellement frauduleux à partir de règles, typologies et analyses ; ne vaut pas condamnation ou confirmation. |
| **Partage de renseignement antifraude** | Échange encadré d'indicateurs ou signaux de risque entre acteurs ; dans OSEF, les signaux sont minimisés et fictifs. |

## 2. Messages ISO 20022 et champs transactionnels

| Terme | Définition et rôle |
|---|---|
| **ISO 20022** | Norme internationale de modélisation et de messages financiers ; les scénarios Tazama emploient des messages conformes à des familles ISO 20022. |
| **pacs** | Famille de messages « Payments Clearing and Settlement » dans ISO 20022. |
| **pacs.008** | Message de transfert de crédit de client entre institutions financières (`FIToFICstmrCdtTrf`) ; injecté de manière fictive dans le TMS. |
| **pacs.002** | Message de rapport d'état d'un paiement (`FIToFIPmtStsRpt`) ; l'identifiant de son message est utilisé pour demander le rapport Admin Tazama. |
| **pain.001 / pain.013** | Messages de la famille « Payments Initiation ». Le scénario Newman employé s'intitule « sans pain.001/013 » : il ne les inclut pas. |
| **FIToFIPmtSts** | Objet de rapport de statut interbancaire tel qu'exposé dans le JSON Tazama du test `pacs.002` ; chemin effectivement vérifié dans le lab. |
| **GrpHdr** | Group Header, en-tête de groupe d'un message ISO 20022. |
| **MsgId / msgid** | Identifiant de message. Dans le lab, `transaction.FIToFIPmtSts.GrpHdr.MsgId` doit concorder avec le `msgid` interrogé et `data.transactionID`. |
| **EndToEndId** | Identifiant de bout en bout d'une instruction ou opération, généré de façon synthétique par Newman. Ne pas le confondre avec `MsgId`. |
| **transactionID** | Identifiant associé au rapport Tazama (`data.transactionID`), comparé strictement au `MsgId` recherché. |
| **dbtr / debtor** | Débiteur, partie à l'origine du paiement dans les données ISO 20022. |
| **cdtr / creditor** | Créancier, bénéficiaire du paiement. |
| **dbtrId / cdtrId** | Identifiants de débiteur et de créancier dans le jeu de données de démonstration. Interdits dans le signal minimal FRAUD-001. |
| **dbtrAcctId / cdtrAcctId** | Identifiants des comptes du débiteur et du créancier dans les tests synthétiques. |
| **MSISDN** | Mobile Station International Subscriber Directory Number, numéro téléphonique identifiant un abonnement mobile ; **donnée potentiellement personnelle**, non transférée dans le relais. |
| **PAN** | Primary Account Number, numéro principal d'une carte de paiement ; ne jamais transférer dans les signaux du lab. |
| **Schéma JSON** | Contrat sur les noms, types et contraintes des champs d'un objet JSON ; FRAUD-001 le vérifie avant création. |
| **DataCache** | Objet de données auxiliaires présent dans le rapport Tazama de démonstration ; non recopié vers PSP B. |
| **Network map** | Configuration Tazama décrivant le routage des messages et les composants de traitement. Ne désigne pas une carte géographique. |

## 3. Tazama, ses 13 services et son moteur de détection

| Terme | Définition et rôle dans le profil Tazama Public DockerHub |
|---|---|
| **Tazama / Tazama Core** | Plateforme open source de surveillance transactionnelle utilisée comme moteur d'évaluation dans FRAUD-002. |
| **Stack / pile logicielle** | Ensemble coordonné de services logiciels, configurations, bases et bus nécessaires au fonctionnement. |
| **Public DockerHub profile** | Configuration de démonstration Tazama déployant le profil public avec des images depuis Docker Hub. Elle **n'est pas destinée à la production**. |
| **Tazama Demo (`tazama-demo`)** | Interface web permettant de simuler et visualiser des transactions ; un affichage incomplet ne prouve pas l'absence d'un rapport côté Admin. |
| **TMS — Transaction Monitoring Service (`tms-service`)** | API qui reçoit les messages transactionnels à évaluer ; port 5000 en localhost sur la VM. |
| **Event Director (`event-director`)** | Service orchestrant ou orientant les traitements à partir de la configuration de routage. |
| **Rule Processor** | Service exécutant une règle et retournant son résultat ; dans ce profil, `rule-901` et `rule-902`. |
| **Rule 901 / Rule 902** | Règles identifiées dans le profil Tazama testé ; leurs résultats contribuent à la typologie 999-901-902. Les étiquettes numériques n'impliquent pas à elles seules une signification métier universelle. |
| **EFRuP — Event-Flow Rule Processor** | Composant ou résultat de règle de flux d'événements observé dans les tests ; pondération nulle dans le scénario NALT validé. |
| **Typology Processor (`typology-processor`)** | Service qui agrège ou interprète plusieurs résultats de règles selon une typologie configurée. |
| **Typologie** | Regroupement de règles et de conditions destiné à identifier un scénario de risque ; dans le profil testé : `999-901-902@4.0.0`. |
| **Typology 999-901-902@4.0.0** | Identifiant/version de typologie observée dans les rapports du profil public ; ses trois règles incluent 901, 902 et EFRuP. |
| **Event Adjudicator (`event-adjudicator`)** | Service qui finalise l'évaluation et contribue à la détermination du résultat selon la configuration. |
| **Event Flow (`event-flow`)** | Service gérant des conditions ou événements liés aux entités et comptes selon le profil. |
| **Admin Service (`admin-service`)** | API d'administration et de consultation des rapports ; port 5100 en loopback, endpoint `getreportbymsgid`. |
| **Batch PPA (`batch-ppa`)** | API de prétraitement par lots du profil Tazama ; une erreur de healthcheck indépendante a été corrigée dans le lab. L'abréviation **PPA** n'est pas développée davantage sans référence confirmée. |
| **PostgreSQL (`core-postgres`)** | Base relationnelle utilisée pour configurations et données persistantes Tazama ; port hôte 15432 en loopback dans cette configuration. |
| **NATS (`nats`)** | Bus de messagerie asynchrone pub/sub entre composants de la pile. |
| **Valkey (`valkey`)** | Magasin clé-valeur en mémoire, utilisé notamment comme cache. |
| **Redis** | Magasin clé-valeur dont les interfaces et usages sont proches de ceux de Valkey ; terme apparu dans des messages de dépendance. |
| **Rule result / `ruleResults`** | Résultat de l'exécution d'une règle, contenant selon le schéma des valeurs et des métadonnées. |
| **`indpdntVarbl`** | Champ « independent variable » du résultat de règle, testé par la collection Newman ; sa signification métier dépend de la règle. |
| **Score / `result`** | Valeur calculée pour une règle ou typologie. Dans les cas documentés : NALT 200, ALRT 600. Ce n'est pas une probabilité de fraude. |
| **Rule weighting / pondération** | Contribution paramétrée des règles au résultat de typologie. La collection vérifie leur total. |
| **`alertThreshold`** | Seuil de déclenchement d'alerte dans le profil : 300 pour la typologie de démonstration vérifiée. |
| **`interdictionThreshold`** | Seuil paramétré d'interdiction, observé à 500 dans le profil testé. **Son franchissement ne prouve pas qu'un paiement a été effectivement bloqué.** |
| **`review` / review flag** | Indicateur de revue dans le résultat d'évaluation ; `false` dans le scénario NALT validé. |
| **NALT** | Code de statut retourné par Tazama pour le cas sans alerte dans ce profil ; l'adaptateur OSEF applique **NO_PUBLISH**. |
| **ALRT** | Code de statut d'alerte produit par Tazama pour le scénario synthétique positif ; reste un **signal de risque**, non une fraude prouvée. |
| **`tadpResult`** | Objet de résultat présent dans le rapport Admin Tazama du profil ; ses typologies et règles ont été inspectées lors des tests. L'expansion exacte du sigle **TADP** n'est pas établie ici. |
| **`typologyResult`** | Ensemble des résultats de typologies contenus dans `tadpResult`. |
| **`data.report`** | Objet de rapport exposé par l'API Admin et utilisé par le classificateur OSEF. |
| **`getreportbymsgid`** | Endpoint GET de l'API Admin qui cherche un rapport par son identifiant de message. |
| **Asynchronisme** | Traitement dans lequel la réponse d'acceptation d'un message arrive avant la disponibilité de son rapport final. L'observation de HTTP 204 puis HTTP 200 est compatible avec ce phénomène. |
| **HTTP 204 avant rapport** | Réponse sans contenu, rencontrée lors d'un GET Admin immédiatement après soumission ; ne pas interpréter comme un rapport NALT ni appeler `response.json()` sur un corps vide. |
| **Polling / attente bornée** | Interroger périodiquement une ressource jusqu'à succès ou limite de temps/nombre de tentatives ; la PR #77 applique au plus 30 lectures espacées de deux secondes, sans répéter les POST de transaction. |

## 4. FRAUD-001, adaptateur OSEF et politique de partage

| Terme | Définition et rôle |
|---|---|
| **OSEF** | Open Source Enterprise Factory, équipe et démarche de construction de services/labs open source. |
| **FRAUD-001** | Laboratoire de relais de signaux antifraude entre PSP simulés ; ne détecte pas lui-même la fraude transactionnelle. |
| **FRAUD-002** | Laboratoire d'évaluation Tazama et d'adaptation contrôlée d'un résultat de détection vers FRAUD-001. |
| **Relay / relais** | Service intermédiaire qui stocke les signaux, impose des autorisations et permet leur consultation par le destinataire. Port 8090 dans le lab. |
| **Inbox** | « Boîte de réception » du PSP B, endpoint `GET /inbox` ; seuls les signaux encore éligibles/actifs sont présentés. |
| **Adapter / adaptateur** | Composant traduisant le rapport Tazama vérifié vers le contrat JSON minimal de FRAUD-001. |
| **Mapping / mappage** | Correspondance explicite entre champs, statuts et catégories de deux systèmes ; **ne pas déduire la sévérité du score sans politique approuvée**. |
| **Transformation minimale / minimisation** | Conserver seulement les cinq champs autorisés par FRAUD-001 pour la transmission, sans rapport brut ni données personnelles. |
| **`transaction_token`** | Jeton opaque identifiant un signal de laboratoire, avec préfixe `demo-` ; ce n'est pas le `MsgId` original en clair. |
| **Jeton opaque** | Identifiant dont la valeur ne révèle pas directement les données sous-jacentes. |
| **HMAC** | Hash-based Message Authentication Code, code d'authentification calculé à partir d'une clé secrète et d'un message ; ici sert à dériver un jeton stable. |
| **SHA-256 / HMAC-SHA256** | Fonction de hachage cryptographique / construction HMAC utilisant SHA-256. |
| **Séparation de domaine** | Inclusion d'un contexte distinct dans les données signées/hachées pour éviter de réutiliser implicitement une même clé à des fins différentes. |
| **`OSEF_FRAUD002_LAB_TOKEN_KEY`** | Variable d'environnement contenant la clé HMAC dédiée au jeton OSEF ; ne jamais afficher, publier ni committer. |
| **`LAB_USER_KEY`** | Clé de laboratoire autorisant l'appel aux interfaces PSP A/PSP B ; stockée localement dans le `.env` de FRAUD-001. |
| **`PSP_A_KEY` / `PSP_B_KEY`** | Clés de service distinctes utilisées pour l'accès au relais selon le rôle de chaque PSP. |
| **`ADMIN_KEY`** | Clé d'administration distincte permettant de lire le journal d'audit du relais. |
| **`X-Lab-Key` / `X-API-Key`** | Noms d'en-têtes HTTP utilisés pour transmettre les clés de laboratoire ou de service. |
| **`category`** | Catégorie de signal autorisée, par exemple `suspicious-transfer`. |
| **`severity`** | Gravité assignée (`low`, `medium`, `high`) selon une politique de laboratoire, et non automatiquement depuis le score Tazama. |
| **`recipient`** | Destinataire autorisé du signal ; ici `psp-b`. |
| **`expires_in_hours`** | Durée de validité du signal exprimée en heures ; valeur utilisée : 1. |
| **`approved_for_lab`** | Paramètre booléen de politique qui autorise techniquement le cas de laboratoire ; ne remplace pas une approbation organisationnelle indépendante. |
| **`approval_reference`** | Référence documentaire de la politique approuvée (dans le lab : `OSEF-D06-LAB-20261119`). |
| **Allowlist / liste d'autorisation** | Liste fermée de valeurs, statuts ou destinataires permis ; le reste est refusé. |
| **Opt-in / activation explicite** | Action volontaire requise pour autoriser l'envoi, avec option `--send-synthetic-lab`. Par défaut, aucun POST. |
| **Dry-run / simulation à blanc** | Exécution qui vérifie et classe sans publier de signal ni réaliser d'effet métier. |
| **Preview / prévisualisation** | Mode affichant seulement une décision minimale avant l'envoi ; n'expose pas le rapport brut. |
| **Lecture seule / read-only** | Opération GET ou traitement local sans écriture ; les lecteurs D02/E05 consultent le rapport Admin. |
| **Fail-closed** | Principe de refus par défaut lorsque l'état est absent, non autorisé, inattendu ou invalide. |
| **`NO_PUBLISH`** | Décision interne de non-publication, notamment pour le statut `NALT`. |
| **`NO_SEND`** | Décision de ne pas soumettre un signal, notamment lorsqu'une clé manque ou qu'un contrôle échoue. |
| **`REVIEW_ONLY`** | Décision d'analyse positive nécessitant une revue ou autorisation complémentaire, sans envoi automatique. |
| **`ALRT_CANDIDATE`** | Motif associé à un rapport ALRT qualifié en candidat à revue. |
| **`PREVIEW_ONLY`** | Décision E05 signifiant que le rapport a passé la qualification sans activation de la transmission. |
| **`SEND_NOT_ENABLED`** | Motif indiquant que l'option volontaire d'envoi n'a pas été fournie. |
| **`SENT_AND_RECEIVED`** | Décision indiquant, selon les contrôles de l'adaptateur, qu'un signal a été soumis et retrouvé dans PSP B. |
| **`PSP_B_CONFIRMED`** | Motif de confirmation de la réception côté PSP B. |
| **`DUPLICATE` / `PSP_A_409`** | Résultat de tentative de réémission d'un jeton déjà enregistré ; le serveur le refuse par HTTP 409. |
| **Idempotence** | Propriété garantissant qu'une répétition de la même opération logique ne crée pas plusieurs effets ; ici, le jeton stable et le HTTP 409 limitent les doublons. |
| **TTL — Time To Live** | Durée pendant laquelle un signal reste valable ; après expiration il n'est plus présenté dans l'inbox. |
| **Purge physique** | Suppression réelle des lignes expirées dans SQLite ; **distincte du simple filtrage à la lecture**. |
| **Audit / journal d'audit** | Trace d'opérations (`create`, `read`, refus, etc.) avec acteur, date et résultat, sans secrets. |
| **Traçabilité / corrélation** | Capacité à relier une action à une entrée et à une preuve ; nécessite un identifiant cohérent sans exposer de données privées. |
| **Reprise manuelle** | Réessai effectué après remise en route du relais ; **ne prouve pas** un mécanisme automatique de haute disponibilité. |

## 5. HTTP, API, données et interfaces

| Terme | Définition et rôle |
|---|---|
| **API — Application Programming Interface** | Interface définissant comment deux applications échangent des requêtes et réponses. |
| **REST** | Style d'architecture d'API utilisant notamment les ressources et méthodes HTTP ; les services du lab ont des endpoints HTTP. |
| **HTTP / HTTPS** | Protocole d'échange web / variante protégée par TLS ; le lab utilise HTTP sur interfaces de test isolées. |
| **Endpoint / route** | Adresse d'une opération API, par exemple `/submit`, `/signals`, `/inbox`, `/audit`, `/health`. |
| **GET** | Méthode HTTP utilisée pour consulter un rapport, des signaux ou l'état d'un service. |
| **POST** | Méthode HTTP utilisée ici pour soumettre un message Tazama ou créer un signal. |
| **JSON — JavaScript Object Notation** | Format d'échange structuré utilisé pour requêtes, rapports et politiques. |
| **Corps (body)** | Données transportées dans une requête ou réponse HTTP. |
| **Header / en-tête** | Métadonnées HTTP, dont les clés de laboratoire. |
| **HTTP 200 OK** | Opération réussie ; peut signifier lecture ou acceptation selon endpoint. |
| **HTTP 201 Created** | Création du signal acceptée par le relais / PSP A dans FRAUD-001. |
| **HTTP 204 No Content** | Opération sans corps de réponse ; observée lorsque le rapport Admin n'était pas encore disponible. |
| **HTTP 401 Unauthorized** | Accès non authentifié ou identifiants insuffisants dans le lab. |
| **HTTP 409 Conflict** | Conflit ; employé pour refuser un jeton de signal déjà existant. |
| **HTTP 422 Unprocessable Content** | Requête correctement formée HTTP mais rejetée pour des données métier/schéma invalides. |
| **HTTP 503 Service Unavailable** | Service ou dépendance indisponible ; observé lors de l'arrêt contrôlé du relais. |
| **Timeout** | Temps maximal autorisé pour obtenir une réponse avant d'abandonner l'appel. |
| **Retry / nouvelle tentative** | Répétition d'une lecture ou soumission selon une politique maîtrisée ; le polling ne réémet pas la transaction. |
| **AuthN / authentification** | Vérification de l'identité ou d'une clé d'accès. |
| **AuthZ / autorisation** | Décision déterminant si une identité peut faire une action donnée ; PSP A ne peut pas consulter les signaux de PSP B. |
| **TLS / mTLS** | Chiffrement du transport / authentification mutuelle par certificats ; non démontrés pour les échanges interservices du lab. |
| **OAuth 2.0 / OIDC** | Cadre d'autorisation / couche d'identité fédérée ; mentionnés comme évolutions possibles, non mis en œuvre dans FRAUD-001. |
| **Keycloak** | Solution d'identité et d'accès open source, optionnelle selon le profil Tazama ; non nécessaire au scénario FRAUD-001 minimal. |
| **OWASP API Security Top 10** | Référentiel de risques de sécurité des API, pertinent pour revue de conception, sans valoir audit réalisé. |
| **Donnée personnelle / sensible** | Information permettant d'identifier une personne ou révélant des données protégées ; le signal du lab en exclut les comptes, montants et références clients. |
| **Redaction / expurgation** | Retrait ou masquage des secrets et informations sensibles avant publication de preuves. |

## 6. Cloud, infrastructure, systèmes et réseau

| Terme | Définition et rôle |
|---|---|
| **VM — Virtual Machine** | Machine virtuelle ; la VM du lab s'appelle `osef-fraud-01`. |
| **VirtualBox** | Hyperviseur local utilisé sur l'ordinateur hôte Windows pour exécuter Ubuntu. |
| **Ubuntu / Linux** | Système d'exploitation du laboratoire. |
| **Windows host** | Ordinateur physique hébergeant VirtualBox et la VM. |
| **WSL2** | Windows Subsystem for Linux 2, environnement Linux sur Windows ; option générique de laboratoire, distincte de la VM VirtualBox utilisée. |
| **vCPU** | Processeur virtuel attribué à une machine virtuelle. |
| **RAM** | Mémoire vive ; les services Tazama ont besoin d'un dimensionnement compatible. |
| **SSD / VDI** | Disque à mémoire flash / Virtual Disk Image, format de disque virtuel VirtualBox. |
| **Partition / système de fichiers** | Découpage du disque / organisation logique des données ; l'extension du VDI ne garantit pas celle de la partition Ubuntu. |
| **Snapshot** | Instantané d'une VM pour retour en arrière ; ne remplace pas automatiquement une sauvegarde complète. |
| **Sauvegarde / backup** | Copie permettant de restaurer configuration et données, notamment SQLite et secrets `.env`. |
| **Docker Engine** | Moteur exécutant les conteneurs. |
| **Conteneur / image Docker** | Instance isolée d'une application / artefact servant à créer une telle instance. |
| **Docker Compose** | Outil décrivant et lançant plusieurs conteneurs à partir de fichiers YAML. |
| **Overlay Compose** | Fichier de configuration additionnel appliqué au Compose de base ; le lab l'utilise pour limiter les ports exposés. |
| **YAML** | Format de configuration textuel utilisé par Docker Compose. |
| **Docker Hub / GHCR** | Registres d'images : Docker Hub et GitHub Container Registry. |
| **Healthcheck** | Test automatique d'état d'un conteneur ; son succès ne garantit pas la réussite des opérations métier. |
| **Liveness / readiness** | « Vivant » / « prêt à traiter » ; deux propriétés distinctes d'un service. |
| **Healthy / unhealthy** | États Docker dérivés du healthcheck. Un `unhealthy` peut être dû à une commande de test cassée alors que le processus répond. |
| **Distroless** | Image de conteneur réduite sans outils classiques ni parfois `/bin/sh` ; un healthcheck `CMD-SHELL` peut alors échouer. |
| **Batch PPA healthcheck fix** | Correction OSEF remplaçant un contrôle incompatible avec l'image Batch PPA par une sonde HTTP, ensuite observée `healthy`. |
| **Loopback / localhost / `127.0.0.1`** | Interface réseau locale d'une machine ; utilisée pour limiter la portée des API Tazama et FRAUD-001. |
| **Host-only VirtualBox** | Réseau privé entre l'hôte et les VM ; l'adresse de lab utilisée est `192.168.255.10`. |
| **NAT — Network Address Translation** | Mode réseau permettant à la VM d'utiliser une traduction d'adresses, sans exposition directe de tous ses services. |
| **Port TCP** | Numéro identifiant un service réseau ; ports principaux : relay 8090, PSP A 8091, PSP B 8092, TMS 5000, Admin 5100, Demo 3011. |
| **Bind / publication de port** | Association d'un service à une adresse IP et un port d'écoute ; `127.0.0.1` et `192.168.255.10` ne sont pas équivalents en surface d'accès. |
| **Firewall / pare-feu** | Filtrage réseau limitant les flux autorisés entre réseaux et services. |
| **SSH / tunnel SSH** | Accès distant sécurisé / redirection protégée de ports, utilisé pour consulter les interfaces de la VM depuis Windows. |
| **Prometheus / Grafana** | Outils de métriques et visualisation cités comme extensions possibles ; non nécessaires à la preuve fonctionnelle du lab. |
| **SRE — Site Reliability Engineering** | Discipline d'ingénierie de la fiabilité opérationnelle, utile pour la revue, les métriques et les scénarios de panne. |
| **HA / haute disponibilité** | Architecture permettant de maintenir le service malgré des défaillances ; un simple arrêt/redémarrage manuel du relais ne la prouve pas. |
| **Failover / basculement** | Transfert d'activité vers un autre composant lors d'une panne ; non démontré dans FRAUD-001. |
| **SLA — Service Level Agreement** | Engagement de niveau de service entre fournisseur et client ; aucun SLA de production n'est établi par le laboratoire. |

## 7. Tests, qualité, sécurité et GitHub

| Terme | Définition et rôle |
|---|---|
| **Lab / sandbox** | Environnement contrôlé d'apprentissage/expérimentation isolé des clients. |
| **MVP — Minimum Viable Product** | Première version réduite permettant de valider une proposition de valeur ; FRAUD-001 constitue la base minimale du partage. |
| **Gate / jalon** | Critère d'acceptation à passer avant d'avancer. FRAUD-002 comporte les étapes A à E et les sous-étapes D01–D06, E01–E05. |
| **D01–D06** | Série d'étapes allant du classificateur hors réseau à la prévisualisation, puis à l'émission contrôlée d'un signal. |
| **E01–E05** | Scénarios de contrôle : doublons/audit, panne, accès/TTL, non-régression, raccordement/revue finale. |
| **T01–T10** | Tests FRAUD-001 : création, doublon, clés, lecture, schéma, audit, expiration, panne/reprise et séparation des rôles. |
| **T11** | Scénario additionnel de purge physique des signaux expirés, distinct de T08. |
| **Fixture** | Fichier de données synthétiques figé servant à reproduire un test. |
| **Test unitaire** | Test ciblé sur une fonction isolée, généralement sans réseau ; 83 tests Python ont réussi dans la version examinée. |
| **Test d'intégration / E2E** | Vérification de la coopération de composants ou de bout en bout ; le lab a démontré Tazama → adaptateur → PSP A → relais → PSP B. |
| **Test de non-régression** | Rejeu de contrôles existants pour vérifier qu'un changement n'a pas cassé une fonctionnalité. |
| **Test négatif** | Test vérifiant le refus d'un cas invalide : mauvaise clé, doublon, rapport NALT, ID incohérent. |
| **Test de charge** | Mesure du comportement sous trafic élevé ; non réalisée par la simple réussite des 83 tests. |
| **Chaos / panne contrôlée** | Interruption volontaire et encadrée d'un composant, ici le relais, pour observer les erreurs et la reprise. |
| **Postman** | Environnement de conception et d'exécution de requêtes API et de collections de tests. |
| **Newman** | Exécuteur en ligne de commande de collections Postman ; la collection officielle Tazama 2.1 a réussi 39 assertions cumulées en deux phases. |
| **Collection Postman** | Fichier de requêtes, scripts et assertions organisés ; l'upstream Tazama est conservé inchangé par OSEF. |
| **Newman globals** | Variables partagées entre requêtes d'une collection ; la correction #77 exporte temporairement le `pacs.002 MsgId` pour le contrôle du rapport. |
| **Assertion** | Condition testée automatiquement ; 13 + 26 assertions Newman réussies dans les deux dossiers du test. |
| **`JSONError`** | Erreur de traitement JSON ; observée lorsque le script Newman appelait `pm.response.json()` après HTTP 204 sans contenu. |
| **Python `unittest`** | Cadre de tests standard Python ; a exécuté les 83 tests de FRAUD-002. |
| **Bash / script shell** | Langage de commandes servant à automatiser diagnostics et tests sur Ubuntu. |
| **curl** | Outil CLI de requêtes HTTP pour les contrôles d'état et d'API. |
| **CLI — Command Line Interface** | Interface de commandes textuelles dans le terminal. |
| **FastAPI** | Cadre Python servant à exposer les API FRAUD-001. |
| **Pydantic** | Bibliothèque Python de validation des structures et types de données. |
| **HTTPX** | Client HTTP Python mentionné dans l'architecture initiale ; les lecteurs Tazama effectivement versionnés peuvent utiliser `urllib.request`, et non obligatoirement HTTPX. |
| **`urllib.request`** | Bibliothèque standard Python utilisée dans le lecteur sécurisé Tazama pour les GET en loopback. |
| **SQLite** | Base relationnelle embarquée utilisée pour stocker les signaux et le journal FRAUD-001. |
| **Git** | Système de contrôle de version permettant de retracer les changements du code et des documents. |
| **GitHub** | Plateforme hébergeant le dépôt, les issues, les branches et les PR OSEF. |
| **Repository / dépôt** | Espace Git versionné contenant code, tests et documentation. |
| **Branch / branche** | Ligne de développement isolée ; toute modification OSEF est d'abord préparée sur une branche. |
| **Commit / SHA** | Enregistrement d'une modification / empreinte identifiant une version Git ; important pour reproduire les résultats. |
| **Pull Request / PR** | Demande de revue avant l'intégration de modifications dans `main`. |
| **Merge / fusion** | Intégration de changements approuvés dans la branche principale. |
| **`git pull --ff-only`** | Synchronisation Git n'acceptant qu'une avance rapide, afin d'éviter des fusions implicites. |
| **Upstream** | Projet source maintenu par la communauté officielle, par opposition aux adaptations OSEF. |
| **Fork** | Copie GitHub d'un dépôt permettant de préparer des contributions sans modifier directement l'upstream. |
| **Issue** | Ticket GitHub décrivant un travail, une anomalie ou une recette ; FRAUD-002 utilise l'issue #50. |
| **Checklist / case à cocher** | Critère dont la validation doit reposer sur une preuve ; une case décochée ne signifie pas automatiquement un test échoué. |
| **PV — procès-verbal de recette** | Document de synthèse des vérifications, réserves, signatures/approbations et décision de clôture. |
| **Revue indépendante** | Évaluation par un second ingénieur non auteur principal, couvrant architecture, risques, code, données et résultats. |
| **Preuve expurgée** | Extrait terminal/capture dont les secrets et informations identifiantes ont été retirés. |
| **Version pinning / version figée** | Fixation explicite d'une version de code, d'image et de dépendances pour permettre la reproductibilité. |
| **Licence open source** | Conditions juridiques de modification, redistribution et utilisation d'un logiciel ; doit être vérifiée par composant et image, distinctement de sa simple disponibilité. |
| **Production readiness** | Aptitude démontrée à exploiter un système de manière sûre et durable ; **non obtenue par les tests de ce laboratoire**. |

## 8. Correspondance rapide des commandes et codes observés

| Expression | Signification |
|---|---|
| `bash scripts/test-lab.sh` | Exécute le périmètre minimum des tests FRAUD-001. |
| `bash scripts/test-lab.sh --extended` | Exécute T01–T10, dont la panne contrôlée du relais et l'expiration. |
| `python3 -m unittest discover ...` | Lance les tests unitaires Python de FRAUD-002. |
| `bash labs/FRAUD-002/scripts/test-tazama-e2e.sh` | Lance la collection officielle Newman via le script OSEF sécurisé. |
| `tazama-read-only-dry-run.py` | Lit le rapport Tazama et renvoie une décision sans publication. |
| `tazama-direct-lab-submit.py` | Lit et qualifie un rapport Tazama en mémoire ; `--send-synthetic-lab` active un envoi explicite en lab. |
| `wait-tazama-newman-report.py` | Vérifie la disponibilité du rapport après les POST Newman, en réessayant seulement HTTP 204. |
| `docker compose ps` | Liste l'état des conteneurs du projet Compose actif. |
| `docker compose stop relay` / `start relay` | Arrête / redémarre le relais pour le scénario de panne. |
| `curl -fsS ... /health` | Teste un endpoint de santé en lecture seule. |
| `.env` | Fichier local de variables/clé de configuration ; **ne jamais le committer**. |

## 9. Erreurs d'interprétation à éviter

1. **ALRT ≠ fraude prouvée** et **score supérieur à interdictionThreshold ≠ paiement effectivement bloqué**.
2. **NALT ≠ erreur HTTP** ; c'est un statut de rapport métier. **HTTP 204 ≠ NALT** ; c'est l'absence de corps de réponse à cet instant.
3. **200 pour un POST ISO 20022 ≠ rapport Admin immédiatement disponible** : le traitement peut se poursuivre après acceptation.
4. **Healthy ≠ prêt, sécurisé, conforme ou testé de bout en bout** ; un healthcheck valide n'est pas un test métier.
5. **TTL dépassé et absence dans l'inbox ≠ purge des données SQLite** ; la purge exige sa propre preuve.
6. **503 suivi de 200 après redémarrage manuel ≠ basculement automatique ni haute disponibilité**.
7. **39 assertions Newman + 83 tests Python + T01–T10 réussis ≠ validation pour une institution financière en production**.
8. **Une case GitHub cochée ≠ vérification indépendante effectuée** ; les liens et journaux doivent permettre la revue.

## 10. Sources de référence

### Dépôt et documentation OSEF
- [Issue de suivi FRAUD-002 #50](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/50)
- [FRAUD-001 — README et scénarios](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/blob/main/labs/FRAUD-001/README.md)
- [FRAUD-002 — README](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/blob/main/labs/FRAUD-002/README.md)
- [13 services Tazama](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/blob/main/labs/FRAUD-002/docs/ARCHITECTURE-13-SERVICES-TAZAMA.md)
- [Contrat de mapping](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/blob/main/labs/FRAUD-002/docs/GATE-D-CONTRAT-TAZAMA-FRAUD-001.md)
- [Gate E05 direct Tazama](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/blob/main/labs/FRAUD-002/docs/GATE-E05-Tazama-DIRECT.md)
- [Gate E04 Newman/HTTP 204](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/blob/main/labs/FRAUD-002/docs/GATE-E04-NEWMAN-204-READINESS.md)
- [PR #76](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/pull/76) · [PR #77](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/pull/77)

### Sources officielles externes
- [Tazama Core — README des services](https://github.com/tazama-lf/tazama-stack/blob/83e4b12c16986aedfff843ed84b7045ac912ec0a/core/README.md)
- [Tazama — collection Postman/Newman](https://github.com/tazama-lf/postman)
- [ISO 20022 — catalogue officiel](https://www.iso20022.org/iso-20022-message-definitions)
- [FastAPI](https://fastapi.tiangolo.com/) · [Docker Compose](https://docs.docker.com/compose/) · [Git](https://git-scm.com/docs) · [Newman](https://learning.postman.com/docs/collections/using-newman-cli/newman-options)
- [Open Source Initiative — définition open source](https://opensource.org/osd)

**Note de traçabilité :** les résultats de tests repris ici proviennent des comptes rendus de terminal fournis lors de la recette et rattachés aux PR OSEF. Le glossaire définit les termes ; il ne remplace pas le PV de recette et ne certifie pas la qualité des logiciels upstream.