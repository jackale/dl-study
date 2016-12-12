import numpy as np
import gate

table = ((0,0), (0,1), (1,0), (1,1))

mes = '    ({0},{1}) => {2}'
methods = ['AND', 'OR', 'NAND', 'NOR', 'XOR']

for method_name in methods:
    try:
        method = getattr(gate, method_name)
        print(method_name)
        for x1, x2 in table:
            print(mes.format(x1, x2, method(x1, x2)))
    except AttributeError:
        print(method_name + ' is not defined.')
