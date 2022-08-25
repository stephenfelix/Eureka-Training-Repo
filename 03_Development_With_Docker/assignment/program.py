import matplotlib
matplotlib.use('tkAgg')
import matplotlib.pyplot as plt
from random import randint

plt.plot(range(1, 11), [randint(0, 100) for _ in range(0, 10)])
plt.show()
