import random


class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def attack(self, enemy):
        damage = random.randint(10,20)
        print(f"{self.name} атакует {enemy.name} и наносит {damage} урона.")
        enemy.health -= damage

    def is_alive(self):
        return self.health > 0


def main():
    warrior1 = Warrior("Воин Змей")
    warrior2 = Warrior("Воин Илья")

    while warrior1.is_alive() and warrior2.is_alive():
        attacker = random.choice([warrior1, warrior2])
        enemy = warrior2 if attacker == warrior1 else warrior1
        attacker.attack(enemy)
        print(f"{enemy.name} имеет {enemy.health} здоровья.")

    if warrior1.is_alive():
        print(f"{warrior1.name} одержал победу!")
    else:
        print(f"{warrior2.name} одержал победу!")


if __name__ == "__main__":
    main()

