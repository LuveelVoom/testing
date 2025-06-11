import random
eggs = random.randint(1,24)
priceeggs = random.randint(3,10)
amounteggs = 0
n = "1"
oneandnegativeone = [-1, 1]
money = 100
print("It is day 1. The following are currently avaliable to buy:")
print(str(eggs) + " eggs at " + str(priceeggs) + " doubloons per egg")
quant = input("How many eggs would you like to purchase?")
while n is "1":
    if int(quant) * priceeggs < money:
        if int(quant) <= eggs:
            money = money - (int(quant) * priceeggs)
            amounteggs = amounteggs + int(quant)
            priceeggs = abs(priceeggs + random.randint(0,abs(int(quant))) * int(random.choice(oneandnegativeone))) + 1
            eggs = eggs - int(quant)
            n = "0"
            break
print("You now have " + str(amounteggs) + " eggs and " + str(money) + " doubloons.")
print("It is day 2. The following are currently avaliable to buy:")
print(str(eggs) + " eggs at " + str(priceeggs) + " doubloons per egg")
print("You currently have " + str(amounteggs) + " eggs.")
quant = input("How many eggs would you like to purchase? Enter a negative number to sell eggs.")
n = "1"
while n == "1":
    if int(quant) * priceeggs < money and int(quant)>=0:
        if int(quant) <= eggs:
            money = money - (int(quant) * priceeggs)
            amounteggs = amounteggs + int(quant)
            priceeggs = abs(priceeggs + random.randint(0,abs(int(quant))) * int(random.choice(oneandnegativeone))) + 1
            eggs = eggs - int(quant)
            n = "0"
            break
    elif int(quant) < 0:
            money = money - (int(quant) * priceeggs)
            amounteggs = amounteggs + int(quant)
            priceeggs = abs(priceeggs + random.randint(0,abs(int(quant))) * int(random.choice(oneandnegativeone))) + 1
            eggs = eggs - int(quant)
            n = "0"
            break
print("You now have " + str(amounteggs) + " eggs and " + str(money) + " doubloons.")
print("It is day 3. The following are currently avaliable to buy:")
print(str(eggs) + " eggs at " + str(priceeggs) + " doubloons per egg")
print("You currently have " + str(amounteggs) + " eggs.")
quant = input("How many eggs would you like to purchase? Enter a negative number to sell eggs.")
n = "1"
while n == "1":
    if int(quant) * priceeggs < money and int(quant)>=0:
        if int(quant) <= eggs:
            money = money - (int(quant) * priceeggs)
            amounteggs = amounteggs + int(quant)
            priceeggs = abs(priceeggs + random.randint(0,abs(int(quant))) * int(random.choice(oneandnegativeone))) + 1
            eggs = eggs - int(quant)
            n = "0"
            break
    elif int(quant) < 0:
            money = money - (int(quant) * priceeggs)
            amounteggs = amounteggs + int(quant)
            priceeggs = abs(priceeggs + random.randint(0,abs(int(quant))) * int(random.choice(oneandnegativeone))) + 1
            eggs = eggs - int(quant)
            n = "0"
            break
print("You now have " + str(amounteggs) + " eggs and " + str(money) + " doubloons.")
print("It is day 4. The following are currently avaliable to buy:")
print(str(eggs) + " eggs at " + str(priceeggs) + " doubloons per egg")
print("You currently have " + str(amounteggs) + " eggs.")
quant = input("How many eggs would you like to purchase? Enter a negative number to sell eggs.")
n = "1"
while n == "1":
    if int(quant) * priceeggs < money and int(quant)>=0:
        if int(quant) <= eggs:
            money = money - (int(quant) * priceeggs)
            amounteggs = amounteggs + int(quant)
            priceeggs = abs(priceeggs + random.randint(0,abs(int(quant))) * int(random.choice(oneandnegativeone))) + 1
            eggs = eggs - int(quant)
            n = "0"
            break
    elif int(quant) < 0:
            money = money - (int(quant) * priceeggs)
            amounteggs = amounteggs + int(quant)
            priceeggs = abs(priceeggs + random.randint(0,abs(int(quant))) * int(random.choice(oneandnegativeone))) + 1
            eggs = eggs - int(quant)
            n = "0"
            break
print("You now have " + str(amounteggs) + " eggs and " + str(money) + " doubloons.")
print("It is day 5, the final day. The following are currently avaliable to buy:")
print(str(eggs) + " eggs at " + str(priceeggs) + " doubloons per egg")
print("You currently have " + str(amounteggs) + " eggs.")
quant = input("How many eggs would you like to purchase? Enter a negative number to sell eggs.")
n = "1"
while n == "1":
    if int(quant) * priceeggs < money and int(quant)>=0:
        if int(quant) <= eggs:
            money = money - (int(quant) * priceeggs)
            amounteggs = amounteggs + int(quant)
            priceeggs = abs(priceeggs + random.randint(0,abs(int(quant))) * int(random.choice(oneandnegativeone))) + 1
            eggs = eggs - int(quant)
            n = "0"
            break
    elif int(quant) < 0:
            money = money - (int(quant) * priceeggs)
            amounteggs = amounteggs + int(quant)
            priceeggs = abs(priceeggs + random.randint(0,abs(int(quant))) * int(random.choice(oneandnegativeone))) + 1
            eggs = eggs - int(quant)
            n = "0"
            break
print("Your score was " + str(money) + " doubloons.")

