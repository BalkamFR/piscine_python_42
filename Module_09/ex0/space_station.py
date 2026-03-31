from pydantic import BaseModel, Field
from datetime import datetime

class SpaceStation(BaseModel):
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
		space_station = SpaceStation(
				station_id="ISS001", 
				name="International Space Station", 
				crew_size=6, 
				oxygen_level=92.3, 
				power_level=85.5,
				last_maintenance = "2024-03-29T12:00:00"
			)
		print("Valid station created:")
		print(f"ID: {space_station.station_id}")
		print(f"Name: {space_station.name}")
		print(f"Crew: {space_station.crew_size} people")
		print(f"Power: {space_station.power_level}%")
		print(f"Oxygen: {space_station.oxygen_level}%")
		if space_station.is_operational == True:
			print("Status: Operational")
		else:
			print("Status: Not Operational")
	except Exception as e:
		print(e.errors()[0]['msg'])
	print("\n========================================")
	print("Expected validation error:")
	try:
		space_station = SpaceStation(
				station_id="ISS001", 
				name="International Space Station", 
				crew_size=21, 
				oxygen_level=92.3, 
				power_level=85.5,
				last_maintenance = "2024-03-29T12:00:00"
			)
		print("Valid station created:")
		print(f"ID: {space_station.station_id}")
		print(f"Name: {space_station.name}")
		print(f"Crew: {space_station.crew_size} people")
		print(f"Power: {space_station.power_level}%")
		print(f"Oxygen: {space_station.oxygen_level}%")
		if space_station.is_operational == True:
			print("Status: Operational")
		else:
			print("Status: Not Operational")
	except Exception as e:
		print(e.errors()[0]['msg'])

if __name__ == '__main__':
	main()