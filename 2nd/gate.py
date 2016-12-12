import numpy as np
def perceptron (w1, w2, b):
    w = np.array([w1, w2])
    return lambda x1, x2: 1 if (b + np.sum(w*np.array([x1,x2]))) > 0 else 0

AND  = perceptron(0.5, 0.5, -0.7)
OR   = perceptron(0.8, 0.8, -0.7)
NAND = perceptron(-0.5, -0.5, 0.7)
NOR  = perceptron(-0.8, -0.8, 0.7)

def XOR (x1, x2):
    s1 = OR(x1, x2)
    s2 = NAND(x1, x2)
    return AND(s1, s2)
