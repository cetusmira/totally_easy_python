#section_03.py

import os

# 파일명 변경하기 함수
def changeFilename(filelist, size, change):
    number = 0

    print('-'*50)        
    for name in filelist:
        if name[-4: ]=='.jpg':
            number += 1
            strnumber = str(number).zfill(size)
            newname = '자연' + strnumber + '.jpg'        
            if change:
                os.rename(path+name, path+newname)
            print(name, '->', newname)
    print('-'*50)

# 프로그램 시작
while True:
    print('프로그램을 종료하고 싶으면 q를 입력하세요.')

    # 폴더 경로 입력받기
    path = input('경로를 입력해주세요(형식: c:/temp/) ') 

    if path == 'q':
        break
    elif path == '':
        path = 'c:/temp/'
    elif path[-1] != '/':
        path += '/'

    # 폴더에서 파일정보 가져오기        
    try:
        files = os.listdir(path)
        for file in files:
            print(file)
    except:
        print('경로를 다시 확인하세요.')
        continue

    # 파일정보 확인하기
    go = input('해당 폴더의 파일이 맞나요? (y/n) ').lower()
    if go == 'n':
        continue
    elif go == 'q':
        break

    size = len(input('숫자부분의 자릿수에 맞춰 0을 넣어주세요(ex, 000): '))

    # 파일 변경 전 확인하기
    changeFilename(files, size, False)

    go = input('이대로 변경할까요? (y/n) ').lower()
    if go == 'n':
        continue
    elif go == 'q':
        break

    # 파일 변경하기
    changeFilename(files, size, True)
    print('파일명 변경 완료')

    # 재실행 / 종료
    ans = input('또 다른 파일명을 수정할건가요?(y/n): ').lower().startswith('y')
    if ans:
        continue
    else:
        break
    
# 프로그램 종료
