# Ai반 2기 - 7주차 정규수업(16:30~18:30) mission
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

## while 반복문
## : "조건"에 대한 반복문
## [문법] while 조건:
##          반복할 문장
## while문 연습문제1: 기본적인 활용
'''
i = 1
while i <= 3:
    print(f'{i} 꼬마')
    i += 1
'''
## while문 연습문제2: 무한루프와 break를 활용하여 게임 시작메뉴를 만들어보자
'''
while True:
    select = int(input("1을 입력하여 게임을 종료하세요."))
    if select == 1:
        print("끝")
        break
'''
## while문 연습문제3: continue
## : continue 문을 활용하여 1~10까지 숫자 중 홀수만 출력하는 프로그램 작성
'''
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
'''

## 반복문 mission1-1: 원하는 단의 구구단만 출력하기
## for 반복문을 활용하여 출력을 원하는 구구단의 단 수를 입력받고, 1~9까지 곱한 구구단 출력하기
'''
num = int(input("수를 입력하세요"))
for i in range(1,10):
    print(f'{num} * {i} = {num*i}')
'''
## 반복문 mission1-2: 2~9단 모두 출력하기
## for 반복문을 활용하여, 2단~9단까지 모두 출력하기
'''
print('구구단')
for i in range(2, 10):
    print(f'[{i}단]')
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}')
    print('------------------------------------')
'''
## 반복문 mission2-1: while문을 활용하여 반복문 mission1-1과 같은 결과를 출력해보자
'''
i = 0
num = int(input('수를 입력하세요'))
while i < 9:
    i += 1
    print(f'{num} * {i} = {num*i}')
'''
## 반복문 mission2-2: while문을 활용하여 반복문 mission1-2와 같은 결과를 출력해보자.
'''
i = 1
print('구구단')
while i < 9:
    print(f'[{i}단]')
    i += 1
    j = 0
    while j < 9:
        j += 1
        print(f'{i} * {j} = {i * j}')
    print('-----------------')
'''
## 반복문 mission3: 영단어 타자연습 프로그램 - Nope
# -영타연습 Program-
# 1. 연습할 영단어가 담긴 리스트를 만든다.
# 2. 리스트에서 순서대로 단어를 가져와 화면에 출력한다
# 3. 프로그램 사용자는 단어를 그대로 입력한다.
# 4. 입력이 끝나면 전체 문제, 맞은 문제, 틀린 문제의 수가 출력된다.



## 반복문 mission4-1: turtle을 활용한 미디어아트1
'''
import turtle as t

t.bgcolor('gray')
t.pencolor('purple')
t.speed(0)

for i in range(0,1000,2):
    t.fd(i)
    t.left(89)
t.mainloop()
'''
## 반복문 mission4-2: turtle을 활용한 미디어아트1

import turtle as t

t.bgcolor('black')
color = ['pink', 'red', 'yellow', 'purple', 'blue','green']
t.speed(0)

for i in range(1000):
    t.color(color[i % len(color)])
    t.fd(i)
    t.left(59)
t.mainloop()

## 반복문 mission5-1: turtle을 활용한 미디어아트2
'''
import turtle as t
n = 200
t.bgcolor('black')
t.pencolor('skyblue')
t.speed(0)
for i in range(n):
    t.circle(200)
    t.left(360/n)

t.mainloop()
'''
## 반복문 mission5-2: turtle을 활용한 미디어아트2


# [반복문 추가 문제]
## 이중 for문 연습문제(warming-up)
## : 이중 for문을 활용하여 높이5의 직각삼각형 만들기


## 반복문 추가문제 Mission1: Up-Down 게임 만들기(feat. random 함수)
## >> random 함수를 활용하여 1~100까지의 숫자를 생성하고 up-down 게임 만들어보기


## 반복문 추가문제 Mission2:  ASCII 코드를 활용한 슬록머신


## 반복문 추가문제 Mission3: turtle 모듈을 활용하여 무지개 만들기
### for 반복문 Mission2: turtle 모듈을 활용하여 무지개 만들기
