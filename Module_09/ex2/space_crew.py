from pydantic import BaseModel, model_validator, Field
from datetime import datetime
from enum import Enum


class RankGrade(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: RankGrade
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(default_factory=datetime.now)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation_rules(self):
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        valide_crew: int = 0
        for crew in self.crew:
            if crew.rank == RankGrade.COMMANDER \
                    or crew.rank == RankGrade.CAPTAIN:
                valide_crew += 1
        if valide_crew == 0:
            raise ValueError("Must have at least one Commander or Captain")
        years_experience_total: int = 0
        for crew in self.crew:
            if crew.years_experience >= 5:
                years_experience_total += 1
            if not crew.is_active:
                raise ValueError("All crew members must be active")
        if years_experience_total < (
                len(self.crew) / 2) and self.duration_days > 365:
            raise ValueError(
                "Long missions (> 365 days) need 50%"
                "experienced crew (5+ years)")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        sarah_connor = CrewMember(
            member_id="ID_001",
            name="Sarah Connor",
            rank="commander",
            age=42,
            specialization="Mission Command",
            years_experience=20,
        )
        john_smith = CrewMember(
            member_id="ID_002",
            name="John Smith",
            rank="lieutenant",
            age=38,
            specialization="Navigation",
            years_experience=15,
        )
        alice_johnson = CrewMember(
            member_id="ID_001",
            name="Alice Johnson",
            rank="officer",
            age=28,
            specialization="Engineering",
            years_experience=10,
        )
        crew_list_mars: list = [sarah_connor, john_smith, alice_johnson]
    except Exception as e:
        print(e.errors()[0]['msg'])
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            duration_days=900,
            crew=crew_list_mars,
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for crew in mission.crew:
            print(f" - {crew.name} ({crew.rank.value}) - "
                  f"{crew.specialization}")
    except Exception as e:
        print(e.errors()[0]['msg'])
    print("\n=========================================")
    try:
        sarah_connor = CrewMember(
            member_id="ID_001",
            name="Sarah Connor",
            rank="cadet",
            age=18,
            specialization="Mission Command",
            years_experience=1,
        )
        john_smith = CrewMember(
            member_id="ID_002",
            name="John Smith",
            rank="lieutenant",
            age=38,
            specialization="Navigation",
            years_experience=15,
        )
        alice_johnson = CrewMember(
            member_id="ID_001",
            name="Alice Johnson",
            rank="officer",
            age=28,
            specialization="Engineering",
            years_experience=10,
        )
        crew_list_lune: list = [sarah_connor, john_smith, alice_johnson]
    except Exception as e:
        print("Expected validation error:")
        print(e.errors()[0]['msg'])
    try:
        mission = SpaceMission(
            mission_id="M2021_LUNE",
            mission_name="Lune Colony Establishment",
            destination="Lune",
            duration_days=2000,
            crew=crew_list_lune,
            budget_millions=5500.0
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for crew in mission.crew:
            print(f" - {crew.name} ({crew.rank.value}) - "
                  f"{crew.specialization}")
    except Exception as e:
        print("Expected validation error:")
        print(e.errors()[0]['msg'])


if __name__ == '__main__':
    main()
