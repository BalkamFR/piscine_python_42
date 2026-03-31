from pydantic import BaseModel, model_validator, Field
from datetime import datetime 
from enum import Enum

class ContactType(Enum):
	RADIO = "radio"
	VISUAL = "visual"
	PHYSICAL = "physical"
	TELEPATHIC = "telepathic"

class AlienContact(BaseModel):
	contact_id: str = Field(min_length=5, max_length=15)
	timestamp : datetime = datetime.now()
	location: str = Field(min_length=3, max_length=100)
	contact_type: ContactType
	signal_strength: float = Field(ge=0 , le=10)
	duration_minutes: int = Field(ge=1, le=1440)
	witness_count: int = Field(ge=1, le=100.0)
	message_received: str = Field(None, max_length=500)
	is_verified: bool = False

	@model_validator(mode='after')
	def contact_validator(self):
		if self.contact_id[0] != 'A' or \
		self.contact_id[1] != 'C':
			raise ValueError("Contact id not good format")
		if self.contact_type == ContactType.PHYSICAL \
			and self.is_verified is False:
			raise ValueError("Contact type is not good")
		return self
def main() -> None:
	print("Alien Contact Log Validation")
	print("======================================")
	try:
		print("Valid contact report:")
		alien = AlienContact(
			contact_id="AC_2024_001", 
			location="Area 51, Nevada", 
			contact_type= ContactType.RADIO, 
			signal_strength= 8.5,
			duration_minutes=45,
			witness_count = 5,
			message_received = "Greetings from Zeta Reticuli",
		)
		print(f"ID: {alien.contact_id}")
		print(f"Type: {alien.contact_type.value}")
		print(f"Location: {alien.location}")
		print(f"Signal: {alien.signal_strength}/10")
		print(f"Duration: {alien.duration_minutes} minutes")
		print(f"Witnesses: {alien.witness_count}")
		print(f"Message: '{alien.message_received}'")
		print(f"datatime: {alien.timestamp}")
	except Exception as e:
		print("Expected validation error:")
		print(e)
	print("\n======================================")
	try:
		print("Valid contact report:")
		alien = AlienContact(
			contact_id="AC_2024_001", 
			location="Area 51, Nevada", 
			contact_type= ContactType.PHYSICAL, 
			signal_strength= 8.5,
			duration_minutes=45,
			witness_count = 3,
			message_received = "Greetings from Zeta Reticuli",
		)
		print(f"ID: {alien.contact_id}")
		print(f"Type: {alien.contact_type.value}")
		print(f"Location: {alien.location}")
		print(f"Signal: {alien.signal_strength}/10")
		print(f"Duration: {alien.duration_minutes} minutes")
		print(f"Witnesses: {alien.witness_count}")
		print(f"Message: '{alien.message_received}'")
		print(f"datatime: {alien.timestamp}")
	except Exception as e:
		print("Expected validation error:")
		print(e.errors()[0]['msg'])

if __name__ == '__main__':
	main()
	