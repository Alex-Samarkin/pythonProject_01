# Автор: [Самаркин А.И.$]
# Описание:
#
#
# Дата:

import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats
import statsmodels as stm

# массив целых чисел a
a = np.array([2,3,4])
# печать массива
print(f"Массив a= {a}")
# тип элементов массива
print(f"Тип массива {a.dtype}")

b = np.array([1.2,3.0,4.1])
print(f"Массив a= {b}")
print(f"Тип массива {b.dtype}")

# произведение массивов
print(a*b)

# матрица из трех строк и семи столбцов, заполнена нулями
print( np.zeros([3,7], dtype=np.float))
# матрица из пяти строк, заполнена 1
print( np.ones([5,5], dtype=np.float))

t1 = np.arange(0.0,10.0,0.1)
print(t1)

t2 = np.linspace(0.0, 6.0*np.pi, 1000)
print(t2)

x = np.sin(3.0*t2)
y = np.sin(5*t2)

plt.plot(x,y)
plt.show()

ro = t2+t2*np.sin(25.0*t2)+10.0
x = ro*np.cos(t2)
y = ro*np.sin(t2)

plt.plot(x,y)
plt.show()

print("")
