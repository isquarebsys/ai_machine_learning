from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
# import urllib
import urllib.request

import numpy as np
import tensorflow as tf

# Data sets
SQUARE_TRAINING = "D:/ws/git/ai_machine_learning/tensforflow_py/square_test/squares_data.csv"
SQUARE_TEST = "D:/ws/git/ai_machine_learning/tensforflow_py/square_test/squares_data.csv"

def main():
  # If the training and test sets aren't stored locally, download them.
  # if not os.path.exists(IRIS_TRAINING):
  #   # raw = urllib.urlopen(IRIS_TRAINING_URL).read()
  #   raw = urllib.request.urlopen(IRIS_TRAINING_URL).read()
  #   with open(IRIS_TRAINING, "wb") as f:
  #     f.write(raw)
  #
  # if not os.path.exists(IRIS_TEST):
  #   raw = urllib.request.urlopen(IRIS_TEST_URL).read()
  #   with open(IRIS_TEST, "wb") as f:
  #     f.write(raw)

  # Load datasets.
  # target_dtype, takes the numpy datatype of the dataset's target value
  # features_dtype, which takes the numpy datatype of the dataset's feature values
  training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=SQUARE_TRAINING,
      target_dtype=np.float32,
      features_dtype=np.float32)
  test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=SQUARE_TEST,
      target_dtype=np.float32,
      features_dtype=np.float32)

  # Specify that all features have real-value data
  # All the feature data is continuous
  #     so tf.contrib.layers.real_valued_column is the appropriate function to use to construct the feature columns
  #     There are 2 features in the data set->input and the squared number
  feature_columns = [tf.contrib.layers.real_valued_column("", dimension=2)]

  # Build 3 layer DNN with 1, 2, 1 units respectively
  # tf.contrib.learn offers a variety of predefined models, called Estimators [to run training and evaluation operations on your data]
  # Here, you we use a Deep Neural Network Classifier model to fit the data

  classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                              hidden_units=[1, 2, 1],
                                              n_classes=2,
                                              model_dir="/tmp/square_model")
      # hidden_units: 3 hidden layers, containing 1, 2, and 1 neurons respectively
      # n_classes=2. represent whether is is square or not
      # model_dir: directory in which TensorFlow will save checkpoint data during model trainingd


  # Define the training inputs
  def get_train_inputs():
    x = tf.constant(training_set.data)
    y = tf.constant(training_set.target)
    return x, y
    # Datasets in tf.contrib.learn are named tuples; you can access feature data and target values via the data and target fields
    # We define as constants because the data is small enough that it can be stored in TensorFlow constants


  # Fit model.
  classifier.fit(input_fn=get_train_inputs, steps=1000)
  # The state of the model is preserved in the classifier, which means you can train iteratively if you like.
    # For example, the above is equivalent to the following
        # classifier.fit(x=training_set.data, y=training_set.target, steps=1000)
        # classifier.fit(x=training_set.data, y=training_set.target, steps=1000)


  # Define the test inputs
  def get_test_inputs():
    x = tf.constant(test_set.data)
    y = tf.constant(test_set.target)

    return x, y

  # Evaluate accuracy.
  accuracy_score = classifier.evaluate(input_fn=get_test_inputs,steps=1)["accuracy"]
    # Your accuracy result may vary a bit, but should be higher than 90%. Not bad for a relatively small data set!
  print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

  # Classify 2 new flower samples.
  def new_samples():
    return np.array(
      [[3,9],
       [2,4]], dtype=np.float32)

  predictions = list(classifier.predict(input_fn=new_samples))

  print(
      "New Samples, Class Predictions:    {}\n"
      .format(predictions))

if __name__ == "__main__":
    main()