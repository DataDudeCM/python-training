def digital_root(n):
    if len(str(n)) == 1:
        return n
    else:
        digitsum = 0
        for i in str(n):
            digitsum += int(i)
        return digital_root(digitsum)

print(digital_root(16))