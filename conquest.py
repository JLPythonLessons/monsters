import random
import json
from planets import Planet
from creatures import Creature

def display():
    print(f'\nInventory: {inventory}', f'\nHealth: {hp}', f'\nStrength: {strength}')

def enemy_display():
    print(f'\nName: {enemy}', f'\nHealth: {enemy_hp}', '\nStrength: 4')

def rand_bool():
    return random.choice([True, False])

def load_creatures():
    with open('creatures.json', 'r') as f:
        creatures_json = json.load(f)

    creatures = {}
    for name, stats in creatures_json.items():
        creatures[name] = Creature.from_json(stats)
    return creatures

def load_planets():
    with open('planets.json', 'r') as f:
        planets_json = json.load(f)

    planets = {}
    for name, stats  in planets_json.items():
        planets[name] = Planet.from_json(stats)
    return planets

# Start of the game
print("Welcome to Conquest!", "\nYour goal is to conquer every planet and establish peace.")
input("press enter to start the first battle...")
creatures = load_creatures()
planets = load_planets()

inventory = []
player = list(creatures).pop(random.randrange(len(creatures)))
enemy = random.choice(list((creatures.values())))

# print(f"The first battle is with a {enemy} on planet {planets} \n")
print(f"{enemy} has an hp of 50 and a strength of 4. Diminish its health to defeat it!")
print("\nThese are your stats: ")
display()

count = 0
while True:
    count += 1
    # Enemy turn
    if count % 2 == 0:
        print(f"{enemy} attacks you!")
        if rand_bool():
            hp -= 4
            print("{enemy}'s attack hit you!\n")
            display()
        else:
            print("{enemy}'s attack missed you!\n")
            display()
    # Player turn
    else:
        # Action prompt
        while True:  
            choice = input("\nIt's time to act!. Either attack or run away like a cooward. Type either \'attack\', or \'run\'. "
                           "\nYou will have to retype your input if you misspell it: ")
            # Check if the input is spelled correctly
            if choice in ['attack', 'run']:
                break
            # Create an error if it isn't spelled correctly
            print("\nYour input did not read as \"attack\" or \"run\".")

        # Check if it's attack
        if choice == "attack":
            if rand_bool():
                enemy_hp -= 10
                print(f"\nYour attack hit the {enemy}!") 
            else:
                print("\nYour attack missed! You stoopid.")
            enemy_display()
        # Check if it's run
        elif choice == "run":
            if rand_bool():
                print("\nYou ran away from your duty you cooward!")
                break
            else:
                print("\nYou failed to run away you cooward!")
                continue
        # Checks for victory or loss each round of turns
    if hp<=0 and enemy_hp>0:
        print("\nYou have lost! Return to the home you came from.")
        break
    elif hp>0 and enemy_hp<=0:
        print("\nYou have defeated your enemy and attained victory! Congratulations!")
        break
