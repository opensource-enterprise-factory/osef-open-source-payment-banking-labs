# FIN-20261124-04 — Registre des projets et standards sous surveillance

**Date :** 24 novembre 2026. **Nature :** registre méthodologique ; les sources listées ne sont pas assimilées à des annonces des dernières 24 heures.

| Sous-domaine | Sources officielles de contrôle | Résultat de l'édition et travaux associés |
|---|---|---|
| Monétique/EMV/PCI | https://www.emvco.com/news/ ; https://www.pcisecuritystandards.org/ | Aucune release normative récente confirmée ; [EMV-TOKEN #108](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/108) |
| ISO 8583/20022 | https://www.iso20022.org/ ; documentation ISO sous droits applicables | Aucune modification normative récente confirmée ; [ISO-MAP #109](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/109) |
| Core banking | https://github.com/apache/fineract/releases ; https://mifos.org/ | Pas de release 24 h authentifiée ; [Fineract #14](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/14) |
| Fraude/AML | https://tazama.org/ ; https://github.com/jube-home/jube/releases ; https://www.linuxfoundation.org/press | OFTA est une annonce antérieure (18/11), pas une nouvelle norme certifiée ; [FRAUD #63](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/63), [KYC-AML #110](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/110) |
| Streaming/sécurité | https://kafka.apache.org/ ; https://flink.apache.org/ ; https://openssf.org/ | Avis de sécurité antérieurs ; aucune exposition OSEF confirmée ; [FRAUD-007 #82](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/82) |
| FINOS/FDC3/CALM | https://www.finos.org/blog ; https://fdc3.finos.org/ | Aucune release 24 h établie ; [CALM #112](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/112) |
| LF Decentralized Trust | https://www.lfdecentralizedtrust.org/ | Annonce projets antérieure ; [LFDT-MAP #113](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/113) |
| Régulateurs UEMOA/CEMAC | https://www.bceao.int/ ; https://www.beac.int/ | Appel LIF BCEAO documenté ; autres mises à jour non systématiquement vérifiées |
| Fintech/investissements | Communications officielles des sociétés et fonds | Aucun lead commercial OSEF, financement nouveau ou partenariat de la journée confirmé |
| Business/consultations | https://www.afdb.org/en/about-us/careers/current-vacancies/consultants ; BCEAO | Appel BAD et LIF à qualifier, voir fiches dédiées |

## Contrôle des licences
Ne pas confondre licence open source reconnue par l'OSI, standard accessible, produit propriétaire et source-available. Pour les composants Marble éventuellement sous ELv2, vérifier précisément l'édition et le texte de licence avant tout modèle SaaS ou service managé. Un simulateur PI-SPI ne donne aucun agrément BCEAO.

## Actions
Chaque nouveau run doit inscrire source réellement consultée, heure UTC si disponible, événement/release/commit et date, résultat, lien, incertitudes, et écart au run précédent. **Une source non consultée ne peut pas recevoir le statut « aucune nouveauté ».**
