#project_6-4.py

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from pylab import axis
import numpy as np

kr_font = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=kr_font)

x = np.arange(-5, 5, 0.01)
def f(x):
    '''y 좌표(이차함수 y = x**2 + 3*x + 1) 구하기'''
    y = []
    for num in x:
        y.append(num**2 + 3*num + 1)
    return y

plt.plot(x, f(x))
axis(xmin=-5, xmax=5, ymin=-3, ymax=40)
plt.xlabel('x 축')
plt.ylabel('y 축')
plt.title('이차함수 그래프')
plt.show()