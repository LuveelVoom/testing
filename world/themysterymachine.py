import random
target = random.randint(2,100)
current = 1
rotator = 1
score = 0
difficulty = 0
while not current == target:
    randor = random.randint(0,3)
    print(str(current))
    print(str(target))
    print(difficulty)
    if not random.randint(-1,difficulty) > 3:
        print(str(randor))
    else:
        print("-1")
    if not random.randint(-1,difficulty) > 5:
        print(str(rotator))
    else:
        print("-2")
    inpu = input("Enter number?")
    if rotator == 1:
        current = int(inpu) + current
    elif rotator == 2:
        current = int(inpu) - current
    elif rotator == 3:
        current = int(inpu) * current
    if current % 5 == 0:
        target = target + random.randint(-5,5)
    if current % 7 == 0:
        target = target * 2
        rotator = 1
    if randor == 3:
        current = current + (target % 10)
    if randor == 2:
        difficulty = difficulty + 1
    rotator = rotator + 1
    current = current + difficulty * random.randint(-1,1)
    print(str(current))
    score = score + 1
print("You won after " + str(score) + " operations.")
        
    
    
    