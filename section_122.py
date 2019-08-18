#section_122.py

try:
    number = int(input('나눌 숫자를 입력하세요 '))
    result = 10/number
except ValueError:
    print('숫자만 입력하세요.')
except ZeroDivisionError:
    print('0으로 나누면 안되요.')
except:
    print('2가지 외에 개발자가 전혀 예측하지 못한 에러ㅠㅠ')
else:
    print(result)
