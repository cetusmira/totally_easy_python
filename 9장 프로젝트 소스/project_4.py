#project_4.py

import random

count = 0

print('게임하자. 컴퓨터인 내가 생각하는 수를 6번 안에 맞추면 돼. 준비됐으면 엔터를 쳐.')
input()

goal = random.randint(1, 100)
print('좋아. 숫자를 정했으니 한 번 맞춰봐')

while count < 6 :
    guess = input('당신이 예상하는 숫자는? ')
    guess = int(guess)

    count += 1
    
    if guess == goal:
        break
    elif guess > goal:
        print('더 작은 수야..')
    else:
        print('더 큰 수야..')
    
if guess == goal :
    count = str(count)
    print('대박! ' + count + '번 만에 맞췄어!')
else:
    goal = str(goal)
    print('이런.. 내가 생각한 숫자는 ' + goal + '인데..ㅋㅋ')

print('프로그램 종료')
