import numpy as np
def perceptron (w, b):
    return lambda x: 1 if (b + np.sum(w*x)) > 0 else 0

AND  = perceptron(np.array([0.5, 0.5]), -0.7)
OR   = perceptron(np.array([0.8, 0.8]), -0.7)
NAND = perceptron(np.array([-0.5, -0.5]), 0.7)
NOR   = perceptron(np.array([-0.8, -0.8]), 0.7)
