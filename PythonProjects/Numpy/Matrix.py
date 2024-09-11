from numpy import *
# import numpy as m
# arr = m.array([[12,35,61,],[95,67,28]])
# print(arr)
# mat = m.matrix(arr)         # Convert Array into Matrix
# print(mat)

# mat = matrix('15 38; 28 28 ; 36 95 ;3 2')
# print(mat)

import numpy as np
from functools import reduce
arr2 = np.array([1, 15, 5, 0], dtype='bool')
# for i in arr2:
#     print(i)

res = reduce(lambda a, b: (for i in arr2), arr2)
print(res)
# def ch(array):
#     for i in array:
#         print(i)
# ch(np.array([1,15,5,0],dtype='bool'))



