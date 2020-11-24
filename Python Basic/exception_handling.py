try:
    print(3/1)
    #print(3/0)

#except Exception as e:
#print(e)
except :
    print("0으로는 나눌 수 없습니다.")

else:
    print("예외 없이 성공적으로 실행 되었습니다.")

finally: #예외와 상관없이 무조건 실행하는 것
    print("예외 처리를 마칩니다")

