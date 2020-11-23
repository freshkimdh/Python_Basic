
#클래스의 멥버: 클래스 내부에 포함되는 변수
#클래스의 함수: 클래스 내부에 포함되는 함수, 메소드라고 부릅니다.

#상속: 다른 클래스의 멤버 변수와 메소드를 물려 받아 사용하는 기법
#부모와 자식 관계가 존재
#자식 클래스: 부모 클래스를 상속 받은 클래스
class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(self.name, "이(가) 공격을 수행합니다. [ 전투력:", self.power, "]")

unit = Unit("홍길동", 375)
unit.attack()

class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type

monster = Monster("슬라임", 10, "초급")
monster.attack()
