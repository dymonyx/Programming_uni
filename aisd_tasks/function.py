import numpy as np
from matplotlib import pyplot as plt

n = 20
step = 0.1
x = np.arange(0, n + 1, step)
o1 = np.ones(int((n + 1) / step))
onlogn = np.log2(x) * x
on2 = x ** 2



plt.axis([0, n, 0, 45])
plt.xticks(range(1, n + 1, 2))
plt.xlabel("n")
plt.ylabel("f(n)")
plt.plot(x, onlogn, label="O(n*log(n))")
plt.plotц
plt.legend()
plt.grid()
plt.show()