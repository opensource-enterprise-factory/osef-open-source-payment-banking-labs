# OSEF — Positionnement stratégique Payment & Banking Open Source

**Proposition de stratégie — 16 novembre 2026.** Document prospectif : aucune traction commerciale, homologation réglementaire ou partenariat n'est présumé.

**Feuille de route détaillée :** [Vision et plan 2027–2029](OSEF-PAYMENT-ENGINEERING-ROADMAP-2027-2029.md).

## Positionnement recommandé
**OSEF = fabrique communautaire et partenaire d'ingénierie Open Source pour les systèmes bancaires, monétiques et de paiement.** OSEF aide des prestataires de services financiers, ESN et équipes techniques à étudier, intégrer, tester, fiabiliser et maintenir des composants ouverts, sans se présenter comme opérateur de paiement ou établissement agréé.

## Valeur pour l'écosystème
1. Compétences locales mesurables : labs reproductibles et mainteneurs/contributeurs formés.
2. Moins de dépendance à un seul fournisseur grâce à la compréhension des interfaces, au code inspectable et aux stratégies de sortie.
3. Réduction des risques techniques : tests de contrat, interopérabilité, charge, sécurité, reprise et observabilité.
4. Production de biens communs réutilisables : simulateurs fictifs, documentation FR/EN, outils de tests, contributions upstream.
5. Meilleure capacité de dialogue entre banques, fintechs, SFD, EME, ESN et communautés amont.

Ces impacts sont des objectifs; ils devront être mesurés et ne sont pas encore démontrés par OSEF.

## Frontière entre biens communs et prestations

| Ouvert / communautaire | Prestations commerciales possibles |
|---|---|
| Catalogues sourcés et documentation générique | Cartographies SI et diagnostics d'intégration contractuels |
| Simulateurs ISO 8583 et données fictives | Adaptateurs, déploiements et intégrations autorisés pour un client |
| Tests génériques et configurations de lab | Tests de conformité de protocole, performance et fiabilité dans le périmètre contractuel |
| Guides d'exploitation et contribution upstream | Support/SRE, maintenance corrective, formation dédiée, transfert de compétences |
| Bibliothèques et correctifs publiables selon licences | Formation d'équipes monétiques et accompagnement des ESN |

**La valeur facturable est le travail d'intégration, de garantie de service contractuelle et d'expertise, non l'exclusivité sur un code ouvert.** Contrats et livrables doivent respecter les licences amont (notamment AGPL) et prévoir la confidentialité client, le partage des améliorations et la politique de publication.

## Offres pilotes proposées (non commercialisées)
- **Payment OSS Discovery** — diagnostic d'architecture, gouvernance, licences, dépendances et risques, sur périmètre convenu.
- **Payment Interoperability Lab** — banc de tests ISO 8583 ou API avec données synthétiques et rapports de compatibilité, sans connexion live.
- **Payment Platform Reliability** — observabilité, résilience, tests de reprise et runbooks d'une plateforme client autorisée.
- **Payment OSS Enablement** — formation, mentorat, contribution amont et transfert de compétences aux équipes client/ESN.

## Priorités commerciales de départ
- Cible principale : ESN/intégrateurs et fournisseurs technologiques qui ont besoin de compétence de déploiement, de tests ou de support.
- Cibles suivantes : DSI, équipes monétiques, EME, fintechs et SFD, sous réserve de mandats explicites.
- OSEF comme **sous-traitant technique ou partenaire de l'ESN**, pas compétiteur de ses activités commerciales ni intermédiaire dans les flux financiers.
- Modèles de revenus : forfait de diagnostic défini, projet d'intégration au jalon, maintenance/SRE récurrente, formation facturée. Aucun tarif sans données de coûts et validation du marché.

## Éviter
- Exploiter ou détenir les fonds des clients, prétendre participer aux systèmes de paiement sans agrément, revendiquer une conformité PCI DSS/BCEAO sans validation.
- Se présenter comme partenaire officiel de Mojaloop, jPOS, Moov ou FINOS sans accord.
- Exposer des secrets/données bancaires dans les labs.
- Vendre de la dépendance propriétaire ou des promesses de souveraineté sans preuves techniques.
- Supposer qu'une licence Open Source supprime les frais d'exploitation, de support, de sécurité ou de certification.

## Hypothèses à tester auprès de 10 prospects
1. Quelle difficulté de déploiement/intégration coûte le plus d'effort ?
2. Quels formats et systèmes peuvent être reproduits sans données confidentielles ?
3. Quel budget et quel décideur pour un diagnostic ?
4. Un simulateur neutre constituerait-il une valeur ajoutée pour une ESN ?
5. Quelles exigences de sécurité, confidentialité et responsabilité contractuelle ?
6. À quelles conditions un client paierait-il un support d'une brique open source ?

## Indicateurs de 90 jours (cibles proposées)
- 3 labs démontrés et revus, dont 1 ISO 8583;
- 2 contributions amont proposées et documentées, sans présumer de leur acceptation;
- 5 entretiens qualifiés avec ESN/banques/fintechs;
- 1 offre pilote rédigée et chiffrée sur des coûts réels;
- 1 revue juridique et licences sur les solutions retenues.

## Références de contexte
- BCEAO — PI-SPI et paiements instantanés : https://www.bceao.int/
- Mojaloop : https://mojaloop.io/
- Open Source Definition : https://opensource.org/osd
- Moov ISO8583 : https://github.com/moov-io/iso8583
- jPOS : https://github.com/jpos/jPOS

**Avertissement :** la présence d'une technologie ou de PI-SPI dans ce document n'implique aucune connexion, homologation ou partenariat avec ces opérateurs.
