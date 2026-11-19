# FRAUD-004 — Créer la VM `osef-fraud-04` (VirtualBox / Ubuntu Server)

> **Statut : procédure préparatoire, non exécutée.** Aucune VM ou installation n'est présumée créée. Issue de suivi : [#68](https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/68).

## 1. But et architecture

Préparer une VM Ubuntu Server **indépendante** de `osef-fraud-01` (FRAUD-001/002) pour les essais Kubernetes k3s + Helmfile du [Tazama Helm Working Group](https://github.com/tazama-lf/technical-steering-committee/discussions/21).

```text
Windows 11 / VirtualBox
├── osef-fraud-01  (FRAUD-001/002 : ne pas modifier)
└── osef-fraud-04  (FRAUD-004)
    ├── NIC 1 : NAT / DHCP (Internet)
    ├── NIC 2 : Host-Only / 192.168.255.20/24 (à confirmer libre)
    └── Ubuntu Server -> k3s -> Helm 3 / Helmfile 1.x -> Tazama core/onprem
```

## 2. Prérequis et dimensionnement

- Windows 11 avec VirtualBox installé, virtualisation matérielle activée, réseau Host-Only opérationnel.
- ISO **Ubuntu Server 22.04 LTS amd64** depuis https://releases.ubuntu.com/22.04/ ; comparer le SHA256 local à `SHA256SUMS` publié sur le site officiel.
- Proposition **non officielle** pour le laboratoire : **8 vCPU, 16 Gio RAM, 160 Gio VDI dynamique**. Ce ne sont pas des exigences minimales certifiées de Tazama. Adapter aux ressources réellement disponibles; **arrêter `osef-fraud-01` si nécessaire**.
- Vérifier que `192.168.255.20` n'est pas déjà attribuée et que le réseau Host-Only existant est bien `192.168.255.0/24`.

PowerShell Windows :
```powershell
Get-CimInstance Win32_ComputerSystem |
  Select-Object NumberOfLogicalProcessors,@{Name="RAM_GiB";Expression={[math]::Round($_.TotalPhysicalMemory/1GB,2)}}
Get-PSDrive C
Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.IPAddress -like '192.168.255.*'}
```

**Ne pas allouer tous les processeurs ou toute la mémoire du PC à la VM.** Le VDI dynamique pourra croître jusqu'à 160 Gio : surveiller l'espace réellement libre.

## 3. Création dans VirtualBox (interface graphique)

1. VirtualBox → **New** ; nom : `osef-fraud-04` ; type Linux / Ubuntu 64-bit.
2. Sélectionner l'ISO Ubuntu Server ; choisir l'installation manuelle (désactiver « Unattended Installation » si proposé).
3. Hardware : **16384 MB RAM** et **8 CPU** *si l'hôte le permet*.
4. Virtual Hard Disk : **Create new**, **VDI**, **dynamically allocated**, **160 GB**.
5. VM **éteinte**, ouvrir **Settings → Network** :
   - Adapter 1 : Enable / Attached to **NAT** / Cable Connected.
   - Adapter 2 : Enable / Attached to **Host-only Adapter**, sélectionner le réseau Host-Only existant associé à `192.168.255.0/24` / Cable Connected.
6. Vérifier que la VM FRAUD-001/002 n'a pas été modifiée.

## 4. Installation d'Ubuntu Server

Démarrer la VM. Dans l'assistant :
- Installer Ubuntu Server; choisir langue/clavier selon le poste.
- NAT en DHCP pour l'accès Internet; configurer Host-Only après installation.
- Utiliser le disque virtuel proposé; vérifier soigneusement qu'il s'agit bien du **disque de la nouvelle VM**.
- Hostname : `osef-fraud-04`.
- Créer un utilisateur non-root, par exemple `lionel`, avec mot de passe unique.
- Cocher **Install OpenSSH server**.
- Aucun snap optionnel nécessaire.
- Terminer, éjecter l'ISO si demandé, redémarrer.

## 5. Mise à jour et diagnostic initial

Dans la console Ubuntu :
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y openssh-server curl git jq vim ca-certificates openssl dnsutils
sudo systemctl enable --now ssh
sudo hostnamectl set-hostname osef-fraud-04

hostnamectl
lsb_release -a
free -h
nproc
lsblk
df -h
ip -br addr
ip route
ls -l /etc/netplan/
sudo cat /etc/netplan/*.yaml
```

Noter les noms **réels** des interfaces. Souvent `enp0s3` = NAT et `enp0s8` = Host-Only, mais ne pas le supposer.

## 6. Configurer Host-Only en IP fixe

**Préalable :** vérifier dans VirtualBox que le réseau Host-Only est `192.168.255.0/24`, que l'IP `192.168.255.20` est libre, et identifier l'interface correspondant à l'adaptateur 2.

Faire une sauvegarde du fichier Netplan existant, puis **adapter ce fichier**, sans supprimer d'autres paramètres nécessaires :
```bash
sudo cp /etc/netplan/50-cloud-init.yaml /etc/netplan/50-cloud-init.yaml.bak
sudo nano /etc/netplan/50-cloud-init.yaml
```
Le nom `50-cloud-init.yaml` est un **exemple** : utiliser le nom réellement présent dans `/etc/netplan/`. Si cloud-init gère la configuration réseau, vérifier son mécanisme avant de modifier durablement le fichier.

Exemple **uniquement si les interfaces sont bien enp0s3 et enp0s8** :
```yaml
network:
  version: 2
  ethernets:
    enp0s3:
      dhcp4: true
    enp0s8:
      dhcp4: false
      addresses:
        - 192.168.255.20/24
```

Appliquer depuis **la console VirtualBox** (pour ne pas perdre l'accès SSH) :
```bash
sudo netplan generate
sudo netplan try
ip -br addr
ip route
ping -c 3 1.1.1.1
getent hosts github.com
```

Ne pas configurer de passerelle par défaut sur l'interface Host-Only. La route Internet doit rester sur le NAT.

Depuis PowerShell Windows :
```powershell
Test-NetConnection 192.168.255.20 -Port 22
ssh lionel@192.168.255.20
```
Adapter `lionel` au compte effectivement créé. Éviter de désactiver le pare-feu pour résoudre un problème réseau.

## 7. Critères d'acceptation de la VM (avant Kubernetes)

- [ ] Nom `osef-fraud-04` confirmé par `hostnamectl`.
- [ ] Ubuntu Server installé et mises à jour effectuées.
- [ ] RAM, CPU et disque vérifiés avec `free -h`, `nproc`, `lsblk`, `df -h`.
- [ ] NAT fonctionnel : résolution DNS et accès Internet.
- [ ] Host-Only `192.168.255.20/24` présent et sans conflit.
- [ ] SSH depuis Windows opérationnel.
- [ ] `osef-fraud-01` préservée.
- [ ] Aucune clé privée, mot de passe ou configuration sensible publiée.

### Sorties à fournir pour revue P0/P1
```bash
hostnamectl
free -h
nproc
lsblk
ip -br addr
ip route
```
Expurger tout renseignement sensible avant publication. Conserver les résultats dans le dossier de preuves FRAUD-004, avec date et version du système.

## 8. Étape suivante : Kubernetes et Tazama (ne pas exécuter avant validation)

Après validation de la VM :
1. Installer **k3s** sur nœud unique selon https://docs.k3s.io/quick-start et vérifier `Ready` + StorageClass.
2. Installer Helm 3, Helmfile 1.x et les dépendances du dépôt officiel.
3. Cloner `https://github.com/tazama-lf/tazama-helm` sur `dev` et enregistrer le SHA.
4. Préparer les secrets localement (ne jamais committer `values/secrets.yaml`).
5. Suivre **exactement la version courante** du guide officiel : https://github.com/tazama-lf/tazama-helm/blob/dev/README.md ; scénario `core onprem`.
6. Capturer états des pods, readiness, logs et tests E2E ; ne déclarer aucun test réussi sans preuve.

### Sources
- Ubuntu ISO : https://releases.ubuntu.com/22.04/
- VirtualBox documentation : https://www.virtualbox.org/manual/
- k3s : https://docs.k3s.io/quick-start
- Tazama Helm : https://github.com/tazama-lf/tazama-helm
- Issue de suivi OSEF : https://github.com/opensource-enterprise-factory/osef-open-source-payment-banking-labs/issues/68
