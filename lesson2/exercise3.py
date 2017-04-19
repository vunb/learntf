import tensorflow as tf

x = tf.Variable(0, name = 'x')

model = tf.global_variables_initializer()

with tf.Session() as session:
    for i in range(5):
        session.run(model)
        x = x + 2
        result = session.run(x)
        print(result)