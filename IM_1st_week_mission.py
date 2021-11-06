# Ai반 2기 python 중급반 - 1주차 정규수업(16:30~18:30) mission
'''
[수업을 시작하기 전에!]
1. 웨일ON으로 원격 회의실 접속하기
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기~
5. 수업시간 집중~~~!! 딴 짓! 멈춰~~~~~!

[저번주 복습]
여러가지 반복문 Mission 수행: 미디어아트2, Up-down game, 무지개 그리기
'''


# [함수]
##: 여러개의 명령어들을 묶어서 한꺼번에 처리할 수 있도록 만든 하나의 명령어 묶음에 이름을 붙인 것.
## 문법: def 함수이름(매개변수1, 매개변수2, ...):
##         명령어 블럭
##         return 반환값

## docstring: 함수에 대한 설명을 나타내는 문장 - 아래 함수들 생성시 doc-string 작성해주기

## 연습문제1: 입력X, 출력X인 함수
## >> 함수를 호출하면 별모양을 그리는 DrawStar_100()
'''
import turtle as t

color = ['green', 'skyblue', 'darkblue', 'white', 'yellow']

def DrawStar_100():
    for i in range(5):
        t.bgcolor('black')
        t.pencolor(color[i % len(color)])
        t.forward(100)
        t.right(144)
        t.forward(100)
        t.left(72)


DrawStar_100()
t.mainloop()
'''
## 연습문제2: 입력O, 출력X인 함수
## >> 한 변의 길이를 입력하면, 그 한변의 길이를 가지는 별을 그리는 DrawStar()

# 모듈 불러오기
import turtle as t


color = ['skyblue', 'blue', 'darkblue', 'purple', 'white']

length = int(input("길이를 입력하세요"))

# 함수 정의
def DrawStar_100(length):
    for i in range(5):
        t.bgcolor('black')
        t.pencolor(color[i % len(color)])
        t.forward(length)
        t.right(144)
        t.forward(length)
        t.left(72)

# main 문 : 직접 실행
DrawStar_100(length)
t.mainloop()



## 연습문제3: 입력X, 출력O인 함수
## >> 1~100까지 랜덤한 정수 1개를 반환하는 getRandomNum()
'''
import random

def  getRandomNum():
    return random.randint(1,100)

num = getRandomNum()
print(num)
'''
## 연습문제4: 입력O, 출력O인 함수
## >> a,b를 입력하면 두 수의 합을 반환하는 add()
'''
def add(x, y):
    return x + y

X = add(18, 28)
print(X)
'''

## 함수 Mission: 앞서 반복문 Mission4에서 그린 무지개를 "함수"로 만들어보자
## 조건은 ppt '함수 Mission' 참고
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

## [튜플]
## : 간단하게 말해 "수정, 추가, 삭제가 불가능한 리스트" 라고 간주할 수 있다.
## 연습문제1: 튜플 만들기
## 2가지 방법으로 튜플을 선언해보고, 두 변수의 값고 자료형을 출력해보자.
'''
numbers1 =              # ()로 튜플 만들기
numbers2 =              # ()없이 튜플 만들기
print(numbers1, type(numbers1))
print(numbers2, type(numbers2))
'''
## 연습문제2: 원소가 하나인 튜플 만들기
## 선언시 ,(쉽표)를 넣지 않은 경우와 쉼표를 넣어 변수를 만들고, 변수들의 값과 자료형을 비교해보자.
## ※ 결과를 비교해보는 것이 중요!!
'''
num1 =          # ()로 만든 경우
num2 =          # (,)로 만든 경우
num3 =          # 숫자 1개만 넣어준 경우
num4 =          # 숫자, 로 만들어준 경우
print("num1: ", num1, type(num1))
print("num2: ", num2, type(num2))
print("num3: ", num3, type(num3))
print("num4: ", num4, type(num4))
'''
## 연습문제3: 튜플 ↔ 리스트로 변환
## : tuple을 만들고 이를 list로 변환 후 값과 자료형을 출력한 후, 이를 다시 튜플로 바꾸어 같은 과정을 반복해보자.
'''
numbers = 
numbers =                          # 튜플을 list로 변환하기
print(numbers, type(numbers))
numbers =                          # 다시 list를 tuple로 변환해주기 
print(numbers, type(numbers))
'''
## 연습문제4: 패킹과 언패킹 그리고 a, b 값 바꾸기
## 4-1) 패킹과 언패킹을 하여 자료형을 출력해보자.
## 4-2) 패킹 언패킹 개념을 활용하여 a, b의 값 바꾸어보자
## ※ 결과를 확인하는 것이 중요!!
'''
# 패킹
a = 
b = 
<code 작성>     # numbers로 a,b를 패킹해주기 
print("numbers:", numbers, type(numbers))   # 결과확인(데이터 값, 자료형 확인)

# 언패킹
<code 작성>      # numbers에 포함된 숫자를 c, d로 언패킹해주기 
print("c: ", c, type(c))
print("d: ", d, type(d), end='\n\n')        # 결과확인(데이터 값, 자료형 확인)

# 응용: a, b의 값 바꿔주기
print("a: ", a)
print("b: ", b)
<code 작성>       # a와 b의 값을 바꿔주기 (패킹&언패킹 응용)         
print("a: ", a)     # 결과 확인
print("b: ", b)
'''

## 연습문제5: 튜플과 관련된 함수
## ※ 결과 확인이 중요!!
'''
numbers = 100, 546, 896, 10, 777, 1, 2, 3
print()         # max(): 튜플에서 최댓값을 반환하는 함수
print()         # min(): 튜플에서 최솟값을 반환하는 함수
print()         # sum(): 튜플에 포함된 원소들의 함을 반환하는 함수
print()         # .count(): 입력한 숫자가 튜플에 몇 개 있는지 세어주는 함수(메서드)
print()         # .index(): 입력한 숫자의 인덱스를 반환해주는 함수(메서드)
'''

## [딕셔너리]
## : 키(key)와 데이터(value)를 가지고 있는 "사전과 같은 자료형"
## key값을 통해 value값을 불러올 수 있다.

## 연습문제1: 딕셔너리 만들기
## : 자신이 좋아하는 youtuber 채널이름(key)과 구독자 수(value)를 말해보자.
##   그리고, 모두가 말한 youtuber들의 이름과 구독자수로 dictionary 자료형을 만들어보자.
##   만약, 남은 시간이 얼마 없다면, 미리 작성해놓은 데이터를 사용하도록 하자

youtuber = {

}

## 연습문제2: 딕셔너리 제어1-값에 접근하기
## : 자신이 가장 좋아하는 youtuber의 구독자 수를 출력해보자
'''
print()     # ()안에 값에 접근하는 문장 넣어주기
'''
## 연습문제3: 딕셔너리 제어2-값 할당(or 수정)하기
## : 자신이 가장 좋아하는 유투버의 구독자 수에 1000이 더 큰 숫자를 넣고 이를 출력해보자
'''
                              # 딕셔너리 값 할당 명령 수행
print(youtuber[""])
'''
## 연습문제3: 딕셔너리 제어3-삭제하기
## : 자신이 두번째로 좋아하는 youtuber를 딕셔너리에서 삭제해보자
'''
                              # 딕셔너리 값 지우기 명령 수행
print(youtuber)
'''
## 연습문제4: 딕셔너리 관련 함수
## .items(), .keys(), .values()의 결과와 데이터 타입을 출력해보자
## ※ 결과 확인이 중요!!
'''
print()     # .items(): key와 value 쌍을 반환하는 함수
print()     # .keys(): 원소가 key로 이루어진 데이터를 포함하는 list를 반환하는 함수
print()     # .values(): 원소가 value로 이루어진 데이터를 포함하는 list를 반환하는 함수
'''

# [클래스(class)]
## 클래스와 객체
## 클래스: 객체를 만들기 위한 "설계도"
## 객체: 설계도로부터 만들어낸 "제품"

## 클래스를 사용하는 이유
## LOL 인벤 챔피언들 정보: https://lol.inven.co.kr/dataninfo/champion/compare.php
## LOL 혹은 자신이 좋아하는 게임의 캐릭터 3가지를 선택하여 해당 캐릭터의 정보(채력, 공격력, 이동속도)를 입력하고,
## "게임 시작 인사, 캐릭터 능력을 각각 출력(함수)"등을 수행하는 프로그램을 만들어 보자

## case1: class를 활용하지 않은 경우
# 정보 출력 함수 정의
'''
# character_info() 함수 정의하기
def character_info(name, attack, health, speed):
    # name 출력
    # 기본 공격력(attack) 출력
    # 기본 체력(health) 출력
    # 기본 속도(speed) 출력

# character1 만들어주기(정보 할당)
    ## character1의 name 정의
    ## character1의 attack 정의
    ## character1의 health 정의
    ## character1의 speed 정의
print(f"{character1_name}님 소환사의 협곡에 오신 것을 환영합니다.")

# <character_info()를 호출하여 character1의 정보 출력하기 >

# character2 만들어주기(정보 할당)
    ## character1의 name 정의
    ## character1의 attack 정의
    ## character1의 health 정의
    ## character1의 speed 정의
print(f"{character1_name}님 소환사의 협곡에 오신 것을 환영합니다.")

character_info(character2_name, character2_attack, character2_health, character2_speed)
'''
## >> 캐릭터를 하나 만들 때마다 작성해야 하는 코드가 많고 복붙해서 수정하기도 귀찮다...

## case2: 클래스를 사용한 경우
# Character class 정의해주기
    # 생성자 정의 - name, attack, health, speed 입력
        # self.name
        # self.attack
        # self.healrh
        # self.speed
        # 소환사 협곡! 환영!

    # character_info() 메서드 정의
        # name 출력
        # attack 출력
        # health 출력
        # speed 출력

# 첫번째 캐릭터 만들기
# 두번쨰 캐릭터 만들기

# 첫번째 캐릭터의 character_info() 메서드 호출
# 두번째 캐릭터의 character_info() 메서드 호출