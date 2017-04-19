# Hằng số cũng có thể là một mảng
# Kết quả giá trị in ra cũng là một mảng !
# Input: x = [10, 15, 20]
# Output: y = [15, 20, 25]

import tensorflow as tf

x = tf.constant([10, 15, 20], name = 'x')
y = tf.Variable(x + 5, name = 'y')

model = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(model)
    result = session.run(y)
    print(result)