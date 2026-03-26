<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:bb9af7,100:7aa2f7&height=220&section=header&text=Module%2004%20:%20Adv%20OOP&fontSize=52&fontAlignY=38&fontColor=EDEDED&animation=fadeIn" width="100%"/>
</div>

# 🚀 Module 04 : Bootcamp Python - Architecture Objet Avancée

Ce module pousse les concepts de la programmation orientée objet vers leurs retranchements. On y aborde l'héritage complexe, la surcharge de constructeurs, et surtout l'utilisation des **Classes de Base Abstraites (ABC)** pour définir des contrats stricts dans votre code.

---

## 📂 Analyse des Exercices

### 🔵 ex0 : Loading
**Fichier** : `Loading.py`
- **Concept** : Générateurs et Temps réel.
- **Logique** : Création d'une barre de progression dynamique. Cela nécessite de comprendre comment un générateur peut s'intercaler dans une boucle de traitement pour fournir un feedback visuel.

### 🔵 ex1 : S1E7 (Inheritance)
**Fichier** : `S1E7.py`
- **Concept** : **Héritage et Overloading**.
- **Logique** : Implémentation de classes comme `Stark` ou `Lannister`. On apprend à surcharger le constructeur `__init__` tout en appelant `super().__init__()` pour maintenir la cohérence de la classe parente.

### 🔵 ex2 : S1E9 (Abstractions)
**Fichier** : `S1E9.py`
- **Concept** : **Abstract Base Classes (ABC)**.
- **Logique** : Définition d'une classe `Character` qui ne peut pas être instancée directement. Elle force ses enfants à implémenter certaines méthodes (comme `die()`). C'est la base de la conception par contrat.

### 🔵 ex3 & ex4 : Advanced Interactions
- **Concept** : Méthodes statiques et de classe dans un contexte d'héritage.
- **Détails** : Exploration de la manière dont les méthodes `@classmethod` peuvent être héritées et surchargées pour adapter l'instanciation au type de l'enfant.

---

## 🧠 Notions Approfondies

### 1. Pourquoi l'Abstraction (ABC) ?
L'abstraction permet de définir "ce qu'un objet fait" sans dire "comment il le fait". C'est un outil de design puissant qui garantit que deux classes différentes (ex: `Hero` et `NPC`) partagent la même interface minimale indispensable pour le reste du moteur de jeu.

### 2. La magie de `super()`
`super()` n'appelle pas seulement le parent direct ; il suit le **MRO** (Method Resolution Order). C'est essentiel pour éviter de dupliquer du code et pour s'assurer que l'état de l'objet est initialisé correctement de bas en haut.

### 3. Les Propriétés (`@property`)
Ce module introduit souvent l'idée de transformer des attributs en méthodes calculées. On peut lire `obj.attr` comme une variable, mais derrière, une fonction est appelée pour valider ou transformer la donnée.

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7aa2f7,100:bb9af7&height=120&section=footer" width="100%"/>
</div>
