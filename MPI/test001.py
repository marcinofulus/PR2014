#%%px --block
from mpi4py import MPI
import time
import numpy as np 
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
t = MPI.Wtime()
print("result =",np.max(np.random.randn(5000,5000//4)))
t = MPI.Wtime() - t
print(rank,":: execution time:",t)