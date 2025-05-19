
# 📚 JupyterCards – Générateur de cartes mémoire à partir de fichiers JSON

JupyterCards est un outil permettant de générer et visualiser des cartes mémoire automatiquement à partir de cours structurés au format `.json`. En complément, nous avons implémenté des outils permettant l'extraction et avons modifié JupyterCards afin de l'adapter à notre problème.
Ce dépot sert à installer une version de notre outil d'extraction et de transformation de cours en carte. A l'aide d'une interface Jupyter Notebook, nous pouvons en avoir une visualisation.

---

## 🧰 Prérequis

> - Python 3.11
> - pip + jupyter + ipykernel
> - Node.js LTS
> - Git

---

## 🚀 Installation rapide

### 0. Installer un environnement 


Je travaille dessus pour produire quelque chose de généraliste (ce que j'ai fait actuellement ne me satisfait pas)

1. Installer python sur votre machine (si ce n'est pas deja fait) : [python 3.11](https://www.python.org/downloads/release/python-3110/)
2. Installer node sur votre machine : [node v22.15.1](https://nodejs.org/fr/download)
3. installer Jupyter et ipykernel : 
ouvrir un terminal et taper la commande suivante :
```bash
pip install jupyter ipykernel
```

### 1. Cloner le projet
placer vous dans le repertoire ou vous souhaitez faire l'installation puis effectuer la commande suivante :

```bash
git clone https://github.com/Ismaelwn/test_creations_cartes.git
cd test_creations_cartes
```

Une fois dans le dossier test_creations_cartes :
y deposer votre repertoire avec vos cours 

### 2. Installer les librairies nécessaires

installer la premiere librairie, qui contient les outils d'extraction :
```bash
pip install git+https://github.com/Ismaelwn/exploration_jupytercards.git
```
installer la deuxieme librairie, qui contient les outils de representation et d'affichage d'une carte :
```bash
pip install git+https://github.com/Ismaelwn/jupytercards.git
```

Fin de l'installation des librairies et outils nécessaires.

## 🧪 Utilisation

### 1. Préparer vos cours

- Vos cours doivent être **au format `.json`**.
- Vous pouvez stocker :
  - soit un **dossier contenant plusieurs fichiers `.json`**
  - soit un **fichier unique** dans le dossier `TER`.

### 2. Générer les cartes

Dans le dossier, 

```bash
cd Test_creation_cartes
```

#### ➤ Vous spécifiez le chemin absolu du fichier ou dossier

```bash
python run_creation_cartes.py <nom_du_dossier_ou_fichier>
```



## 🃏 Visualisation des cartes

1. Restez dans le dossier 
2. Ouvrez le notebook `example.ipynb`
3. Exécutez les cellules pour :
   - afficher la liste des cartes au hasard
   - retourner une carte
   - visualiser son contenu

> 💡 Pour l’instant, la **visualisation fonctionne uniquement via un notebook Jupyter**.


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

