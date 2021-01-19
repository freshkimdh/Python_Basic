# 함수 만들기
def print_root(a, b, c):
    r1 = a * b * c
    r2 = a + b + c
    print('곱셉은 {}, 덧셈은 {}'.format(r1,r2))

x = 5
y = 1
z = 3

print_root(x,y,z)

# 함수 리턴
def print_add(value) :
    result = value + 5
    return result

n = print_add(5)
print('리턴함수{} '.format(n))


# 초기값 True, False
def say(name, age, man=True):
    print("이름은",name)
    print("나이는",age)
    if man:
        print("남자")
    else:
        print("여자")

say("수진",55)
say("수진",25,False)

