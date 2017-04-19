import math
import numpy as np
import tensorflow as tf

x = np.random.randint(1000, size = 10000)
# x2 = tf.Variable(math.pow(x, 2))
y = tf.Variable(5 * x * x - 3 * x + 15)

print(len(x))

model = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(model)
    result = session.run(y)
    print(x)
    print(result)
