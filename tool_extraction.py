from exploration_jupytercards import extract
from exploration_jupytercards import file
import sys
import os

#  Argument positionnel : chemin du répertoire « content »
current_dir = os.getcwd()
content_dir = sys.argv[1]
#content_par = os.path.dirname(content_dir)
if not os.path.isdir(content_dir):
    raise FileNotFoundError(f"Le répertoire '{content_dir}' est introuvable.")

os.makedirs(current_dir+"/JSON", exist_ok=True)

file_counter = 0
for fichier in os.listdir(content_dir):
    if fichier.endswith(".json"):
        chemin = os.path.join(content_dir, fichier)
        extract.extract_admonition_ast_from_file(chemin, file_counter)
        file_counter+=1
        print(file_counter)
        print(f"— {fichier} traité —\n")
