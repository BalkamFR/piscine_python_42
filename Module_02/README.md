<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:bb9af7,100:7aa2f7&height=220&section=header&text=Module%2002%20:%20Exceptions&fontSize=52&fontAlignY=38&fontColor=EDEDED&animation=fadeIn" width="100%"/>
</div>

# 🛡️ Module 02 : Gestion d'Erreurs et de Ressources

La robustesse est l'une des qualités les plus importantes d'un logiciel professionnel. Ce module enseigne comment anticiper, attraper et gérer proprement les situations imprévues (erreurs utilisateur, systèmes indisponibles) en utilisant le système d'exceptions de Python.

---

## 📂 Analyse des Exercices

### 🟡 ex0 : First Exception
**Fichier** : `ft_first_exception.py`
- **Concept** : Le bloc `try...except`.
- **Détails** : Apprendre à capturer une `ValueError` (souvent générée lors d'une conversion de type échouée de `input()`) pour éviter que le programme ne crash brutalement.

### 🟡 ex1 : Different Errors
**Fichier** : `ft_different_errors.py`
- **Concept** : Spécificité des erreurs.
- **Logique** : Gérer séparément plusieurs types d'erreurs dans un seul bloc : `ZeroDivisionError` (mathématiques), `FileNotFoundError` (I/O) et `KeyError` (dictionnaires). On apprend ici que l'ordre des `except` compte.

### 🟡 ex2 : Custom Errors
**Fichier** : `ft_custom_errors.py`
- **Concept** : Domaines d'erreurs personnalisés.
- **Logique** : Création d'une hiérarchie d'exceptions propres au projet : `GardenError` (Base), héritée par `PlantError` et `WaterError`. Cela permet d'être beaucoup plus précis dans les logs et le débogage.

### 🟡 ex3 : Finally Block
**Fichier** : `ft_finally_block.py`
- **Concept** : Nettoyage des ressources.
- **Logique** : Utilisation du mot-clé `finally`. Qu'une erreur survienne ou non, le code dans ce bloc sera exécuté. Crucial pour fermer des fichiers ou des connexions réseau (ex: couper la pompe à eau).

### 🟡 ex4 : Raise Errors
**Fichier** : `ft_raise_errors.py`
- **Concept** : Déclenchement manuel.
- **Logique** : Utilisation de `raise` pour forcer une erreur lorsque la logique métier est violée (ex: tenter d'arroser avec une quantité négative), même si Python n'aurait pas levé d'erreur technique.

### 🟡 ex5 : Garden Management
**Fichier** : `ft_garden_management.py`
- **Concept** : Synthèse et Validation Statique.
- **Détails** : Regroupement de méthodes de validation statiques au sein de la classe `GardenError`. Une approche centralisée pour vérifier l'état du jardin avant toute opération critique.

---

## 🧠 Notions Approfondies

### 1. Pourquoi des Custom Exceptions ?
Les exceptions standards (`ValueError`, `TypeError`) sont trop génériques. Créer une `WateringTimeoutError` indique immédiatement au développeur la nature exacte du problème sans avoir à analyser le message d'erreur.

### 2. Le flux d'une exception
Lorsqu'un `raise` survient, Python arrête l'exécution immédiate et cherche un bloc `except` correspondant dans la pile d'appels. Si rien n'est trouvé, le programme s'arrête. Le `finally` agit comme un filet de sécurité pour garantir la cohérence du système.

### 3. L'importance du typage dans les exceptions
En héritant de `Exception`, nos classes personnalisées bénéficient de toutes les fonctionnalités natives (backtraces, affichage du message).

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7aa2f7,100:bb9af7&height=120&section=footer" width="100%"/>
</div>
