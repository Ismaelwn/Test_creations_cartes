import subprocess
import sys
import os
import exploration_jupytercards  # Ton package installé via pip

# ————————————————————————————————————
# 1. Récupérer le dossier content (argument optionnel)
# ————————————————————————————————————
content_dir = sys.argv[1] if len(sys.argv) > 1 else "content"
print(f"🧬  Extraction des définitions dans : {content_dir}")

# ————————————————————————————————————
# 2. Étape Python : tool_extraction.py
# ————————————————————————————————————
try:
    result1 = subprocess.run(
        ["python", "tool_extraction.py", content_dir],
        capture_output=True, text=True, check=True
    )
    print(f"🧪  Sortie tool_extraction.py :\n{result1.stdout}")
except subprocess.CalledProcessError as e:
    print(f"🚨  Erreur dans tool_extraction.py :\n{e.stderr}")
    sys.exit(1)

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

try:
    result3 = subprocess.run(
        ["python", "tool_toDict.py"],
        capture_output=True, text=True, check=True
    )
    print(f"🧪  Sortie tool_toDict.py :\n{result3.stdout}")
except subprocess.CalledProcessError as e:
    print(f"🚨  Erreur dans tool_toDict.py :\n{e.stderr}")
    sys.exit(3)