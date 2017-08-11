# http://tflearn.org/
# Install tflearn http://tflearn.org/installation/
    # pip install tflearn
# AttributeError: module 'tensorflow.contrib.learn' has no attribute 'input_data'

import tflearn

net = tflearn.input_data(shape=[None, 100, 5000])
net = tflearn.lstm(net, 64)
net = tflearn.dropout(net, 0.5)
net = tflearn.fully_connected(net, 5000, activation='softmax')
net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy')

model = tflearn.SequenceGenerator(net, dictionary=id(1), seq_maxlen=100)
model.fit(1, 2)
model.generate(50, temperature=1.0)