import subprocess
import sys
import os
from exploration_jupytercards import tools, preprocess   # ton package installé via pip
import exploration_jupytercards

current_dir = os.getcwd()
nextpart_dir = os.path.join(os.getcwd(),"_build", "content")

if len(sys.argv) > 1:
    content_dir = sys.argv[1]
else:
    raise FileNotFoundError(
        "Le répertoire de contenu n'est pas spécifié. "
        "Veuillez fournir un argument avec le chemin du dossier."
    )

# 0. Pré-traitement des .md et déplacement des fichiers temporaires
print("Pré-traitement des fichiers Markdown")
preprocess.pre_build(current_dir, content_dir)
preprocess.moove_files_JSON(content_dir, os.path.join(current_dir, "_build", "content"))
print("\n"+"Fin du Pré-traitement des fichiers Markdown")

print("\n"+"\n"+f"Début de l'Extraction des définitions dans : {content_dir}")
tools.extract_tools(current_dir)
print("\n"+f"Fin de l'Extraction des définitions dans : {content_dir}")
print("\n")
js_path = os.path.join(
    os.path.dirname(exploration_jupytercards.__file__),
    "AstToHTML.js"
)
print("\n"+"\n"+"Début de la Conversion HTML via JS…")
try:
    result2 = subprocess.run(
        ["node", js_path],
        capture_output=True, text=True, check=True, encoding='utf-8', errors='replace'
    )
    print(f"Sortie index.js :\n{result2.stdout}")
except subprocess.CalledProcessError as e:
    print(f"Erreur dans index.js :\n{e.stderr}")
    sys.exit(2)
print("\n"+"Fin de la Conversion HTML via JS…")
print("\n")

print("\n"+"\n"+"Début de la Création du dictionnaire final ")
tools.toDict_tools(current_dir)
print("\n"+"Fin de la Création du dictionnaire final ")
