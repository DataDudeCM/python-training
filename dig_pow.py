def dig_pow(n,p):
    n = str(n)
    answer = 0
    for d in range(len(str(n))):
        answer = answer + pow(int(n[d]),p)
        p += 1
    k = 0
    while k * int(n) < answer:
        k += 1
        print(k, int(n), k*int(n))
        if k * int(n) == answer:
            return k
    return -1

print(dig_pow(46288,3))
