<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:bb9af7,100:7aa2f7&height=220&section=header&text=Module%2001%20:%20OOP%20Intro&fontSize=52&fontAlignY=38&fontColor=EDEDED&animation=fadeIn" width="100%"/>
</div>

# 🏛️ Module 01 : Introduction à la POO et aux Structures de Données

Ce module marque le passage d'une programmation procedurale simple à l'organisation de données sous forme d'objets. On y apprend à encapsuler des données et des comportements au sein de classes, tout en introduisant des concepts architecturaux comme le pattern Factory.

---

## 📂 Analyse des Exercices

### 🟢 ex0 : Garden Intro
**Fichier** : `ft_garden_intro.py`
- **Concept** : Définition d'une classe `Plant`.
- **Détails** : Apprentissage de la création d'attributs simples (nom, espèce) et d'une méthode d'affichage. C'est le premier contact avec l'état interne d'un objet.

### 🟢 ex1 : Garden Data
**Fichier** : `ft_garden_data.py`
- **Concept** : Registre d'objets.
- **Logique** : Utilisation de listes pour stocker plusieurs instances de plantes. On apprend ici à itérer sur une collection d'objets pour extraire des informations globales (ex: liste de tous les noms).

### 🟢 ex2 : Plant Growth
**Fichier** : `ft_plant_growth.py`
- **Concept** : Mutation d'état.
- **Logique** : Mise en place de méthodes `grow(height_increase)` et `age()`. L'objet n'est plus statique ; il évolue au fil du temps. Les méthodes modifient directement `self.height` et `self.age`.

### 🟢 ex3 : Plant Factory
**Fichier** : `ft_plant_factory.py`
- **Concept** : **Pattern Factory**.
- **Logique** : Création d'une fonction (ou classe) capable de générer des objets `Plant` à partir d'un dictionnaire ou de données brutes. Cela centralise la logique d'instanciation.

### 🟢 ex4 : Garden Security
**Fichier** : `ft_garden_security.py`
- **Concept** : Validation des données.
- **Logique** : Implémentation de gardes dans les méthodes pour empêcher des valeurs impossibles (ex: hauteur négative). C'est le début de la programmation défensive.

### 🟢 ex5 : Plant Types (Héritage)
**Fichier** : `ft_plant_types.py`
- **Concept** : **Héritage de base**.
- **Détails** : Création de classes filles `Flower`, `Tree` et `Vegetable` qui héritent de `Plant`. On explore comment spécialiser un comportement tout en réutilisant le code de la classe parente.

### 🟢 ex6 : Garden Analytics
**Fichier** : `ft_garden_analytics.py`
- **Concept** : Synthèse avancée.
- **Détails** : 
    - **Class Methods** (`@classmethod`) : Méthodes liées à la classe plutôt qu'à l'instance.
    - **Static Methods** (`@staticmethod`) : Fonctions utilitaires logées dans la classe.
    - **Nested Classes** : Utilisation d'une classe `GardenStats` à l'intérieur de la gestion du jardin pour isoler les calculs statistiques.

---

## 🧠 Notions Approfondies

### 1. L'Encapsulation
L'idée est de regrouper les données (attributs) et les traitements (méthodes) au sein d'une même entité. Cela permet de cacher la complexité interne et de ne présenter qu'une interface propre.

### 2. Le Pattern Factory (Introduction)
Le pattern Factory permet d'isoler la logique de création d'objets. Au lieu de faire `p = Plant()` partout, on utilise `factory.create_plant()`, ce qui facilite grandement la maintenance et l'évolution du code.

### 3. @classmethod vs @staticmethod
- **Classmethod** : Reçoit la classe (`cls`) en premier argument. Utile pour les constructeurs alternatifs.
- **Staticmethod** : Ne reçoit ni `self` ni `cls`. C'est juste une fonction "rangée" dans la classe par souci d'organisation.

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7aa2f7,100:bb9af7&height=120&section=footer" width="100%"/>
</div>
