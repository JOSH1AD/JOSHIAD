# Ai반 2기 python 중급반 - 5주차 정규수업(16:30~18:30) mission
'''
[수업을 시작하기 전에!]
1. 웨일ON으로 원격 회의실 접속하기
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기~
5. 수업시간 집중~~~!! 딴 짓! 멈춰~~~~~!

[저번주 복습]
1. 딕셔너리 자료형 이론 및 연습문제 풀이
2. class의 기본 개념
'''

# [class(1) 넘어간 내용...]
## <class 생성 및 호출>
## <class 생성 문법>
## class 클래스 이름:
##     def 메서드 이름1(self, 입력변수1, 입력변수2, ...):
##         실행명령
##     def 메서드 이름2(self, 입력변수1, 입력변수2. ...):
##         실행명령

## <class 호출 문법>
## 클래스 선언하기: 인스턴스 = 클래스이름()
## 매서드 호출하기: 인스턴스.메서드()

## 연습문제: 모든 자료형은 class이다.
## 정수형, 실수형, 문자열, 불린형 등의 다양한 자료형을 가진 변수를 선언 후
## type() 명령을 통해 자료형을 출력하여 보자(class 확인 할 것)
## + 추가적으로 .__dir__() 역시 출력해보자
'''
a = 12              # int
b = 0.125           # float
c = '안녕하세요'      # str
d = True            # bool

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(a.__dir__())
print(b.__dir__())
print(c.__dir__())
print(d.__dir__())
'''

# [class(2)]
## <생성자>
## : 객체가 생성될 때 자동으로 호출되는 메서드.
## [문법] class 클래스이름:
##           def __init__(self, 입력변수들):
##               초기화 실행 문장

## class Mission1
## : Mission에 언급된 내용대로 Cat class를 만들어 보자
'''
class Cat:
    def cry(self):
        print('야옹')
    def tail_wag(self):
        print('야옹')
    def translate_cry(self):
        print('하찮은 닝겐!')
    def translate_tw(self):
        print('닝겐!')

Siamese = Cat()
Siamese.cry()
Siamese.tail_wag()
Siamese.translate_cry()
Siamese.translate_tw()
'''
## 생성자 연습문제
## : Monster 클래스를 만들고 step에 따라 생성자와 메서드가 추가된 Monster 클래스를 만들어보자.
## step1) 가장 기본적인 Monster 클래스를 만들어 보자
##        : say 메서드만을 가지는 Monster 클래스

'''
class Monster:
    def say(self):
        print('나는 아주아주아주아주아주아주 무서운 몬스터다!')
Goblin = Monster()
Goblin.say()
'''
## step2) Monster 클래스에 속성(name, health, attack, speed)을 추가하여 초기화해보자.
##        또한, 인스턴스 생성 시에 say의 내용이 출력되도록 만들어보자.
'''
class Monster:
    def __init__(self, name, health, attack, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.speed = speed
    def say(self):
        print(f'나는 아주아주아주아주아주아주 무서운 {self.name}다!')
Goblin = Monster('고블린', 100, 50, 30)
wolf = Monster('늑대', 200, 100, 50)
Goblin.say()
wolf.say()
'''
class Monster:
    def __init__(self, name, health, attack, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.speed = speed
    def say(self):
        print(f'나는 아주아주아주아주아주아주 무서운 {self.name}다!')
    def decrease_health(self, num):
        self.health -= num
    def get_health(self):
        return self.health
    def info(self):
        print(f'[{self.name}]')
        print(f'체력: {self.health}')
        print(f'공격력: {self.attack}')
        print(f'이동속도: {self.speed}')

Goblin = Monster('고블린', 100, 50, 30)
wolf = Monster('늑대', 200, 100, 50)

Goblin.say()
Goblin.info()
Goblin.decrease_health(50)
print()
print(Goblin.get_health())
print('------------------------------')
wolf.say()
wolf.info()

'''
<Monster 객체에 여러가지 메서드 추가하기 >

<golblin과 wolf를 Monster 객체로 선언하고 메서드 호출하기>
'''

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
<Monster class 작성하기>
'''

## step2) 자식 클래스: Wolf, Shark, Dragon
## - Monster 클래스를 상속 받을 것.
## - 몬스터의 속성에 맞게 move를 메서드 오버라이딩할 것.
'''
<Moster class를 상속받은 Wolf, Shark, Dragon class 작성하기>

<각 class들로 객체 만든 후, move 메서드 호출하기>
'''