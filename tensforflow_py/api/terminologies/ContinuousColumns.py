# You can specify a continuous feature like so

import tensorflow as tf
age = tf.contrib.layers.real_valued_column("age")
print(age)