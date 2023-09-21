f = open('input.txt').readline()
a = f.split(" ")
f = open('input.txt').readlines()
if f[1] == '+':
    counter = 0
    for i in range(len(a)):
        counter +=int(a[i])
if f[1] == '-':
    counter = a[0]
    for i in range(len(a)-1):
        counter = int(counter) - int(a[i+1])
if f[1] == '*':
    counter = 0
    for i in range(len(a)):
        counter *=int(a[i])
print(counter)
f1 = open('output.txt', 'w')
f1.write(str(counter))
f1.close()
    
