# PP5
# 2021-10-05
# Sharer: Selina (Lechen) Qian Coder: Yuhan Zhang
import numpy as np

class Layer():
    def __init__(self, shape, actv):
        self.actv = actv
        self.weights = np.random.uniform(-1.0, 1.0, size=shape)
        self.biases = np.random.normal(0.0, 0.1, size=shape[1])

    def forward(self, inputs):
        # your code
        z = np.dot(inputs, self.weights) + self.biases
        z = self.actv(z)
        return z

    def __repr__(self):
        # your code
        rep = 'The shape of the weights is ' + str(self.weights.shape) + '. \n The shape of the biases is ' + str(self.biases.shape) + '.'
        return rep
    
    def __str__(self):
        # your code
        rep = 'The number of inputs is ' + str(self.weights.shape[0]) + '.'
        return rep
    
    def __add__(self, other):
        # your choice
        if self.weights.shape[1] == other.weights.shape[1]:
          total_weights = self.weights + other.weights
          return Layer(total_weights.shape, self.actv)
        else:
          print('The shape of the two inputs should be the same.')


if __name__ == "__main__":

    t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # input to the network

    shape1 = [100,100]
    shape2 = [100,1]

    # Run through the network
    layer1 = Layer(shape1, np.tanh) # First layer
    layer2 = Layer(shape2, np.tanh) # Last layer

    h1 = layer1.forward(t)
    h2 = layer2.forward(h1)

# Try the three dunder functions

# Try __repr__
    print(repr(layer1))

# Try __str__
    print(layer1)

# Try __add__
    shape3 = [100, 100]
    layer3 = Layer(shape3, np.tanh)
    added_layer = layer1 + layer3
