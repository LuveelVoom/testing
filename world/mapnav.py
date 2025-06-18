import random
current = random.randint(0,6)
city_names = [
    "Youngermoore",    # 0
    "Grimehold",     # 1
    "Snuffyreach",     # 2
    "Backthen",     # 3
    "Breadhollow",  # 4
    "Bashinriver",    # 5
    "Yellingwind"   # 6
]

map_edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [2, 3],
    [3, 4],
    [2, 5],
    [1, 5],
    [4, 6],
    [5, 4],
    [0, 5],
    [5, 6],
    [3, 5],
    [1, 6],
    [4, 2],
    [6, 0]
]

def start():
    array1 = [0,1,2,3,4,5,6]
    array1.remove(current)
    return random.choice(array1)

def getoutgoing(possibles):
    for x in range(0,len(map_edges)):
        if map_edges[x][0] == current:
            possibles.append(map_edges[x][1])
    return possibles

def travel():
    global current
    act,possibles = action()
    print(act,possibles) #
    if city_names.index(act) in possibles:
        current = city_names.index(act)
    elif act == "BACK":
        print("no stack :(")
        
        
        


def action():
    act = " "
    possibles = []
    getoutgoing(possibles)
    print("Your goal is to reach " + str(city_names[targ]) + ".")
    print("You are currently in " + city_names[current] + ". You can go to these cities: ")
    for y in range(0,len(possibles)):
        workingcity = possibles[y]
        print(city_names[workingcity])
    print("You can also go BACK.")
    act = input("Where would you like to go?")
    return act,possibles

        
        
targ = start()
while current != targ:
    travel()
    