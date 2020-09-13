import numpy as np
import matplotlib.pyplot as plt

#Data preparation
x = np.arange(0, 6, 0.1)    #From 0 to 6 with 0.1 intervals
y = np.sin(x)

#Drawing a graph
plt.plot(x,y)
plt.show()