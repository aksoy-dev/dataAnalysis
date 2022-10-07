import numpy as np

a=np.arange(15).reshape(3,5)   #3,5 lik bir arraydır "[[ 0  1  2  3  4] [ 5  6  7  8  9] [10 11 12 13 14]] "
print(a)
print(type(a))
print("Dimension Count:  " + str(a.ndim))  #2 boyutlu 


b=np.arange(10)
print(b.shape)  #10'a birlik bir satır
print(b.ndim)   #1 lik satır






