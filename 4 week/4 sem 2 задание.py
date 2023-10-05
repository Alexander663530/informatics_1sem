import matplotlib.pyplot as plt
import numpy as np



fig = plt.figure()

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)



values1 = np.random.normal(0,10, 100)
values2 = np.random.normal(0, 10, 10000)



ax1.hist(values1, 100)
ax2.hist(values2, 100)

plt.show()
