# Ai반 2기 python 중급반 - 8주차 정규수업(16:30~18:30) mission
'''
[수업을 시작하기 전에!]
1. 웨일ON으로 원격 회의실 접속하기
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기~
5. 수업시간 집중~~~!! 딴 짓! 멈춰~~~~~!

[저번주 복습]
1. 파일 입출력: 파일 쓰기, 이어쓰기, 읽기
2. 이벤트 처리 프로그램
3. turtle을 활용한 이벤트 마우스 이벤트 처리
'''


# [이벤트 처리]
## turtle 마우스 이벤트 처리 Mission
'''
import turtle as t
import random

# randomColor 함수: 랜덤한 r,g,b 값을 반환하는 함수
def randomColor():
    r = random.random()  # r: random.random(): 0~1상이의 랜덤한 값 할당
    g = random.random()  # g
    b = random.random()  # b
    return r, g, b          # return

# leftClick 핸들링 함수: 거북이 스탬프 모양을 찍는 함수
def turtleStamp(x, y):
    t.hideturtle()      # 거북이 숨기기
    t.setposition(x, y)  # (x,y)좌표로 거북이 이동
    t.setheading(random.randint(0,360)) # 랜덤하게 거북이의 머리 방향 지정(0~360도)
    t.shapesize(random.randint(1,10))   # 랜덤하게 거북이의 크기 설정(1~10)
    r, g, b = randomColor() # 랜덤 r,g,b 값 가져오기(randomColor 함수 사용하기)
    t.fillcolor(r, g, b)      # 스템프 색상 설정(랜덤 r,g,b 값 넣기)
    t.pencolor(r, g, b)       # 스템프 테두리 색성 설정(랜덤 r,g,b 값 넣기)
    t.stamp()                 # 스템프 찍기 명령

# rightClick 이벤트 핸들링 함수: 화면을 초기화하는 함수
def rightClick(x, y):
    t.clear()
    # 화면 초기화

t.title('거북이 마우스 이벤트 처리 프로그램')  # 프로그램 제목 지정
t.shape('turtle')                        # 도장 모양을 turtle으로 설정
t.speed(0)                               # 속도 설정
t.penup()                                # 펜 들기

t.onscreenclick(turtleStamp, 1)       # 이벤트 설정: onscreenclick
# <오른쪽 클릭 이벤트 설정>
t.onscreenclick(rightClick, 3)
t.mainloop()
'''
'''
## turtle 키보드 마우스 처리 Mission


import turtle as t
import random
import pygame
def randomColor():
    r = random.random()  # r: random.random(): 0~1상이의 랜덤한 값 할당
    g = random.random()  # g
    b = random.random()  # b
    return r, g, b          # return

# up 이벤트 핸들링 함수: 위 방향으로 10만큼 이동 및 색상 변화
def up():
    t.setheading(90)# 가려는 방향에 맞게 방향설정
    r, g, b = randomColor()# 랜덤 색상 r,g,b 가져오기
    t.pencolor(r, g, b)# 펜 색상 설정
    t.fillcolor(r, g, b)# 거북이의 색상도 같이 설정
    t.forward(10)# 10만 큼 이동

# down 이벤트 핸들링 함수: 아래방향으로 10만큼 이동 및 색상 변화
def down():
    t.setheading(270)# 가려는 방향에 맞게 방향설정
    r, g, b = randomColor()# 랜덤 색상 r,g,b 가져오기
    t.pencolor(r, g, b)# 펜 색상 설정
    t.fillcolor(r, g, b)# 거북이의 색상도 같이 설정
    t.forward(10)# 10만 큼 이동

# right 이벤트 핸들링 함수: 오른쪽으로 10만큼 이동 및 색상 변화
def right():
    t.setheading(0)# 가려는 방향에 맞게 방향설정
    r, g, b = randomColor()# 랜덤 색상 r,g,b 가져오기
    t.pencolor(r, g, b)# 펜 색상 설정
    t.fillcolor(r, g, b)# 거북이의 색상도 같이 설정
    t.forward(10)# 10만 큼 이동

# left 이벤트 핸들링 함수: 왼쪽으로 10만큼 이동 및 색상 변화
def left():
    t.setheading(180)# 가려는 방향에 맞게 방향설정
    r, g, b = randomColor()# 랜덤 색상 r,g,b 가져오기
    t.pencolor(r, g, b)# 펜 색상 설정
    t.fillcolor(r, g, b)# 거북이의 색상도 같이 설정
    t.forward(10)# 10만 큼 이동

# clear_bg: 배경 초기화
def clear_bg():
    t.clear()

# close_window: 프로그램을 종료하는 함수
def close_window():
    t.bye()
pygame.init()
bg_sound = pygame.mixer.Sound("Star.mp3")
bg_sound.play(-1)
t.title('마리오의 별을 훔쳐먹은 거북이')# 프로그램 제목 설정
t.bgcolor('black')# 배경색 설정
t.shape('classic')# 모양을 turtle로 설정
t.pensize(10)# 펜 사이즈를 10으로 설정

t.onkeypress(up, "Up")# up 함수 이벤트 처리(onpress)
t.onkeypress(down, "Down")# down 함수 이벤트 처리(onpress)
t.onkeypress(right, "Right")# right 함수 이벤트 처리(onpress)
t.onkeypress(left, "Left")# left 함수 이벤트 처리(onpress)
t.onkeypress(clear_bg, "space")# cleag_bg 함수 이벤트 처리(onpress)
t.onkeypress(close_window, "Escape")# cloase_window 함수 이벤트 처리(onpress)
t.listen()# listen을 실행시켜 주어야 키 입력 모두가 실행되어 입력키에 반응함.

t.mainloop()
'''
from tkinter import *
window = Tk()
window.title('test GUI')
window.geometry("200x300+100+100")
window.resizable(True, False)
window.mainloop()



