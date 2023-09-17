f = open('input.txt').readline()
a = f.split(' ')
b = open('input.txt').readlines()
A = []

counter = 0
if b[1] == '+\n':
    for i in range(len(a)):
        counter += int(a[i], int(b[2]))
elif b[1] == '-\n':
    counter = int(a[0], int(b[0]))
    for i in range(len(a)-1):
        counter = counter - int(a[i+1], int(b[2]))
elif b[1] == '*\n':
    for i in range(len(a)):
        counter *= int(a[i], int(b[2]))
print(''.join(map(str, A)))

A.append(counter % int(b[2]))
d = counter // int(b[2])
A.append(d % int(b[2]))
while d <= int(b[2]):
    d = d // int(b[2])
    A.append(d % int(b[2]))
A.reverse()





