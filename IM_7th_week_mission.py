# Ai반 2기 python 중급반 - 7주차 정규수업(16:30~18:30) mission
'''
[수업을 시작하기 전에!]
1. 웨일ON으로 원격 회의실 접속하기
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기~
5. 수업시간 집중~~~!! 딴 짓! 멈춰~~~~~!

[저번주 복습]
1. class: 상속
2. class: super()와 클래스 변수
'''

# [class(3) 이어서...]
## class Mission: 아이템 구성안과 설계도를 활용하여, class와 객체를 생성해 보자
## 이때, 부모 클래스: Item // 자식 클래스: WearableItem, UsableItem 이다.
'''
## 아이템 클래스
## 모든 아이템들의 아이템 수를 500개로 제한한다.(클래스 변수)

## 장비 아이템 클래스
class WearableItem(Item):

# 소모품 아이템 클래스

# 객체 생성(각 객체 생성 및 테스트)
'''

# [예외처리]
# : 프로그램 실행 중에 발생하는 예외를 미연에 방지하는 것.
'''
## 예외처리가 필요한 이유 예시:  계산기 프로그램
num1 = int(input("첫 번째 숫자를 입력해 주세요(숫자를 입력해 주세요): "))
num2 = int(input("두 번째 숫자를 입력해 주세요(숫자를 입력해 주세요): "))
print(num1+num2)
'''
## 예외처리 연습문제: 환율 계산 문제
'''
try:
    won = float(input("원화 입력>>  "))
    dollar = float(input("달러 입력>>  "))
    exchange_rage = won / dollar
except ValueError as e:
    print("문자열 처리 예외가 발생하였습니다.", e)
except ZeroDivisionError as e:
    print("분모에는 0이 들어갈 수 없습니다", e)
else:
    print("오류가 발생하지 않았습니다.")
finally:
    print("얘는 그냥 실행 돼")
'''


'''
## 에러 발생시키기 연습문제
kkaak = input("문자열을 입력해주세요: >>")
if kkaak == "까마귀 날자":
    raise Exception("배 떨어진다.")
'''
'''
## 예외처리 Mission: 영어단어 공부하기 문제를 'while문 + 예외 처리'로 풀어보자
word = ['oh sujin', 'Pneumonoultramicroscopicsilicovolcanoconiosis', 'Supercalifragilisticexpialidocious']
i=0
count = 0
while True:
    try:
        print(word[i])
    except:
        break
    temp = input()
    if temp == word[i]:
        count += 1
    i += 1
print(f"전체 개수: {len(word)}")
print(f"맞은 개수: {count}")
print(f"틀린 개수: {i-count}")
'''
# [파일 입출력]
## 파일 입출력 연습문제1: 파일 쓰기(w: 새로쓰기 혹은 덮어쓰기)

f = open("test.txt", 'w', encoding= 'utf-8')
f.write('안녕하세요 :D')
f.close()

## 파일 입출력 연습문제2: 파일 추가하기(a: 추가하기)


## 파일 입출력 연습문제3: 파일 읽기(r: 읽기)
## way1) readline 함수 사용(한 줄 씩 읽어오기)


## way2) readlines 함수 사용(모든 줄을 읽어와, 각 줄을 리스트의 요소로 반환)


## way3) read 함수 사용(문서 전체를 하나의 문자열로 가져오기)


# [이벤트 처리]
## turtle 마우스 이벤트 처리 연습문제
'''
# <import>
# turtle & random 

# randomColor 함수: 랜덤한 r,g,b 값을 반환하는 함수
def randomColor():
    # r: random.random(): 0~1상이의 랜덤한 값 할당
    # g
    # b
    # return

# leftClick 핸들링 함수: 거북이 스탬프 모양을 찍는 함수
def turtleStamp(x, y):
    # 거북이 숨기기
    # (x,y)좌표로 거북이 이동
    # 랜덤하게 거북이의 머리 방향 지정(0~360도)
    # 랜덤하게 거북이의 크기 설정(1~10)
    # 랜덤 r,g,b 값 가져오기(randomColor 함수 사용하기)
    # 스템프 색상 설정(랜덤 r,g,b 값 넣기)
    # 스템프 테두리 색성 설정(랜덤 r,g,b 값 넣기)
    # 스템프 찍기 명령

# 프로그램 제목 지정
# 도장 모양을 turtle으로 설정
# 속도 설정
# 펜 들기

# 이벤트 설정: onscreenclick


'''

## turtle 마우스 이벤트 처리 Mission
'''
# <import>
# turtle & random 

# randomColor 함수: 랜덤한 r,g,b 값을 반환하는 함수
def randomColor():
    # r: random.random(): 0~1상이의 랜덤한 값 할당
    # g
    # b
    # return

# leftClick 이벤트 핸들링 함수: 거북이 스탬프 모양을 찍는 함수
def leftClick(x, y):
    # 거북이 숨기기
    # (x,y)좌표로 거북이 이동
    # 랜덤하게 거북이의 머리 방향 지정(0~360도)
    # 랜덤하게 거북이의 크기 설정(1~10)
    # 랜덤 r,g,b 값 가져오기(randomColor 함수 사용하기)
    # 스템프 색상 설정(랜덤 r,g,b 값 넣기)
    # 스템프 테두리 색성 설정(랜덤 r,g,b 값 넣기)
    # 스템프 찍기 명령

# rightClick 이벤트 핸들링 함수: 화면을 초기화하는 함수
def rightClick(x, y):
    # 화면 초기화

# 프로그램 제목 설정 
# 도장 모양을 turtle으로 설정
# 속도 설정
# 펜 들기

# 왼쪽 클릭 이벤트 설정 
# 오른쪽 클릭 이벤트 설정


'''

## turtle 키보드 마우스 처리 연습문제
'''
# <import>
# turtle & random 

# randomColor 함수: 랜덤한 r,g,b 값을 반환하는 함수
def randomColor():
    # r: random.random(): 0~1상이의 랜덤한 값 할당
    # g
    # b
    # return

# up 이벤트 핸들링 함수: 
def up():
    # 가려는 방향에 맞게 방향설정
    # 랜덤 색상 r,g,b 가져오기
    # 펜 색상 설정
    # 거북이의 색상도 같이 설정
    # 10만 큼 이동

# down 이벤트 핸들링 함수: 아래방향으로 10만큼 이동 및 색상 변화
def down():
    # 가려는 방향에 맞게 방향설정
    # 랜덤 색상 r,g,b 가져오기
    # 펜 색상 설정
    # 거북이의 색상도 같이 설정
    # 10만 큼 이동

# 프로그램 제목 설정
# 배경색 설정
# 모양을 turtle로 설정 
# 펜 사이즈를 10으로 설정

# up 함수 이벤트 처리(onpress)
# down 함수 이벤트 처리(onpress)
# listen을 실행시켜 주어야 키 입력 모두가 실행되어 입력키에 반응함.

'''

## turtle 키보드 마우스 처리 Mission
## 추가 활동: Star.mp3 배경음 넣기
'''
# <import>
# turtle & random 

# randomColor 함수: 랜덤한 r,g,b 값을 반환하는 함수
def randomColor():
    # r: random.random(): 0~1상이의 랜덤한 값 할당
    # g
    # b
    # return

# up 이벤트 핸들링 함수: 위 방향으로 10만큼 이동 및 색상 변화
def up():
    # 가려는 방향에 맞게 방향설정
    # 랜덤 색상 r,g,b 가져오기
    # 펜 색상 설정
    # 거북이의 색상도 같이 설정
    # 10만 큼 이동

# down 이벤트 핸들링 함수: 아래방향으로 10만큼 이동 및 색상 변화
def down():
    # 가려는 방향에 맞게 방향설정
    # 랜덤 색상 r,g,b 가져오기
    # 펜 색상 설정
    # 거북이의 색상도 같이 설정
    # 10만 큼 이동
    
# right 이벤트 핸들링 함수: 오른쪽으로 10만큼 이동 및 색상 변화
def right():
    # 가려는 방향에 맞게 방향설정
    # 랜덤 색상 r,g,b 가져오기
    # 펜 색상 설정
    # 거북이의 색상도 같이 설정
    # 10만 큼 이동
    
# left 이벤트 핸들링 함수: 왼쪽으로 10만큼 이동 및 색상 변화
def left():
    # 가려는 방향에 맞게 방향설정
    # 랜덤 색상 r,g,b 가져오기
    # 펜 색상 설정
    # 거북이의 색상도 같이 설정
    # 10만 큼 이동

# clear_bg: 배경 초기화
def clear_bg():
    
# close_window: 프로그램을 종료하는 함수
def close_window():
    t.bye()

# 프로그램 제목 설정
# 배경색 설정
# 모양을 turtle로 설정 
# 펜 사이즈를 10으로 설정

# up 함수 이벤트 처리(onpress)
# down 함수 이벤트 처리(onpress)
# right 함수 이벤트 처리(onpress)
# left 함수 이벤트 처리(onpress)
# cleag_bg 함수 이벤트 처리(onpress)
# cloase_window 함수 이벤트 처리(onpress)
# listen을 실행시켜 주어야 키 입력 모두가 실행되어 입력키에 반응함.


'''

