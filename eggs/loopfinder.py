import random
level = 1
health = 18 + (4 * level)
enemyhealth = 10 * level
enemy = random.choice(["goblin","dwarf","spider","zombie","human","wizard"])
while True:
    print("You are fighting a " + str(enemy) + " with " + str(enemyhealth) + " health. You have " + str(health) + " health.")
    action = int(input("What would you like to do? 0: Heal  1: Attack  2: Cast a Spell"))
    if action == 0:
        if health < (20 + (2 * level)):
            health = health + level
            print("You healed, healing " + str(2 * level) + " damage.")
        else:
            print("You were already at full health!")
    elif action == 1:
        damage = random.randint(1,2) + random.randint(0, level)
        enemyhealth = enemyhealth - damage
        print("You attacked, dealing " + str(damage) + " damage.")
    else:
        if random.randint(0,2) > 0:
            spell = random.choice(["ice bolt","fire bolt","death ray","explosion","chaos field"])
            damage = random.randint(0,3 * level)
            enemyhealth = enemyhealth - damage
            print("You cast " + spell + ", dealing " + str(damage) + " damage.")
        else:
            print("Your spell failed!")
    if enemyhealth > 0:
        damage = random.randint(1,level * 2)
        health = health - damage
        print("The enemy attacked, dealing " + str(damage) + " damage.")
    if enemyhealth <= 0 and health > 0:
        print("You defeated the " + str(enemy) + " and gained " + str(random.randint(level,level * level)) + " experience, which let you level up!")
        level = level + 1
        health = 20 + (2 * level)
        enemyhealth = 10 * level
    elif health <= 0:
        print("You died at level " + str(level) + ".")
            
            




