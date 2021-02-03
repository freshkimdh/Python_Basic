
# 파이썬의 method는 항상 첫번째 인자로 self를 전달
# self는 현재 해당 메소드가 호출되는 객체 자신을 가리킴
# java의 this에 해당
# 이름은 self 일 필요는 없으나, 관례적으로 self 사용

# self는 객체 자신을 가리키는 것 (할당된 메모리 주소)

class Person:
    def __init__(self, name, age):
        print('self', self)
        self.name = name
        self.age = age

    def sleep(self):
        print('self: ', self)
        print(self.name, '은 잠을 잡니다.')

a = Person('Aaron', 20)
b = Person('Bob', 30)

print(a)
print(b)

a.sleep()
b.sleep()
