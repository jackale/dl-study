import numpy as np

def init_nework():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network

def activate(x):
    return sigmoid(x)

def identity_function(x):
    return x

def output(x):
    return identity_function(x)
    


def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = activate(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = activate(a2)
    a3 = np.dot(z2, W3) + b3
    y = output(a3)

    return y

def step_function (x):
    y = x > 0
    return y.astype(np.int)

def sigmoid (x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

network = init_nework()
x = np.array([1.0, 0.5])

y = forward(network, x)
print(y)

