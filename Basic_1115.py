# if 문
print("if문")
hungry = True
if hungry:
    print("I am hungry")

hungry = False
if hungry:
    print("I am hungry")
else:
    print("I am not hungry")

# for 문
print("for 문")
for i in[1,2,3]:
    print(i)

# 함수
print("함수")
def hello():
    print("Hello World!")
hello()

#클래스
print("클래스")
class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good bye " + self.name + "!")

m = Man("DaeHwan")
m.hello()
m.goodbye()
