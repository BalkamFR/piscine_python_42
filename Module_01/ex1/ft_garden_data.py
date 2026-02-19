class Plant:
    """Représente une plante et ses données de croissance."""

    def __init__(self, Name: str, Height: int, Age: int) -> None:
        """
        Initialise la plante.
        Name (str): Nom de la plante.
        Height (int): Taille en centimètres.
        Age (int): Âge en jours.
        """
        self.Name = Name
        self.Height = Height
        self.Age = Age

    def print_data(self) -> None:
        print(f"{self.Name}: {self.Height}cm, {self.Age} days old")


if __name__ == '__main__':
    Rose = Plant("Rose", 25, 30)
    Sunflower = Plant("Sunflower", 80, 45)
    Cactus = Plant("Cactus", 15, 120)

    list_all_plant = [Rose, Sunflower, Cactus]

    print("=== Garden Plant Registry ===")
    for plant in list_all_plant:
        plant.print_data()
