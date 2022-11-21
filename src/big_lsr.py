# 
import numpy as np
# big data
data_number = 100000000
x = np.linspace(0, 1, data_number)
y = 1 + x + x * np.random.random(len(x))
# 误差项和因变量存在关联,不符合一般假设的情形
# %%
# assemble matrix A
A = np.vstack([x, np.ones(len(x))]).T

# turn y into a column vector
y = y[:, np.newaxis]
alpha = np.zeros(A.shape[1])
# use least square iteration
lr = 1 / np.sqrt(data_number)
max_iter = 100
threshold = 0.001
for iter in range(max_iter):
    gi = A.T* (A.dot(alpha) - y[:,0])
    g = gi.sum(axis=1)
    alpha_delta = - lr * g
    if np.max(np.abs(alpha_delta)) < threshold:
        break
    alpha += alpha_delta
print(iter, alpha)

# 
# Broadcast
# Map

# Reduce