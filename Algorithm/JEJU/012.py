
# 11. 1부터 100까지 모두 더하는 for 문 사용
s = 0

for i in range(1,101) : # 1 이상 101 미만
    s += i

# print(s)    

# ================================================= # 

# 12. 게임 캐릭터 클래스 만들기
# self - 클래스의 인스턴스 지칭

class Wizard:
    # 초기화 메소드
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    
    # 클래스 정보를 출력하는 메소드
    def attack(self):
        print("파이어볼")


x = Wizard(health=545, mana=210, armor=10)
print(x.health, x.mana, x.armor)
x.attack()

