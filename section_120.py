#section_120.py

import random

class Motor:
    def __init__(self):
        self.distance = 0
        
    def forward(self):
        print('앞으로 이동한다')
        self.distance += 1
        
    def backward(self):
        print('뒤로 이동한다')
        self.distance -= 1
        
class Robot:
    '''다양한 로봇을 만드는 클래스'''
    def __init__(self):
        self.drive = Motor()
        
    def __str__(self):
        return '이동거리: {}'.format(self.drive.distance)

robot = Robot()

for i in range(10):
    if random.randint(0,1):
        robot.drive.forward()
    else:
        robot.drive.backward()
        
print(robot)
