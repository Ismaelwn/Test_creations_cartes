
# 📚 JupyterCards – Générateur de cartes mémoire à partir de fichiers JSON

JupyterCards est un outil permettant de générer et visualiser des cartes mémoire automatiquement à partir de cours structurés au format `.json`.  
Il combine une interface en ligne de commande (Node.js) pour la création de cartes et une interface Jupyter Notebook pour leur visualisation.

---

## 🧰 Prérequis

Aucun besoin d’installer manuellement Git, Node.js ou Python si vous utilisez les scripts suivants :

- Windows : [`install_env_windows.bat`](install_env_windows.bat)
- Linux/macOS : [`install_env_linux.sh`](install_env_linux.sh)

> Ces scripts téléchargent et installent automatiquement :
> - Python 3.11
> - pip + jupyter + ipykernel
> - Node.js LTS
> - Git

---

## 🚀 Installation rapide

### 1. Cloner le projet

```bash
git clone https://github.com/Ismaelwn/test_user_jupytercards.git
cd test_user_jupytercards
```

### 2. Lancer le script d'installation

#### ▸ Sous Linux/macOS

```bash
chmod +x install_env_linux.sh
./install_env_linux.sh
```

#### ▸ Sous Windows

Double-cliquez simplement sur le fichier `install_env_windows.bat`

---

## 📁 Installation des dépendances manuellement (optionnel)

### Python

```bash
pip install -r requirements.txt
```

### Node.js (dans le dossier `TER`)

```bash
cd TER
npm install
```

---

## 🧪 Utilisation

### 1. Préparer vos cours

- Vos cours doivent être **au format `.json`**.
- Vous pouvez stocker :
  - soit un **dossier contenant plusieurs fichiers `.json`**
  - soit un **fichier unique** dans le dossier `TER`.

### 2. Générer les cartes

Dans le dossier `TER`, exécutez :

```bash
cd TER
```

#### ➤ Option A : Vous spécifiez le chemin absolu du fichier ou dossier

```bash
node main.js /chemin/vers/fichier_ou_dossier.json
```

#### ➤ Option B : Vous avez déjà placé les fichiers dans `TER`

⚠️ Non encore implémenté. À terme, vous pourrez simplement faire :

```bash
node main.js
```

---

## 🃏 Visualisation des cartes

1. Restez dans le dossier `TER`
2. Ouvrez le notebook `notebook_visualisation.ipynb`
3. Exécutez les cellules pour :
   - afficher la liste des cartes
   - retourner une carte au hasard
   - visualiser son contenu

> 💡 Pour l’instant, la **visualisation fonctionne uniquement via un notebook Jupyter**.

---

## 📂 Arborescence recommandée

```
test_user_jupytercards/
├── exploration_jupytercards/     # installé via pip depuis GitHub
├── jupytercards/                 # installé via pip depuis GitHub
├── install_env_windows.bat       # script auto Windows
├── install_env_linux.sh          # script auto Linux/macOS
├── .gitignore
├── README.md
├── exapmle.ipynb
```

---

## 📦 Dépendances utilisées

### Python
- `ipykernel`
- `jupyter`

### Node.js
- `fs` (natif)
- `path` (natif)


---

## 🙋 Support

Pour toute question, bug ou suggestion :

- Ouvrez une **issue GitHub**
- Contactez l’auteur : [https://github.com/Ismaelwn](https://github.com/Ismaelwn)

---

## 📄 Licence

Ce projet est libre d'utilisation, de modification et de diffusion.
