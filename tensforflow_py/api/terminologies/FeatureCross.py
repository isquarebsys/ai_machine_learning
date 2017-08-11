# Because linear models assign independent weights to separate features,
#   they can't learn the relative importance of specific combinations of feature values
    # If you have a feature 'favorite_sport' and a feature 'home_city' and you're trying to predict whether a person likes to wear red,
    #  your linear model won't be able to learn that baseball fans from St. Louis especially like to wear red.
#   You can get around this limitation by creating a new feature 'favorite_sport_x_home_city'.
        # The value of this feature for a given person is just the concatenation
        # of the values of the 2 source features: 'baseball_x_stlouis', for example. This sort of combination feature is called a feature cross

# The crossed_column() method makes it easy to set up feature crosses:


sport = tf.contrib.layers.sparse_column_with_hash_bucket(\
    "sport", hash_bucket_size=1000)
city = tf.contrib.layers.sparse_column_with_hash_bucket(\
    "city", hash_bucket_size=1000)
sport_x_city = tf.contrib.layers.crossed_column(
    [sport, city], hash_bucket_size=int(1e4))