# https://www.tensorflow.org/api_docs/python/tf/zeros
# For example: tf.zeros([3, 4], tf.int32) ==> [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

import tensorflow as tf
data=tf.zeros([3, 4], tf.int32)
print(data)

singleDimension=tf.Variable(tf.zeros([10]))
print(singleDimension)