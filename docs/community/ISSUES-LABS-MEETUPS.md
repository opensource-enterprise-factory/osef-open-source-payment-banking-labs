# OSEF — Comment distinguer les Labs et les Meetups dans GitHub Issues

**Mise à jour : 17 novembre 2026** · Classification des issues en `type:lab` et `type:meetup`.

## Accès direct

- **[🧪 Tous les labs](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues?q=is%3Aissue+label%3A%22type%3Alab%22)** — filtre GitHub `is:issue label:"type:lab"`
- **[🎤 Tous les meetups](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues?q=is%3Aissue+label%3A%22type%3Ameetup%22)** — filtre GitHub `is:issue label:"type:meetup"`
- **[Proposer une nouvelle issue](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/new/choose)** — choisir le template « Lab » ou « Meetup ».

**Situation initiale vérifiée :** les 41 premières issues du dépôt (#1 à #41) décrivent des labs ou sujets de labs ; elles ont reçu le label `type:lab`. L'issue [#42](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/42), avec `type:meetup`, propose un premier partage ISO 8583 **sans date ni intervenant confirmés**.

**Attention :** l'index de recherche GitHub peut afficher les nouvelles issues et les nouveaux labels après un délai ; vérifier directement [#42](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/42) si le filtre Meetups semble vide.

## Comprendre les catégories

| Aspect | Lab | Meetup |
|---|---|---|
| Label | `type:lab` | `type:meetup` |
| Titre des nouvelles issues | `[LAB] …` | `[MEETUP] …` |
| But | Construire, tester, produire des preuves | Partager, expliquer, débattre, faire une démonstration |
| Rattachement | Cours TC / MON / PNI et exigences ARC-BDAT | Cours, architecture, lab/issue à présenter |
| Livrables | Code, contrats, diagrammes, logs expurgés, tests, PR | Chronogramme, supports autorisés, compte rendu et prochaines contributions |
| Statut | Proposé → Documenté → Construit → Testé → Revu → Validé en lab | Proposé → Préparé → Programmé → Réalisé |

Le **label** est le critère de filtrage principal. Les identifiants OPB restent stables pour préserver les liens existants : il n'est pas nécessaire de renommer toutes les anciennes issues. Les nouveaux templates insèrent les labels adéquats automatiquement.

## Règle Lab ↔ Meetup

- Un lab peut inspirer plusieurs meetups, sans garantir qu'un événement aura lieu.
- Un meetup peut référencer plusieurs labs et cours ; il doit citer leurs numéros d'issues.
- Une démonstration ne peut être annoncée comme fonctionnelle qu'après test réel et preuve conservée.
- Une issue meetup « proposée » n'est pas un événement confirmé ; dates, intervenants et inscriptions restent à valider.
- Lors de la réalisation d'un meetup, mettre à jour son issue avec les supports autorisés, les décisions et les issues labs ouvertes.

**Exemple :** [Lab #41 — ISO 8583 fictif](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/41) ↔ [Meetup proposé #42 — ISO 8583](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/42).

## Risque de doublons du catalogue OPB

**Des IDs pédagogiques identiques apparaissent dans plusieurs issues GitHub :** par exemple **OPB-020 = #28 et #40**, et **OPB-009 = #9 et #29**. Les numéros d'issue GitHub ne sont **pas** égaux aux numéros d'ID OPB.

**Règles provisoires de dédoublonnage :**
1. **Ne supprimer ni fermer automatiquement aucune issue** avant revue de son contenu, commentaires, responsable, avancement et dépendances.
2. Rechercher `OPB-XXX` dans les titres, identifier les entrées portant le même ID et comparer leurs descriptions et preuves.
3. Décider une issue canonique **par ID**, après avoir identifié l'éventuel travail utile de chaque doublon.
4. Si une duplication est confirmée, ajouter un commentaire avec référence croisée ; la fermeture éventuelle doit être motivée et documentée.
5. Mettre ensuite à jour les liens de [labs/README.md](../../labs/README.md) et des parcours Academy vers les **bons numéros GitHub**.

**Important :** le catalogue historique contient des liens d'issues parfois déduits mécaniquement de l'ID ; ne pas supposer que `OPB-009` renvoie à `#9` sans vérifier le titre de l'issue. La distinction entre sujet, issue ouverte, lab construit et lab testé doit rester explicite.

## Contribution

- [Template Lab](../../.github/ISSUE_TEMPLATE/lab.md)
- [Template Meetup](../../.github/ISSUE_TEMPLATE/meetup.md)
- [Catalogue des cours](../../docs/academy/CATALOGUE-COURS-DETAILLES.md)
- [Matrice compétences / BDAT / labs](../../docs/academy/MATRICE-COMPETENCES-BDAT-LABS.md)
- [Sécurité](../../SECURITY.md)

**English summary:** Separate OSEF GitHub issues with `type:lab` and `type:meetup`. Preserve existing OPB IDs, link related lab and meetup issues, and review duplicate issue numbers before closing anything.
