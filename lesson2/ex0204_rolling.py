import tensorflow as tf
import numpy as np

mean = tf.Variable(0., name = 'mean')
n = 10000

model = tf.global_variables_initializer()

with  tf.Session() as session:
    for i in range(5):
        session.run(model)
        
        arr = np.random.randint(1000, size = n)
        sum = np.sum(arr)

        mean = (mean + sum) / n

        session.run(model)
        result = session.run(mean)
        print(result)
