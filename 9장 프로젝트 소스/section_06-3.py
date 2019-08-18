#section_06-3.py

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from pylab import axis

kr_font = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=kr_font)

x = [0, 1, 2, 3, 4, 5]
def f(x):
    '''y 좌표(일차함수 y=x+1) 구하기'''
    y = []
    for num in x:
        y.append(num + 1)
    return y

plt.plot(x, f(x))
axis(xmin=0, xmax=5, ymin=0, ymax=7)
plt.xlabel('x 축')
plt.ylabel('y 축')
plt.title('일차함수 그래프')
plt.show()