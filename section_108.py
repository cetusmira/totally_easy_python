#section_108.py

class Robot:
    name = '휴보'
    weight = 45

    def speak(self):
        print('안녕하세요. 휴보입니다.')

    def move(self):
        print('휴보가 이동한다.')

robot1 = Robot()
robot2 = Robot()
robot3 = Robot()

print(type(robot1))
robot2.speak()
