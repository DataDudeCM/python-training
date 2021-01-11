prod = int(input("Enter a fib product: "))

def productFib(prod):
    a =[]
    a.append(0)
    a.append(1)
    n=1
    while a[n-1] * a[n] < prod:
        a.append(a[n]+a[n-1])
        n += 1
    if a[n] * a[n-1] == prod:
        a.append(True)
        return a[-3:]
    else:
        a.append(False)
        return a[-3:]
    return 

print(productFib(prod))