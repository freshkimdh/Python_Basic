# parameter 인자 - 메소드를 수행 할 때 필요한 입력값을 받는 변수를 의미합니다.

# 패킹
args = 1,2,3
print("args =", args)

# 언패킹
a,b,c = args
print("a = ",a)

x, *new_args = args
print(x)
print(new_args)


def func(a, b=3):
     return a + b

print(func(10, 10)) # 20 출력
print(func(10)) # 13출력
