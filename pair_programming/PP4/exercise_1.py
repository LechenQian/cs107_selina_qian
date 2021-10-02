import numpy as np

def layer(shape,actv):

    def inner(inputs, weights, bias):
        h = actv(np.dot(inputs,weights)+bias)
        return h

    return inner

t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # input to the network
shape1 = [100,50]
shape2 = [50,1]

layer1 = layer(shape1, np.tanh) # Define layer 1
layer2 = layer(shape2, np.tanh) # Define layer 2

# Initialize weights and biases
w1 = np.random.normal(0, 0.5, size=(shape1[0], shape1[1]))
w2 = np.random.normal(0, 0.5, size=(shape2[0], shape2[1]))
b1 = np.random.normal(0, 2, size=(1, shape1[1]))
b2 = np.random.normal(0, 2, size=(1, shape2[1]))

# Run through the network
h1 = layer1(t, w1, b1) # First layer


h2 = layer2(h1, w2, b2) # Last layer
print('The result of the h2 layer :', h2)

