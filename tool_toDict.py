import os
from exploration_jupytercards import toDict
from exploration_jupytercards import file

l = []
chemin_courant = os.getcwd()
dossier = os.listdir("JSON")
for fichier in dossier:
    if fichier.endswith(".json"):
        dict_ = toDict.convToDict("JSON/"+fichier)
        l.append(dict_)
        print(f"--- {fichier} traité ---\n")

file.writeInFile(l, chemin_courant+"/def_converted.json")