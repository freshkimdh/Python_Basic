# 11. 1부터 100까지 모두 더하는 for 문 사용

s = 0 

for i in range(1,101):
    s += i

# print(s)

# ================================================= # 

# 12. 게임 캐릭터 클래스 만들기

class Wizard:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def attack(self):
        print("파이어볼")


# x = Wizard(health=545, mana=210, armor=10)
# print(x.health, x.mana, x.armor)
# x.attack()

# ================================================= # 

# 13. 몇번째 행성?
# 행성의 순서를 나타내는 숫자 n이 입력됩니다. 예를 들어 수성은 첫번째 행성 입니다.
# 출력으로 그 순서에 해당하는 행성의 이름을 출력하세요.

planets = ['수성','금성','지구','화성','목성','토성','천왕성','혜성']

n = int(input()) - 1
print(planets[n])