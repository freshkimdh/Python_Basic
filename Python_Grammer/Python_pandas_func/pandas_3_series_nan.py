import pandas as pd

array1 = pd.DataFrame([[1, 2], [3, 4]], index=['A', 'B'])
array2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['B', 'C', 'D'])

print(array1)
print(array2)

array = array1.add(array2, fill_value=0) # 0,1,2 차이 알기
print(array)
 
