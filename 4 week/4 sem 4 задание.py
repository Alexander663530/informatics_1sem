import matplotlib.pyplot as plt
import numpy as np



#Считывае данных с файла .csv и преобразование в список целых чисел
iris = np.loadtxt('iris_data.csv', dtype = str)
b = []
for i in range(len(iris)):
    c = iris[i].split(',')
    b.append(c)



#Вычисление коэффициентов прямой для Petal
length1 = []
width1 = []
for i in range (len(b)):
    length1.append(float(b[i][3]))
    width1.append(float(b[i][4]))

x1 = np.asarray(length1)
y1 = np.asarray(width1)

A = np.vstack([x1, np.ones(len(x1))]).T

m, c = np.linalg.lstsq(A, y1, rcond = None)[0]



#Вычисление коэффициентов прямой для Sepal
length2 = []
width2 = []
for i in range (len(b)):
    length2.append(float(b[i][1]))
    width2.append(float(b[i][2]))

x2 = np.asarray(length2)
y2 = np.asarray(width2)

A = np.vstack([x2, np.ones(len(x2))]).T

p, q = np.linalg.lstsq(A, y2, rcond = None)[0]



#Построение графиков
fig = plt.figure(figsize=(8,9), dpi=190)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)



ax1.set_title('Petal')
ax1.set_xlabel('length')
ax1.set_ylabel('width')

ax1.plot(x1, y1, 'o', markersize = 1)
ax1.plot(x1, m*x1 + c, 'r')



ax2.set_title('Sepal')
ax2.set_xlabel('length')
ax2.set_ylabel('width')

ax2.plot(x2, y2, 'o', markersize = 1)
ax2.plot(x2, p*x2 + q, 'r')



plt.show()








