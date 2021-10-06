Sharer: Selina Qian; Coder: Selina Qian
import numpy as np

def layer(shape,actv):

    def inner(inputs, weights, bias):
        h = actv(np.dot(inputs,weights)+bias)
        return h

    return inner
if __name__ == "__main__":
    N = 100 
    W = 3 
    C = 1 

    t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # Input data

    shape1 = [np.size(t), W] # Size of layer 1
    layer1 = layer(shape1, np.tanh) # Instantiate layer 1
    
    shape2 = [W, C] # Size of layer 2 (it's the output layer here)
    layer2 = layer(shape2, np.tanh) # Instantiate layer 2

    # Initialize weights and biases
    w1 = np.random.normal(0, 0.5, size=(shape1[0], shape1[1]))
    w2 = np.random.normal(0, 0.5, size=(shape2[0], shape2[1]))
    b1 = np.random.normal(0, 2, size=(1, shape1[1]))
    b2 = np.random.normal(0, 2, size=(1, shape2[1]))

    # Run through the network
    h1 = layer1(t, w1, b1) # First layer


    h2 = layer2(h1, w2, b2) # Last layer
    print('The result of the h2 layer :', h2)

