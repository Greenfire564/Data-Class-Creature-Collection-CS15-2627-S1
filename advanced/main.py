from dataclasses import dataclass

@dataclass
class Creature:
    name: str
    species: str
    level: int
    health: float

c1, c2, c3 = Creature("Name", "Raph", 5, 100.0), Creature("Lead", "Fish", 2, 45.5), Creature("Raph", "Golem", 10, 250.0)

for c in (c1, c2, c3):
    print(f"Name: {c.name}, Species: {c.species}, Level: {c.level}, Health: {c.health}")


c1.level, c1.health = 6, 120.0
print(f"Updated Raph: Name: {c1.name}, Species: {c1.species}, Level: {c1.level}, Health: {c1.health}")

name, species = input("Name: "), input("Species: ")

while True:
    try:
        level = int(input("Level: "))
        break
    except ValueError: print("Enter a valid #.")

while True:
    try:
        health = float(input("Health: "))
        break
    except ValueError: print("Enter a valid number.")

user = Creature(name, species, level, health)
print(f"Created: Name: {user.name}, Species: {user.species}, Level: {user.level}, Health: {user.health}")