'''import math
num = int(input("Please input number."))
for n in range(2,int(math.sqrt(num))):
    if num % n == 0:
        num = num // n
        print(str(n))
print(int(num))'''

num = int(input("Enter a positive integer: "))
n = 2                       # start with the first prime

while num > 1:              # stop when we’ve broken num down to 1
    if num % n == 0:        # does n divide num exactly?
        print(n)            # n is a prime factor
        num //= n           # divide num by n (same as num = num // n)
    else:
        n += 1  
            
        
            



