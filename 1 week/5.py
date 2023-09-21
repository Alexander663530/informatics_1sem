N = int(input())
b = int(input())
c = int(input())
A = []
if c == 10:
    print(int(str(N), b))
else:
    A.append(int(str(N), b)%c)
    d = int(str(N), b)//c
    A.append(d%c)
    while d >= c:
        d = d//c
        A.append(d%c)
    A.reverse()
    print(''.join(map(str, A)))
        
    
