#section_095.py

import time

print('현재시각:', time.time())

def manyloop(max):
    t1 = time.time()
    for a in range(max):
        pass
    t2 = time.time()
    print(t2-t1, '초 경과')

number = int(input('숫자를 입력하세요: '))
manyloop(number)
