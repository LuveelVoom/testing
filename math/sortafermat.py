import random
b = []
low = int(input("lower?"))
high = int(input("higher?"))
itc = int(input("count?"))
thresh = int(input("notability threshold?"))
currant = random.randint(low,high)

for k in range(0,itc):
    currant = random.randint(low,high)
    a = []
    for x in range(2,currant):
        for y in range(2,currant):
            for z in range(2,currant):
                if x*y == (x+y)*z:
                    a.append(y)
                    # print(str(x) + " " + str(y)+ " "+str(z))
    for p in range(1,currant):
        if p not in a:
            b.append(p)
    print("Finished an iteration, pick was " + str(currant) + " and iteration number was " + str(k))
for p in range(0,high):
    if b.count(p) >= thresh:
        print(p)
print("Done.")       