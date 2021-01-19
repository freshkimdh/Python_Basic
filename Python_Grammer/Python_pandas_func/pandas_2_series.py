import pandas as pd

# 길이가 다르더라도 데이터 공간이 생성되어 더해진다.

array1 = pd.Series([1,2,3], index=['a','b','c'])
array2 = pd.Series([4,5,6], index=['b','c','d'])


# fill_value = 0 : 0의 경우는 해당 index
array = array1.add(array2, fill_value=0)
print(array)
 
