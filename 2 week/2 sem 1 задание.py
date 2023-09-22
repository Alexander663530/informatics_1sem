a = input().split()
A = []
S = 0
S1 = 0
for i in range (int(a[0])):
    S += i+1
for i in range (int(a[0])-1):
    S1 += int(a[i+1])
D = S - S1
print(D)
