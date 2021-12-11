# Ai반 2기 python 중급반 - 6주차 정규수업(16:30~18:30) mission
'''
[수업을 시작하기 전에!]
1. 웨일ON으로 원격 회의실 접속하기
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기~
5. 수업시간 집중~~~!! 딴 짓! 멈춰~~~~~!

[저번주 복습]
1. class의 구성과 문법
2. class 생성자
'''


# [class (2)-1: 상속]
## <상속>
## : 부모 클래스의 속성과 메서드를 자식클래스가 물려받을 수 있도록 만든 기능
## 상속을 사용하는 이유: 클래스들에 중복된 코드를 제거하고 유지보수를 하기 위해 사용하기 위해서 사용.

## <메서드 오버라이딩(덮어쓰기)>
## : 부모 클래스에 있는 메서드를 자식클래스에서 동일한 이름으로 다시 만드는 것

## 상속 연습문제
## :Monster 클래스를 만들고, 상속을 활용하여 Wolf, Shark, Dragon 클래스를 만들어,각각의 객체를 생성해보자.
##
## step1) 부모 클래스: Monster 클래스 정의하기
## - 속성: name, health, attack
## - 메서드: move("self.name 지상에서 이동하기"를 출력하는 메서드, 이후 해당 몬스터의 이동방법이 출력되도록 할 것임.)
'''
import random

class monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

class wolf(monster):
    pass

class shark(monster):
    def move(self):
        print(f"[{self.name}] 헤엄치기!!!!!")

class dragon(monster):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
    
    
    def move(self):
        print(f"[{self.name}] 비행!!!!!!!")

Wolf = wolf('야생늑대', 50, 10)
Wolf.move()

baby_shark = shark("아기상어", 10000, 5000)
baby_shark.move()

D = dragon("용제", 1000000, 1000000)
D.move()
'''
## step2) 자식 클래스: Wolf, Shark, Dragon
## - Monster 클래스를 상속 받을 것.
## - 몬스터의 속성에 맞게 move를 메서드 오버라이딩할 것.
'''
<Moster class를 상속받은 Wolf, Shark, Dragon class 작성하기>

<각 class들로 객체 만든 후, move 메서드 호출하기>
'''


# [class(3): supuer()와 클래스 변수]
## <super()와 클래스변수>
## super(): 부모클래스의 메서드들의 내용들을 그대로 가져와  자식 클래스 추가하고 싶은 경우에 사용하는 명령
## 클래스변수: 해당 클래스로 만든 모든 객체들이 공유하는 변수\
import random
class monster:
    max_num = 10
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")


class wolf(monster):
    pass


class shark(monster):
    def move(self):
        print(f"[{self.name}] 헤엄치기!!!!!")


class dragon(monster):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ["화염방사", "울부짖기", "플레어"]
        self.effect = [" 효과는 굉장했다! ", " 효과가 별로인 듯하다! "]



    def skill(self):
        print(f"[{self.name}] 은(는) [{self.skills[random.randint(0,2)]}]을(를) 사용했다! [{self.effect[random.randint(0,1)]}]")

    def move(self):
        print(f"[{self.name}] 비행!!!!!!!")\

D = dragon('용제', 500000000000, 50000000000)
D.skill()
'''
Wolf = wolf("늑대", 50, 100)
print(f"늑대 생성 후: {Wolf.max_num}")

baby_shark = shark("아기상어", 50, 60)
print(f"상어 생성 후: {baby_shark.max_num}")

D = dragon("디워", 5, 5)
print(f"날아다니는 도마뱀 생성 후: {D.max_num}")
'''

## super()와 클래스 변수 연습문제: RPG게임 업데이트
## : ‘상속 및 메서드 오버라이딩 연습문제’에서 만들었던 내용들을 업데이트해보자
## - 드래곤 클래스에 ‘인스턴스 속성’으로 ‘3개의 스킬(불뿜기, 꼬리치기, 날개치기)’을 추가
## - 드래곤이 스킬을 쓰면 속성 중 하나가 무작위로 사용되도록 설정(random 모듈 이용)
'''
import random
# 부모 클래스
# class Monster 작성

# 자식 클래스
# class Wolf 작성
# class Shark 작성
# class Dragon 작성

# wolf 객체 생성 및 move 호출, max_num 확인
# shark 객체 생성 및 move 호출, max_num 확인
# dragon 객체 생성 및 move 호출, max_num 확인
'''

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

## 예외처리가 필요한 이유 예시:  계산기 프로그램


## 예외처리 연습문제: 환율 계산 문제


## 에러 발생시키기 연습문제


## 예외처리 Mission: 영어단어 공부하기 문제를 'while문 + 예외 처리'로 풀어보자

