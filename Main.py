from CPU import CPU
from random import randint


cpu = CPU(num_of_cores=4)

n = 20
for i in range(n):
    cpu.bus.instruction(processor=randint(0, 3), r_w=randint(0, 1), address=8, value=randint(0, 15))
    cpu.printStatus()
