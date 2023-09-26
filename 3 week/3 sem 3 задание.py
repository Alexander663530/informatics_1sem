def gcd(a, b):
    if a > b:
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    elif a == b:
        return a
    else:
        if a == 0:
            return b
        else:
            return gcd(a, b % a)


    

w = input().split()

a = int(w[0])
b = int(w[1])
d = gcd(a, b)


z = 0
x = 0

while z >= 0:
    x = z
    if (d - (a * x)) % b == 0:
        break
    x = -z
    if (d - (a * x)) % b == 0:
        break
    z += 1

y = int((d - (a * (x))) / b)
e = [str(x), str(y), str(d)]
print(' '.join(e))
