<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:bb9af7,100:7aa2f7&height=220&section=header&text=Module%2006%20:%20The%20Codex&fontSize=52&fontAlignY=38&fontColor=EDEDED&animation=fadeIn" width="100%"/>
</div>

# 📘 Module 06 : The Codex - Les Mystères de l'Import

Dernière étape avant l'architecture de cartes complexe, ce module s'intéresse à la manière dont Python organise ses fichiers et gère les dépendances. On y explore les entrailles du système d'importation et les pièges classiques comme les dépendances circulaires.

---

## 📂 Analyse des Exercices

### 🔵 ex0 : The Sacred Scroll (`__init__.py`)
**Détails** : Apprentissage du rôle du fichier `__init__.py`. C'est lui qui transforme un répertoire ordinaire en un **Package Python**. On y définit ce qui doit être exporté et accessible par l'utilisateur final.

### 🔵 ex1 : Import Transmutation (Pathways)
**Détails** : Manipulation des chemins d'importation. On apprend à faire des imports relatifs (`from .module import X`) et absolus. C'est essentiel pour structurer un projet qui grandit au-delà d'un seul dossier.

### 🔵 ex2 : The Great Pathway Debate
**Détails** : Exploration de `sys.path`. Comprendre comment Python cherche les modules sur votre machine. C'est la base pour résoudre les erreurs de type `ModuleNotFoundError`.

### 🔵 ex3 : Circular Curse
**Concept** : **Dépendances Circulaires**.
**Détails** : Que se passe-t-il si A importe B, et B importe A ? Python lève une erreur ou crée des objets incomplets. Ce module enseigne les techniques pour briser ce cycle (imports locaux, refactoring).

---

## 🧠 Notions Approfondies

### 1. Packages vs Modules
Un module est un fichier `.py`. Un package est un dossier contenant des modules et un fichier `__init__.py`. Les packages permettent une organisation hiérarchique propre.

### 2. Le mécanisme d'Import
Quand vous faites `import X`, Python :
1. Cherche dans `sys.modules` (cache).
2. Cherche dans les dossiers de `sys.path`.
3. Compile le fichier en bytecode (.pyc).
4. Exécute le module pour créer ses objets.

### 3. Sortir du "Circular Curse"
Pour éviter qu'une application ne se bloque dans une boucle d'import :
- Déplacer l'import à l'intérieur d'une fonction.
- Utiliser un pattern de médiateur.
- Extraire la logique partagée dans un troisième module neutre.

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7aa2f7,100:bb9af7&height=120&section=footer" width="100%"/>
</div>
