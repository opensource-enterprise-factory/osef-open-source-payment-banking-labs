# FRAUD-002 — Option B retenue : une seule VM VirtualBox redimensionnée

> **Décision enregistrée le 18 novembre 2026 :** conserver `osef-fraud-01` pour FRAUD-001 et FRAUD-002. **Décision seulement : aucun redimensionnement ni déploiement Tazama encore exécuté.**
>
> **Laboratoire isolé, données fictives uniquement.** Préserver FRAUD-001 : ses tests T01–T10 ont réussi selon le journal transmis par l'ingénieur.

## État initial vérifié / rapporté

- VirtualBox sur laptop Windows 11, VM `osef-fraud-01`, Ubuntu 22.04.5 LTS.
- VM actuelle : **2 vCPU, ~3,8 Gio RAM, 25 Go de partition racine, ~20 Go disponibles, swap 0**.
- Docker Engine 29.10.0 / Compose v5.8.0.
- FRAUD-001 : trois services Docker (PSP A, relay SQLite, PSP B), ports 8090–8092 en loopback et sur l'interface host-only `192.168.255.10`.
- Tazama cloné sur la **même VM** dans `/home/lionel/tazama-stack`, au commit `83e4b12c16986aedfff843ed84b7045ac912ec0a` ; profil Public (DockerHub) : 13 services déclarés.
- **Non vérifiés** : RAM/CPU/disque du PC Windows ; type VDI/VHD/VMDK du disque ; disposition partitions/LVM ; snapshots existants.

## Cible OSEF proposée (à condition que le PC hôte le permette)

| Paramètre | Avant | Cible proposée |
|---|---|---|
| Machines | 1 | **1** |
| vCPU | 2 | **4** (sans dépasser une attribution prudente du CPU hôte) |
| RAM | ~4 Gio | **12 Gio (12 288 Mio)** si Windows dispose d'une réserve suffisante ; sinon revoir la cible |
| Disque virtuel | ~25 Go utiles dans Ubuntu | **80 Go de capacité logique** (avec espace réel suffisant sur l'hôte) |
| Swap Ubuntu | 0 | **4 Gio facultatifs**, après vérification du système ; uniquement marge de secours |
| OS | Ubuntu 22.04.5 LTS | **Conserver l'OS installé** |
| FRAUD-001 et Tazama | FRAUD-001 seul | Deux projets Compose isolés, ports surveillés |

**Aucune preuve officielle qu'une VM 4 vCPU/12 Gio/80 Go soit suffisante pour Tazama**. C'est un point de départ expérimental. Si le laptop n'a que 16 Go de RAM ou pas assez de CPU, **ne pas forcer cette allocation** : mesurer l'hôte et recalibrer avant toute opération.

## 0. Avant d'éteindre : mesurer et protéger

### Sur Windows 11 (PowerShell, sans droits administrateur particuliers)

```powershell
# RAM physique totale et nombre de processeurs logiques de l'hôte.
Get-CimInstance Win32_ComputerSystem |
  Select-Object @{Name='RAM_Go';Expression={[math]::Round($_.TotalPhysicalMemory/1GB,1)}},
                NumberOfLogicalProcessors,NumberOfProcessors

# Stockage libre sur les lecteurs Windows.
Get-PSDrive -PSProvider FileSystem |
  Select-Object Name,@{Name='Libre_Go';Expression={[math]::Round($_.Free/1GB,1)}}

# VirtualBox doit être installé ; répertorier les VMs et leurs disques.
& "$env:ProgramFiles\Oracle\VirtualBox\VBoxManage.exe" list vms
```

**Ne pas se baser uniquement sur le disque C:** si les fichiers VirtualBox résident sur un autre lecteur.

### Dans Ubuntu, depuis `osef-fraud-01`

```bash
# Relever la partition et le système de fichiers AVANT modification :
lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINTS
findmnt -no SOURCE,FSTYPE /
df -h /
sudo pvs 2>/dev/null || true
sudo vgs 2>/dev/null || true
sudo lvs 2>/dev/null || true

# Sauvegarder la sortie de test et vérifier l'état de FRAUD-001 :
cd /home/lionel/osef-open-source-payment-banking-labs/labs/FRAUD-001
docker compose ps
```

**Sauvegarde impérative :**
1. Enregistrer une copie/export de la VM **sur un stockage distinct**, avec assez d'espace et vérifier que l'export peut être lu.
2. Sauvegarder les données persistantes Docker du relais (**volume SQLite**, pas seulement le dossier Git) et le fichier `.env` de manière protégée. Ne pas publier `.env` ou les clés.
3. Conserver la sortie T01–T10 en dehors de la VM si disponible.
4. **Ne pas exécuter** `docker compose down --volumes`, `docker volume prune` ou `docker system prune --volumes`.

### Arrêt propre de la VM

```bash
sudo shutdown -h now
```

Attendre dans VirtualBox l'état **Éteinte / Powered Off**, pas **Sauvegardée / Saved**.

## 1. RAM et vCPU — VirtualBox sur Windows (VM éteinte)

1. Sélectionner `osef-fraud-01` dans VirtualBox.
2. **Configuration → Système → Carte mère / Mémoire** : mettre **12 288 Mio** si le PC hôte peut conserver suffisamment de RAM pour Windows.
3. **Configuration → Système → Processeur** : configurer **4 vCPU** si le PC hôte dispose de ressources suffisantes.
4. Conserver la configuration réseau NAT + Host-only existante, les adresses et le montage du disque ; ne pas changer le contrôleur ou le type de stockage.
5. Valider, **sans redémarrer** si l'agrandissement du disque reste à effectuer.

Source : [manuel officiel VirtualBox](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/working-with-vms.html).

## 2. Disque virtuel : agrandir le média (VM éteinte, après sauvegarde)

**Le type de média n'est pas encore confirmé.** Dans VirtualBox : **Outils → Gestionnaire de médias virtuels** (libellé variable selon version), sélectionner le disque **réellement attaché à `osef-fraud-01`**, relever son format, son emplacement, sa capacité, son mode d'allocation et la présence éventuelle de snapshots.

- Pour un **VDI ou VHD dynamique redimensionnable**, utiliser l'interface **Taille** pour porter la capacité logique à **80 Go**, si VirtualBox autorise cette opération.
- Si disque **VMDK**, image fixe, snapshots ou média non redimensionnable : **ne pas forcer** un `modifymedium --resize` ; adopter une procédure de clonage/conversion ou d'ajout de disque **après vérification de la configuration et sauvegarde**.
- Ne pas confondre **taille logique du disque** et **espace libre sur Windows** ; le fichier dynamique augmentera pendant l'utilisation. Ne pas dépasser l'espace disponible sur l'hôte.

Source : [VirtualBox, redimensionnement des médias](https://github.com/VirtualBox/virtualbox/blob/main/doc/manual/en_US/man_VBoxManage-modifymedium.xml).

## 3. Redémarrer Ubuntu : vérifier la nouvelle capacité

```bash
# Contrôler les ressources et la structure avant toute écriture sur partitions.
nproc
free -h
lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINTS
findmnt -no SOURCE,FSTYPE /
df -h /
```

**Il est normal que `df -h /` affiche encore ~25 Go** immédiatement après l'agrandissement du VDI. Le partitionnement et le système de fichiers doivent être étendus **suivant la structure réellement observée**.

Ne pas exécuter aveuglément `growpart`, `parted`, `resize2fs`, `xfs_growfs`, `pvresize` ou `lvextend` : il faut d'abord distinguer une racine `/dev/sda2` ext4 directe, une configuration LVM ou un autre système.

## 4. Étendre la partition et le système de fichiers (étape conditionnelle)

**Bloqué jusqu'à lecture de :** `lsblk -f`, `lsblk -o NAME,SIZE,TYPE,MOUNTPOINTS`, `findmnt -no SOURCE,FSTYPE /`. Les commandes de croissance seront documentées pour la disposition exacte. Aucune instruction générique destructive n'est retenue.

La sauvegarde reste obligatoire. Vérifier après extension :

```bash
df -h /
lsblk -f
```

Source : [Ubuntu — ajuster la taille d'un système de fichiers](https://help.ubuntu.com/stable/ubuntu-help/disk-resize.html).

## 5. Régression de FRAUD-001 (avant lancement Tazama)

```bash
cd /home/lionel/osef-open-source-payment-banking-labs/labs/FRAUD-001
docker compose ps

# Ce scénario arrête momentanément le relais pour tester son retour (T09) ;
# l'exécuter uniquement pendant une fenêtre de test du labo.
set -o pipefail
bash scripts/test-lab.sh --extended 2>&1 | tee /tmp/fraud-001-post-resize.log
```

N'effacer ni le volume SQLite, ni les clés de lab. Vérifier l'accès aux ports de la VM comme avant l'opération.

## 6. Porte de décision avant démarrage de Tazama

- [ ] RAM et CPU du PC Windows vérifiés, allocation sûre pour l'hôte.
- [ ] VM sauvegardée/exportée et volumes Docker sauvegardés.
- [ ] RAM/CPU de `osef-fraud-01` augmentés et vérifiés.
- [ ] VDI étendu à 80 Go **si compatible**, puis partition et système de fichiers vérifiés et étendus.
- [ ] Tests T01–T10 FRAUD-001 repassés.
- [ ] Ports de Tazama comparés à 8090–8092 ; aucun service Tazama publié inutilement hors localhost.
- [ ] Profil Tazama réduit au nécessaire, mesures CPU/RAM/disque prévues.

**Attention au script officiel Tazama** : le lanceur `core/tazama-core.sh` peut exécuter `docker compose down --volumes` pour certains projets Tazama ; ne pas l'employer sans comprendre la commande affichée. Le profil inspecté contient 13 services, dont les besoins réels en mémoire ne sont pas encore mesurés.

## Statut d'exécution

- [x] **Option B retenue par l'utilisateur.**
- [x] Documentation et guide de redimensionnement ajoutés au dépôt OSEF.
- [ ] Inventaire du PC Windows et format du disque VirtualBox.
- [ ] Sauvegarde.
- [ ] Redimensionnement.
- [ ] Validation Ubuntu et régression FRAUD-001.
- [ ] Déploiement Tazama et tests.

## Références

- [Choix A/B et comparatif](DIMENSIONNEMENT-VIRTUALBOX.md)
- [Issue FRAUD-002 #50](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/50)
- [Issue FRAUD-001 #43](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/43)
- [Tazama officiel — commit inspecté](https://github.com/tazama-lf/tazama-stack/tree/83e4b12c16986aedfff843ed84b7045ac912ec0a)
