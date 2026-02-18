class Plant:
    def __init__(self, Name: str, Height: int, Age: int) -> None:
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
