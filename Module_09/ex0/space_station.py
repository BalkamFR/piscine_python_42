from pydantic import BaseModel, model_validator, Field
from datetime import datetime

class UserProfile(BaseModel):
	station_id: str = Field(min_length=3, max_length=10)
	name: str = Field(min_length=1, max_length=50)
	crew_size: int = Field(ge=1 , le=20)
	oxygen_level: float = Field(ge=0.0, le=100.0)
	power_level: float = Field(ge=0.0, le=100.0)
	last_maintenance : datetime 
	is_operational: bool = True
	notes: str = Field(None, max_length=200)


def main() -> None:
	print("Space Station Data Validation")
	print("========================================")
	try:
		user = UserProfile(
				station_id="ISS001", 
				name="International Space Station", 
				crew_size=6, 
				oxygen_level=92.3, 
				power_level=85.5,
				last_maintenance = "2024-03-29T12:00:00"
			)
		print("Valid station created:")
		print(f"ID: {user.station_id}")
		print(f"Name: {user.name}")
		print(f"Crew: {user.crew_size} people")
		print(f"Power: {user.power_level}%")
		print(f"Oxygen: {user.oxygen_level}%")
		if user.is_operational == True:
			print("Status: Operational")
		else:
			print("Status: Not Operational")

	except Exception as e:
		print(e)
	print("========================================")
	print("Expected validation error:")
	try:
		user = UserProfile(
				station_id="ISS001", 
				name="International Space Station", 
				crew_size=21, 
				oxygen_level=92.3, 
				power_level=85.5,
				last_maintenance = "2024-03-29T12:00:00"
			)
		print("Valid station created:")
		print(f"ID: {user.station_id}")
		print(f"Name: {user.name}")
		print(f"Crew: {user.crew_size} people")
		print(f"Power: {user.power_level}%")
		print(f"Oxygen: {user.oxygen_level}%")
		if user.is_operational == True:
			print("Status: Operational")
		else:
			print("Status: Not Operational")

	except Exception as e:
		print(e.errors()[0]['msg'])

if __name__ == '__main__':
	main()