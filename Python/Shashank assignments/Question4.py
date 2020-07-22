# Let's make Machine learn!!
import numpy as np

X = np.random.normal(0, 1, (20, 20))
y = (np.random.rand(20) * 5).astype('int32')

# theta = (X^T * X)^-1 . (X^T * y)
first = np.linalg.inv(np.transpose(X).dot(X))
second = np.transpose(X).dot(y)
theta = first.dot(second)

# print(X)
# print(y)
print(theta)
