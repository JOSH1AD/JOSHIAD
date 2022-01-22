# Ai반 2기 python 중급반 - 10주차 정규수업(16:30~18:30) mission
'''
[수업을 시작하기 전에!]
1. 웨일ON으로 원격 회의실 접속하기
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기~
5. 수업시간 집중~~~!! 딴 짓! 멈춰~~~~~!

[저번주 복습]
1. 이벤트 처리 프로그램
2. turtle을 활용한 키보드 이벤트 처리
'''
'''
print("강한친구 대한육군 \n"*2)
'''
# Problem 1: 윤년
'''
year = int(input())
if year%4 == 0 and year%100 != 0 or year%400 == 0:
    print(1)
else:
    print(0)
'''
# Problem 2: 별찍기 - 2
'''
N = int(input())

for i in range(1, N+1):
    print(' '*(N-i), '*'*i, sep='')
'''
# Problem 3: X보다 작은 수
N, X = map(int, input().split())
numbers = list(map(int, input().split()))

for num in numbers:              #for i in range(N)
    if num < X:                  # if numbers[i] < X:
        print(num, end=' ')      #print(numbers[i], end=' ')




# Problem 4: 더하기 사이클



# 추가문제: ACM 호텔

