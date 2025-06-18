import math
priornumb = []
elements = []
p = 1
k = input("To what?")
for x in range(0,int(k)-1):
    while p == 1 and p < int(k):
        cut = x % int(k)
        priornumb.append(cut)
        x = math.floor(cut*cut)
        if x % int(k) in priornumb:
            elements.append(len(priornumb))
            p = 0
        elif p > 100000:
            print("Number not detected after 100,000 iterations. A loop may have been entered, here are the last 100 numbers:")
            hunders = priornumb[-100:]
            print(str(hunders))
            elements.append[0]
            p = 0
        else:
            p =+ 1
    priornumb = []
    p = 1
for w in range(0,int(k)):
    value = elements.count(w)
    if value > 0:
        print("Number " + str(w) + " occured " + str(value) + " times.")
    
    
        
    


