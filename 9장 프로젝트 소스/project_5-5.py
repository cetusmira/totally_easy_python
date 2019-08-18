#project_5-5.py

# 1 - 모듈 임포트
import pygame
import random

# 2 - 게임 변수 초기화
    # 2.1 - 게임 화면
pygame.init()
screen = pygame.display.set_mode((480, 640))

# 2.2 - 시간관련 변수
FPS = 30
fpsClock = pygame.time.Clock()

try:
    # 3 - 그림과 효과음 삽입
        # 3.1 - 그림 삽입
    spaceshipimg = pygame.image.load("./img/spaceship.png")
    asteroid0 = pygame.image.load("./img/asteroid00.png")
    asteroid1 = pygame.image.load("./img/asteroid01.png")
    asteroid2 = pygame.image.load("./img/asteroid02.png")
    asteroidimgs = (asteroid0, asteroid1, asteroid2)
    gameover = pygame.image.load("./img/gameover.jpg")

    # 3.2 - 효과음 삽입
    takeoffsound = pygame.mixer.Sound("./audio/takeoff.wav")
    landingsound = pygame.mixer.Sound("./audio/landing.wav")
    takeoffsound.play()
except Exception as err:
    print('그림 또는 효과음 삽입에 문제가 있습니다.: ', err)
    pygame.quit()
    exit(0)

# 5 - 게임 루프
running = True
while running:
    # 6 - 화면을 그리기에 앞서 화면을 흰색으로 지우기
    screen.fill((255, 255, 255))

    # 7 - 키보드/마우스 이벤트
    for event in pygame.event.get():
        # X 버튼을 클릭하면 게임 종료
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # 9 - 게임 요소 상태 변경
        # 9.1 - spaceship 위치/그리기
    screen.blit(spaceshipimg, (240, 600))

    landingsound.play()

        # 9.2 - asteroids 추가하기
    screen.blit(asteroidimgs[0], (240, 320))

    # 10 - 게임 속도
    fpsClock.tick(FPS)

    # 11 - 화면 전체 업데이트
    pygame.display.flip()

# 12 - 게임 종료 화면
screen.blit(gameover, (0, 0))

pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()