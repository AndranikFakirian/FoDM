import numpy as np
arr=np.arange(4).reshape(2, 2)
print(np.linalg.det(arr))
print(np.linalg.inv(arr))
narr=np.arange(4)
narr=narr[::-1]
narr=narr.reshape(2, 2)
print(arr@narr)