 # -*- coding: utf-8 -*-     
import numpy as np
from numpy.linalg import *
def main():
    lst = [[1,3,5],[2,4,6]]
    print(type(lst))
    np_lst = np.array(lst)
    print(type(np_lst))
    np_lst2 = np.array(lst, dtype=np.float)
    #2 Some Arrays
    print(np_lst2.shape) 
    print(np_lst2.ndim) 
    print(np_lst2.dtype)
    print(np_lst2.itemsize)
    print(np_lst2.size)
    #2 Some Arrays
    print(np.zeros([2,4]))
    print(np.ones([3,5]))
    print("Rand:")
    print(np.random.rand(2,4))
    print(np.random.rand())
    print("RandInt:")
    print(np.random.randint(1,10,3))
    print("Randn:")
    print(np.random.randn(2,4))
    print("Chioce:")
    print(np.random.choice([10, 20, 30]))
    print("Distribute:")
    print(np.random.beta(1,10,100))
    #3 Array Opes
    lst2=np.arange(1,11).reshape([2,-1])
    print(lst2)
    print("Exp")
    print(np.exp(lst))
    print("Exp2")
    print(np.exp2(lst))
    print("Sqrt")
    print(np.sqrt(lst))
    print("Sin")    
    print(np.sin(lst))
    print("Log")    
    print(np.log(lst))

    list = np.array([[[1, 2, 3, 4],
                      [4, 5, 6, 7, ]],
                    [[7, 8, 9, 10],
                    [11, 12, 13, 14]],
                    [[15, 16, 17, 18],
                    [19, 20, 21, 22]]
                     ])
    # axis取值跟维数有关，维数从 0 开始算起，axis值越大，深入的程度越深
    print(list.sum(axis=1))
    print(list.max(axis=0))
    print(list.min(axis=0))
    lst1 = np.array([10, 20, 30, 40])
    lst2 = np.array([4, 3, 2, 1])
    print("Add")
    print(lst1+lst2)
    print("Dot")
    # 数组点乘
    print(np.dot(lst1.reshape([2,2]),lst2.reshape([2,2])))
    #将两个数组相连，即list2添加到list1中，传的是tup
    print(np.concatenate((lst1, lst2), axis=0))
    print(np.vstack((lst1, lst2)))
    print(np.hstack((lst1, lst2)))
    print(np.split(lst1, 2))
    print(np.copy(lst1))

    #4 liner 
    print(np.eye(3))
    lst = np.array([[1,2],[3,4]])
    print(inv(lst))
    print("T:")
    print(lst.transpose())
    print("Det")
    print(det(lst))
    print(eig(lst))
    y=np.array([[5.], [7.]]) # 嘿嘿
    print(solve(lst, y))

    # Others
    print("FFT:")
    print(np.fft.fft(np.array([1,1,1,1,1,1,1])))
    print (np.corrcoef([1, 0, 1],[0, 2, 1])) 
    print (np.poly1d([3,1,3]))
if __name__=="__main__":
    main()