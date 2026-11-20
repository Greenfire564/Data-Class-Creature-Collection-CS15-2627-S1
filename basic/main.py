from dataclasses import dataclass
@dataclass
class Creature:
    name: str
    species: str
    level: int
    health: float
creature1 = Creature("Name", "Dragon", 5, 100.0)
creature2 = Creature("Lead", "Fish", 2, 45.5)
creature3 = Creature("Raph", "Golem", 10, 250.0)
print("Starting Creatures")
print(f"Name: {creature1.name}, Species: {creature1.species}, Level: {creature1.level}, Health: {creature1.health}")
print(f"Name: {creature2.name}, Species: {creature2.species}, Level: {creature2.level}, Health: {creature2.health}")
print(f"Name: {creature3.name}, Species: {creature3.species}, Level: {creature3.level}, Health: {creature3.health}")
creature1.level = 6
creature1.health = 120.0
print("After Updating Name")
print(f"Name: {creature1.name}, Species: {creature1.species}, Level: {creature1.level}, Health: {creature1.health}")
print(f"Name: {creature2.name} Species: {creature1.species}, Level: {creature2.level}, Health: {creature2.health}")