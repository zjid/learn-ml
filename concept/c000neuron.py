# This code imitates the structure of sigmoid neuron.
# The sigmoid part is quantized poorly inside dictionary.

# Declace neuron object based on:
# - number of feeds (inputs) as number of elements in weight list
# - weight values
# - bias value

# Below, there are 2 sample models: model() and nand()

class neuron:

  # Poorly quantized sigmoid
  activator = {
    -4: 0,
    -3: 0.1,
    -2: 0.2,
    -1: 0.3,
    0: 0.5,
    1: 0.7,
    2: 0.8,
    3: 0.9,
    4: 1
  }

  def __init__(self, weight = [0, 0], bias = 0):
    '''Determine weights and bias.'''
    self.weight = weight
    self.bias = bias

  def __call__(self, feed):
    '''Feed size equals to weight size'''
    if type(feed) in [list, tuple, iter]:
      z = sum([self.weight[i] * feed[i] for i in range(len(self.weight))])
    else:
      z = self.weight[0] * feed
    return neuron.activator[int(max(-4, min(4, z + self.bias)))]

def model(feed = [0, 0]):
  '''I don't know what I'm doing.'''
  layer0 = [neuron([9, 1], 5) for i in range(2)]
  layer1 = [neuron(bias=-3) for i in range(2)]
  layer2 = [neuron([2, 2])]
  out0 = [n(feed) for n in layer0]
  print(out0)
  out1 = [n(out0) for n in layer1]
  print(out1)
  out2 = layer2[0](out1)
  print(out2)
# model([-1, 10])

def nand(feed = [0, 0]):
  '''Functional NAND gate with 2 inputs.'''
  layer0 = neuron([1, 1], -1)
  out0 = layer0(feed)
  layer1 = neuron([-100], 60)
  out1 = layer1(out0)
  print(out1)

# Test the NAND gate
for f in [[0,0], [0,1], [1,0], [1,1]]:
  nand(f)