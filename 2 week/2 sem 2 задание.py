a = input().split()
c = []
for i in range (0, len(a)-1, 2):
    c = a[i]
    a[i] = a[i+1]
    a[i+1] = c
b = ''.join(a)
print(b)



    
