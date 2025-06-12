import random
eggs = random.randint(6,30)
priceeggs = random.randint(3,10)
amounteggs = 0
n = "1"
oneandnegativeone = [-1, 1]
money = 100
day = input("How many days would you like to play for?")
cday = 1
print("It is day 1. The following are currently avaliable to buy:")
print(str(eggs) + " eggs at " + str(priceeggs) + " doubloons per egg")
quant = input("How many eggs would you like to purchase?")
while n is "1":
    if int(quant) * priceeggs < money:
        if int(quant) <= eggs:
            money = money - (int(quant) * priceeggs)
            amounteggs = amounteggs + int(quant)
            priceeggs = abs(priceeggs + random.randint(0,abs(int(quant))) * int(random.choice(oneandnegativeone))) + 1
            eggs = eggs - int(quant) + random.randint(0,round(int(quant)//2))
            n = "0"
            break
while cday <= int(day):
    print("You now have " + str(amounteggs) + " eggs and " + str(money) + " doubloons.")
    print("It is day " + str(cday) +". The following are currently avaliable to buy:")
    print(str(eggs) + " eggs at " + str(priceeggs) + " doubloons per egg")
    print("You currently have " + str(amounteggs) + " eggs.")
    print("You have " + str(money) + " doubloons.")
    quant = input("How many eggs would you like to purchase? Enter a negative number to sell eggs.")
    n = "1"
    while n == "1":
        if int(quant) * priceeggs < money and int(quant)>=0:
            if int(quant) <= eggs:
                money = money - (int(quant) * priceeggs)
                amounteggs = amounteggs + int(quant)
                priceeggs = abs(priceeggs + random.randint(0,abs(int(quant))) * int(random.choice(oneandnegativeone))) + 1
                eggs = eggs - int(quant) + random.randint(0,round(int(quant)//2))
                n = "0"
                cday = cday + 1
                break
        elif int(quant) < 0:
            if int(quant) < -int(amounteggs):
                money = money - (int(quant) * priceeggs)
                amounteggs = amounteggs + int(quant)
                priceeggs = abs(priceeggs + random.randint(0,abs(int(quant))) * int(random.choice(oneandnegativeone))) + 1
                eggs = eggs - int(quant) + random.randint(0,round(int(quant)//2))
                n = "0"
                cday = cday + 1
                break
print("Your score was " + str(money) + " doubloons.")