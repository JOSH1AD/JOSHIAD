# Ai반 2기 - 8주차 정규수업(16:30~18:30) mission
'''
[수업을 시작하기 전에!]
1. 웨일ON으로 원격 회의실 접속하기
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기~
5. 수업시간 집중~~~!! 딴 짓! 멈춰~~~~~!

[6주차 내용 복습]
1. 리스트 자료형
2. for 반복문
3. for 반복문 연습문제
'''


# [반복문 이어서...]
## 반복문 mission5-2: turtle을 활용한 미디어아트2
'''
import turtle as t

n = 200
t.bgcolor('black')
color = ['green', 'purple', 'skyblue', 'darkblue', 'white', 'yellow']
t.speed(0)

for i in range(n):
    t.pencolor(color[i % len(color)])
    t.circle(150)
    t.left(360/n)
t.mainloop()
'''

# [반복문 추가 문제]
## 이중 for문 연습문제(warming-up)
## : 이중 for문을 활용하여 높이5의 직각삼각형 만들기
'''
for i in range(1,11):
    for j in range(i):
        print('*', end=' ')
    print()
'''
## 반복문 추가문제 Mission1: Up-Down 게임 만들기(feat. random 함수)
## >> random 함수를 활용하여 1~100까지의 숫자를 생성하고 up-down 게임 만들어보기
"""
import random

random_num = random.randint(1, 100)
count = 0


while count <= 5:
    user_num = int(input('숫자를 1~100까지 입력하세요>>'))
    count += 1
    if random_num == user_num:
        print("Congratulation")
        break
    elif random_num > user_num:
        print("UP")
    else:
        print("DOWN")
print(f"시도한 횟수: {count}")
"""
## 반복문 추가문제 Mission3: turtle 모듈을 활용하여 무지개 만들기
### for 반복문 Mission2: turtle 모듈을 활용하여 무지개 만들기

import turtle

# 변수 및 객체 선언
win = turtle.Screen()
t = turtle.Turtle('turtle')
rainbow_size = 300         # 무지개 크기(너비)
pen_size = 50              # 펜 굵기
rainbow_color = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']      # 활용할 색상 지정
t.speed(10)                # 거북이 속도 설정

# 펜 초기 설정
t.pensize(pen_size)

# for 반복문 실행(무지개 그리기)

# <Mission: 이 부분을 작성해 주세요>

for i in range(7):
    t.setheading(90)
    t.penup()
    t.setpos(rainbow_size-(pen_size*i),0)
    t.pencolor(rainbow_color[i])
    t.pendown()
    t.circle(rainbow_size-(pen_size*i), 180)
turtle.mainloop()




# [함수]
##: 여러개의 명령어들을 묶어서 한꺼번에 처리할 수 있도록 만든 하나의 명령어 묶음에 이름을 붙인 것.
## 문법: def 함수이름(매개변수1, 매개변수2, ...):
##         명령어 블럭
##         return 반환값

## docstring: 함수에 대한 설명을 나타내는 문장

## 연습문제1: 입력X, 출력X인 함수
## >> 함수를 호출하면 별모양을 그리는 DrawStar_100()
'''
import turtle
<DrawStar_100 함수 정의>

win = turtle.Screen()
<DrawStart_100 함소 호출>
win.mainloop()
'''
## 연습문제2: 입력O, 출력X인 함수
## >> 한 변의 길이를 입력하면, 그 한변의 길이를 가지는 별을 그리는 DrawStar()
'''
import turtle
<DrawStar() 함수 정의해주기> 

win = turtle.Screen()
DrawStar(200)
win.mainloop()
'''
## 연습문제3: 입력X, 출력O인 함수
## >> 1~100까지 랜덤한 정수 1개를 반환하는 getRandomNum()
'''
import random
<getRandomNum() 함수 정의해주기>

<getRandomNum() 함수를 호출하여 반환값을 num 변수에 할당하기>
print(num)
'''
## 연습문제4: 입력O, 출력O인 함수
## >> a,b를 입력하면 두 수의 합을 반환하는 add()
'''
<add() 함수 정의해주기>

<add() 함수를 호출하여 반환값을 X 에 할당하기 >
print(X)
'''

## 함수 Mission: 앞서 반복문 Mission4에서 그린 무지개를 "함수"로 만들어보자
## 조건은 ppt 30p - 함수 Mission 참고
'''
# Mission: draw_rainbow() 함수 정의하기
def draw_rainbow(t, rainbow_size, pen_size, x, y):
    """
    입력한 t가 rainbow_size크기의 지름과 pen_size 두께의 색상띠를 가지는 무지개를 (x,y)에 그리는 함수
    :param t: 그림을 그릴 turtle 객체
    :param rainbow_size: 무지개의 지름
    :param pen_size: 무지개를 그릴 펜의 두께
    :param x: 무지개가 그려질 x좌표
    :param y: 무지개가 그려질 y좌표
    """
    # 설정(작성할 부분1)


    # 그리기(작성할 부분2)


import turtle

win = turtle.Screen()
win.screensize(1000,1000)
t = turtle.Turtle('turtle')
t.speed(0)

# 이제 draw_rainbow를 활용하여 무지개를 마음껏 그려보자(작성할 부분3)


turtle.mainloop()
'''