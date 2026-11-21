# 12 — Checkpoints du parcours Payment Engineer OSEF

> Modèle de pilotage à utiliser pour chaque ingénieur, sans données RH sensibles dans le dépôt public. Aucun participant ni mentor n'a été désigné automatiquement.

## Légende des états

- `not-started` : pas commencé ;
- `blocked` : dépendance ou erreur documentée ;
- `in-progress` : travaux non encore validés ;
- `evidence-ready` : les preuves d'exécution sont disponibles ;
- `reviewed` : revue technique indépendante effectuée ;
- `qualified-internal` : décision **interne OSEF** documentée, et non certification externe.

## Checkpoints recommandés

| Checkpoint | Références | Preuves de sortie | Relecteur attendu |
|---|---|---|---|
| C0 — Installation | BASE-003 | VM propre, versions et commandes de reconstruction | Pair technique |
| C1 — Protocoles | MON-001 | ISO 8583 fictif valide et invalide documentés | Ingénieur monétique |
| C2 — Core banking | CORE-001/002 | API et comptes fictifs testés | Ingénieur bancaire |
| C3 — Interopérabilité | RAIL-001/002/003 | Scénarios succès/rejet/retry sans double effet métier | Ingénieur switch |
| C4 — Sécurité | SEC-002/003/004 | Accès refusés, analyse de dépendances, absence de secrets | Sécurité / SRE |
| C5 — Intégration | CORE-004/005/006 | Contrats et rapprochement sur ledger fictif | Architecte paiement |
| C6 — Résilience et fraude | SRE-001/002, FRAUD-002/007 | Incident reproduit, alertes, métriques et RETEX | SRE / antifraude |
| C7 — Contribution | BIZ-002 | Lien upstream réel, statut observé et revue | Mentor technique |

## Définition d'une preuve valide

Une vidéo seule ou une capture d'écran ne suffit pas. Fournir commits et versions, instructions, fixtures artificielles, tests automatisés ou commandes de vérification, sorties nettoyées, erreurs observées, conclusions et limites. Une PR acceptée upstream n'est pas obligatoire pour apprendre, mais toute revendication d'acceptation nécessite une source.

## Gestion des blocages

1. Ouvrir une issue ou commentaire précis avec erreur expurgée et étapes de reproduction.
2. Marquer le checkpoint `blocked`, avec la dépendance et le responsable à désigner.
3. Ne pas contourner les contrôles de sécurité pour avancer.
4. Proposer un lab alternatif du même niveau si une dépendance upstream rend le parcours inexécutable.
5. Revoir le niveau de difficulté à partir de faits observés après réalisation.

## Grille de revue

Se reporter à [la grille du pilote L1–L2](../../roadmap/pilot-L1-L2/RUBRIC.md) : 25 points reproductibilité, 25 fonctionnel, 20 fiabilité, 20 sécurité/licences, 10 documentation. Seuil indicatif : 80/100 et zéro défaut critique, avec revue indépendante.

## Modèle d'issue de progression

```markdown
## Mon parcours
Pseudonyme :
Filière :
Checkpoint actuel :
Statut : not-started

## Environnement
Versions / SHA :
Lab / issue :
Données de test : synthétiques uniquement

## Tests et preuves
Commandes :
Résultat réel :
Résultat attendu :
Écarts et risques :
Liens vers les rapports :

## Demande de revue
Question précise :
Relecteur (à confirmer) :
Décision : pending
```
