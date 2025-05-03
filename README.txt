²Guide utilisation :

0 - Pré requis :

*Les pages de cours  sont dans cette version obligées d'etre au format json.

1 - environnement :

* Installer Visual studio code
* créer un environnement
* installer git sur sa machine : https://git-scm.com/downloads/
* Installer node sur votre machine : https://nodejs.org/fr
* Installer python : https://www.python.org/downloads/ (peut etre aussi sur votre IDE)
* Installer ipKernel
* Installer jupyter ( possible aussi )
* Redemarrer votre IDE
 
2 - Installation dossiers
 *ouvrir un terminal, choisir le dossier où vous souhaitez installer l'outil et executer les commandes suivantes :
 *git clone https://github.com/Ismaelwn/test_user_jupytercards.git
 *cd test_user_jupytercards;
 *une fois dans le dossier, installer les deux dossiers JupyterCards et Exploration_JupyterCards
  a - télécharger exploration_JupyterCards, taper dans votre terminal en verifiant bien que vous êtes dans le dossier test_user_jupytercards
  git https://github.com/Ismaelwn/exploration_jupytercards.git
  b - télécharger JupyterCards, taper dans votre terminal en verifiant bien que vous êtes dans le dossier test_user_jupytercards
  git https://github.com/Ismaelwn/jupytercards.git
 *taper la commande ls pour verifier que vous avez bien les deux dossiers téléchargées

3 - Utilisation
  **Préparer vos cours :
    - Données : un dossier contenant vos cours ou tout simplement un cours.
    
  **Création des cartes

  *Lancer un terminal dans le dossier "TER", 2 choix s'offrent à vous : 
2 choix s'offrent à vous :
   Soit vous avez la possibilité de spécifier le chemin absolu du dossier contenant vos pages de cours ou bien votre fichier de cours, il faudra taper la commande suivant : node main.js <nom_fichier_ou_dossier>
   Soit vous avez dans notre dossier TER directement stockés un fichier de cours ou bien un dossier contenant vos pages de cours, il faudra alors taper simplement la commande sans paramètre <nom_fichier_ou_dossier> ( pas encore implementé )

  **
    Afficher le nom des fichiers et tenter d'executer le code sur le terminal (afficher les cartes les retourner)


4 - Visualisation des cartes 

Après avoir réaliser toutes les opérations ci dessus, retourner dans le dossier mère "TER", ouvrer et executer le notebook


NB : Pour la visualisation, je n'ai pas trouvé de moyen plus efficient de le lancer que depuis un notebook.
