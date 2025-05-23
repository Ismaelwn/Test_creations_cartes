import subprocess
import sys
import os
import exploration_jupytercards  # Ton package installé via pip
from exploration_jupytercards import tools

# ————————————————————————————————————
# 1. Récupérer le dossier content (argument optionnel)
# ————————————————————————————————————

current_dir = os.getcwd()
content_dir = sys.argv[1] if len(sys.argv) > 1 else "content"
#print(current_dir)
#print(content_dir)
print(f"🧬  Extraction des définitions dans : {content_dir}")

# ————————————————————————————————————
# 2. Étape Python : tool_extraction.py
# ————————————————————————————————————

tools.extract_tools(current_dir)

# ————————————————————————————————————
# 3. Étape JS : index.js (dans exploration_jupytercards)
# ————————————————————————————————————
# Récupérer le chemin du fichier JS dans le package installé

js_path = os.path.join(
    os.path.dirname(exploration_jupytercards.__file__),
    "AstToHTML.js" 
)

print("🔬  Conversion HTML via JS…")

try:
    result2 = subprocess.run(
        ["node", js_path],
        capture_output=True, text=True, check=True
    )
    print(f"🧪  Sortie index.js :\n{result2.stdout}")
except subprocess.CalledProcessError as e:
    print(f"🚨  Erreur dans index.js :\n{e.stderr}")
    sys.exit(2)

# ————————————————————————————————————
# 4. Étape Python : tool_toDict.py
# ————————————————————————————————————
print("🧬  Création du dictionnaire final (tool_toDict.py)…")
tools.toDict_tools(current_dir)
