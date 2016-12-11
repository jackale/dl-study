import numpy as np
import gate

table = ((0,0), (0,1), (1,0), (1,1))

mes = '    ({0},{1}) => {2}'
methods = ['AND', 'OR', 'NAND', 'NOR']

for method_name in methods:
    try:
        method = getattr(gate, method_name)
        print(method_name)
        for x1, x2 in table:
            x = np.array([x1, x2])
            print(mes.format(x1, x2, method(x)))
    except AttributeError:
        print(method_name + ' is not defined.')
