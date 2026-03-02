import sys


class Inventory:
    def __init__(self) -> None:
        self.all_items: dict = convert_tab_to_dict()

    def __repr__(self):
        return (f"{self.all_items}")

    def all_item_calc(self):
        res: int = 0
        for key, value in self.all_items.items():
            res = int(value) + res
        return res

    def iventory_analysis(self) -> None:
        print("=== Inventory System Analysis ===")
        print(f"Total items in inventory: {self.all_item_calc()}")
        print(f"Unique item types: {len(self.all_items)}\n")

    def current_inventory(self) -> None:
        nbr_all_item = self.all_item_calc()
        value_pourcent: int = 0
        all_items_sorted: list
        all_items_sorted = sorted(
            self.all_items.items(),
            key=lambda item: item[1],
            reverse=True)
        for key, value in all_items_sorted:
            value_pourcent = round(((int(value) / nbr_all_item) * 100), 2)
            print(f"{key}: {value} units ({value_pourcent}%)")
        print()

    def inventory_statistics(self) -> None:
        print("=== Inventory Statistics ===")
        max = sorted(
            self.all_items.items(),
            key=lambda item: item[1],
            reverse=True)
        min = sorted(self.all_items.items(), key=lambda item: item[1],)
        print(f"Most abundant: potion ({max[0][1]} units)")
        print(f"Least abundant: sword ({min[0][1]} unit)\n")

    def item_categories(self) -> None:
        print("=== Item Categories ===")
        moderate: dict = {}
        scare: dict = {}
        for key, value in self.all_items.items():
            if int(value) >= 5:
                moderate.update({key: value})
            else:
                scare.update({key: value})
        print(f"Moderate: {moderate}")
        print(f"Scare: {scare}\n")

    def management_suggestions(self) -> None:
        print("=== Management Suggestions ===")
        print("Restock needed:", end=' ')
        for key, value in self.all_items.items():
            if int(value) == 1:
                print(key, end=', ')
        print("\n")

    def dictionary_properties_demo(self) -> None:
        print("=== Dictionary Properties Demo ===")
        print("Dictionary keys: ", end=' ')
        for key in self.all_items.keys():
            print(key, end=', ')
        print("\nDictionary values: ", end=' ')
        for value in self.all_items.values():
            print(value, end=', ')
        sword = self.all_items.get("sword")
        if sword is None:
            print(f"\nSample lookup - 'sword'in inventory: {sword}")
        else:
            print("\nSample lookup - 'sword'in inventory: True")


def convert_tab_to_dict():
    all_items_dict = {}
    list_brut: list = []
    n = len(sys.argv)
    i: int = 1
    while i < n:
        list_brut.append(sys.argv[i])
        i += 1
    for item in list_brut:
        try:
            item_split = item.split(':')
            all_items_dict.update({item_split[0]: int(item_split[1])})
        except BaseException:
            print("Please add good format")
            all_items_dict.clear()
            return {}
    return all_items_dict


def main() -> None:
    if len(sys.argv) > 1:
        players: Inventory = Inventory()
        if len(players.all_items) != 0:
            players.iventory_analysis()
            players.current_inventory()
            players.inventory_statistics()
            players.item_categories()
            players.management_suggestions()
            players.dictionary_properties_demo()
    else:
        print("argument missing")


if __name__ == '__main__':
    main()
