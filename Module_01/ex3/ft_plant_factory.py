class Plant:
    """Modèle représentant le cycle de vie et la croissance d'une plante."""

    def __init__(
            self,
            name_plant: str,
            starting_height_plant: int,
            starting_age_plant: int):
        """
        Initialise une nouvelle instance de plante.
        name_plant (str): Nom de l'espèce.
        starting_height_plant (int): Taille initiale en cm.
        starting_age_plant (int): Âge initial en jours.
        day_plant (int): Jour actuel de suivi.
        """
        self.name_plant: str = name_plant
        self.starting_height_plant: int = starting_height_plant
        self.starting_age_plant: int = starting_age_plant
        self.day_plant: int = 1
        print(
            f"Created: {name_plant} ({starting_height_plant}cm,"
            f"{starting_age_plant}"
            " days)")

    def age(self) -> None:
        """Incrémente l'âge global et le compteur de jours."""
        self.starting_age_plant += 1
        self.day_plant += 1

    def grow(self) -> None:
        """Augmente la taille de la plante de 1cm."""
        self.starting_height_plant += 1

    def get_info(self):
        """Retourne les informations de la plante sous forme de texte."""
        return (f"{self.name_plant}: {self.starting_height_plant}cm,"
                f"{self.starting_age_plant} days old")

    def print_data_plant(self):
        print(f"{self.name_plant}: {self.starting_height_plant}cm, "
              f"{self.starting_age_plant} days old")


if __name__ == '__main__':
    print("=== Plant Factory Output ===")
    plants_list = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]

    plant_obj_list = []
    for data in plants_list:
        plant_obj_list.append(Plant(*data))

    print(f"\nTotal plants created: {len(plant_obj_list)}")
