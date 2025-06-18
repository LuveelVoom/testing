a = int(input("How high?"))
m = {}
def fib(a):
    #print(a)
    if (a == 0) or (a == 1):
        return 1
    elif a in m:
        return m[a]
    else:
        cval = fib(a-1)+fib(a-2)
        m[a] = cval
        return cval
    
print(fib(a))

    