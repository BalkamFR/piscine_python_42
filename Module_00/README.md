<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:bb9af7,100:7aa2f7&height=220&section=header&text=Module%2000%20:%20Starting&fontSize=52&fontAlignY=38&fontColor=EDEDED&animation=fadeIn" width="100%"/>
</div>

# 🐍 Module 00 : Starting - Les Fondamentaux

Ce module pose les bases du langage Python à travers une série d'exercices progressifs sur le thème de la gestion d'un jardin. L'objectif est de maîtriser les entrées/sorties, les types de données de base, les structures de contrôle et une introduction à la récursivité.

---

## 📂 Détail des Exercices

### 🔵 ex0 : Hello Garden
**Fichier** : `ft_hello_garden.py`
- **Objectif** : Premier script Python.
- **Détails** : Utilisation de la fonction `print()` pour afficher un message de bienvenue à la communauté. C'est l'équivalent du "Hello World".

### 🔵 ex1 : Garden Plot Area
**Fichier** : `ft_plot_area.py`
- **Objectif** : Manipulation des entrées utilisateur et calculs de base.
- **Logique** : 
    1. Demande la longueur et la largeur via `input()`.
    2. Conversion des chaînes en entiers via `int()`.
    3. Calcul de la surface (`longueur * largeur`).
    4. Affichage du résultat.

### 🔵 ex2 : Harvest Total
**Fichier** : `ft_harvest_total.py`
- **Objectif** : Accumulation de données.
- **Logique** : Demande le poids de récolte pour trois jours différents et affiche la somme totale. Cela permet de s'exercer à l'enchaînement des inputs et à l'arithmétique simple.

### 🔵 ex3 : Plant Age Check
**Fichier** : `ft_plant_age.py`
- **Objectif** : Structures conditionnelles (`if / else`).
- **Logique** : Si l'âge saisi est > 60 jours, la plante est prête. Sinon, elle a besoin de plus de temps. Introduction aux opérateurs de comparaison.

### 🔵 ex4 : Water Reminder
**Fichier** : `ft_water_reminder.py`
- **Objectif** : Logique de décision plus fine.
- **Logique** : Rappel d'arrosage basé sur le temps écoulé depuis le dernier apport en eau (> 2 jours).

### 🔵 ex5 : Count to Harvest
**Fichier** : `ft_count_harvest.py`
- **Objectif** : Iteration vs Récursion.
- **Détails** : 
    - **Iterative** : Utilise une boucle `for` avec `range()`.
    - **Recursive** : Une fonction qui s'appelle elle-même jusqu'à atteindre le cas de base (jour de récolte). C'est une introduction cruciale à la pile d'appels.

### 🔵 ex6 : Garden Summary
**Fichier** : `ft_garden_summary.py`
- **Objectif** : Formatage de chaînes de caractères.
- **Logique** : Utilisation des f-strings (ou `.format()`) pour générer un rapport propre incluant le nom du jardin et le nombre de plantes.

### 🔵 ex7 : Seed Inventory (Type Annotations)
**Fichier** : `ft_seed_inventory.py`
- **Objectif** : Introduction au typage statique (Type Hints).
- **Détails** : La fonction `ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None` doit être strictement annotée. Elle adapte son message selon l'unité (`packets`, `grams`, `area`). C'est le premier pas vers la rigueur de `mypy`.

---

## 🧠 Concepts Clés Appris

### 1. Dynamic Typing vs Type Hints
Python est dynamiquement typé, mais pour des projets robustes, on utilise des **Type Hints** (ex7). Cela aide les IDE et les outils comme `mypy` à détecter les bugs avant l'exécution.

### 2. Récursivité
La récursivité (ex5) consiste à décomposer un problème en sous-problèmes plus petits. La fonction s'appelle elle-même jusqu'à une "condition d'arrêt" (base case). Attention à la `RecursionError` si la condition n'est jamais remplie !

### 3. F-Strings (Formatted String Literals)
Introduites en Python 3.6, les f-strings (`f"Bonjour {nom}"`) sont le moyen le plus rapide et lisible de concaténer du texte et des variables.

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7aa2f7,100:bb9af7&height=120&section=footer" width="100%"/>
</div>
