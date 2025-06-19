import random
current = "null"
targ = "null"
city_names = [
    "Youngermoore",    # 0
    "Grimehold",     # 1
    "Snuffyreach",     # 2
    "Backthen",     # 3
    "Breadhollow",  # 4
    "Bashinriver",    # 5
    "Yellingwind"   # 6
]
backstack = [] ### This name tells us nothing about its use. 

map_edges = [
    [0, {"mname": "Globlin",         "mhp": -10}, 1],
    [0, {"mname": "Spider Teen",   "mhp": 20}, 2],
    [1, {"mname": "Orc Route",      "mhp": 25}, 3],
    [2, {"mname": "Mraith",         "mhp": 30}, 3],
    [3, {"mname": "Internet Troll",   "mhp": 4000}, 4],
    [2, {"mname": "Gnat Swarm",      "mhp": random.randint(0,100)}, 5],
    [1, {"mname": "Fire Ache",     "mhp": 22}, 5],
    [4, {"mname": "Copromancer",    "mhp": 50}, 6],
    [5, {"mname": "Normal Chest",    "mhp": 1}, 4],
    [0, {"mname": "Skeleton Sam", "mhp": random.randint(100,300)}, 5],
    [5, {"mname": "Cute Dog",      "mhp": -20}, 6],
    [3, {"mname": "Normal-Sized Toad",     "mhp": 23}, 5],
    [1, {"mname": "Smog Sag",        "mhp": 3}, 6],
    [4, {"mname": "Spectator",        "mhp": 0}, 2],
    [6, {"mname": "Dim Paladin",   "mhp": 60}, 0]
]



def start():
    choosestart = list(range(len(city_names))) ### This should really be list(range(len(cities)) to be more general
    print(choosestart)
    choosestart.remove(current)
    return random.choice(choosestart)
    ### BTW, this can be done with a single line in various ways -- but that's for later

### Another useful thing to do is to order your functions in a sensible way, usually the callers go right below
### the functions they call (or some people do right above)

def getoutgoing():
    destinations = []
    edges = []
    ### Function comment: takes ... returns ... (although getoutgoing is an ok name, the python standard is to use _ like: get_outgoing)
    for x in range(0,len(map_edges)): ### Giving vars meaningful names (not just x and y) will also help remember what's going on s mcould be map_index, or just index
        if map_edges[x][0] == current:
            destinations.append(map_edges[x][2]) 
            edges.append(map_edges[x][1]) 
    return destinations,edges

def travel():
    ### Block comment!
    global current
    act,destinations = action() ### take_step()? -- the naming of functions is NOT trivial -- unless you comment everywhere it's the only way you can tell what's going on!
    if act == "BACK":
        if len(backstack) > 0: ### Since backstack isn't a useful name, I can't even begin to guess what this is intended to do -- is backstack the path stack?
            current = pops()
    elif city_names.index(act) in destinations:
        stack()
        current = city_names.index(act)
        
def stack(): ### Confusing name -- push_current_on_path_stack()
    ### Block comment or better fn name 
    global backstack
    global current
    backstack.append(current)
    return stack

def pops(): ### pop_path_stack()
    ### Block comment or better fn name  
    global backstack
    global current
    q = backstack.pop((len(backstack)-1))
    return q
    
    
def action():
    ### Block comment! (this one's too complex to just have the whole comment be its name)
    act = " "
    destinations,edges = getoutgoing() ### This is where (at least one of) your problem(s) is -- ask me to explain
    print("Your goal is to reach " + str(city_names[targ]) + ".")
    print("You are currently in " + city_names[current] + ". You can go to these cities: ")
    for y in range(0,len(destinations)): ### better var than y?
        workingcity = destinations[y]
        workingmob = edges[y]
        print(city_names[workingcity] + ", but you must fight a " + workingmob["mname"] + " with " + str(workingmob["mhp"]) + " health.")
    print("You can also go BACK.")
    act = input("Where would you like to go?")
    return act,destinations

def run():
    global current 
    global targ
    current = random.randint(0,6)
    targ = start()
    while current != targ:
        travel()
    print("You were sucessful.")

run()