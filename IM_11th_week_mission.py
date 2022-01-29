# Ai반 2기 python 중급반 - 11주차 정규수업(16:30~18:30) mission
'''
[수업을 시작하기 전에!]
1. 웨일ON으로 원격 회의실 접속하기
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기~
5. 수업시간 집중~~~!! 딴 짓! 멈춰~~~~~!
'''

# Problem 1: 더하기 사이클
import copy

N = int(input())

if N < 10:
    N *= 10

dummy = copy.copy(N)
count = 0

while True:

    dummy = (dummy%10)*10 + ((dummy//10) + (dummy%10))%10
    count += 1
    if N == dummy:
        break

print(count)
# Problem 2: 평균은 넘겠지

T = int(input())
N = []
scores = []

for i in range(T):
    temp = list(map(int, input().split()))
    N.append(temp[0])
    scores.append(temp[1:])

for i in range(T):
# Problem 3: 셀프 넘버


# 추가 문제: ACM 호텔

