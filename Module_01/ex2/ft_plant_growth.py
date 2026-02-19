class Plant:
    """Gère la croissance et le suivi d'une plante."""

    def __init__(
            self,
            name_plant: str,
            height_plant: int,
            age_plant: int) -> None:
        """
        Initialise les attributs de la plante.
        name_plant (str): Nom de l'espèce.
        height_plant (int): Taille actuelle en cm.
        age_plant (int): Âge total en jours.
        day_plant (int): Compteur de jours de simulation.
        """
        self.name_plant: str = name_plant
        self.height_plant: int = height_plant
        self.age_plant: int = age_plant
        self.day_plant: int = 1

    def age(self) -> None:
        """Incrémente l'âge global et le jour actuel."""
        self.age_plant += 1
        self.day_plant += 1

    def grow(self) -> None:
        """Augmente la taille de la plante de 1cm."""
        self.height_plant += 1

    def get_info(self) -> str:
        """Retourne les informations formatées de la plante."""
        return (f"{self.name_plant}: {self.height_plant}cm, {self.age_plant} "
                "days old")

    def print_days(self) -> None:
        print(f"=== Day {self.day_plant} ===")

    def print_data_plant(self) -> None:
        print(f"{self.name_plant}: {self.height_plant}cm, {self.age_plant} "
              "days old")

    def simulator_age(self, age_more: int) -> None:
        """
        Simule la croissance sur une période donnée.
        age_more (int): Nombre de jours à simuler.
        """
        self.print_days()
        self.print_data_plant()
        i = 0
        while (i < age_more):
            self.age()
            self.grow()
            i += 1
        self.print_days()
        self.print_data_plant()
        print(f"Growth this week: +{age_more}cm")


if __name__ == '__main__':
    rose: Plant = Plant("rose", 25, 30)
    rose.simulator_age(6)
