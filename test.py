import numpy as np

import scipy as sp

import matplotlib.pyplot as plt

print(np.__version__)
print(sp.__version__)
print(plt.__doc__)

t=np.arange(0.0,6*np.pi,0.001)
x = np.sin(7.0*t)
y = np.sin(13*t)

plt.plot(x,y)
plt.show()
