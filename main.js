import { exec } from 'child_process';
import path from 'path';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

// 🔁 Nécessaire pour pouvoir utiliser __dirname en ES Module
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// 1ᵉʳ argument : chemin du dossier « content » ; défaut = "./content"
const contentDir = process.argv[2] ?? 'content';

console.log(`🧬  Extraction des définitions dans : ${contentDir}`);

// Chemins absolus vers les scripts
const extractPy = path.resolve(__dirname, 'exploration_jupytercards/extract.py');
const astToHTML = path.resolve(__dirname, 'exploration_jupytercards/AstToHTML.js');
const toDictPy = path.resolve(__dirname, 'exploration_jupytercards/toDict.py');

// ————————————————————————————
// ÉTAPE 1 : extract.py — extraction JSON → AST
// ————————————————————————————
exec(`python "${extractPy}" "${contentDir}"`, (error, stdout, stderr) => {
  if (error) {
    console.error(`🚨  Erreur Python (extract.py) : ${error.message}`);
    console.error(stderr);
    return;
  }
  console.log(`🧪  Sortie extract.py :\n${stdout}`);
  console.log('🔬  Conversion HTML…');

  // ————————————————————————————
  // ÉTAPE 2 : AstToHTML.js — AST → fichiers HTML
  // ————————————————————————————
  exec(`node "${astToHTML}"`, (error2, stdout2, stderr2) => {
    if (error2) {
      console.error(`🚨  Erreur JavaScript (AstToHTML.js) : ${error2.message}`);
      console.error(stderr2);
      return;
    }
    console.log(`🧪  Sortie AstToHTML.js :\n${stdout2}`);
    console.log('🧬  Création du dictionnaire (toDict.py)…');

    // ————————————————————————————
    // ÉTAPE 3 : toDict.py — titre def + HTML → dictionnaire JSON
    // ————————————————————————————
    exec(`python "${toDictPy}" "${contentDir}"`, (error3, stdout3, stderr3) => {

      if (error3) {
        console.error(`🚨  Erreur Python (toDict.py) : ${error3.message}`);
        console.error(stderr3);
        return;
      }
      console.log(`🧪  Sortie toDict.py :\n${stdout3}`);
    });
  });
});
