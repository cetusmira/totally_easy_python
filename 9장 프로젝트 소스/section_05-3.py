#section_05-3.py

# 1 - 모듈 임포트
import pygame
import random
 
# 2 - 게임 변수 초기화
    # 2.1 - 게임 화면
pygame.init()
screen=pygame.display.set_mode((480, 640))

# 5 - 게임 루프    
running = True
while running:
    # 6 - 화면을 그리기에 앞서 화면을 흰색으로 지우기
    screen.fill((255,255,255))

    # 7 - 키보드/마우스 이벤트
    for event in pygame.event.get():
        # X 버튼을 클릭하면 게임 종료
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0)

    # 9 - 게임 요소 상태 변경      
            
    # 11 - 화면 전체 업데이트
    pygame.display.flip()

# 12 - 게임 종료 화면
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
