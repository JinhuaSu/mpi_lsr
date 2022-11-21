from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
#%%

data_number = 100000000 
each_buffer_size = data_number // size
data_number = each_buffer_size * size
lr = 0.0001 / np.sqrt(data_number)
max_iter = 100
threshold = 0.001
feature_num = 2

def get_alpha_delta(rank,A, alpha, y):
    # print(rank,A.shape,y.shape, alpha.shape)
    gi = A.T* (A.dot(alpha) - y[:,0])
    g = gi.sum(axis=1)
    alpha_delta = - lr * g
    return alpha_delta

x, y, A, alpha = None, None, None, np.empty(feature_num, dtype=np.float64)
recv_alpha_delta = None
recv_A = np.empty(each_buffer_size*feature_num, dtype=np.float64)
recv_y = np.empty(each_buffer_size, dtype=np.float64)
each_cal_alpha_delta = np.empty(2, dtype=np.float64)
recv_alpha_delta = None
flag = None

if rank == 0:
# big data
    x = np.linspace(0, 1, data_number)
    y = 1 + x + x * np.random.random(len(x))
    # 误差项和因变量存在关联,不符合一般假设的情形
    # assemble matrix A
    A = np.vstack([x, np.ones(len(x))]).T
    A = A.reshape((size,each_buffer_size*feature_num))
    flag = False
    # turn y into a column vector
    y = y[:, np.newaxis]
    y =y.reshape((size,each_buffer_size*1))
    alpha = np.zeros(2)
    recv_alpha_delta = np.empty([size, feature_num], dtype=np.float64)
    
alpha_delta = None
# comm.Bcast(A, root=0)
# use least square iteration
comm.Scatter(A, recv_A, root=0)
comm.Scatter(y, recv_y, root=0)
recv_A = recv_A.reshape((each_buffer_size,feature_num))
recv_y = recv_y.reshape((each_buffer_size,1))
for iter in range(max_iter):
    comm.Bcast(alpha, root=0)
    comm.bcast(flag, root=0)
    print(iter, alpha)
    if flag:
        break
    each_cal_alpha_delta = get_alpha_delta(rank,recv_A, alpha, recv_y)
    comm.Gather(each_cal_alpha_delta, recv_alpha_delta, root=0)
    if rank == 0:
        alpha_delta = recv_alpha_delta.sum(axis=0) 
        alpha += alpha_delta
        if np.max(np.abs(alpha_delta)) < threshold:
            flag=True

print(iter, alpha)

