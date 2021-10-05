import numpy as np

class Layer():
    def __init__(self, shape, actv):
        self.actv = actv
        self.weights = np.random.uniform(-1.0, 1.0, size=shape)
        self.biases = np.random.normal(0.0, 0.1, size=shape1[1])

    def forward(self, inputs):
        z = np.dot(inputs, self.weights) + self.biases
        z = self.actv(z)
        return z

    def __repr__(self):
        rep = 'Layer(initial wegihts:' + self.weights + ', initial biases' + self.biases + 'activation function:' + str(self.actv) +'.'
        return rep
    
    def __str__(self):
        return 'Layer(activation function:' + str(self.actv) +'.'

    def __add__(self, other):
        added_weights = self.weights + other.weights
        
        return added_weights


if __name__ == "__main__":

    t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # input to the network

    shape1 = [100,100]
    shape2 = [100,1]

    # Run through the network
    layer1 = Layer(shape1, np.tanh) # First layer
    layer2 = Layer(shape2, np.tanh) # Last layer

    h1 = layer1.forward(t)
    h2 = layer2.forward(h1)
    added_weights = layer1 + layer2
