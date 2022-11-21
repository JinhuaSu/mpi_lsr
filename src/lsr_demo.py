#%%
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
#%%
# generate x and y
x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))
# 误差项和因变量存在关联,不符合一般假设的情形
# %%
# assemble matrix A
A = np.vstack([x, np.ones(len(x))]).T

# turn y into a column vector
y = y[:, np.newaxis]
#%%
# Direct least square regression(mathematical simplified)
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),y)
print(alpha)
#%%
# plot the results
plt.figure(figsize = (10,8))
plt.plot(x, y, 'b.')
plt.plot(x, alpha[0]*x + alpha[1], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
# %%
alpha = np.zeros(A.shape[1])
# use least square iteration
lr = 0.01
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
# %%
