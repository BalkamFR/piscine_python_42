def ft_count_harvest_recursive(n):
	if n > 0:
		nbr = ft_count_harvest_recursive(n - 1)
		print(f"Day {nbr}")
	else:
		nbr = 0
	return nbr + 1


def ft_print_harvest_recursive() -> None:
	days: int = int(input("Days until harvest: "))
	ft_count_harvest_recursive(days)
	print("Harvest time!")


ft_print_harvest_recursive()

