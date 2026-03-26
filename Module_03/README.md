<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:bb9af7,100:7aa2f7&height=220&section=header&text=Module%2003%20:%20Data%20Quest&fontSize=52&fontAlignY=38&fontColor=EDEDED&animation=fadeIn" width="100%"/>
</div>

# 💎 Module 03 : Data Quest - Maîtrise des Collections

Ce module explore les structures de données intégrées de Python au-delà des bases. L'accent est mis sur l'efficacité mémoire (Générateurs) et la concision du code (Compréhensions), tout en manipulant des structures variées comme les Tuples, les Sets et les Dictionnaires complexes.

---

## 📂 Analyse des Exercices

### 🔴 ex0 : Command Quest
**Fichier** : `S0E0.py`
- **Concept** : Gestion avancée de la ligne de commande.
- **Détails** : Structuration d'un script capable de réagir à différents drapeaux (flags) et arguments de manière robuste.

### 🔴 ex1 : Score Cruncher
**Fichier** : `ex1_logic.py` (ou équivalent)
- **Concept** : Analyse de listes.
- **Logique** : Transformation et agrégation de données numériques. Utilisation de fonctions comme `sum()`, `min()`, `max()` et calculs de moyennes.

### 🔴 ex2 : Position Tracker
**Fichier** : `ex2_logic.py`
- **Concept** : Immuabilité avec les **Tuples**.
- **Logique** : Utilisation de tuples pour représenter des coordonnées XYZ. L'immuabilité garantit qu'une position enregistrée ne sera pas modifiée accidentellement par une autre partie du programme.

### 🔴 ex3 : Achievement Hunter
**Fichier** : `ex3_logic.py`
- **Concept** : Unicité avec les **Sets**.
- **Logique** : Suivi de succès ou d'identifiants uniques. Les sets permettent des opérations d'intersection et de différence extrêmement rapides par rapport aux listes.

### 🔴 ex4 : Inventory Master
**Fichier** : `ex4_logic.py`
- **Concept** : **Dictionnaires imbriqués**.
- **Logique** : Gestion d'un inventaire complexe où chaque clé pointe vers un autre dictionnaire. Apprentissage de la navigation profonde dans les données.

### 🔴 ex5 : Stream Wizard
**Fichier** : `ex5_logic.py`
- **Concept** : **Générateurs (`yield`)**.
- **Logique** : Création de fonctions qui retournent des itérateurs. Cela permet de traiter des flux de données potentiellement infinis sans charger l'intégralité du contenu en mémoire RAM.

### 🔴 ex6 : Data Alchemist
**Fichier** : `ex6_logic.py`
- **Concept** : **Compréhensions**.
- **Logique** : Rédaction de transformations de données complexes en une seule ligne élégante (List/Dict comprehensions). C'est le summum de l'écriture "Pythonique".

---

## 🧠 Notions Approfondies

### 1. Pourquoi utiliser des Générateurs ?
Contrairement à une liste qui stocke tout d'un coup, un générateur calcule la valeur suivante seulement quand on la lui demande. C'est la différence entre lire un livre entier d'un coup ou lire une page à la fois. C'est vital pour le Big Data.

### 2. Sets et Hash Tables
Les sets utilisent une table de hachage interne, ce qui rend la vérification d'appartenance (`if x in my_set`) instantanée ($O(1)$), peu importe la taille de l'ensemble. Dans une liste, c'est proportionnel à sa taille ($O(n)$).

### 3. La puissance des List Comprehensions
Elles ne sont pas seulement esthétiques ; elles sont souvent légèrement plus rapides que les boucles `for` classiques car elles sont optimisées au niveau de l'interpréteur CPython.

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7aa2f7,100:bb9af7&height=120&section=footer" width="100%"/>
</div>
