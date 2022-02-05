# Ai반 2기 python 중급반 - 11주차 정규수업(16:30~18:30) mission
'''
[수업을 시작하기 전에!]
1. 웨일ON으로 원격 회의실 접속하기
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기~
5. 수업시간 집중~~~!! 딴 짓! 멈춰~~~~~!
'''

# Problem 1: 평균은 넘겠지
'''
T = int(input())
N = []
scores = []
result = []
for i in range(T):
    temp = list(map(int, input().split()))
    N.append(temp[0])
    scores.append(temp[1:])

for i in range(T):

    # step1) 각 케이스마다 평균 구하기
    avg = sum(scores[i]) / N[i]

    # step2) 평균이 넘는 사람 수 세기
    count = 0
    for score in scores[i]:
        if score > avg:
            count += 1

    # step3) % 구하기
    percent = count / N[i] * 100
    result.append(percent)

for i in result:
    print(f"{i:.3f}%")
'''
# Problem 2: 셀프 넘버

import copy

N = 10000
numbers = [True] * (N+1)

def d(n):
    temp = n + sum(list(map(int, list(str(n)))))
    if temp <= N:
        numbers[temp] = False

for i in range(1, N+1):
    d(i)

for i in range(1, N+1):
    if numbers[i] == True:
        print(i)

