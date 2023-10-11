import random

class Warrior:
    def __init__(self, name, health=100, armor_points=20, stamina_points=30):
        self.name = name
        self.health = health
        self.armor_points = armor_points
        self.stamina_points = stamina_points

    def attack(self, enemy):
        damage = random.randint(10, 30)
        self.stamina_points -= 10
        if self.stamina_points < 0:
            damage -= random.randint(0, 10)
        if damage < 0:
            damage = 0
        enemy.defend(self, damage)

    def defend(self, attacker, damage):
        if self.stamina_points > 0:
            self.stamina_points -= random.randint(0, 20)
            self.armor_points -= random.randint(0, 10)
            if self.armor_points < 0:
                self.health -= damage
            if self.health < 0:
                self.health = 0
            print(f"{self.name} защищается и имеет {self.health} здоровья и {self.armor_points} брони.")
        else:
            self.health -= damage
            if self.health < 0:
                self.health = 0
            print(f"{self.name} не может больше защищаться и имеет {self.health} здоровья.")

    def is_alive(self):
        return self.health > 10

def main():
    name1 = input("Введите имя первого воина: ")
    name2 = input("Введите имя второго воина: ")

    warrior1 = Warrior(name1)
    warrior2 = Warrior(name2)

    while warrior1.is_alive() and warrior2.is_alive():
        if random.choice([True, False]):
            warrior1.attack(warrior2)
        if random.choice([True, False]):
            warrior2.attack(warrior1)

    if warrior1.is_alive():
        print(f"{warrior1.name} одержал победу!")
    else:
        print(f"{warrior2.name} одержал победу!")

if __name__ == "__main__":
    main()

    import random


    class Warrior:
        def __init__(self, name, health=100):
            self.name = name
            self.health = health

        def attack(self, enemy):
            damage = 20
            print(f"{self.name} атакует {enemy.name} и наносит {damage} урона.")
            enemy.health -= damage

        def is_alive(self):
            return self.health > 0


    def main():
        warrior1 = Warrior("Воин 1")
        warrior2 = Warrior("Воин 2")

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



