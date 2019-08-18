#section_102.py

f = open('c:/temp/myfile.txt', 'w')
poem = '''
살어리 살어리랏다 쳥산에 살어리랏다
멀위랑 달래랑 먹고 쳥산에 살어리랏다
얄리 얄리 얄랑셩 얄라리 얄라

우러라 우러라 새여 자고 니러 우러라 새여
널라와 시름 한 나도 자고 니러 우리노라
얄리 얄리 얄라셩 얄라리 얄라
'''
f.write(poem)
f.close()

f = open('c:/temp/myfile.txt', 'r')

all = f.readlines()

print(all)

for sentence in all:
    print(sentence)

f.close()
