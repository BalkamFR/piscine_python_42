# Module 07: DataDeck - Master the Art of Abstract Card Architecture

Ce module est une plongée profonde dans l'architecture orientée objet (POO) avancée en Python. Il explore l'utilisation des classes de base abstraites (ABC), de l'héritage multiple, des interfaces et des patterns de conception (Design Patterns) comme la **Factory** et la **Strategy**, tout en maintenant une rigueur de typage stricte avec **MyPy** et une conformité **Flake8**.

---

## 🛠️ Configuration Technique

- **Python 3.12+**
- **Type Hinting Strict** : Toutes les fonctions et méthodes sont typées. Les collections génériques (`list`, `dict`) sont paramétrées.
- **Linting** : Conformité totale avec `flake8` (PEP 8).
- **Statique Analysis** : `mypy --strict` pour garantir une sécurité de type maximale.

---

## 📂 Structure du Projet & Détails des Fichiers

### 🔵 Exercice 0 : Card Foundation (`ex0/`)
La base de toute l'architecture.

#### `Card.py`
- **Classe `Rarity(Enum)`** : Définit les niveaux de rareté (Common, Rare, etc.). Utiliser un `Enum` permet d'éviter les erreurs de frappe et de centraliser les constantes.
- **Classe `Card(ABC)`** : Classe de base abstraite.
    - `__init__` : Initialise le nom, le coût et la rareté.
    - `play(game_state)` : **Abstraite**. Forcer chaque type de carte à définir son propre comportement de jeu.
    - `get_card_info()` : Retourne un dictionnaire des métadonnées de la carte.
    - `is_playable(mana)` : Logique partagée pour vérifier si la carte est lançable.

#### `CreatureCard.py`
- **Classe `CreatureCard(Card)`** : Une carte représentant une unité avec `attack` et `health`.
    - `play()` : Implémentation concrète (la créature arrive sur le terrain).
    - `attack_target(target)` : Gère les combats de base entre créatures.

---

### 🟢 Exercice 1 : Deck Builder (`ex1/`)
Extension des types de cartes et gestion de collection.

#### `SpellCard.py`
- **Classe `SpellCard(Card)`** : Cartes à effet immédiat.
    - `resolve_effect(targets)` : Applique l'effet du sort sur une liste de cibles.

#### `ArtifactCard.py`
- **Classe `ArtifactCard(Card)`** : Objets permanents avec une `durability`.
    - `activate_ability()` : Utilise l'effet de l'artefact.

#### `Deck.py`
- **Classe `Deck`** : Un conteneur de cartes.
    - `add_card()` / `remove_card()` : Gestion dynamique.
    - `shuffle()` : Utilise `random.shuffle`.
    - `draw_card()` : Pioche une carte en s'assurant que le deck n'est pas vide.
    - `get_deck_stats()` : Calcule des statistiques (nombre par type, coût moyen).

---

### 🟡 Exercice 2 : Ability System (`ex2/`)
Utilisation de l'héritage multiple et des interfaces.

#### `Combatable.py` & `Magical.py`
- Ces fichiers définissent des **Interfaces Abstraites**. Elles ne contiennent pas de logique mais "promettent" que toute classe les implémentant aura des méthodes comme `attack()`, `defend()`, `cast_spell()`, etc.

#### `EliteCard.py`
- **Héritage Multiple** : `class EliteCard(Card, Combatable, Magical)`.
- C'est le fichier le plus complexe. Il combine les attributs d'une créature (via `Card`) et les capacités de combat et de magie.
- Il résout le problème des **Redéfinitions d'attributs** en annotant clairement les membres dans le constructeur.

---

### 🔴 Exercice 3 : Game Engine (`ex3/`)
Implémentation de patterns architecturaux.

#### `CardFactory.py` & `FantasyCardFactory.py`
- **Pattern Abstract Factory** : La `CardFactory` définit une interface pour créer des objets sans spécifier leurs classes concrètes. `FantasyCardFactory` est l'implémentation qui crée des créatures fantaisies, des sorts de feu, etc.

#### `GameStrategy.py` & `AggressiveStrategy.py`
- **Pattern Strategy** : Permet de changer l'algorithme "d'IA" de jeu dynamiquement. `AggressiveStrategy` priorise toujours les dégâts au joueur adverse.

#### `GameEngine.py`
- Coordonne tout le système en utilisant une `Factory` pour générer des cartes et une `Strategy` pour simuler des tours.

---

### 🟣 Exercice 4 : Tournament Platform (`ex4/`)
Synthèse finale.

#### `Rankable.py`
- Interface pour les objets ayant un classement (rating, wins, losses).

#### `TournamentCard.py`
- Combine `Card`, `Combatable` et `Rankable`. C'est une carte qui peut combattre et dont les performances sont suivies.

#### `TournamentPlatform.py`
- Gère les matchs entre les cartes, met à jour leurs scores (système de rating) et génère des classements (`get_leaderboard`).

---

## 🧠 Notions Complexes Expliquées

### 1. Classes de Base Abstraites (ABC)
En Python, une ABC empêche l'instanciation directe d'une classe. Si vous essayez de faire `c = Card()`, Python lèvera une erreur. Cela garantit que la logique "générique" n'est jamais utilisée seule ; on doit toujours passer par une implémentation concrète (`CreatureCard`).

### 2. Héritage Multiple & MRO
Python permet à une classe d'hériter de plusieurs parents. C'est puissant mais risqué (problème du diamant). Ici, nous l'utilisons pour créer des **Interfaces**. Une `EliteCard` "est une" Carte, "est" Combatable, et "est" Magique.

### 3. Pattern Abstract Factory
Au lieu de faire `c = CreatureCard(...)` partout dans votre code, vous demandez à une `Factory` de le faire : `factory.create_creature()`. Cela permet de changer tout le set de cartes du jeu (ex: passer de "Fantasy" à "Sci-Fi") sans modifier une seule ligne de logique dans le `GameEngine`.

### 4. Pattern Strategy
C'est le principe du "Brancher et Jouer" (Plug and Play) pour les algorithmes. Le `GameEngine` possède une stratégie. Il dit juste `strategy.execute_turn()`. Il ne sait pas si la stratégie est agressive, défensive ou aléatoire. Cela rend le code extrêmement modulaire et facile à tester.

---

## 🚀 Vérification du Projet

Pour vérifier que le code est propre et typé :

```bash
# Vérification du Linting
flake8 Module_07

# Vérification du Typage Strict
mypy --strict Module_07
```

Chaque exercice possède son propre fichier `main.py` pour tester les fonctionnalités localement.
