
def	create_plant(name, height, age):
	print(name, end=": ")
	print(height, end="cm, ")
	print(age, end=" days old \n")

if __name__ == '__main__':
	print("=== Garder Plant Registry ===")
	create_plant("Rose", 25, 30)
	create_plant("Sunflower", 80, 45)
	create_plant("Cactus", 15, 120)
	