#section_121.py

number = int(input('나눌 숫자를 입력하세요 '))

try:
    result = 10/number
except ZeroDivisionError:
    print('0으로 나누면 안되요.')
else:
    print(result)
    
