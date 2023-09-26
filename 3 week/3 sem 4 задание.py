def pyramid(n, b):
    s = b
    if n == 0:
        return []
    if n == 1:
        return[s]
    else:
        tmp = []
        for i in range (len(pyramid(n-2, b))):
            d = pyramid(n-2, b)
            tmp.append(d[i] + s)
        return [s] + tmp + [s]

a = input().split()
c = pyramid(int(a[0]), a[1])
for i in range (len(c)):
    print(c[i], sep = '\n')
    
    

