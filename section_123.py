#section_123.py

def openFile():
    file = open('없는파일.txt')
    line = file.readline()
    number = int(line.strip())

try:
    openFile()
except OSError as err:
    print('시스템 에러: ', err)
except:
    print('내가 예측할 수 없는 오류ㅠ')
else:
    print(number)

    
