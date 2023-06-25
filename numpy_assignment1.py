#1. Create a null vector of size 10 but the fifth value which is 1.
# import numpy as np
# x=np.zeros(10)
# x[4]=1
# print(x)

#2.Create a vector with values ranging from 10 to 49.
# import numpy as np
# a=np.arange(10,50)
# print(a)

#3.Create a 3x3 matrix with values ranging from 0 to 8
# import numpy as np
# z=np.arange(9).reshape(3,3)
# print(z)

#4.Find indices of non-zero elements from [1,2,0,0,4,0]Find indices of non-zero elements from [1,2,0,0,4,0]
# import numpy as np
# nz=np.nonzero([1,2,0,0,4,])
# print(nz)

#5.Create a 10x10 array with random values and find the minimum and maximum values.
# import numpy as np
# ra_va=np.random.randint((10,10))
# a=[10,8,9]
# b=[5,4,3]
# print("random numbers are ",ra_va)
# print(ra_va.max())
# print(ra_va.min())

#6.Create a random vector of size 30 and find the mean value.
import numpy as np
z=np.random.random(30)
mean=z.mean()
print(mean)