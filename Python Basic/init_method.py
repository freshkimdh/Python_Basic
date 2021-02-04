
# 생성자, 클래스 인스턴스가 생성될 때 호출 됨
# self 인자는 항상 첫번째에 오며 자기 자신을 가리킴
# 이름이 꼭 self일 필요는 없지만, 관례적으로 self로 사용
# 생성자에서는 해당 클래스가 다루는 데이터를 정의

class Person:
    def __init__(self, name, age=10): # self는 기본적으로 오는 파라미터
        # print(self, 'is generated')
        self.name = name
        self.age = age

# 각각 다른 메모리 주소에 객체가 생성
# p1 = Person()
# p2 = Person()

# print(p1.name, p1.age)

# p1.name = 'aaron'
# p1.age = 20

# print(p1.name, p1.age)

p1 = Person('Bob', 30)
p2 = Person('Kate', 20)
p3 = Person('Aaron')

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)




# init 함수는 객체 생성될 때 불러와짐
# call 함수는 인스턴스 생성될 때 불러와짐

class A:
    def __init__(self):
        print('init')
    def __call__(self):
        print('call')

a = A()

a()

print('a = ',a)
