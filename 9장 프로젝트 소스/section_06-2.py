#section_06-2.py

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

fontname = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=fontname)

x = [1, 2, 3, 4, 5]
y = [4, 5, 6, 7, 6]

x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 7, 4, 3]

plt.plot(x, y)
plt.plot(x1, y1)
plt.xlabel('x 축')
plt.ylabel('y 축')
plt.title('직선 그래프')
plt.show()