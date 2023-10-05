import matplotlib.pyplot as plt
import numpy as np
a = np.loadtxt('iris_data.csv', dtype = str)

b = []
for i in range(len(a)):
    c = a[i].split(',')
    b.append(c)
print(b)


number = len(a)
setosa = 0
versicolor = 0
virginica = 0
for i in range (number):
    if b[i][len(b[i])-1] == 'Iris-setosa':
        setosa += 1
    elif b[i][len(b[i])-1] == 'Iris-versicolor':
        versicolor += 1
    elif b[i][len(b[i])-1] == 'Iris-virginica':
        virginica += 1



l1 = 0
l2 = 0
l3 = 0
l4 = 0
for i in range (number):
    if float(b[i][len(b[i])-3]) > 1.2:
        l1 += 1
    if float(b[i][len(b[i])-3]) < 1.2:
        l2 += 1
    if float(b[i][len(b[i])-3]) > 1.5:
        l3 += 1
    if float(b[i][len(b[i])-3]) < 1.5:
        l4 += 1


fig = plt.figure()

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.pie([setosa, versicolor, virginica], labels = ['setosa', 'versicolor', 'virginica'])
ax2.pie([l1, l2, l3, l4], labels = ['>1.2', '<1.2', '>1.5', '<1.5'])

plt.show()



        
    


  
    

