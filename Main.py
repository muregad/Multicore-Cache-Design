from CPU import CPU
from random import randint
import numpy as np
from Coverage import Coverage

# I ===> 0
# S ===> 1
# E ===> 2
# M ===> 3


encode = {"I": 0, "S": 1, "E": 2, "M": 3}


num_of_cores = 4

cpu = CPU(num_of_cores=num_of_cores)
t = 10000

x = np.zeros((t, 6))
y = np.zeros((t, 4))
cvg = Coverage()
for i in range(t):
    x[i, 0:4] = [encode[cpu.processors[0].Cache.getState(address=8)], encode[cpu.processors[1].Cache.getState(address=8)], encode[cpu.processors[2].Cache.getState(address=8)], encode[cpu.processors[3].Cache.getState(address=8)]]
    processor = np.random.randint(0, 4)
    r_w = np.random.randint(0, 2)
    x[i, 4] = processor
    x[i, 5] = r_w
    # if(r_w == 2):
    #     cpu.processors[0].Cache.reset()
    #     cpu.processors[1].Cache.reset()
    #     cpu.processors[2].Cache.reset()
    #     cpu.processors[3].Cache.reset()
    # else:
    print(x[i,0:4])
    cvg.sample(x[i])
    print(f"Iteration {i} ===> Coverage: {cvg.get_coverage()}")
    cpu.bus.instruction(processor=processor, r_w=r_w, address=8, value=randint(0, 15))
    cpu.printStatus()
    y[i] = [encode[cpu.processors[0].Cache.getState(address=8)], encode[cpu.processors[1].Cache.getState(address=8)], encode[cpu.processors[2].Cache.getState(address=8)], encode[cpu.processors[3].Cache.getState(address=8)]]
    print(y[i])
    print("------------------------------")

# print(cvg.uncoveredMapped)
# print(x)
# print(y)
