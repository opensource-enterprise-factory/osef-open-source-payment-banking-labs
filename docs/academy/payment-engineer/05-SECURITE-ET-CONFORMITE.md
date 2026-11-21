# 05 — Sécurité, confidentialité et conformité : règles de travail

## Cadre non négociable pour les labs

- **Aucun moyen de paiement réel** : pas de carte réelle, PAN, CVV, PIN, compte client, identité KYC, secret bancaire ou paiement de production.
- **Isolement** : VM/réseau de lab, données synthétiques, ports et services minimisés. Pas d'accès à des réseaux de production.
- **Secrets** : injection hors du dépôt, rotation et suppression après test ; refuser les vrais secrets dans les issues, captures et logs.
- **Données** : chiffrement et accès proportionnés au contexte, conservation limitée, pas de PII dans les preuves partagées.
- **Dépendances** : inventorier composants, licences et vulnérabilités vérifiées, avec dates et versions exactes.
- **Accès** : moindre privilège, contrôles API/roles, journalisation des actions administratives.
- **Tests actifs** : sécurité offensive ou charge uniquement sur un environnement contrôlé et autorisé.

## Sources et couches à ne pas confondre

| Sujet | Nature | Ce qu'un lab peut prouver | Ce qu'il ne prouve pas |
|---|---|---|---|
| ISO 8583 / ISO 20022 | Standards de messages | Encodage/décodage et tests de contrat sur exemples | Conformité exhaustive à toutes les éditions/profils |
| EMV | Spécifications/certification | Compréhension TLV et simulation sans données de carte | Certification EMV |
| PCI DSS | Standard de sécurité | Contrôles pédagogiques et inventaire d'écarts | Attestation PCI DSS |
| BCEAO/UEMOA/PI-SPI | Cadre institutionnel / rails | Cas d'usage contextualisés | Homologation ou raccordement réel |
| FAPI/OAuth/OIDC | Standards/profils de sécurité API | Tests de comportement d'un montage donné | Certification formelle automatique |
| Code open source | Licence et projet précis | Évaluation du code et de ses dépendances | Autorisation implicite de toutes les utilisations commerciales |

## Démarche de vérification réglementaire

1. Identifier pays, type d'établissement, service et date de référence.
2. Retrouver le texte officiel exact et son champ d'application.
3. Citer la publication, modification et date d'effet lorsque disponibles.
4. Tenir séparément la **preuve technique** du lab, l'avis juridique/compliance et la décision de l'autorité.
5. Consigner les textes non accessibles/versions non confirmées comme **points ouverts**.

Ne pas inventer d'exigences BCEAO, de CVE ou de licence ; le rôle du responsable conformité est de vérifier les obligations applicables à chaque cas.

## Références officielles

[BCEAO](https://www.bceao.int/) · [PCI Security Standards Council](https://www.pcisecuritystandards.org/) · [EMVCo](https://www.emvco.com/) · [ISO 20022](https://www.iso20022.org/) · [OpenID Foundation](https://openid.net/) · [OSI](https://opensource.org/licenses).
