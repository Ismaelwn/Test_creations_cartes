# JupyterCards – Flashcard Generator from JSON Files


[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue?logo=python)](https://www.python.org/) 
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

JupyterCards is a tool that automatically generates and displays flashcards from courses structured in `.json` format. In addition, we have implemented extraction tools and modified JupyterCards to adapt it to our problem. This repository is used to install a version of our extraction and course-to-card transformation tool. With a Jupyter Notebook interface, we can visualize the result.

## Get Started

> * Python >= 3.11
> * pip >= 24.0.1

---

## Quick Installation

### 1. Clone the repository

Go to the directory where you want to perform the installation, then run:

```bash
git clone https://github.com/Ismaelwn/test_creations_cartes.git
cd test_creations_cartes
```

Once inside the `test_creations_cartes` folder, drop your directory containing your courses there.

### 2. Install the required libraries

Install the first library, which contains the extraction tools:

```bash
pip install git+https://github.com/Ismaelwn/exploration_jupytercards.git
```

Install the second library, which contains the representation and display tools for a card:

```bash
pip install git+https://github.com/Ismaelwn/jupytercards.git
```

The installation step is complete.

## Usage

### 1. Prepare your courses

* Your courses must be **in `.json` format** and **in `.md` format**.
* You must store them in a directory, required for flashcard generation.

### 2. Generate the cards

Inside the folder:

```bash
cd Test_creation_cartes
```

#### Specify the absolute path of the file or folder

```bash
python run_creation_cartes.py <name_of_folder_or_file>
```

## Card Visualization

1. Stay in the folder.
2. Open the notebook `example.ipynb`.
3. Run the notebook cells:

   * The cards will appear in each output as a list of cards arranged randomly.
   * Click to flip a card.
   * View their contents.

## Support

For any question, bug, or suggestion:

* Open a **GitHub issue**
* Contact the author: [https://github.com/Ismaelwn](https://github.com/Ismaelwn)
