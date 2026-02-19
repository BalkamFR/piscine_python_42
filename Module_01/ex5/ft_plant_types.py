class Plant:
    """Classe de base pour la gestion générique d'une plante."""

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int) -> None:
        """
        Initialise et valide les données de base.
        name_plant (str): Nom de l'espèce.
        starting_height_plant (int): Taille initiale.
        starting_age_plant (int): Âge initial.
        """
        res = self.set_height(starting_height_plant)
        if (res == 1):
            return
        res = self.set_age(starting_age_plant)
        if (res == 1):
            return
        self.__name_plant: str = name_plant
        self.__type_plant: str = "Not define"

    def set_height(self, height_update: int) -> int:
        """
        Définit la taille avec contrôle de validité.
        height_update (int): Nouvelle taille en cm.
        """
        if (height_update < 0):
            self.__starting_height_plant: int = -1
            print(f"Invalid operation attempted: height {height_update}cm"
                  "[REJECTED]")
            print("Security: Negative height rejected")
            return (1)
        else:
            self.__starting_height_plant: int = height_update
            return (0)

    def set_age(self, age_update: int) -> int:
        """
        Définit l'âge avec contrôle de validité.
        age_update (int): Nouvel âge en jours.
        """
        if (age_update < 0):
            self.__starting_age_plant: int = -1
            print(
                f"Invalid operation attempted: age {age_update}cm [REJECTED]")
            print("Security: Negative age rejected")
            return (1)
        else:
            self.__starting_age_plant: int = age_update
            return (0)

    def get_height(self) -> int:
        """Récupère la taille actuelle."""
        return (self.__starting_height_plant)

    def get_age(self) -> int:
        """Récupère l'âge actuel."""
        return (self.__starting_age_plant)

    def get_name(self) -> str:
        """Récupère le nom de la plante."""
        return (self.__name_plant)

    def __repr__(self) -> str:
        """Retourne la représentation textuelle de l'objet."""
        return (f"{self.__name_plant} ({self.__class__.__name__}): "
                f"{self.__starting_height_plant}cm,"
                f" {self.__starting_age_plant} day")


class Flower(Plant):
    """Représente une plante produisant des fleurs."""

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int,
            color_plant: str) -> None:
        """
        Initialise une fleur avec sa couleur.
        name_plant (str): Nom de la fleur.
        starting_height_plant (int): Taille initiale.
        starting_age_plant (int): Âge initial.
        color_plant (str): Couleur des pétales.
        """
        super().__init__(name_plant, starting_height_plant, starting_age_plant)
        self.bloom("beautifully")
        self.__color: str = color_plant

    def bloom(self, bloom_flower: str) -> None:
        """
        Définit l'état de floraison.
        bloom_flower (str): Description de la floraison.
        """
        self.__bloom_flower: str = bloom_flower

    def __repr__(self) -> str:
        """Retourne les détails de la fleur et sa floraison."""
        return (f"{self.get_name()} ({self.__class__.__name__}): "
                f"{self.get_height()}cm,"
                f" {self.get_age()} days,"
                f" {self.__color} color"
                f"\n{self.get_name()} is blooming {self.__bloom_flower}")


class Tree(Plant):
    """Représente un arbre avec des propriétés."""

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int) -> None:
        """
        Initialise un arbre et calcule son diamètre.
        name_plant (str): Nom de l'arbre.
        starting_height_plant (int): Taille initiale.
        starting_age_plant (int): Âge initial.
        """
        super().__init__(name_plant, starting_height_plant, starting_age_plant)
        self.__trunk_diameter: int = starting_height_plant / 10
        self.produce_shade(self.__trunk_diameter * 1.55)

    def produce_shade(self, shade_tree: int) -> None:
        """
        Calcule la surface d'ombre.
        shade_tree (int): Valeur brute de l'ombre.
        """
        self.__produce_shade: int = "%.0f" % shade_tree

    def __repr__(self) -> str:
        """Retourne les détails de l'arbre et son ombrage."""
        return (
            f"{self.get_name()} ({self.__class__.__name__}): "
            f"{self.get_height()}cm, "
            f"{self.get_age()} days, "
            f"{self.__trunk_diameter}cm diameter"
            f"\n{self.get_name()} provide {self.__produce_shade}"
            " square meters of shade")


class Vegetable(Plant):
    """Représente une plante potagère."""

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int,
            harves_plant: str,
            nutritional_plant: str) -> None:
        """
        Initialise un légume avec ses propriétés nutritives.
        name_plant (str): Nom du légume.
        starting_height_plant (int): Taille initiale.
        starting_age_plant (int): Âge initial.
        harves_plant (str): Saison de récolte.
        nutritional_plant (str): Apport nutritionnel principal.
        """
        super().__init__(name_plant, starting_height_plant, starting_age_plant)
        self.__harvest_season: str = harves_plant
        self.__nutritional_value: str = nutritional_plant

    def __repr__(self) -> str:
        """Retourne les détails du légume et ses nutriments."""
        return (f"{self.get_name()} ({self.__class__.__name__}): "
                f"{self.get_height()}cm,"
                f" {self.get_age()} days,"
                f" {self.__harvest_season} harvest"
                f"\n{self.get_name()} is rich {self.__nutritional_value}")


if __name__ == '__main__':
    print("=== Garden Plant Types ===")
    Rose: Flower = Flower("Rose", 25, 30, "red")
    Tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    Oak: Tree = Tree("Oak", 500, 1825)
    print("")
    print(Rose)
    print("")
    print(Oak)
    print("")
    print(Tomato)
