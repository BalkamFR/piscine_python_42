<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:bb9af7,100:7aa2f7&height=220&section=header&text=Module%2005%20:%20Intermediate&fontSize=52&fontAlignY=38&fontColor=EDEDED&animation=fadeIn" width="100%"/>
</div>

# 🧙‍♂️ Module 05 : Python Intermédiaire - Notions Avancées

Ce module s'attaque à des outils de méta-programmation et d'analyse de données textuelles. On y découvre comment "envelopper" des fonctions pour modifier leur comportement (Décorateurs) et comment analyser finement du contenu textuel.

---

## 📂 Analyse des Exercices

### 🟢 ex0 : Building (String Analysis)
**Fichier** : `Building.py`
- **Concept** : Analyse fréquentielle et filtrage.
- **Logique** : Analyse d'une chaîne de caractères pour compter le nombre de majuscules, minuscules, signes de ponctuation et chiffres. Cela renforce la maîtrise des méthodes de classe `str` (`isupper()`, `isdigit()`, etc.).

### 🟢 ex1 : NULL Queries
**Fichier** : `NULL_queries.py`
- **Concept** : Gestion des données manquantes.
- **Logique** : Simulation d'un système de recherche capable de détecter et de gérer les valeurs `None`, `NaN` ou les chaînes vides. C'est une compétence clé pour le nettoyage de données (Data Cleaning).

### 🟢 ex2 : Call Limit (Decorators)
**Fichier** : `callLimit.py`
- **Concept** : **Décorateurs avec arguments**.
- **Logique** : Création d'un décorateur `@callLimit(n)` qui empêche une fonction d'être appelée plus de `n` fois. C'est un exercice de haut niveau qui demande de comprendre les fonctions imbriquées (closures) et la portée des variables.

---

## 🧠 Notions Approfondies

### 1. Que sont les Décorateurs ?
Un décorateur est une fonction qui prend une autre fonction en entrée et en retourne une version "étendue". C'est le pattern **Wrapper**. On l'utilise pour ajouter du logging, faire des vérifications de permission, ou comme ici, limiter l'usage d'une ressource.

### 2. Closures et Nonlocal
Dans un décorateur complexe, on a besoin de garder un état (le compteur d'appels). La variable se trouve dans la portée de la fonction parente. Pour la modifier depuis la fonction enfant, on utilise souvent le mot-clé `nonlocal`.

### 3. Analyse de Données Textuelles
L'analyse de texte (NLP de base) repose sur la capacité à itérer proprement et à utiliser les bonnes méthodes de test de caractères. Python est particulièrement performant dans ce domaine grâce à sa gestion native des chaînes Unicode.

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7aa2f7,100:bb9af7&height=120&section=footer" width="100%"/>
</div>
