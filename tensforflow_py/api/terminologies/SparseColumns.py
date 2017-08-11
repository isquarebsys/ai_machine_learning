import tensorflow as tf

eye_color = tf.contrib.layers.sparse_column_with_keys(
  column_name="eye_color", keys=["blue", "brown", "green"])

print(eye_color)

# You can also generate FeatureColumns for categorical features for which you don't know all possible values
# For this case you would use sparse_column_with_hash_bucket(), which uses a hash function to assign indices to feature values
education = tf.contrib.layers.sparse_column_with_hash_bucket(\
    "education", hash_bucket_size=1000)

print(education)