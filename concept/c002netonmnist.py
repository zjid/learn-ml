# The network module is retyped from
# http://neuralnetworksanddeeplearning.com/chap1.html

import numpy as np
from keras.datasets import mnist
from context import port
network = port.network

(train_x, train_y), (test_x, test_y) = mnist.load_data()
# print('x train', train_x.shape)
# print('y train', train_y.shape)
# print('x test', test_x.shape)
# print('y test', test_y.shape)
# print('sample x', train_x[0])
# print('sample y', train_y[0])

def vectorized(j):
  v = np.zeros([10, 1])
  v[j] = 1.0
  return v

# Restructure data
train_x = np.reshape(train_x, [60000, 784, 1])
train_x = train_x.astype(np.float) / 255.0 # due to overflow for np.exp()
train_y = [vectorized(y) for y in train_y]
test_x = np.reshape(test_x, [10000, 784, 1])
test_x = test_x.astype(np.float) / 255.0
# test_y = [vectorized(y) for y in test_y]

net = network.Network([784, 30, 10])
net.SGD(list(zip(train_x, train_y)), 30, 10, 3.0, list(zip(test_x, test_y)))

# Epoch 0: 9086 / 10000
# Epoch 1: 9220 / 10000
# Epoch 2: 9303 / 10000
# Epoch 3: 9334 / 10000
# Epoch 4: 9386 / 10000
# Epoch 5: 9405 / 10000
# Epoch 6: 9371 / 10000
# Epoch 7: 9452 / 10000
# Epoch 8: 9446 / 10000
# Epoch 9: 9452 / 10000
# Epoch 10: 9481 / 10000
# Epoch 11: 9450 / 10000
# Epoch 12: 9459 / 10000
# Epoch 13: 9468 / 10000
# Epoch 14: 9468 / 10000
# Epoch 15: 9481 / 10000
# Epoch 16: 9469 / 10000
# Epoch 17: 9475 / 10000
# Epoch 18: 9504 / 10000
# Epoch 19: 9475 / 10000
# Epoch 20: 9474 / 10000
# Epoch 21: 9468 / 10000
# Epoch 22: 9490 / 10000
# Epoch 23: 9492 / 10000
# Epoch 24: 9495 / 10000
# Epoch 25: 9488 / 10000
# Epoch 26: 9505 / 10000
# Epoch 27: 9494 / 10000
# Epoch 28: 9483 / 10000
# Epoch 29: 9465 / 10000

# Good for starter.