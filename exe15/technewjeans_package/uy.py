#Uy module
import os
import time

class Game:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, other_character):
        other_character.health -= self.power
        print("===================================")
        print(f"{self.name} attacks {other_character.name} for "
                f"{self.power} damage.")
        print("===================================")

    def heal(self, amount):
        self.health += amount
        print("===============================================")
        print(f"{self.name} heals for {amount} points. Current health: "
                f"{self.health}.")
        print("===============================================")

    def defend(self):
        self.defending = True
        print("===================================")
        print(f"{self.name} is defending, reducing incoming damage by half.")
        print("===================================")

    def level_up(self):
        self.health += 20
        self.power += 5
        print("===================================")
        print(f"{self.name} levels up! New health: "
                f"{self.health}, New power: {self.power}.")
        print("===================================")

    def status(self):
        print("===============================")
        print(f"{self.name} - Health: {self.health}, Power: {self.power}")
        print("===============================")    

    def uy_menu():
        hero = Game("Hero", 100, 20)
        villain = Game("Villain", 80, 15)

        while True:
            os.system('cls')
            print("\n--- Game Menu ---")
            print("1. Hero or Villain attacks")
            print("2. Heal Hero or Villan")
            print("3. Hero or Villain defends")
            print("4. Hero levels up")
            print("5. Show Status")
            print("6. Quit/Back to Main Menu")
            choice = input("Choose an action (1-6): ")

            match choice:
                case "1":
                    os.system('cls')
                    attacker = input("Who attacks? (hero/villain): ").lower()
                    if attacker == "hero":
                        hero.attack(villain)
                    elif attacker == "villain":
                        villain.attack(hero)
                    else:
                        print("Invalid character choice." +
                        "Please select 'Hero' or 'Villain'.")
                    input("\nPress enter to continue.")
                case "2":
                    os.system('cls')
                    healer = input("Who heals? (hero/villain): ").lower()
                    heal_amount = int(input("Enter heal amount: "))
                    if healer == "hero":
                        hero.heal(heal_amount)
                    elif healer == "villain":
                        villain.heal(heal_amount)
                    else:
                        print("Invalid character choice." +
                        "Please select 'Hero' or 'Villain'.")
                    input("\nPress enter to continue.")
                case "3":
                    os.system('cls')
                    defender = input("Who defends? (hero/villain): ").lower()
                    if defender == "hero":
                        hero.defend()
                    elif defender == "villain":
                        villain.defend()
                    else:
                        print("Invalid character choice." +
                        "Please select 'Hero' or 'Villain'.")
                    input("\nPress enter to continue.")
                case "4":
                    os.system('cls')
                    hero.level_up()
                    input("\nPress enter to continue.")
                case "5":
                    os.system('cls')
                    hero.status()
                    villain.status()
                    input("\nPress enter to continue.")
                case "6":
                    print("Returning to Main Menu...")
                    time.sleep(2)
                    break
                case _:
                    print("Invalid choice, please select a valid option.")