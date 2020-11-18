import numpy as np
import tensorflow as tf

list_data = [1,2,3]
array = np.array(list_data)

print(array.size)
print(array.dtype)

print("test")

hello = tf.constant("hello world!")
sess = tf.Session()
print(sess.run(hello))