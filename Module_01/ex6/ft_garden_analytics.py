class Plant:
    """Classe de base définissant les propriétés physiques d'une plante."""

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int):
        """
        Initialise la plante et valide sa création.
        name_plant (str): Identifiant de la plante.
        starting_height_plant (int): Taille de départ en cm.
        """
        self.__name_plant: str = name_plant
        self.__nbr_type_plant: int = + 1
        res = self.set_height(starting_height_plant)
        if (res == 0):
            self.__plant_create = 1
        else:
            self.__plant_create = 0

    def get_plant_create(self):
        """Indique si la plante a été créée avec succès."""
        return (self.__plant_create)

    def set_height(self, height_update: int) -> int:
        """
        Vérifie et définit la taille de la plante.
        height_update (int): Valeur de la taille à appliquer.
        """
        if (height_update < 0):
            self.__starting_height_plant = -1
            print(
                f"Invalid operation ({self.__name_plant})"
                f"attempted: height {height_update}cm")
            print("Security: Negative height [REJECTED]")
            return (1)
        else:
            self.__starting_height_plant = height_update
            return (0)

    def get_height(self) -> int:
        """Récupère la taille actuelle de la plante."""
        return (self.__starting_height_plant)

    def grow_plant(self, size_grow: int):
        """
        Augmente la taille de la plante.
        size_grow (int): Valeur de croissance ajoutée.
        """
        self.__starting_height_plant = self.__starting_height_plant + size_grow

    def get_name(self) -> str:
        """Récupère le nom de la plante."""
        return (self.__name_plant)

    def print_data_plant(self) -> None:
        print(f" - {self.get_name()}: {self.__starting_height_plant}cm")

    def get_type_and_nbr_plant(self):
        """Retourne la classification de la plante."""
        return (f"{self.__nbr_type_plant} regular")


class FloweringPlant(Plant):
    """Extension de Plant ajoutant des attributs de floraison."""

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            color_plant: str,
            blooming_plant: str):
        """
        Initialise une plante à fleurs.
        name_plant (str): Nom de la plante.
        starting_height_plant (int): Taille initiale.
        color_plant (str): Couleur des fleurs.
        blooming_plant (str): État de floraison.
        """
        super().__init__(name_plant, starting_height_plant)
        self.__color_plant = color_plant
        self.__blooming_plant = blooming_plant
        self.__nbr_type_plant: int = + 1

    def get_color_plant(self) -> str:
        """Récupère la couleur de la plante."""
        return (self.__color_plant)

    def get_blooming_plant(self) -> str:
        """Récupère l'état de floraison."""
        return (self.__blooming_plant)

    def print_data_plant(self) -> str:
        print(f" - {self.get_name()}: {self.get_height()}cm "
              f"{self.get_color_plant()} ({self.get_blooming_plant()})")

    def get_type_and_nbr_plant(self):
        """Retourne la classification comme plante à fleurs."""
        return (f"{self.__nbr_type_plant} flowering")


class PrizeFlower(FloweringPlant):
    """Plante de compétition possédant un score de prix."""

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            color_plant: str,
            blooming_plant: str,
            prize_plant: int):
        """
        Initialise une fleur de prix.
        name_plant (str): Nom de la plante.
        starting_height_plant (int): Taille initiale.
        color_plant (str): Couleur.
        blooming_plant (str): État de floraison.
        prize_plant (int): Points de prix attribués.
        """
        super().__init__(
            name_plant,
            starting_height_plant,
            color_plant,
            blooming_plant)
        if prize_plant < 0:
            self.__prize_plant = 0
        else:
            self.__prize_plant = prize_plant
        self.__nbr_type_plant: int = + 1

    def print_data_plant(self) -> str:
        print(f" - {self.get_name()}: {self.get_height()}cm "
              f"{self.get_color_plant()} flowers "
              f"({self.get_blooming_plant()}),  "
              f"Prize points: {self.__prize_plant}")

    def get_type_and_nbr_plant(self):
        """Retourne la classification comme fleur de prix."""
        return (f"{self.__nbr_type_plant} prize flowers")


class GardenManager:
    """Gestionnaire principal des jardins et de leur population."""
    all_plant_bad: list = []

    def __init__(self, name_garden_add: str):
        """
        Initialise un nouveau jardin.
        name_garden_add (str): Nom du jardin.
        """
        self.name_garden = name_garden_add
        self.__score_garden = 0
        self.all_plants = []
        self.total_grow = 0
        self.GardenStats.all_garden.append(self)

    def add_plants_garden(self, name_plant: list):
        """
        Ajoute une plante au jardin après vérification.
        name_plant (Plant): Objet plante à intégrer.
        """
        if name_plant.get_plant_create() == 1:
            self.all_plants.append(name_plant)
        else:
            self.all_plant_bad.append(name_plant)
        self.__score_garden += 10
        if name_plant.get_plant_create() == 1:
            print(
                f"Added {name_plant.get_name()} to {self.name_garden} garden")

    def grow_all_plant(self, size_grow: int):
        """
        Applique une croissance uniforme à toutes les plantes.
        size_grow (int): Valeur de croissance en cm.
        """
        print(f"\n{self.name_garden} is helping all plants grow...")
        for plant in self.all_plants:
            print(f"{plant.get_name()} grew {size_grow}cm")
            self.total_grow = size_grow + self.total_grow
            plant.grow_plant(size_grow)

    def getname(self):
        """Récupère le nom du responsable ou du jardin."""
        return (self.name_garden)

    def getscore(self):
        """Récupère le score de gestion du jardin."""
        return (self.__score_garden)

    def getnamegarden(self):
        """Récupère le nom du jardin."""
        return (self.name_garden)

    def print_all(self):
        print()
        print(f"=== {self.name_garden} Garden Report ===")
        print("Plants in garden:")
        self.GardenStats.print_all_plants(self)
        print()
        self.GardenStats.print_stats(self)
        print("\n")

    @classmethod
    def validation_test(cls):
        """Vérifie si des erreurs de validation de taille ont eu lieu."""
        if len(cls.all_plant_bad) == 0:
            print("Height validation test: True")
        else:
            print("Height validation test: False")

    @staticmethod
    def print_text_demo():
        print("\n=== Garden Management System Demo ===\n")

    class GardenStats:
        """Classe interne pour le calcul et l'affichage des statistiques."""
        all_garden: list = []

        def print_all_plants(self):
            for plant in self.all_plants:
                plant.print_data_plant()

        def print_stats(self):
            print(
                f"Plants added: {len(self.all_plants)}, "
                f"Total growth: {self.total_grow}cm")
            print("Plant types: ", end='')
            for plant in self.all_plants:
                print(plant.get_type_and_nbr_plant(), end=', ')

        def print_report(self):
            print()
            print(f"=== {self.name_garden} Garden Report ===")
            print("Plants in garden:")
            self.print_all_plants()
            print()
            self.print_stats()
            print("\n")

        @classmethod
        def garden_scores(cls):
            print("Garden scores - ", end='')
            for user in cls.all_garden:
                print(f"{user.getname()}: {user.getscore()}", end=', ')
            print()

        @classmethod
        def total_gardens(cls):
            print(f"Total gardens managed: {len(cls.all_garden)}")


if __name__ == '__main__':
    oak = Plant("Oak tree", 100)
    rose = FloweringPlant("Rose", 25, "red", "blooming")
    Sunflower = PrizeFlower("Sunflower", 50, "yellow", "blooming", 10)
    GardenManager.print_text_demo()
    alice = GardenManager("Alice")
    bob = GardenManager("bob")
    alice.add_plants_garden(oak)
    alice.add_plants_garden(rose)
    alice.add_plants_garden(Sunflower)
    bob.add_plants_garden(Sunflower)
    alice.grow_all_plant(1)
    alice.print_all()
    GardenManager.validation_test()
    GardenManager.GardenStats.garden_scores()
    GardenManager.GardenStats.total_gardens()
