# http://tflearn.org/
# Error: AttributeError: module 'tensorflow.contrib.learn' has no attribute 'fully_connected'
    # pip install tflearn

import tflearn

tflearn.init_graph(num_cores=8, gpu_memory_fraction=0.5)
net = tflearn.input_data(shape=[None, 784])
net = tflearn.fully_connected(net, 64)
net = tflearn.dropout(net, 0.5)
net = tflearn.fully_connected(net, 10, activation='softmax')
net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy')

model = tflearn.DNN(net)
model.fit(1, 2)