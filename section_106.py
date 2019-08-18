#section_106.py

poem1 = '''
살어리 살어리랏다 쳥산에 살어리랏다
멀위랑 달래랑 먹고 쳥산에 살어리랏다
얄리 얄리 얄랑셩 얄라리 얄라
'''

with open('c:/temp/myfile.txt', 'w') as f:
    f.write(poem1)

with open('c:/temp/myfile.txt', 'r') as f:
    print('------ 원본 파일 ------')
    print(f.read())

poem2 = '''
우러라 우러라 새여 자고 니러 우러라 새여
널라와 시름 한 나도 자고 니러 우리노라
얄리 얄리 얄라셩 얄라리 얄라
'''

with open('c:/temp/myfile.txt', 'a') as f:
    f.write(poem2)

with open('c:/temp/myfile.txt', 'r') as f:
    print('------ 데이터를 추가한 후 ------')
    print(f.read())
