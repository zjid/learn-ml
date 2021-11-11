# Retyped from
# https://www.askpython.com/python/examples/load-and-plot-mnist-dataset-in-python
# The network module is retyped from
# http://neuralnetworksanddeeplearning.com/chap1.html

from keras.datasets import mnist
from context import port
network = port.network

(train_x, train_y), (test_x, test_y) = mnist.load_data()
print('x train', train_x.shape)
print('y train', train_y.shape)
print('x test', test_x.shape)
print('y test', test_y.shape)

net = network.Network([784, 30, 10])
