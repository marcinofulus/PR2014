import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule

mod = SourceModule("""
    #include <stdio.h>

    __global__ void printf_test()
    {
      printf("GONZO %d.%d.%d\\n", threadIdx.x, threadIdx.y, threadIdx.z);
    }
    """)

func = mod.get_function("printf_test")
func(block=(2,2,1))