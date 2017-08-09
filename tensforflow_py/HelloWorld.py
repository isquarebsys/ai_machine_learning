import tensorflow as tf

#Create a constant that contains a string
hello = tf.constant('Hello, TensorFlow!')

#Create a TensorFlow session
sess = tf.Session()

#Display the value of hello
print(sess.run(hello))

#If successful, the system outputs-> Hello, TensorFlow
