import random

pee = False


class doge:
    def __init__(self,weight,teeth,breed):
        self.weight = weight
        self.teeth = teeth
        self.breed = breed
        
    def growteeth(self):
        self.teeth *= 2
    
    def becomebiggerdog(self):
        self.weight *= 2
        
    def transmute(self):
        self.breed = random.choice(["GIGA ", "UBER ", "SUPER ", "MEGA ", "ULTIMATE ", "DOOM ", "FINAL ", "type 4 instead of 1,2,3 "])+ self.breed.upper() #magic ai bug fix ??? idfk what "upper" does but it works somehow
    
    def pleasehelp(self):
        self.currentprint = ("weight: " + str(self.weight) + ", teeth: " + str(self.teeth) + ", breed: " + str(self.breed))
        print(self.currentprint)
        
puppy = doge(10,10,random.choice(["terrier", "great dane", "wolf", "poodle", "weiner", "former potus joe biden", "creature"]))
while pee == False:
    whattodoaboutnothing = int(input("Would you like to (1) feed, (2) mystery incantation, or (3) mystery potion your dog? All choice boxes must have a number reply or bad things happen."))
    if whattodoaboutnothing == 1:
        puppy.becomebiggerdog()
        puppy.pleasehelp()
    elif whattodoaboutnothing == 2:
        puppy.growteeth()
        puppy.pleasehelp()
    elif whattodoaboutnothing == 3:
        puppy.transmute()
        puppy.pleasehelp()
    elif whattodoaboutnothing == 4:
        print("You retreat from your ravenous " + str(puppy.breed) + " into a secluded corridor of the laboratory.")
        whattodoaboutnothing = int(input("It is right behind you. You reach a fork, do you go (1) left or (2) right?"))
        if whattodoaboutnothing == 1:
            whattodoaboutnothing = int(input("You stand in front of the locked exit door. It is locked by a 4 digit keypad. Enter the number?"))
            if whattodoaboutnothing == 3820:
                print("You manage to escape from your frankensteinian abomination into the wider world. Unfortunately, it also managed to get out.")
                print("At least you live to fight another day.")
                print("NEUTRAL ENDING")
                print("Final stats:")
                puppy.pleasehelp()
                pee = True
            else:
                print("You were horribly consumed by your puppy.")
                print("WRONG WAY ENDING")
                print("Final stats:")
                puppy.pleasehelp()
                pee = True
        if whattodoaboutnothing == 2:
            print("You are in a triangular arboreal garden. There are eight rows of didaffodills. Notably, all water is null.")
            whattodoaboutnothing = int(input("How do you evade puppy? (1) Hide behind one of the eight rows of (2) Make a run for it (3) Throw your entire potion reserve"))
            if whattodoaboutnothing == 1:
                print("It's not the best idea to hide from a creature which can smell a thousand times better than you.")
                print("You were horribly consumed by your puppy.")
                print("NOT A SCIENTIST ENDING")
                print("Final stats:")
                puppy.pleasehelp()
                pee = True
            if whattodoaboutnothing == 2:
                print("It's not the best idea to run at a creature a thousand times faster than you.")
                print("You were horribly consumed by your puppy.")
                print("WAY TOO BRAVE ENDING")
                print("Final stats:")
                puppy.pleasehelp()
                pee = True
            if whattodoaboutnothing == 3:
                print("You manage to throw your potions at the puppy and avoid it successfully. You are now in the room with the keypad.")
                whattodoaboutnothing = int(input("You stand in front of the locked exit door. It is locked by a 4 digit keypad. Enter the number?"))
                if whattodoaboutnothing == 3820:
                    print("You manage to escape from your frankensteinian abomination into the wider world. Just before it can escape, you close the door on it.")
                    print("You escape the building unharmed.")
                    print("GOOD ENDING")
                    print("Final stats:")
                    puppy.pleasehelp()
                    pee = True
                else:
                    print("You were horribly consumed by your puppy.")
                    print("UNOBSERVANT ENDING")
                    print("Final stats:")
                    puppy.pleasehelp()
                    pee = True
            elif pee == False:
                print("You were horribly consumed by your puppy.")
                print("DIDN'T CHOOSE ONE OF THE OPTIONS ENDING")
                print("Final stats:")
                puppy.pleasehelp()
                pee = True
        elif pee == False:
            print("You were horribly consumed by your puppy.")
            print("DIDN'T CHOOSE ONE OF THE OPTIONS ENDING")
            print("Final stats:")
            puppy.pleasehelp()
            pee = True
    elif pee == False:
        print("You grab some more (3) Mystery Potions [tm] from the shelf.")
print("The end.")
            
        
        
